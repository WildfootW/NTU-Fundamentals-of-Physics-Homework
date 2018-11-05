## environment
```
python3 -m pip install --user vpython
```

### trobleshoot
* while import vpthon
```
RuntimeError: There is no current event loop in thread 'Thread-*'
```
I solved this problem by install python3.6 instead of python3.5
```
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.6
sudo apt-get install python3.6-dev
python3.6 -m pip install --user vpython
```

