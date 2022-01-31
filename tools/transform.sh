sed -e '1d' -e '$d' -e 's/  -H //g' -e "s/:/':/" -e "s/: /: '/" -e 's/ \\$/,/g' ./data/curl_headers | sed -e '$s/,//g' | sed -e '1iheaders = {' -e '$a}' > ./data/headers.py
