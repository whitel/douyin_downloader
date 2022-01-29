Douyin PC video downloader
---------------------------
### create python virtual environment
```
sudo apt install -y --no-install-recommends python3-virtualenv python-is-python3 python3-pip
python3 -m virtualenv --python="$(command -v python3)" .env
source .env/bin/activate
pip install beautifulsoup4 lxml requests
```

### Tutorial
1. goto https://douyin.com/ and select a video
2. (on windows)using ctrl-s to save current web page
3. move .html file to douyin_downloader/htmls
4. execute `make download` in douyin_downloader
5. the result is in douyin_downloader/result

### TODO
+ [ ] solve douyin.com captcha problem
+ [ ] parse javascript in python or linux environment

