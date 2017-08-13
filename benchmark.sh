#!/usr/bin/env bash
python -m flamegraph -o $1.log benchmark.py
perl flamegraph.pl $1.log > $1.svg
