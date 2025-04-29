import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests


# Поиск по названию на кириллице
def test1_search_books():
    query = "Ноев ковчег"
    headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDYxMDkzMjAsImlhdCI6MTc0NTk0MTMyMCwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6ImI1MjQyYzE1M2ViYTM0ZjMyYmM0OTdkYzk1MzJkMmY3YzgwNzQ2YmMzMGRjZTQ0OWUxYWVkNzkxODFlNjFmYzkiLCJ0eXBlIjoxMH0.ScBHxeIDCAnKsqYW4AHnysiV9gKbq1V5FiBcQQ-BNuM",
    "Cookie": "__ddg10_=1745942721; __ddg1_=eRmzrM4WwZ6gMsJN0LxB; __ddg8_=9sZNo4QNQYoKjcG0; __ddg9_=212.220.227.192",
    "User-Agent": "PostmanRuntime/7.43.3"
    }

 
    # Проверяем результаты поиска
    search_results = requests.get("https://web-gate.chitai-gorod.ru/api/v2/search/product?phrase=" + query + "&customerCityId=11164&sortPreset=relevance&products[page]=1&products[per-page]=60", headers=headers)
    assert search_results.status_code == 200


# Поиск по названию на латинице
def test2_search_books():
    query = "Master and Margarita"
    headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDYxMDkzMjAsImlhdCI6MTc0NTk0MTMyMCwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6ImI1MjQyYzE1M2ViYTM0ZjMyYmM0OTdkYzk1MzJkMmY3YzgwNzQ2YmMzMGRjZTQ0OWUxYWVkNzkxODFlNjFmYzkiLCJ0eXBlIjoxMH0.ScBHxeIDCAnKsqYW4AHnysiV9gKbq1V5FiBcQQ-BNuM",
    "Cookie": "__ddg10_=1745942721; __ddg1_=eRmzrM4WwZ6gMsJN0LxB; __ddg8_=9sZNo4QNQYoKjcG0; __ddg9_=212.220.227.192",
    "User-Agent": "PostmanRuntime/7.43.3"
    }

 
    # Проверяем результаты поиска
    search_results = requests.get("https://web-gate.chitai-gorod.ru/api/v2/search/product?phrase=" + query + "&customerCityId=11164&sortPreset=relevance&products[page]=1&products[per-page]=60", headers=headers)
    assert search_results.status_code == 200


# Поиск с цифрами в названии 
def test3_search_books():
    query = "300 Спартанцев"
    headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDYxMDkzMjAsImlhdCI6MTc0NTk0MTMyMCwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6ImI1MjQyYzE1M2ViYTM0ZjMyYmM0OTdkYzk1MzJkMmY3YzgwNzQ2YmMzMGRjZTQ0OWUxYWVkNzkxODFlNjFmYzkiLCJ0eXBlIjoxMH0.ScBHxeIDCAnKsqYW4AHnysiV9gKbq1V5FiBcQQ-BNuM",
    "Cookie": "__ddg10_=1745942721; __ddg1_=eRmzrM4WwZ6gMsJN0LxB; __ddg8_=9sZNo4QNQYoKjcG0; __ddg9_=212.220.227.192",
    "User-Agent": "PostmanRuntime/7.43.3"
    }

 
    # Проверяем результаты поиска
    search_results = requests.get("https://web-gate.chitai-gorod.ru/api/v2/search/product?phrase=" + query + "&customerCityId=11164&sortPreset=relevance&products[page]=1&products[per-page]=60", headers=headers)
    assert search_results.status_code == 200


# Поиск по произвольному набору символов
def test4_search_books():
    query = "[:/!^&*)"
    headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDYxMDkzMjAsImlhdCI6MTc0NTk0MTMyMCwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6ImI1MjQyYzE1M2ViYTM0ZjMyYmM0OTdkYzk1MzJkMmY3YzgwNzQ2YmMzMGRjZTQ0OWUxYWVkNzkxODFlNjFmYzkiLCJ0eXBlIjoxMH0.ScBHxeIDCAnKsqYW4AHnysiV9gKbq1V5FiBcQQ-BNuM",
    "Cookie": "__ddg10_=1745942721; __ddg1_=eRmzrM4WwZ6gMsJN0LxB; __ddg8_=9sZNo4QNQYoKjcG0; __ddg9_=212.220.227.192",
    "User-Agent": "PostmanRuntime/7.43.3"
    }

 
    # Проверяем результаты поиска
    search_results = requests.get("https://web-gate.chitai-gorod.ru/api/v2/search/product?phrase=" + query + "&customerCityId=11164&sortPreset=relevance&products[page]=1&products[per-page]=60", headers=headers)
    assert search_results.status_code == 422


# Пустой поиск
def test5_search_books():
    query = ""
    headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDYxMDkzMjAsImlhdCI6MTc0NTk0MTMyMCwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6ImI1MjQyYzE1M2ViYTM0ZjMyYmM0OTdkYzk1MzJkMmY3YzgwNzQ2YmMzMGRjZTQ0OWUxYWVkNzkxODFlNjFmYzkiLCJ0eXBlIjoxMH0.ScBHxeIDCAnKsqYW4AHnysiV9gKbq1V5FiBcQQ-BNuM",
    "Cookie": "__ddg10_=1745942721; __ddg1_=eRmzrM4WwZ6gMsJN0LxB; __ddg8_=9sZNo4QNQYoKjcG0; __ddg9_=212.220.227.192",
    "User-Agent": "PostmanRuntime/7.43.3"
    }

 
    # Проверяем результаты поиска
    search_results = requests.get("https://web-gate.chitai-gorod.ru/api/v2/search/product?phrase=" + query + "&customerCityId=11164&sortPreset=relevance&products[page]=1&products[per-page]=60", headers=headers)
    assert search_results.status_code == 400
