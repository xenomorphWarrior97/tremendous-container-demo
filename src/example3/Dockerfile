FROM registry.access.redhat.com/ubi8/ubi as build-stage

RUN dnf install -y gcc-c++ make && dnf clean all

WORKDIR /usr/workspace
COPY src/cpp_word_counter/main.cpp .
RUN g++ -std=c++17 -O2 -o word-counter main.cpp

FROM registry.access.redhat.com/ubi8/ubi-minimal AS deployed-app-stage
COPY --from=build-stage /usr/workspace/word-counter /bin/word-counter

ENTRYPOINT ["word-counter"]
