FROM python:3.9.2-buster

ADD . /app
WORKDIR /app

#USER thedevilsvoice:thedevilsvoice
RUN \
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367;\
DEBIAN_FRONTEND=noninteractive apt update; \
DEBIAN_FRONTEND=noninteractive apt install -y apt-utils;\
DEBIAN_FRONTEND=noninteractive apt -y autoremove;\
DEBIAN_FRONTEND=noninteractive apt install -y make git wget pandoc latexmk \
python3-pip python3-graphviz texlive-fonts-recommended texlive-latex-extra \
texlive-xetex texlive-fonts-extra

# Python3 setup
RUN pip3 install -rrequirements.txt

#RUN make clean && make book
# cd recipes && sphinx-build -b latex -d _build/doctrees . _build/xetex && cd _build/xetex; xelatex *.tex