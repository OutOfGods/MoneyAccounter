coverage3 run tests.py
coverage3 report
if [ "$1" = "html" ]; then
    coverage3 html
    xdg-open htmlcov/index.html &> /dev/null &
fi
