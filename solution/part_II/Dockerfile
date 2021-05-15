FROM centos:8
RUN yum -y install net-tools
RUN mkdir -p /csvserver 
RUN touch /csvserver/csvserver /csvserver/inputdata
WORKDIR /csvserver
COPY csvserver /csvserver/csvserver
COPY inputdata /csvserver/inputdata
EXPOSE 9300
ENV CSVSERVER_BORDER Orange
CMD ["/csvserver/csvserver"]
