import random


# дата: (зараженные, умершие, выздоровевшие)
RF_DATA = {
    '2020-04-05': (658, 2, 22,),
    '2020-04-06': (954, 8, 51,),
    '2020-04-07': (1154, 11, 88,),
    '2020-04-08': (1175, 5, 86,),
    '2020-04-09': (1459, 13, 118,),
    '2020-04-10': (1789, 18, 97,),
    '2020-04-11': (1667, 12, 250,),
    '2020-04-12': (2186, 24, 246,),
    '2020-04-13': (2558, 18, 179,),
    '2020-04-14': (2774, 22, 224,),
    '2020-04-15': (3388, 28, 292,),
    '2020-04-16': (3448, 34, 318,),
    '2020-04-17': (4070, 41, 286,),
    '2020-04-18': (4785, 40, 467,),
    '2020-04-19': (6060, 48, 234,),
    '2020-04-20': (4268, 44, 155,),
    '2020-04-21': (5642, 51, 457,),
    '2020-04-22': (5236, 57, 547,),
    '2020-04-23': (4774, 42, 471,),
    '2020-04-24': (5849, 60, 677,),
    '2020-04-25': (5966, 66, 682,),
    '2020-04-26': (6361, 66, 517,),
    '2020-04-27': (6198, 50, 579,),
    '2020-04-28': (6411, 72, 1110,),
    '2020-04-29': (5841, 108, 1830,),
    '2020-04-30': (7099, 101, 1133,),
    '2020-05-01': (7933, 96, 1601,),
    '2020-05-02': (9623, 57, 1793,),
    '2020-05-03': (10633, 58, 1626,),
    '2020-05-04': (10581, 76, 1456,),
}

DEATH_USER_ID = []
DISCHARGE_USER_ID = []


def get_infections_csv(path: str) -> None:
    csv = open(path, 'w')
    csv.write('user_id,eventType,time\n')
    user_id = 10000
    for date in RF_DATA:
        for row in range(RF_DATA.get(date)[0]):
            csv.write(f'{user_id},Диагностирован COVID,{date}\n')
            user_id += 1
    csv.close()


def get_death_csv(path: str) -> None:
    csv = open(path, 'w')
    csv.write('user_id,eventType,time\n')
    user_id_start = 10000
    user_id_end = 10000
    for date in RF_DATA:
        for row in range(RF_DATA.get(date)[1]):
            while True:
                death_user_id = random.randint(user_id_start, user_id_end + RF_DATA.get(date)[0])
                if death_user_id not in DEATH_USER_ID:
                    break
            csv.write(f'{death_user_id},Умер от COVID,{date}\n')
            DEATH_USER_ID.append(death_user_id)
        user_id_end += RF_DATA.get(date)[0]
    csv.close()


def get_discharge_csv(path: str) -> None:
    csv = open(path, 'w')
    csv.write('user_id,eventType,time\n')
    user_id_start = 10000
    user_id_end = 10000
    for date in RF_DATA:
        for row in range(RF_DATA.get(date)[2]):
            while True:
                discharge_user_id = random.randint(user_id_start, user_id_end + RF_DATA.get(date)[0])
                if discharge_user_id not in DEATH_USER_ID and discharge_user_id not in DISCHARGE_USER_ID:
                    break
            csv.write(f'{discharge_user_id},Выздоровел от COVID,{date}\n')
            DISCHARGE_USER_ID.append(discharge_user_id)
        user_id_end += RF_DATA.get(date)[0]
    csv.close()


if __name__ == "__main__":
    get_infections_csv('/Users/dirtrider/Downloads/covid_rf.csv')
    get_death_csv('/Users/dirtrider/Downloads/covid_rf_death.csv')
    get_discharge_csv('/Users/dirtrider/Downloads/covid_rf_discharge.csv')
