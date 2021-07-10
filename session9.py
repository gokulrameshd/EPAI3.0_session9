#importing packages
from faker import  Faker
from collections import namedtuple  
import datetime
from datetime import date 
from decimal import Decimal
import numpy as np
import statistics
import random


fake = Faker()

def get_named_tuple(population):
    '''
    This function generates list of fake person details.
    Attributes : 'name','blood_type','current_location','DOB'
    '''
    info_list = []
    person = namedtuple('person',['name','blood_type','current_location','DOB']) 
    for i in range(population):
        profile =  fake.profile()
        p = person(profile['name'],profile['blood_group'],profile['current_location'],profile['birthdate'])
        info_list.append(p)
    return info_list

def calculateAge(birthDate): 
    '''
    This functions helps to calculate the age from given date to present date.
    '''
    today = date.today() 
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day)) 
    return age 

def get_dict_list(population) :
    info_list = []
    for i in range(population):
        profile =  fake.profile()
        d = {'name':profile['name'],"blood_type":profile['blood_group'],"current_location":profile['current_location'],
            "DOB": profile['birthdate']}
        info_list.append(d)
    return info_list

def cal_mean_current_location(name_tuple_list):
    """
    This function returns the mean current location.
    """
    lan = []
    lon = []
    for i in name_tuple_list:
        lan.append(i.current_location)
        lon.append(i.current_location)
    return np.mean(lan),np.mean(lon)

def named_tuple_cal(population):
    '''
    This function calculates and returns the largest blood type, mean-current_location,
     oldest_person_age ,average age and time taken for calculation using named tuple.
    '''
    t0 = datetime.datetime.now()
    named_tuple_list = get_named_tuple(population)
    lan = []
    lon = []
    age = []
    blood_group = []
    for i in named_tuple_list:
        lan.append(i.current_location[0])
        lon.append(i.current_location[1])
        age.append(calculateAge(i.DOB))
        blood_group.append(i.blood_type)
    try:
        largest_blood_type = statistics.mode(blood_group)
    except:
        uni = np.unique(blood_group)
        c = {}
        mc = 0
        m = ""
        for u in uni:
            c[u] =  blood_group.count(u)
        for u in uni:
            c[u] = blood_group.count(u)
        for k,v in c.items():
            if v > mc :
                m = k
                mc = v
        largest_blood_type = mc
    mean_location = (np.mean(lan),np.mean(lon))
    maximum_age = np.max(age)
    average_age = np.mean(age)
    result = largest_blood_type,mean_location,maximum_age,average_age
    t1 = datetime.datetime.now()
    # print(f'Time taken for claculation{t1-t0}')
    time_elapsed = (t1-t0).total_seconds()
    return result , time_elapsed ,named_tuple_list

def dict_cal(population):
    '''
    This function calculates and returns the
    largest blood type, mean-current_location,
    oldest_person_age ,average age and time taken for calculation using Dictionary.
    '''
    t2 = datetime.datetime.now()
    dict_list = get_dict_list(population)
    lan = [] 
    lon = []
    age = []
    blood_group = []
    for i in dict_list:
        lan.append(i['current_location'][0])
        lon.append(i['current_location'][1])
        age.append(calculateAge(i['DOB']))
        blood_group.append(i['blood_type'])
    try:
        largest_blood_type = statistics.mode(blood_group)
    except:
        uni = np.unique(blood_group)
        m =""
        mc = 0
        c = {}
        for u in uni:
            c[u] =  blood_group.count(u)
        for u in uni:
            c[u] = blood_group.count(u)
        for k,v in c.items():
            if v > mc :
                m = k
                mc = v
        largest_blood_type = m
    #     largest_blood_type = statistics.multimode(blood_group)
    mean_location = (np.mean(lan),np.mean(lon))
    maximum_age = np.max(age)
    average_age = np.mean(age)
    result = largest_blood_type,mean_location,maximum_age,average_age
#     result = statistics.mode(blood_group), (np.mean(lan),np.mean(lon)),np.max(age),np.mean(age)
    t3 = datetime.datetime.now()
    # print(f'Time taken for claculation{t3-t2}')
    time_elapsed = (t3-t2).total_seconds()
    return result,time_elapsed,dict_list

def get_symbol(com_name,i):
    """
    This function returns the symbol for given company name
    """
    symbol = str(i)
    for c in com_name:
        symbol = symbol + '_' + c[0]
    return symbol

def get_random_weights():
    """
    To create dummy weights
    """
    return random.uniform(0,1)

def get_weight(market_capital,total_capital):
    """
    This function return weight calculated based on the market capital
    """
    weight = (market_capital/total_capital)*100
    return weight

def get_weights_list(market_capital_list ,market_sum):
    """
    This function returns list of weights calculated based on the market capital
    and total market capital
    """
    weight_list = []
    for li in market_capital_list:
        weight = get_weight(market_capital = li,total_capital = market_sum)
        weight_list.append(weight)
    return weight_list

def get_random_market_capital():
    """
    This function return random market_capital in range of 500,10000.
    """
    return random.uniform(500,10000) 

def get_market_sum(market_capital_list):
    """
    This function calculate the Total market capital
    """
    total = sum(market_capital_list)
    return total

def update_weight(comp_list , weight_list):
    """
    This function update the weight in the named tuple with the calculated weights
    """
    for c,w in zip(comp_list , weight_list):
        c._replace(weight = w)
    return  comp_list

def get_random_open():
    """
    This function return the random open values 
    """
    return round((random.uniform(300,1000)),2)

def get_high(open_value):
    """
    This function calculates the high value
    """
    return  round(open_value*(random.uniform(1,1.2)),3)

def get_close(high_value):
    """
    This is function returns the close value
    """
    return round(high_value*(random.uniform(0.8,1)),3)

def create_fake_companies_list(no_of_companies):
    """
    This function generates list of fake companies with following attributes,
    'com_name', "symbol", 'open_value', 'high_value', 'close_value','weight'
    """
    company = namedtuple('company',['com_name', "symbol", 'open_value', 'high_value', 'close_value',"weight",'market_capital'])
    companies_list = []
    market_capital_list = []
    for i in range(no_of_companies):
        com_name = fake.company()
        symbol = get_symbol(com_name,i)
        weight = get_random_weights()
        market_capital = get_random_market_capital()
        open_value = get_random_open()
        high_value = get_high(open_value)
        close_value = get_close(high_value)
        companies_list.append(company(com_name,symbol, open_value, high_value, close_value,weight,market_capital))
        market_capital_list.append(market_capital)
    return companies_list,market_capital_list

def get_stockmarket_points(companies_list,weight_list):
    '''
    This function calculates the stock markets opening point , highest point , closing point.
    The points are calculated by multiplying the values with the normalized weights and summing up all the values.
    '''
    open_points = []
    high_points = []
    close_points = []
    sum_weight = sum(weight_list)
    for com in companies_list:
        open_point = com.open_value * com.weight#/sum_weight
        high_point = com.high_value * com.weight#/sum_weight
        close_point = com.close_value * com.weight#/sum_weight
        open_points.append(open_point)
        high_points.append(high_point)
        close_points.append(close_point)
    return round(sum(open_points),2),round(sum(high_points),2),round(sum(close_points),2)