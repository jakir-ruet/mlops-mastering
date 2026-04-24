```bash
apt update
apt install python3-venv -y
python3 -m venv venv
source venv/bin/activate
pip install pandas numpy scikit-learn
python -c "import numpy, pandas, sklearn; print('OK')"
```

### Data collection by `generating mock data`

```bash
python 01-data-collection.py
```

### Data clearing

```bash
python 02-data-cleaning.py
```

### Data transformation

```bash
python 03-data-transformation.py
```
