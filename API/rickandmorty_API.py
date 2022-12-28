import requests
def get_info(gets):
    url = f'https://rickandmortyapi.com/api/{gets}'
    response = requests.get(url)
    data = response.json() 
    return data


def get_info_for_episode(get):
    url = f'https://rickandmortyapi.com/api/{get}'
    response = requests.get(url)
    data = response.json()
    return data

gets = int(input("Введите id: "))
get = int(input("Номер серии (всего 51): "))

def get_location (gets):
    get_id = get_info(f"character/{gets}")
    for i in get_id.keys():
        if i == "location":
            name = get_id["location"]["name"]
            url_location = get_id["location"]["url"]
            if url_location:
                id_url = url_location.split("/")[-1]
                location = get_info(f"location/{id_url}")
                name_dimension = location["dimension"]
                type_location = location["type"]
                information = f"""
                Нозвание локаци: {name}
                Тип локации: {type_location}
                Измерение: {name_dimension}
                    """
                return information
            else:
                information = f"""
            Нозвание локаци: {name}
            Тип локации: Unknown 
            Измерение: Unknown
                """
                return information
get_location(gets)


def episodes(get):
    get_id_episodes = get_info_for_episode(f"episode/{get}")
    if get <= 51:
        episodes_name =get_id_episodes["name"]
        episodes_air_date = get_id_episodes["air_date"]
        episodes = get_id_episodes["episode"]
        episodes_created = get_id_episodes["created"]
        episodes_information = f"""
        Название эпизода: {episodes_name}
        Дата выхода: {episodes_air_date}
        Эпизод: {episodes}
        Дата создания: {episodes_created}
        """
        return episodes_information
    else:
        return "Такого эпизода нет"
        

def character_episodes(gets):
    get_episodes = get_info(f"character/{gets}")
    for i in get_episodes.keys():
        if i == "episode":
            episodes_information = f"""
            В каких эпизодах был: {get_episodes["episode"]}
            """
    return episodes_information


def get_character_info(gets):
    if gets <= 826:
        character = get_info(f"character/{gets}") 
        information = f"""
        Идентификатор персонажа: {character["id"]}
        Имя персонажа: {character["name"]}
        Его статус:  {character["status"]}
        Гендер: {character["gender"]}
        Раса: {character["species"]}
        Дата создания: {character["created"]}
        {get_location(gets)}
        {character_episodes(gets)}
        {episodes(get)}
        """
        return information
print(get_character_info(gets))

