from setuptools import setup

setup(
    name='flaskr', #패키지 이름
    packages=['MyFlask'], #모듈을 찾기위해 MyFlask/__init__.py를 찾음
    include_package_data=True, #MANIFEST.in에서 명시한 패키지 디렉터리의 데이터파일 포함
    install_requires=[
        'flask',
    ],
)