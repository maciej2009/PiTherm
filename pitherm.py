__author__ = 'MALU'
# coding=utf-8
# !/usr/bin/python
# module: PiConnect.py

# TODO: Dodac swieta
# TODO: Dodac mozlwiosc wlaczenia przyciskiem
# TODO: Dodac regule, jezeli czujka ruchu wykrywa obecnosc domownika

import ConfigParser


def parReadConfig():
    conf = ConfigParser.ConfigParser()
    conf.read("pitherm.cfg")

    global par
    par = {
        # DB
        'db_server' : conf.get('DB', 'db_server'),
        'db_name' :conf.get('DB', 'db_name'),
        'db_username' : conf.get('DB', 'db_username'),
        'db_password' : conf.get('DB', 'db_password'),

        # TODO: Zastanowić się czy te paraetry mają sens.
        'db_timeinterval': float(conf.get('DB', 'db_timeinterval')),
        'db_delay': float(conf.get('DB', 'db_delay')),

        # Pogoda
        'czuj_zew_ID' : conf.get('Pogoda', 'czuj_zew'),
        'czuj_zew_time_read_interval' : conf.get('Pogoda', 'czuj_zew_time_read_interval'),
        'czuj_zew_time_DB_interval' : conf.get('Pogoda', 'czuj_zew_time_read_interval'),

        # Zbiornik


        # General
        'temp_timeinterval': float(conf.get('General', 'temp_timeinterval')),
        'log_loginglevel' : conf.get('General', 'logginglevel'),
        'okresgrzewczy' : bool(int(conf.get('General', 'okresgrzewczy'))),

        # Czujniki
        'czuj_co_zas' : conf.get('Czujniki', 'czuj_co_zas'),
        'czuj_co_return' : conf.get('Czujniki', 'czuj_co_return'),
        'czuj_buf_top' : conf.get('Czujniki', 'czuj_buf_top'),
        'czuj_buf_mid' : conf.get('Czujniki', 'czuj_buf_mid'),
        'czuj_buf_low' : conf.get('Czujniki', 'czuj_buf_low'),
        'czuj_wew_01' : conf.get('Czujniki', 'czuj_wew_01'),
        'czuj_wew_02' : conf.get('Czujniki', 'czuj_wew_02'),
        'czuj_wew_03' : conf.get('Czujniki', 'czuj_wew_03'),
        'czuj_wew_04' : conf.get('Czujniki', 'czuj_wew_04'),
        'czuj_wew_05' : conf.get('Czujniki', 'czuj_wew_05'),
        'czuj_wew_06' : conf.get('Czujniki', 'czuj_wew_06'),
        'czuj_wew_07' : conf.get('Czujniki', 'czuj_wew_07'),
        'czuj_wew_08' : conf.get('Czujniki', 'czuj_wew_08'),
        'czuj_wew_09' : conf.get('Czujniki', 'czuj_wew_09'),
        'czuj_wew_10' : conf.get('Czujniki', 'czuj_wew_10'),
        'czuj_cwu' : conf.get('Czujniki', 'czuj_cwu'),
        'czuj_cwu_cyr' : conf.get('Czujniki', 'czuj_cwu_cyr'),

        # Styczniki

        'st_taryfa' : int(conf.get('Styczniki', 'st_taryfa')),
        'st_co_pompa' : int(conf.get('Styczniki', 'st_co_pompa')),
        'st_co_zawor_otw' : int(conf.get('Styczniki', 'st_co_zawor_otw')),
        'st_co_zawor_zam' : int(conf.get('Styczniki', 'st_co_zawor_zam')),
        'st_grzalka_1' : int(conf.get('Styczniki', 'st_grzalka_1')),
        'st_grzalka_2' : int(conf.get('Styczniki', 'st_grzalka_2')),
        'st_grzalka_3' : int(conf.get('Styczniki', 'st_grzalka_3')),
        'st_cwu_pompa_cyr' : int(conf.get('Styczniki', 'st_cwu_pompa_cyr')),

         # CWU
        'cwu_okno_1_start' : conf.get('CWU', 'cwu_okno_1_start'),
        'cwu_okno_1_stop' : conf.get('CWU', 'cwu_okno_1_stop'),
        'cwu_okno_1_days' : conf.get('CWU', 'cwu_okno_1_days'),
        'cwu_okno_1_temp' : int(conf.get('CWU', 'cwu_okno_1_temp')),
        'cwu_okno_1_hist' : int(conf.get('CWU', 'cwu_okno_1_hist')),
        'cwu_okno_2_start' : conf.get('CWU', 'cwu_okno_2_start'),
        'cwu_okno_2_stop' : conf.get('CWU', 'cwu_okno_2_stop'),
        'cwu_okno_2_days' : conf.get('CWU', 'cwu_okno_2_days'),
        'cwu_okno_2_temp' : int(conf.get('CWU', 'cwu_okno_2_temp')),
        'cwu_okno_2_hist' : int(conf.get('CWU', 'cwu_okno_2_hist')),
        'cwu_okno_3_start' : conf.get('CWU', 'cwu_okno_3_start'),
        'cwu_okno_3_stop' : conf.get('CWU', 'cwu_okno_3_stop'),
        'cwu_okno_3_days' : conf.get('CWU', 'cwu_okno_3_days'),
        'cwu_okno_3_temp' : int(conf.get('CWU', 'cwu_okno_3_temp')),
        'cwu_okno_3_hist' : int(conf.get('CWU', 'cwu_okno_3_hist')),
        'cwu_okno_4_start' : conf.get('CWU', 'cwu_okno_4_start'),
        'cwu_okno_4_stop' : conf.get('CWU', 'cwu_okno_4_stop'),
        'cwu_okno_4_days' : conf.get('CWU', 'cwu_okno_4_days'),
        'cwu_okno_4_temp' : int(conf.get('CWU', 'cwu_okno_4_temp')),
        'cwu_okno_4_hist' : int(conf.get('CWU', 'cwu_okno_4_hist')),
        'cwu_okno_5_start' : conf.get('CWU', 'cwu_okno_5_start'),
        'cwu_okno_5_stop' : conf.get('CWU', 'cwu_okno_5_stop'),
        'cwu_okno_5_days' : conf.get('CWU', 'cwu_okno_5_days'),
        'cwu_okno_5_temp' : int(conf.get('CWU', 'cwu_okno_5_temp')),
        'cwu_okno_5_hist' : int(conf.get('CWU', 'cwu_okno_5_hist')),
        'cwu_okno_6_start' : conf.get('CWU', 'cwu_okno_6_start'),
        'cwu_okno_6_stop' : conf.get('CWU', 'cwu_okno_6_stop'),
        'cwu_okno_6_days' : conf.get('CWU', 'cwu_okno_6_days'),
        'cwu_okno_6_temp' : int(conf.get('CWU', 'cwu_okno_6_temp')),
        'cwu_okno_6_hist' : int(conf.get('CWU', 'cwu_okno_6_hist')),

         # CO

        'co_okno_1_start' : conf.get('CO', 'co_okno_1_start'),
        'co_okno_1_stop' : conf.get('CO', 'co_okno_1_stop'),
        'co_okno_1_days' : conf.get('CO', 'co_okno_1_days'),
        'co_okno_1_temp' : int(conf.get('CO', 'co_okno_1_temp')),
        'co_okno_1_hist' : int(conf.get('CO', 'co_okno_1_hist')),
        'co_okno_2_start' : conf.get('CO', 'co_okno_2_start'),
        'co_okno_2_stop' : conf.get('CO', 'co_okno_2_stop'),
        'co_okno_2_days' : conf.get('CO', 'co_okno_2_days'),
        'co_okno_2_temp' : int(conf.get('CO', 'co_okno_2_temp')),
        'co_okno_2_hist' : int(conf.get('CO', 'co_okno_2_hist')),
        'co_okno_3_start' : conf.get('CO', 'co_okno_3_start'),
        'co_okno_3_stop' : conf.get('CO', 'co_okno_3_stop'),
        'co_okno_3_days' : conf.get('CO', 'co_okno_3_days'),
        'co_okno_3_temp' : int(conf.get('CO', 'co_okno_3_temp')),
        'co_okno_3_hist' : int(conf.get('CO', 'co_okno_3_hist')),
        'co_okno_4_start' : conf.get('CO', 'co_okno_4_start'),
        'co_okno_4_stop' : conf.get('CO', 'co_okno_4_stop'),
        'co_okno_4_days' : conf.get('CO', 'co_okno_4_days'),
        'co_okno_4_temp' : int(conf.get('CO', 'co_okno_4_temp')),
        'co_okno_4_hist' : int(conf.get('CO', 'co_okno_4_hist')),
        'co_okno_5_start' : conf.get('CO', 'co_okno_5_start'),
        'co_okno_5_stop' : conf.get('CO', 'co_okno_5_stop'),
        'co_okno_5_days' : conf.get('CO', 'co_okno_5_days'),
        'co_okno_5_temp' : int(conf.get('CO', 'co_okno_5_temp')),
        'co_okno_5_hist' : int(conf.get('CO', 'co_okno_5_hist')),
        'co_okno_6_start' : conf.get('CO', 'co_okno_6_start'),
        'co_okno_6_stop' : conf.get('CO', 'co_okno_6_stop'),
        'co_okno_6_days' : conf.get('CO', 'co_okno_6_days'),
        'co_okno_6_temp' : int(conf.get('CO', 'co_okno_6_temp')),
        'co_okno_6_hist' : int(conf.get('CO', 'co_okno_6_hist')),

        # Taryfy
        'taryfa1_cena' : float(conf.get('Taryfy', 'taryfa1_cena')),
        'taryfa2_cena' : float(conf.get('Taryfy', 'taryfa2_cena')),

        'taryfa2_1_dni' : conf.get('Taryfy', 'taryfa2_1_dni'),
        'taryfa2_1_godz_start' : conf.get('Taryfy', 'taryfa2_1_godz_start'),
        'taryfa2_1_godz_stop' : conf.get('Taryfy', 'taryfa2_1_godz_stop'),

        'taryfa2_2_dni' : conf.get('Taryfy', 'taryfa2_2_dni'),
        'taryfa2_2_godz_start' : conf.get('Taryfy', 'taryfa2_2_godz_start'),
        'taryfa2_2_godz_stop' : conf.get('Taryfy', 'taryfa2_2_godz_stop'),

        'taryfa2_3_dni' : conf.get('Taryfy', 'taryfa2_3_dni'),
        'taryfa2_3_godz_start' : conf.get('Taryfy', 'taryfa2_3_godz_start'),
        'taryfa2_3_godz_stop' : conf.get('Taryfy', 'taryfa2_3_godz_stop'),

        'taryfa2_4_dni' : conf.get('Taryfy', 'taryfa2_4_dni'),
        'taryfa2_4_godz_start' : conf.get('Taryfy', 'taryfa2_4_godz_start'),
        'taryfa2_4_godz_stop' : conf.get('Taryfy', 'taryfa2_4_godz_stop'),

        'taryfa2_5_dni' : conf.get('Taryfy', 'taryfa2_5_dni'),
        'taryfa2_5_godz_start' : conf.get('Taryfy', 'taryfa2_5_godz_start'),
        'taryfa2_5_godz_stop' : conf.get('Taryfy', 'taryfa2_5_godz_stop'),

        'taryfa2_6_dni' : conf.get('Taryfy', 'taryfa2_6_dni'),
        'taryfa2_6_godz_start' : conf.get('Taryfy', 'taryfa2_6_godz_start'),
        'taryfa2_6_godz_stop' : conf.get('Taryfy', 'taryfa2_6_godz_stop'),

        # Piec
        'poziom1' : conf.getint('Piec', 'poziom1'),
        'poziom2' : conf.getint('Piec', 'poziom2'),
        'poziom3' : conf.getint('Piec', 'poziom3'),
        'poziom4' : conf.getint('Piec', 'poziom4'),
        'poziom5' : conf.getint('Piec', 'poziom5'),
        'poziom6' : conf.getint('Piec', 'poziom6'),
        'piec_delta_temp' : conf.getint('Piec','piec_delta_temp'),
        'piec_delta_time' : conf.getint('Piec','piec_delta_time')*60,

        # Pomieszczenia
        'pom1_temp' : int(conf.get('Pomieszczenia', 'pom1_temp')),
        'pom1_hist': float(conf.get('Pomieszczenia', 'pom1_hist')),
        'pom1_nazwa' : conf.get('Pomieszczenia', 'pom1_nazwa')
        }



