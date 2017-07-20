FROM ubuntu:trusty
RUN echo "deb http://ppa.launchpad.net/mozillateam/firefox-next/ubuntu trusty main" > /etc/apt/sources.list.d/mozillateam-firefox-next-trusty.list
RUN apt-key adv  --keyserver keyserver.ubuntu.com --recv-keys CE49EC21
RUN apt-get update
RUN apt-get install -y firefox xvfb python-pip vim wget 
RUN pip install selenium
RUN pip install urllib
ADD geckodriver /usr/local/bin

RUN apt-get install -y daemon
ADD xvfb_daemon /etc/init.d/xvfb_daemon
RUN chmod +x /etc/init.d/xvfb_daemon
RUN update-rc.d xvfb_daemon defaults

ENV wdir /root/selenium_wd_tests
RUN mkdir -p ${wdir} 
ADD watch.py ${wdir}
ADD vid.py ${wdir}
ADD anonymox-3.2-fx.xpi ${wdir}

ENV DISPLAY :10
WORKDIR ${wdir} 
ARG video_id=GSAfPHun-9I
CMD (service xvfb_daemon start ; while true; do python vid.py $video_id; done;)
