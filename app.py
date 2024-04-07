# %%
import csv
import requests
from bs4 import BeautifulSoup

# %%
def extract_mcqs(soup):
    '''Trích xuất câu hỏi trắc nghiệm từ trang web và trả về dữ liệu dưới dạng dictionary'''
    try:
        # print(soup.contents)
        # Trích xuất câu hỏi
        question = soup.contents[0].strip()
        # Tách số thứ tự câu hỏi từ nội dung câu hỏi
        index = question.split('.')[0]
        # Loại bỏ số thứ tự câu hỏi khỏi nội dung câu hỏi
        question = question.split('.')[1].strip()

        # Trích xuất các lựa chọn từ thẻ p
        options = [str(option).strip() for option in soup.contents[1:-2] if str(option).strip()]
        # print(f'Question: {index} - {question} - {options}')
        # Loại bỏ các phần tử '<br/>' khỏi danh sách lựa chọn, chỉ giữ lại 4 phần tử đầu tiên sau khi đã loại bỏ
        options = [option for option in options if option != '<br/>' and option != '<br>'][:4]

        # Trích xuất câu trả lời và giải thích
        answer_div = soup.find('div', {'class': 'collapseomatic_content'})
        answer = answer_div.contents[0].split(':')[1].strip()
        explanation = answer_div.contents[2].strip()
        # Remove the 'Explanation:' prefix from the explanation
        explanation = explanation.replace('Explanation:', '').strip()

        if len(options) < 4:
            return None

        # Trả về dữ liệu câu hỏi và câu trả lời dưới dạng dictionary
        # question, options, option1, option2, option3, option4, answer, explanation
        return {
            'index': index,
            'question': question, 
            'options': options, 
            'option1': options[0], 
            'option2': options[1], 
            'option3': options[2], 
            'option4': options[3], 
            'answer': answer, 
            'explanation': explanation
        }
    except Exception as e:
        print(e)
        return None

# %%
def getMCQS(url):

    # Gửi một yêu cầu GET đến trang web, chờ đến khi nhận được phản hồi tất cả dữ liệu
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

    # Kiểm tra xem yêu cầu có thành công không
    if response.status_code == 200:
        # Replace all the <br> tags with <br/> tags 
        response_content = response.content.decode('utf-8').replace('<br>', '<br/>')

        # Phân tích cú pháp nội dung HTML của trang
        soup = BeautifulSoup(response_content, 'html.parser')

        # find node có class='entry-content' và itemprop='text'
        soup = soup.find('div', {'class': 'entry-content', 'itemprop': 'text'})

        # delete các node script và style, node có class='sf-mobile-ads' và class='sf-desktop-ads' và class='sf-section'
        for tag in soup(['script', 'style']):
            tag.decompose()

        for tag in soup.find_all('div', {'class': 'sf-mobile-ads'}):
            tag.decompose()

        for tag in soup.find_all('div', {'class': 'sf-desktop-ads'}):
            tag.decompose()

        for tag in soup.find_all('div', {'class': 'sf-section'}):
            tag.decompose()

        all_mcqs = soup.find_all('p')

        # Lặp qua từng câu hỏi trắc nghiệm và trích xuất câu hỏi, các lựa chọn, câu trả lời và giải thích
        
        mcqs = []
        for mcq in all_mcqs:
            # print(mcq)
            try:
                # Nếu thẻ p không phải là câu hỏi trắc nghiệm thì bỏ qua
                if 'View Answer' in mcq.text:
                    question = extract_mcqs(mcq)
                    if question:
                        mcqs.append(question)
            except Exception as e:
                print(mcq)
                print(f"Lỗi: {e}")

        return mcqs

    else:
        print(f"Không thể truy xuất trang web. Mã trạng thái: {response.status_code}")
        return None


# %%
def export_csv(data, filename):
    '''Xuất dữ liệu câu hỏi trắc nghiệm ra file CSV'''
    # Tên các cột trong file CSV
    fields = ['index', 'question', 'options', 'option1', 'option2', 'option3', 'option4', 'answer', 'explanation']

    # Ghi dữ liệu vào file CSV
    # print(f'Ghi {len(data)} dữ liệu vào file {filename}')
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)


# %%
# url = f"https://www.sanfoundry.com/operating-system-mcqs-memory-management-swapping-1/"
# print(f'URL: {url}')

# mcqs = getMCQS(url)
# if mcqs:
#     export_csv(mcqs, 'mcqs.csv')
#     print(f"Đã xuất dữ liệu thành công ra file CSV")

# %%
# Dùng flask để tạo API trả về câu hỏi trắc nghiệm

from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return 'API trả về câu hỏi trắc nghiệm từ trang web'

@app.route('/mcqs/<url>', methods=['GET'])
def get_mcqs(url):
    if not url:
        return jsonify({'error': 'URL không được trống'})
    
    url = f"https://www.sanfoundry.com/{url}/"
    # print(f'URL: {url}')
    
    mcqs = getMCQS(url)
    # export_csv(mcqs, 'mcqs.csv')
    
    return jsonify(mcqs)

if __name__ == '__main__':
    app.run()


