FROM ethanlmiller/ubuntu2004-clang10-python38

COPY . /usr/src/ECTS/
WORKDIR /usr/src/ECTS

RUN mkdir bin
RUN pip3 install --default-timeout=100 -i https://pypi.douban.com/simple -r requirements.txt
RUN make all
CMD ["python3", "GetSellServer.py"]