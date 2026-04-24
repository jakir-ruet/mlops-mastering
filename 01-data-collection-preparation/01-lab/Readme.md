```bash
apt update
apt install python3-venv -y
python3 -m venv venv
source venv/bin/activate
pip install pandas numpy scikit-learn
python -c "import numpy, pandas, sklearn; print('OK')"
```

```bash
python mockdata.py
```
