# fx-hopsworks
FX Exchange Range Ingestion

## Linux Installation
pip install hopsworks
pip install yfinance


## Windows Installation

conda install twofish
setx CONDA_DLL_SEARCH_MODIFICATION_ENABLE 1
pip install hopsworks
pip install yfinance


## MacOS Installation

curl -O https://raw.githubusercontent.com/Homebrew/homebrew-core/f7d0f40bbc4075177ecf16812fd95951a723a996/Formula/librdkafka.rb
brew install --build-from-source librdkafka.rb

export C_INCLUDE_PATH=$(brew --prefix)/include
export LIBRARY_PATH=$(brew --prefix)/lib
pip install hopsworks
pip install yfinance
