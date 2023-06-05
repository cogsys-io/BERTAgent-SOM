#!/usr/bin/env ipython
# -*- coding: utf-8 -*-


from nvm import disp_df
from nvm import clean_str
from nvm.aux_str import CLEAN_STR_MAPPINGS_LARGE as maps0
from nvm.aux_str import REGEX_ABC_DASH_XYZ_ASTERISK as re0
from nvm.aux_pandas import fix_column_names

import os
import pathlib
import numpy as np
import pandas as pd
import re
import json
import yaml
import srsly
import uuid
import random
import numbers
from collections import OrderedDict
from contextlib import ExitStack
import warnings
# warnings.warn("\nwarning")
from hashlib import md5
import humanfriendly as hf
import time
import datetime as dt
from pytz import timezone as tz
tz0 = tz("Europe/Berlin")
from glob import glob
from tqdm import tqdm
import logging
log0.info("DONE: basic imports")

from contexttimer import Timer
import textwrap

HOME = pathlib.Path.home()

tqdm.pandas()

import matplotlib
from matplotlib import pyplot as plt
# import seaborn as sns
# import plotly.graph_objects as go
# import plotly.express as px

# get_ipython().run_line_magic("matplotlib", "qt")
# get_ipython().run_line_magic("matplotlib", "inline")

with Timer() as elapsed:
    time.sleep(0.001)

log0.info(hf.format_timespan(elapsed.elapsed))

log0.info("DONE: extra imports and settings")

log0.info("DONE: more extra imports and settings")

dir0 = "../../data/d0001_sources/"
dir0 = pathlib.Path(dir0)
# dir0.mkdir(mode=0o700, parents=True, exist_ok=True)
assert dir0.exists(), f"The data directory dir0={str(dir0)} not found!"

glob0 = dir0.glob("s*/c*/*.yaml")
glob0 = sorted(list(glob0))

log0.info(f"{len(glob0) = }")

data4 = []
for if0 in glob0:
    of2 = pathlib.Path("../../data/d0002_sources-lowercased")/if0.relative_to("../../data/d0001_sources")
    of2.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    data0 = srsly.read_yaml(if0)
    # log0.info(f"r: {if0} ({len(data0)})")
    data2 = [clean_str(item).lower() for item in data0]
    data2 = list(filter(re0.search, data2))
    data2 = sorted(list(set(data2)))
    data4 += data2
    log0.info(f"w: {of2} ({len(data2)}/{len(data0)} [{len(set(data0))}])")
    srsly.write_yaml(of2, data2)

of4 = pathlib.Path("../../data/d0004_sources-merged-and-deduped")/"merged.yaml"
of4.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
log0.info(f"M: {of4} ({len(data4)})")
data4 = sorted(list(set(data4)))
log0.info(f"W: {of4} ({len(data4)})")
srsly.write_yaml(of4, data4)

data0a = srsly.read_yaml("../../data/d0001_sources/s0003_related-word-collections-and-composite-dictionaries/c2016_DecterFrainFrimer2016a/DecterFrainFrimer2016a_selected_liwc_cats_agency_posit.yaml")
data0b = srsly.read_yaml("../../data/d0001_sources/s0003_related-word-collections-and-composite-dictionaries/c2016_DecterFrainFrimer2016a/DecterFrainFrimer2016a_selected_liwc_cats_agency_negat.yaml")
data0c = list(set(data0a+data0b))
log0.info(f"{len(data0c) = }")
