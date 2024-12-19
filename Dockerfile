FROM bentoml/model-server:0.11.0-py38
LABEL author="ersilia"

RUN pip install rdkit==2023.3.2
RUN pip install torch==1.13.1 --index-url https://download.pytorch.org/whl/cpu
RUN pip install torchvision==0.14.1 --index-url https://download.pytorch.org/whl/cpu
RUN pip install numpy==1.21.6

WORKDIR /repo
COPY . /repo
