# -*- coding: utf-8 -*-
"""
Created on July 2017

@author: JulienWuthrich
"""
import json
import numpy
import hashlib
import pandas as pd


def sha1_for_named_columns(df, columns):
    intersection = [col for col in columns if col in df.columns]
    if len(intersection) == len(columns):
        sha1s = pd.Series(data="", index=range(len(df)))
        for i in columns:
            sha1s = sha1s.map(numpy.str) + df[i].map(numpy.str)
        sha1s = sha1s.apply(
            lambda s: hashlib.sha1(str(s).encode("utf8")).hexdigest()
        )
    else:
        sha1s = pd.Series(data=numpy.nan, index=range(len(df)))

    return sha1s


def hash_frame(df):
    return hashlib.sha1(df.to_string().encode("utf8")).hexdigest()


def cbind(df1, df2):
    return pd.concat([df1, df2], axis=1, ignore_index=True)


def rbind(df1, df2):
    return pd.concat([df1, df2], axis=0, ignore_index=True)


def remove_rows_contains_null(df, col):
    return df[df[col].notnull()]


def keep_rows_contains_null(df, col):
    return df[~df[col].notnull()]


def compare_data_frame(df1, df2, column):
    return df1[~df1[column].isin(df2[column])]


def count_frequency(df, col, colname="Freq"):
    df[colname] = df.groupby(col)[col].transform('count')

    return df


def change_nan_value(df, new_value):
    return df.where((pd.notnull(df)), new_value)


def extract_json(serie, k):
    return serie.map(lambda row: json.loads(row)[k])
