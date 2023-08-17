#!/bin/bash

echo "- program : batch"
echo "- pwd : ${PWD}/${0}"
echo "- job : init setting"


DIR="$( cd "$( dirname "$0" )" && pwd )"
VENV_DIR="${DIR}/ venv"
REQUIREMENT_DIR="${DIR}/requirement.txt"

if [ -e "$VENV_DIR" ]; then
    #echo "$VENV_DIR exists."   
    echo "already set the environment!" 
else
    #echo "$VENV_DIR does not exist."

    # 가상 환경 라이브러리 설치
    #pip install virtualenv
    pip3 install python3-virtualenv
    
    # 가상 환경 생성 및 실행
    echo "start to set the environment!"
    echo "create  venv"
    virtualenv $VENV_DIR
    
    # 프로그램에 필요한 라이브러리 설치
    echo "install library"
    . $VENV_DIR/bin/activate
    pip install -r $REQUIREMENT_DIR
fi