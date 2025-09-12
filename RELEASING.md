# Releasing the dataset

## Recreate the raw data from glottography-data

In case of upstream changes in glottography-data:
```shell
cldfbench download cldfbench_figueira1982atlastotalargentina.py
```

## Recreate the CLDF data

```shell
cldfbench makecldf cldfbench_figueira1982atlastotalargentina.py --glottolog-version v5.2
cldfbench cldfreadme cldfbench_figueira1982atlastotalargentina.py
cldfbench zenodo cldfbench_figueira1982atlastotalargentina.py
cldfbench readme cldfbench_figueira1982atlastotalargentina.py
```

## Validation

```shell
cldf validate cldf
```

```shell
cldfbench geojson.validate cldf
```

```shell
cldfbench geojson.glottolog_distance cldf --format pipe
```

| ID | Distance | Contained | NPolys |
|:---------|-----------:|:------------|---------:|
| east2555 | 2.33 | False | 1 |
| iyow1239 | 0.00 | True | 1 |
| mapu1245 | 0.00 | False | 1 |
| mbya1239 | 1.06 | False | 1 |
| moco1246 | 0.00 | True | 2 |
| para1311 | 1.78 | False | 1 |
| pila1245 | 0.12 | False | 1 |
| sant1432 | 0.00 | True | 1 |
| tehu1242 | 1.34 | False | 4 |
| toba1269 | 2.36 | False | 1 |
| wich1264 | 0.00 | True | 1 |
