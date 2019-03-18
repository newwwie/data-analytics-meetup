## Instructions

### Setting up the Virtual Environment

```bash
virtualenv -p /usr/bin/python3.6 venv
```

### Install the Python Dependencies

```bash
source venv/bin/active
pip install -r requirements.txt
```

### Jupyter Notebook

Setting up the theme like the talk
```bash
source venv/bin/active
jt -t oceans16 -fs 12 -cellw 100% -nfs 13 -tfs 14 -fs 12 -m auto -T -N -altmd \#fff
```

Run the interactive Presentation
```bashjt -t oceans16 -fs 12 -cellw 100% -nfs 13 -tfs 14 -fs 12 -m auto -T -N -altmd fff -altout fff
jupyter nbconvert Intro-Pandas-Dask.ipynb --to slides --post serve --SlidesExporter.reveal_scroll=True
```