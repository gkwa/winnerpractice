Following tutorial from
https://www.lambdatest.com/blog/run-selenium-tests-in-docker/
https://www.selenium.dev/documentation/webdriver/drivers/remote_webdriver/
https://selenium-python.readthedocs.io/getting-started.html
https://github.com/SeleniumHQ/docker-selenium/tree/trunk#dev-and-beta-standalone-mode

* this works

** macos

*** first run

#+begin_example
git clone https://github.com/TaylorMonacelli/winnerpractice
cd winnerpractice
deactivate 2>/dev/null || true
rm -rf .venv
python3 -mvenv .venv
echo source $(pwd)/.venv/bin/activate
source $(pwd)/.venv/bin/activate
pip install --upgrade pip
pip install pre-commit black --upgrade humanfriendly pyyaml prometheus_client selenium jinja2 requests
docker run --rm -it -p 4444:4444 -p 7900:7900 --shm-size 2g selenium/standalone-chrome:beta
open http://localhost:7900/
set +o history
$USERNAME='8675309'; $PASSWORD='PassWRurD1';
set -o history
python test.py
#+end_example

*** subsequent runs

#+begin_example
cd /tmp/winnerpractice
source $(pwd)/.venv/bin/activate
set +o history
export USERNAME='8675309' PASSWORD='PassWRurD1'
set -o history
python test.py
#+end_example

** windows

*** first run

```
Set-Location "c:/Windows/Temp"
New-Item -Type "directory" -Force -Path "c:/Windows/Temp/winnerpractice" | Out-Null
git clone https://github.com/TaylorMonacelli/winnerpractice
cd winnerpractice
python -mvenv .venv
. .\.venv\Scripts\activate.ps1
pip install pre-commit black --upgrade humanfriendly pyyaml prometheus_client selenium jinja2 requests
docker run --rm -it -p 4444:4444 -p 7900:7900 --shm-size 2g selenium/standalone-chrome:beta
start http://localhost:7900/
Set-PSReadLineOption -AddToHistoryHandler {
        param([string]$line)
        return $line.Length -gt 3 -and $line[0] -ne ' ' -and $line[0] -ne ';'
}
 $env:USERNAME='8675309'; $env:PASSWORD='PassWRurD1';
python test.py
```

** 

https://github.com/SeleniumHQ/docker-selenium/tree/trunk#quick-start

docker kill $(docker ps -q)
docker run -d -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-firefox:4.6.0-20221104
docker run -d -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-chrome


**

Couldn't register this node: The hub is down or not responding

**


**

cd c:/Windows/temp/winnerpractice
. c:\Windows\temp\winnerpractice\.venv\Scripts\activate.ps1
python test.py

**

cd c:/Windows/temp/winnerpractice
git pull
. c:\Windows\temp\winnerpractice\.venv\Scripts\activate.ps1
python test.py
