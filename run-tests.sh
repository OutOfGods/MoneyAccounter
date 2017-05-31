coverage3 run tests.py
coverage3 report
if [ "$1" = "html" ]; then
    coverage3 html
    vivaldi-stable htmlcov/index.html &> /dev/null &
fi
