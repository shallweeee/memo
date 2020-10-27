# 파이썬 visualization 개발 환경 설정
> OS: 윈도우즈7  
> 에디터: vscode  
> 파이썬: python 3.8.5 (miniconda3 패포판)  

1. miniconda3 및 파이썬 설치
   * https://docs.conda.io/en/latest/miniconda.html 에서 다운로드
   * c:\ 에 설치 (c:\miniconda3 로 설치됨)
   * 프롴프트 열기  
   시작메뉴 > Anaconda Prompt (miniconda3)
   * 일단은 업데이트부터
   ```
   conda update -y conda
   ```  
   * vis 라는 이름의 환경 생성 및 3.8.5 버전 파이썬 설치
   ```
   conda create -y -n vis python=3.8.5
   ```

2. vscode 설치
   * https://code.visualstudio.com/download 에서 다운로드
   * python 확장 설치  
   C-S-x > 검색: python > python 선택 > install
   * 프로젝트 생성  
   C-k C-o > d:\vis (생성)선택
   * 프로젝트를 앞서 생성한 vis 환경 및 파이썬과 연결  
   C-, > Workspace > 검색: shellargs > 'Terminal > Integrated > Shell Args: Windows' 선택 > 다음 추가
   ```json
   "python.pythonPath": "c:\\miniconda3\\envs\\vis\\python.exe",
   "terminal.integrated.shell.windows": "c:\\windows\\System32\\cmd.exe",
   "terminal.integrated.shellArgs.windows": ["/K", "c:\\miniconda3\\Scripts\\activate.bat c:\\miniconda3 & conda activate vis"]
   ```
   * 설정 확인  
   C-` [터미널 열기] > allow 선택 > VSCode 재시작 > 프롬프트가 '(vis) D:\vis>' 인것 확인

3. 패키지 설치
   * 위의 터미널에서 다음 입력
   ```
   pip install numpy scipy pandas matplotlib pygraphviz pydot pyyaml gdal
   ```
