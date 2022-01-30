sed -e '1d' -e '$d' -e 's/  -H //g' -e "s/:/':/g" -e "s/: /: '/g" -e 's/ \\$/,/g' curl_headers | sed -e '$s/,//g' | sed -e '1iheaders = {' -e '$a}' > headers.py
