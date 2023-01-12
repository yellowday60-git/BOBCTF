# How to USE

```shell
python3 ./monitor.py
```

자동으로 flag_manager 실행 및 auto_ex 처리, flag 제출까지 해줍니다.
ctrl + c로 나갈 수 있습니다.

# 수정해야할것
기본적으로 auto_ex가 꺼져있습니다.
auto_ex.py에서 service마다 익스 코드를 따로 적어주어야 합니다.

각종 변수(서비스 개수, flag 길이, flag 포멧 등 등)는 monitor.py에서만 참조하기 때문에 해당 코드만 수정하면 됩니다.
