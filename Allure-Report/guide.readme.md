**Allure Report (in Python + PyTest)**

install required commands :
   Install Allure Commandline
       i. Node JS – [https://nodejs.org/en/download/prebuilt-installer](https://nodejs.org/en/download/prebuilt-installer)
       ii. cmd → `node --version`
       iii. cmd → `npm -g i allure-commandline`
            iwr -useb get.scoop.sh | iex scoop install allure

install in pycharm terminal –> pip install allure-pytest

in pycharm terminal type -> pytest your_file_name --alluredir=allure_result

you will get allure_result folder in your project path in pycharm you can see that

then type -> allure serve allure-result

it will give you url on terminal in pycharm

click this url you can see report




