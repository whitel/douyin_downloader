Douyin PC video downloader
---------------------------
### Create python virtual environment
```
sudo apt install -y --no-install-recommends python3-virtualenv python-is-python3 python3-pip
python3 -m virtualenv --python="$(command -v python3)" .env
source .env/bin/activate
pip install beautifulsoup4 lxml requests requests-html
```

### Tutorial
1. `cd ~ && git clone https://github.com/whitel/douyin_downloader`
2. (on pc)goto https://douyin.com/ and select a video, using ctrl-s to save current web page
3. move .html file to ~/douyin_downloader/htmls (create one if not exist)
4. execute `make download` in ~/douyin_downloader
5. the result is in ~/douyin_downloader/result

### TODO
+ [x] solve douyin.com captcha problem - by using http headers
+ [x] download pictures content - don't do that right now
+ [ ] parse javascript in python or linux environment
+ [ ] record download status
+ [ ] handle common errors

