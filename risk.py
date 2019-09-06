import numpy as np

territories = dict(
    NORTH_AMERICA=dict(
        ALASKA=dict(
            boarders=["NW_TERRITORY", "ALBERTA", "KAMCHATKA"],
            stars=1),
        NW_TERRITORY=dict(
            boarders=["ALASKA", "ALBERTA", "ONTARIO", "GREENLAND"],
            stars=2),
        GREENLAND=dict(
            boarders=["NW_TERRITORY", "QUEBEC", "ONTARIO", "ICELAND"],
            stars=1),
        ALBERTA=dict(
            boarders=["NW_TERRITORY", "W_USA", "ONTARIO", "ALASKA"],
            stars=1),
        ONTARIO=dict(
            boarders=["NW_TERRITORY", "W_USA", "ALBERTA", "QUEBEC", "GREENLAND", "E_USA"],
            stars=2),
        QUEBEC=dict(
            boarders=["NW_TERRITORY", "W_USA", "ALBERTA", "QUEBEC", "GREENLAND", "E_USA"],
            stars=1),
        W_USA=dict(
            boarders=["CENTRAL_AMERICA", "ALBERTA", "QUEBEC", "EASTERN_USA", "ONTARIO"],
            stars=1),
        E_USA=dict(
            boarders=["CENTRAL_AMERICA", "ALBERTA", "QUEBEC", "W_USA", "ONTARIO"],
            stars=1),
        CENTRAL_AMERICA=dict(
            boarders=["W_USA", "E_USA", "VENEZUELA"],
            stars=1)),
    SOUTH_AMERICA=dict(
        VENEZUELA=dict(
            boarders=["CENTRAL_AMERICA", "PERU", "BRAZIL"],
            stars=2),
        PERU=dict(
            boarders=["VENEZUELA", "BRAZIL", "ARGENTINA"],
            stars=1),
        BRAZIL=dict(
            boarders=["VENEZUELA", "PERU", "ARGENTINA", "N_AFRICA"],
            stars=1),
        ARGENTINA=dict(
            boarders=["BRAZIL", "PERU"],
            stars=1)),
    EUROPE=dict(
        ICELAND=dict(
            boarders=["GREENLAND", "GREAT_BRITAIN", "SCANDINAVIA"],
            stars=1),
        GREAT_BRITAIN=dict(
            boarders=["ICELAND", "SCANDINAVIA", "W_EUROPE", "N_EUROPE"],
            stars=2),
        SCANDINAVIA=dict(
            boarders=["ICELAND", "GREAT_BRITAIN", "N_EUROPE", "UKRAINE"],
            stars=1),
        UKRAINE=dict(
            boarders=["SCANDINAVIA", "S_EUROPE", "N_EUROPE", "MIDDLE_EAST", "AFGHANISTAN", "URAL"],
            stars=1),
        N_EUROPE=dict(
            boarders=["GREAT_BRITAIN", "SCANDINAVIA", "UKRAINE", "S_EUROPE"],
            stars=1),
        W_EUROPE=dict(
            boarders=["GREAT_BRITAIN", "N_EUROPE", "S_EUROPE", "N_AFRICA"],
            stars=2),
        S_EUROPE=dict(
            boarders=["W_EUROPE", "N_EUROPE", "UKRAINE", "N_AFRICA", "EGYPT", "MIDDLE_EAST"],
            stars=1)),
    AFRICA=dict(
        N_AFRICA=dict(
            boarders=["BRAZIL", "W_EUROPE", "S_EUROPE", "EGYPT", "E_AFRICA", "CONGO"],
            stars=1),
        EGYPT=dict(
            boarders=["N_AFRICA", "E_AFRICA", "MIDDLE_EAST", "S_EUROPE"],
            stars=1),
        E_AFRICA=dict(
            boarders=["N_AFRICA", "EGYPT", "CONGO", "S_AFRICA", "MADAGASCAR", "MIDDLE_EAST"],
            stars=2),
        CONGO=dict(
            boarders=["N_AFRICA", "E_AFRICA", "S_AFRICA"],
            stars=2),
        S_AFRICA=dict(
            boarders=["CONGO", "E_AFRICA", "MADAGASCAR"],
            stars=1),
        MADAGASCAR=dict(
            boarders=["S_AFRICA", "E_AFRICA"],
            stars=1)),
    ASIA=dict(
        MIDDLE_EAST=dict(
            boarders=["EGYPT", "E_AFRICA", "S_EUROPE", "UKRAINE", "AFGHANISTAN", "INDIA"],
            stars=1),
        AFGHANISTAN=dict(
            boarders=["MIDDLE_EAST", "UKRAINE", "URAL", "CHINA", "INDIA"],
            stars=1),
        URAL=dict(
            boarders=["UKRAINE", "AFGHANISTAN", "SIBERIA", "CHINA"],
            stars=2),
        SIBERIA=dict(
            boarders=["URAL", "CHINA", "MONGOLIA", "IRKUTSK", "YAKUTSK"],
            stars=1),
        YAKUTSK=dict(
            boarders=["SIBERIA", "IRKUTSK", "KAMCHATKA"],
            stars=2),
        KAMCHATKA=dict(
            boarders=["ALASKA", "JAPAN", "MONGOLIA", "IRKUTSK", "YAKUTSK"],
            stars=1),
        IRKUTSK=dict(
            boarders=["SIBERIA", "YAKUTSK", "KAMCHATKA", "MONGOLIA"],
            stars=2),
        MONGOLIA=dict(
            boarders=["CHINA", "SIBERIA", "IRKUTSK", "KAMCHATKA", "JAPAN"],
            stars=1),
        CHINA=dict(
            boarders=["SLAM", "INDIA", "AFGHANISTAN", "URAL", "SIBERIA", "MONGOLIA"],
            stars=1),
        INDIA=dict(
            boarders=["MIDDLE_EAST", "AFGHANISTAN", "CHINA", "SLAM"],
            stars=1),
        SLAM=dict(
            boarders=["INDIA", "CHINA", "INDONESIA"],
            stars=1),
        JAPAN=dict(
            boarders=["MONGOLIA", "KAMCHATKA"],
            stars=2)),
    OCEANIA=dict(
        INDONESIA=dict(
            boarders=["SLAM", "W_AUSTRALIA", "NEW_GUINEA"],
            stars=1),
        NEW_GUINEA=dict(
            boarders=["INDONESIA", "W_AUSTRALIA", "E_AUSTRALIA"],
            stars=1),
        W_AUSTRALIA=dict(
            boarders=["NEW_GUINEA", "INDONESIA", "E_AUSTRALIA"],
            stars=1),
        E_AUSTRALIA=dict(
            boarders=["W_AUSTRALIA", "NEW_GUINEA"],
            stars=2)))


def deck_set_up(t_dict):
    d = []
    for cont in t_dict:
        for terr in t_dict[cont]:
            d.append([terr, t_dict[cont][terr].get("stars")])
    return d


def create_player_dict(player_count, player_dict):
    if player_count == 2:
        t = 40
    elif player_count == 3:
        t = 35
    elif player_count == 4:
        t = 30
    elif player_count == 5:
        t = 25
    elif player_count == 6:
        t = 20
    for player in range(1, player_count + 1):
        player_dict.update({"PLAYER_{}".format(player): dict(
            name="Player {}".format(player),
            troops=t,
            stars=0,
            territories=0)})


def board_set_up(first_pick_n, max_players, player_dict, map_dict):
    for cont in map_dict:
        for terr in map_dict[cont]:
            map_dict[cont][terr].update({"occupier": None, "troops": 0})
    pid = first_pick_n
    while True:
        if player_dict["PLAYER_{}".format(pid)].get("troops") > 0:
            player_name = player_dict["PLAYER_{}".format(pid)].get("name")
            hidden_temp = []
            for cont in map_dict:
                hidden_temp.append("\n")
                hidden_temp.append(cont)
                hidden_temp.append("-----------------")
                for terr in map_dict[cont]:
                    if map_dict[cont][terr].get("troops") == 0:
                        hidden_temp.append(terr)
            if len(hidden_temp) > 18:
                for c in hidden_temp:
                    print(c)
                choice_cont = None
                while choice_cont is None:
                    choice = input("{} please enter a territory name to claim it \n".format(player_name))
                    for cont in map_dict:
                        if choice in map_dict[cont] and choice in hidden_temp:
                            choice_cont = cont
                    if choice_cont is None:
                        print("Invalid input. Please copy and paste an open territory into the console")
                player_key = player_dict["PLAYER_{}".format(pid)]
                occupy(map_dict[choice_cont][choice], player_key, player_dict)
                troop_placement(player_key, map_dict[choice_cont][choice], 1)
            else:
                break
        if pid < max_players:
            pid += 1
        else:
            pid = 1
    while sum(t["troops"] for t in player_dict.values() if t) > 0:
        if player_dict["PLAYER_{}".format(pid)].get("troops") > 0:
            player_name = player_dict["PLAYER_{}".format(pid)].get("name")
            for cont in map_dict:
                print()
                print(cont)
                print("-----------------")
                for terr in map_dict[cont]:
                    if map_dict[cont][terr].get("occupier") == player_name:
                        print(terr, "(Troop Strength: {})".format(map_dict[cont][terr].get("troops")))
            choice_cont = None
            while choice_cont is None:
                choice = input("{} please enter a territory name to deploy additional troops to \n".format(player_name))
                for cont in map_dict:
                    if choice in map_dict[cont] and map_dict[cont][choice].get("occupier") == player_name:
                        choice_cont = cont
                        bank = player_dict["PLAYER_{}".format(pid)].get("troops")
                        deployment = None
                        while deployment is None:
                            try:
                                deploy = int(input(
                                    "{} please enter the amount of troops you wish to deploy (Max = {}) \n".format(
                                        player_name, bank)))
                                if deploy <= bank:
                                    deployment = deploy
                                else:
                                    raise ValueError
                            except ValueError:
                                print(
                                    "Error: Value entered must be an integer less than the amount of troops in your bank.")
                if choice_cont is None:
                    print("Invalid input. Please copy and paste an open territory into the console")
            player_key = player_dict["PLAYER_{}".format(pid)]
            troop_placement(player_key, map_dict[choice_cont][choice], deployment)
        if pid < max_players:
            pid += 1
        else:
            pid = 1
    return pid


def occupy(country, player_id, player_dict):
    if country["occupier"] is not None:
        loser = country.get("occupier")
        loser = loser.replace(" ", "_").upper()
        player_dict[loser]["territories"] -= 1
    occupier = player_id.get("name")
    country["occupier"] = occupier
    occupier = occupier.replace(" ", "_").upper()
    player_dict[occupier]["territories"] += 1


def troop_placement(player_bank, in_country, troops):
    print(player_bank, in_country, troops)
    if troops <= player_bank["troops"] and in_country["occupier"] == player_bank["name"]:
        player_bank["troops"] -= troops
        in_country["troops"] += troops
    else:
        print("error")


def troop_transfer(out_country, in_country, troops):
    if troops < out_country["troops"] and out_country["occupier"] == in_country["occupier"]:
        out_country["troops"] -= troops
        in_country["troops"] += troops
    else:
        print("error")


def play(first_pick_n, max_players, player_dict, map_dict, deck_arr):
    pid = first_pick_n
    while max_players > 1:
        player = player_dict["PLAYER_{}".format(pid)]
        terr_count = player.get("territories")
        if terr_count > 0:
            troop_pool = terr_count // 3
            if troop_pool < 3:
                troop_pool = 3
            troop_pool += cont_bonus(player, map_dict)
            stars = player.get("stars")
            if stars > 0:
                trade_in = input(
                    "PLAYER {}, you have {} stars available. Would you like to exchange them [Y/N]".format(pid, stars))
                if trade_in == "Y" or trade_in == "YES" or trade_in == "yes" or trade_in == "y" or trade_in == "Yes":
                    player["stars"], troop_pool = trade_stars(stars, troop_pool)
            player["troops"] = troop_pool
            while player["troops"] > 0:
                player_name = player_dict["PLAYER_{}".format(pid)].get("name")
                for cont in map_dict:
                    print()
                    print(cont)
                    print("-----------------")
                    for terr in map_dict[cont]:
                        if map_dict[cont][terr].get("occupier") == player_name:
                            print(terr, "(Troop Strength: {})".format(map_dict[cont][terr].get("troops")))
                choice_cont = None
                while choice_cont is None:
                    choice = input(
                        "{} please enter a territory name to deploy additional troops to \n".format(player_name))
                    for cont in map_dict:
                        if choice in map_dict[cont] and map_dict[cont][choice].get("occupier") == player_name:
                            deployment = None
                            while deployment is None:
                                try:
                                    deploy = int(input(
                                        "{} please enter the amount of troops you wish to deploy (Max = {}) \n".format(
                                            player_name, player["troops"])))
                                    if 0 >= deploy <= player["troops"]:
                                        deployment = deploy
                                        choice_cont = cont
                                    else:
                                        raise ValueError
                                except ValueError:
                                    print(
                                        "Error: Value entered must be an integer less than the amount of troops in your bank.")
                    if choice_cont is None:
                        print("Invalid input. Please copy and paste an open territory into the console")
                player_key = player_dict["PLAYER_{}".format(pid)]
                troop_placement(player_key, map_dict[choice_cont][choice], deployment)
            can_attack = True
            earned_card = False
            while can_attack:
                attacker_dict = {}
                for cont in map_dict:
                    for terr in map_dict[cont]:
                        if map_dict[cont][terr].get("troops") > 1 and map_dict[cont][terr].get(
                                "occupier") == player_name:
                            neighbors = []
                            n_values = []
                            for bt in map_dict[cont][terr]["boarders"]:
                                for cont_b in map_dict:
                                    for terr_b in map_dict[cont_b]:
                                        if terr_b == bt and map_dict[cont_b][terr_b].get("occupier") != player_name:
                                            neighbors.append(
                                                "{} (Defenders: {})".format(bt, map_dict[cont_b][terr_b].get("troops")))
                                            n_values.append([cont_b, bt, map_dict[cont_b][terr_b].get("troops")])
                            if len(n_values) > 0:
                                attacker_dict.update({terr: dict(cont=cont, troops=map_dict[cont][terr]["troops"],
                                                                 p_boarders=neighbors, v_boarders=n_values,
                                                                 boarders=map_dict[cont][terr]["boarders"])})

                if len(attacker_dict) > 0:
                    for cont in map_dict:
                        print()
                        print(cont)
                        print("-----------------")
                        for terr in attacker_dict:
                            if attacker_dict[terr]["cont"] == cont:
                                print("{} (Attackers: {}) can attack: {}".format(terr,
                                                                                 attacker_dict[terr].get("troops") - 1,
                                                                                 attacker_dict[terr].get("p_boarders")))
                    while True:
                        a_terr = input(
                            "Player {} please enter a territory to attack from or enter DONE to end attack phase.\n".format(
                                pid))
                        if a_terr == "D" or a_terr == "d" or a_terr == "DONE" or a_terr == "Done" or a_terr == "done":
                            print("Ending attack phase..")
                            can_attack = False
                            break
                        elif a_terr in attacker_dict:
                            attacking = True
                            while attacking:
                                print("{} has {} troops available and can attack: {}".format(a_terr,
                                                                                             attacker_dict[a_terr].get(
                                                                                                 "troops") - 1,
                                                                                             attacker_dict[a_terr].get(
                                                                                                 "p_boarders")))
                                d_terr = None
                                while d_terr is None:
                                    target = input(
                                        "Enter the name of the hostile territory that you would like to attack: \n")
                                    if target in attacker_dict[a_terr].get("boarders"):
                                        while True:
                                            try:
                                                attackers = int(input(
                                                    "How many troops would you like to send on this attack? [Max = {}]\n".format(
                                                        attacker_dict[a_terr].get("troops") - 1)))
                                                break
                                            except ValueError:
                                                print("Invalid input.")
                                        d_terr = target
                                    else:
                                        print("Invalid target territory")
                                for i in range(0, len(attacker_dict[a_terr]["v_boarders"])):
                                    if attacker_dict[a_terr]["v_boarders"][i][1] == d_terr:
                                        defenders = attacker_dict[a_terr]["v_boarders"][i][2]
                                        defend_cont = attacker_dict[a_terr]["v_boarders"][i][0]
                                map_dict[attacker_dict[a_terr].get("cont")][a_terr]["troops"] -= attackers
                                wave = 1
                                while attackers > 0 and defenders > 0:
                                    print("Wave: {}".format(wave))
                                    wave += 1
                                    print("Attacker Troops: {} Defending Troops: {}".format(attackers, defenders))
                                    if attackers >= 3 and defenders >= 2:
                                        a_rolls = np.random.randint(1, 7, size=3)
                                        d_rolls = np.random.randint(1, 7, size=2)
                                    elif attackers == 2 and defenders >= 2:
                                        a_rolls = np.random.randint(1, 7, size=2)
                                        d_rolls = np.random.randint(1, 7, size=2)
                                    elif attackers == 1 and defenders >= 2:
                                        a_rolls = np.random.randint(1, 7, size=1)
                                        d_rolls = np.random.randint(1, 7, size=2)
                                    elif attackers == 1 and defenders == 1:
                                        a_rolls = np.random.randint(1, 7, size=1)
                                        d_rolls = np.random.randint(1, 7, size=1)
                                    elif attackers == 2 and defenders == 1:
                                        a_rolls = np.random.randint(1, 7, size=2)
                                        d_rolls = np.random.randint(1, 7, size=1)
                                    elif attackers >= 3 and defenders == 1:
                                        a_rolls = np.random.randint(1, 7, size=3)
                                        d_rolls = np.random.randint(1, 7, size=1)
                                    a_rolls = np.sort(a_rolls)[::-1]
                                    a_survivors = len(a_rolls)
                                    d_rolls = np.sort(d_rolls)[::-1]
                                    print("Attacker Rolls: {}".format(a_rolls))
                                    print("Defender Rolls: {}".format(d_rolls))
                                    for i in range(0, min([len(a_rolls), len(d_rolls)])):
                                        if a_rolls[i] > d_rolls[i]:
                                            defenders -= 1
                                        else:
                                            attackers -= 1
                                            a_survivors -= 1
                                attacking = False
                            if defenders == 0:
                                print("Player {} captured {}!".format(pid, d_terr))
                                if not earned_card:
                                    card_i = np.random.randint(0, len(deck_arr))
                                    card = deck_arr[card_i]
                                    deck_arr.pop(card_i)
                                    player["stars"] += card[1]
                                    print(
                                        "Player {} draws the {} card! {} star(s) have been added to their bank.".format(
                                            pid, card[0], card[1]))
                                    earned_card = True
                                player_key = player_dict["PLAYER_{}".format(pid)]
                                occupy(map_dict[defend_cont][d_terr], player_key, player_dict)
                                transfer_min = a_survivors
                                transfer_max = attackers - transfer_min
                                print("{} troops survived the final invasion wave and must stay in {}.".format(
                                    transfer_min, d_terr))
                                print(
                                    "Player {} has {} reserve invasion troops that can be transferred to {}".format(pid,
                                                                                                                    transfer_max,
                                                                                                                    d_terr))
                                while True:
                                    try:
                                        transfer_request = int(input(
                                            "Enter how many addional troops you would like to transfer (Max = {}) \n".format(
                                                transfer_max)))
                                        if 0 >= transfer_request > transfer_max:
                                            raise ValueError
                                        break
                                    except ValueError:
                                        print("Invalid input!")
                                map_dict[attacker_dict[a_terr].get("cont")][a_terr]["troops"] += (
                                    attackers - (transfer_request + transfer_min))
                                map_dict[defend_cont][d_terr]["troops"] = transfer_request + transfer_min
                                print(
                                    "Troops transferred. Player {} now has {} troops in {} and {} remain in {}".format(
                                        pid, map_dict[defend_cont][d_terr].get("troops"), d_terr,
                                        map_dict[attacker_dict[a_terr].get("cont")][a_terr].get("troops"), a_terr))
                            elif attackers == 0:
                                print("Player {} failed to capture {}!".format(pid, d_terr))
                                map_dict[defend_cont][d_terr]["troops"] = defenders
                            break
                else:
                    print("Player {} has no valid territories to attack from, skipping attack phase.".format(pid))
                    can_attack = False

            if pid < max_players:
                pid += 1
            else:
                pid = 1


def trade_stars(s_pool, t_pool):
    exchange_map = {1: 1, 2: 3, 3: 5, 4: 7, 5: 9, 6: 11, 7: 13}
    print("Stars available to trade: {}".format(s_pool))
    for i in exchange_map:
        print("{} star for {} troops".format(i, exchange_map[i]))
    trade_in = True
    while trade_in:
        try:
            s = int(input("Enter the amount of stars you would like to trade in: \n"))
            if 0 <= s <= s_pool:
                s_pool -= s
                t_pool += (2 * s) - 1
                trade_in = False
            else:
                raise ValueError
        except ValueError:
            print("Invalid input: Please enter an integer between 0 and {}".format(s_pool))
    return s_pool, t_pool


def cont_bonus(p, md):
    bonus = 0
    for cont in md:
        owner = True
        for terr in md[cont]:
            cont_owner = md[cont][terr].get("occupier")
            name = p.get("name")
            if cont_owner != name:
                owner = False
                break
        if owner:
            exchange_map = {"ASIA": 7, "NORTH_AMERICA": 5, "EUROPE": 5, "AFRICA": 3, "SOUTH_AMERICA": 2, "OCEANIA": 2}
            sub_bonus = exchange_map[cont]
            bonus += sub_bonus
    return bonus


def main(t):
    deck = deck_set_up(t)
    players = {}
    p = int(input("Enter 2 to 6 players:"))
    create_player_dict(p, players)
    first_pick = np.random.randint(1, p + 1)
    first_pick = board_set_up(first_pick, p, players, t)
    play(first_pick, p, players, t, deck)


main(territories)
