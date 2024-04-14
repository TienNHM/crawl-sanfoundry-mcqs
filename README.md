# CRAWL DATA sanfoundry.com

> This is a crawler to crawl data from sanfoundry.com and store it in a json file.
> This crawler is written in python using Flask to create a REST API to crawl data from sanfoundry.com.

## Table of contents

1. [Operating system](./OS/)
    + [OS - Processes](./OS/Processes/)
    + [OS - Distributed Communication](./OS/Distributed%20Communication/)
    + [OS - CPU Scheduling](./OS/CPU%20Scheduling/)
    + [OS - Process Synchronization](./OS/Process%20Synchronization/)
    + [OS - Deadlocks](./OS/Deadlocks/)
    + [OS - Memory Management](./OS/Memory%20Management/)
    + [OS - IO Systems](./OS/IO%20Systems/)
    + [OS - Real Time Operating Systems (RTOS)](./OS/Real%20Time%20Operating%20Systems%20(RTOS)/)
    + [OS - Multimedia Systems](./OS/Multimedia%20Systems/)
    + [OS - Security](./OS/Security/)
    + [OS - Linux System](./OS/Linux%20System/)
    + [OS - Virtual Memory](./OS/Virtual%20Memory/)
    + [OS - File Systems and their Implementation](./OS/File%20Systems%20and%20their%20Implementation/)
    + [OS - Mass-Storage Structures](./OS/Mass-Storage%20Structures/)
    + [OS - Protection](./OS/Protection/)
    + [OS - Distributed Operating System](./OS/Distributed%20Operating%20System/)
    + [OS - Distributed File Systems](./OS/Distributed%20File%20Systems/)

## Installation

1. Clone the repository
```bash
git clone https://github.com/TienNHM/crawl-sanfoundry-mcqs.git
```

2. Install the dependencies
```bash
pip install Flask
pip install requests
pip install beautifulsoup4
pip install jsonify
```

3. Run the server
```bash
python app.py
```

## API Endpoints

```bash
GET /mcqs/<url>
```

Example:
```bash
GET /mcqs/operating-system-mcqs-memory-management-swapping-1
```

Note: The url is the last part of the url of the page on sanfoundry.com. For example, the url of the page `https://www.sanfoundry.com/operating-system-questions-answers-memory-management-swapping-1/` is `operating-system-mcqs-memory-management-swapping-1`.