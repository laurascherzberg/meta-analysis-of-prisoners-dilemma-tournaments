import imp

import numpy as np
import pandas as pd

import axelrod as axl

process_data = imp.load_source("processe_data", "src/process_data.py")


def test_strategies_properties():
    my_strategies = [
    axl.Cooperator,                   # Always Cooperate
    axl.Defector,                     # Always Defect
    axl.TitForTat,                    # Classic TFT
    axl.TitFor2Tats,                  # More tolerant than TFT
    axl.WinStayLoseShift,            # Pavlov (strong in noisy settings)
    axl.Grudger,                      # Grim Trigger
    axl.Alternator,                   # Alternating pattern
    axl.ForgivingTitForTat,           # More generous TFT
    axl.SuspiciousTitForTat,          # Starts with defection
    axl.HardTitForTat,                # Harsher TFT
    axl.Random,                       # 50/50 stochastic
    axl.RemorsefulProber,             # Prober with forgiveness
    axl.Gradual,                      # Punishes gradually, then forgives
    axl.BackStabber,                  # Reverse-TFT-like
    axl.Prober                    # Prober with no forgiveness
    ]

    df = process_data.get_strategies_properties()

    assert isinstance(df, pd.DataFrame)
    #assert len(df) == len(axelrod.strategies)
    assert len(df) == len(my_strategies)

    for memory_depth in df["Memory_depth"]:
        assert isinstance(memory_depth, float)

    for use_of_game in df["Makes_use_of_game"]:
        assert isinstance(use_of_game, int)

    for use_of_length in df["Makes_use_of_length"]:
        assert isinstance(use_of_length, int)


def test_get_error_for_row():
    row = {
        "CC_to_C_rate": 0,
        "CD_to_C_rate": 0,
        "DC_to_C_rate": 0,
        "DD_to_C_rate": 0,
    }
    error = process_data.get_error_for_row(row)
    assert error < 0.1


def test_fix_name():
    row = {"Name": "Tit For Tat: D"}
    fixed_name = process_data.fix_name(row)

    assert fixed_name == "Tit For Tat"


def get_cooporation_rating_compared_to_max(row):
    row = {"Cooperation_rating": 0.2, "Cooperation_rating_max": 0.8}

    assert process_data.get_cooporation_rating_compared_to_max(row) == 0.25


def get_cooporation_rating_compared_to_median(row):
    row = {"Cooperation_rating": 0.2, "Cooperation_rating_median": 0.8}

    assert process_data.get_cooporation_rating_compared_to_median(row) == 0.25


def get_cooporation_rating_compared_to_mean(row):
    row = {"Cooperation_rating": 0.2, "Cooperation_rating_mean": 0.8}

    assert process_data.get_cooporation_rating_compared_to_mean(row) == 0.25


def get_cooporation_rating_compared_to_min(row):
    row = {"Cooperation_rating": 0.2, "Cooperation_rating_min": 0.4}

    assert process_data.get_cooporation_rating_compared_to_max(row) == 0.25


def get_cooporation_rating_compared_to_min(row):
    row = {"Cooperation_rating": 0.2, "Cooperation_rating_min": 0.0}

    assert process_data.get_cooporation_rating_compared_to_max(row) == 0.0
