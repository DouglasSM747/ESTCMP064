from users import get_users
from math import sqrt


def recommend(username, users):
    user_min_distance = min_distance(username, users)[1]
    my_user = users[username]
    list_movies = []
    for movie in users[user_min_distance]:
        if movie not in my_user:
            list_movies.append((movie, users[user_min_distance][movie], user_min_distance)),
    return list_movies


# Verifica se o user 1 possui mais filmes que o user 2
# E se o user 2 possui somente os movies do user 1, se isso for verdade return -1
# Pois o user 2 nao vai ter nada para oferecer para o user 1
def is_avaliable_user(user1, user2):
    count_moveis_equals = 0
    for movie in user2:
        if movie in user1:
            count_moveis_equals += 1
    if count_moveis_equals == len(user2):
        return True
    else:
        return False


def pearson(r1, r2):
    if is_avaliable_user(r1, r2):
        return -1

    xiyi = 0
    xi = 0
    yi = 0
    expo_xi = 0
    expo_yi = 0
    band_common = 0

    for movie in r1:
        if movie in r2:
            band_common += 1
            xiyi += (r1[movie] * r2[movie])
            xi += r1[movie]
            expo_xi += pow(r1[movie], 2)

    for movie in r2:
        if movie in r1:
            expo_yi += pow(r2[movie], 2)
            yi += r2[movie]

    value_xi_final = pow(xi, 2) / band_common
    value_yi_final = pow(yi, 2) / band_common

    cor_xi = sqrt(expo_xi - value_xi_final)
    cor_yi = sqrt(expo_yi - value_yi_final)

    if cor_xi * cor_yi == 0:
        return -1
    final_result = (xiyi - ((xi * yi) / band_common)) / (cor_xi * cor_yi)
    return final_result


def min_distance(user_name, users):
    my_user = users[user_name]
    list_distance = []
    for user in users:
        if user != user_name:
            list_distance.append((pearson(my_user, users[user]), user))
    list_distance.sort()
    return list_distance[-1]


def main():
    users = get_users()
    input_user = input("Recomendar sistema para: ")
    result_recomend = recommend(input_user, users)
    result_recomend.sort(key=lambda x: x[1], reverse=True)
    print(result_recomend)


main()
