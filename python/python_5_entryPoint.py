print(__name__)
# python 파일.py
# 파일 > 모듈 > 모듈 > 모듈
# 파일 : 진입점(entry point)
# 메인 파일(main)

import python_5_module

print(python_5_module.a,  python_5_module.b, python_5_module.c())

if __name__ == "__main__":
    print("This is Entry Point(entryPoint)")


