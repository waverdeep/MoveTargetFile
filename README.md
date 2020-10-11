# MoveTargetFile
특정 디렉토리를 기준으로 하위에 있는 같은 확장자를 가진 파일들을 원하는 디렉토리에 옮겨주는 스크립트

## Libraries
- os
- glob
- shutil
- multiprocessing
- functools
- tqdm

## Multiprocessing
다량의 파일을 빠르게 이동/복사하기 위해서 Multiprocessing Pool을 생성후 파일 이동/복사를 진행
실행되는 CPU에 따라 속도 및 Pool의 갯수가 다르게 열릴 수 있음
12 core -> 12 개의 프로세스가 열려 작업을 진행
8 core -> 8 개의 프로세스가 열려 작업을 진행
