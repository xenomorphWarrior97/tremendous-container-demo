# Stage 1: Build the C++ application using the Red Hat UBI 8 base image
FROM registry.access.redhat.com/ubi8/ubi as build-stage

# Install required build tools: GCC and Make
RUN dnf install -y gcc-c++ make && dnf clean all

# Set the working directory for the build process
WORKDIR /usr/workspace

# Copy the C++ source file into the container
COPY src/cpp_word_counter/main.cpp .

# Compile the C++ program using C++17 standard and optimization level 2
RUN g++ -std=c++17 -O2 -o word-counter main.cpp

# Stage 2: Use a minimal UBI image for deploying the compiled binary
FROM registry.access.redhat.com/ubi8/ubi-minimal AS deployed-app-stage

# Copy the compiled binary from the build stage into the minimal runtime image
COPY --from=build-stage /usr/workspace/word-counter /bin/word-counter

# Set the binary as the container's entrypoint so it runs on container start
ENTRYPOINT ["word-counter"]
