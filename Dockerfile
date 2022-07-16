FROM selenium/standalone-chrome-debug
RUN sudo apt update
RUN sudo apt install -y pip
RUN pip install selenium
RUN pip install chromedriver_binary==91.0.4472.101.0