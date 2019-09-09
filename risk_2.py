import numpy as np
import pickle


class Deck:
    @staticmethod
    # Call to create and return deck array.
    # Example: deck = Deck.set_up(t_dict)
    def set_up(t_dict):
        deck_arr = []
        for terr in t_dict:
            deck_arr.append([terr, t_dict[terr].get("stars")])
        return deck_arr

    @staticmethod
    # Call to draw a card from the deck array.
    # Example: deck, card = Deck.draw_card(deck)
    def draw_card(deck_arr):
        if len(deck_arr) > 0:
            card_i = np.random.randint(0, len(deck_arr))
            c = deck_arr[card_i]
            deck_arr.pop(card_i)
        else:
            c = ["There are no Cards left in the deck.", 0]
        return deck_arr, c


class CreateDict:
    @staticmethod
    # Call to create and return  territories dict.
    # Example: t_dict = CreateDict.territories()
    def territories():
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
                    boarders=["CENTRAL_AMERICA", "ALBERTA", "QUEBEC", "E_USA", "ONTARIO"],
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
                JAPAN=dict(
                    boarders=["MONGOLIA", "KAMCHATKA"],
                    stars=2),
                CHINA=dict(
                    boarders=["SLAM", "INDIA", "AFGHANISTAN", "URAL", "SIBERIA", "MONGOLIA"],
                    stars=1),
                INDIA=dict(
                    boarders=["MIDDLE_EAST", "AFGHANISTAN", "CHINA", "SLAM"],
                    stars=1),
                SLAM=dict(
                    boarders=["INDIA", "CHINA", "INDONESIA"],
                    stars=1)),
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
        out = {}
        for cont in territories:
            cont_dict = territories[cont]
            for terr in cont_dict:
                terr_dict = cont_dict[terr]
                terr_dict.update({"occupier": None, "troops": 0, "cont": cont})
                out.update({terr: terr_dict})
        return out

    @staticmethod
    # Call to create and return the players dict.
    # Note: player_count must be between 2 and 6, use Prompts.player_count() to get and validate player_count)
    # Example: p_dict = CreateDict.players(p_count)
    def players(player_count):
        player_dict = {}
        if player_count == 2:
            t = 40
        elif player_count == 3:
            t = 35
        elif player_count == 4:
            t = 30
        elif player_count == 5:
            t = 25
        else:
            t = 20
        for player_id in range(1, player_count + 1):
            player_dict.update({player_id: dict(
                name="Player {}".format(player_id),
                troops=t,
                stars=0,
                territories=0,
                id=player_id)})
        return player_dict

    @staticmethod
    def continents():
        return {"NORTH_AMERICA": 5, "SOUTH_AMERICA": 2, "AFRICA": 3, "EUROPE": 5, "ASIA": 7, "OCEANIA": 2}

    @staticmethod
    def star_exchange_rate():
        return {1: 1, 2: 3, 3: 5, 4: 7, 5: 9, 6: 11, 7: 13}

    @staticmethod
    def attacker(t_dict, p_dict, pnp):
        p_name = p_dict[pnp]["name"]
        attacker_dict = {}
        for terr in t_dict:
            if t_dict[terr]["occupier"] == p_name and t_dict[terr]["troops"] > 1:
                neighbors = []
                for bt in t_dict[terr]["boarders"]:
                    for terr_b in t_dict:
                        if terr_b == bt and t_dict[terr_b]["occupier"] != p_name:
                            neighbors.append([bt, t_dict[terr_b]["occupier"], t_dict[terr_b]["troops"]])
                if len(neighbors) > 0:
                    attacker_dict.update({terr: neighbors})
        return attacker_dict

    @staticmethod
    def transfer(t_dict, p_dict, pnp):
        p_name = p_dict[pnp]["name"]
        transfer_dict = {}
        for terr in t_dict:
            if t_dict[terr]["occupier"] == p_name and t_dict[terr]["troops"] > 1:
                neighbors = []
                for bt in t_dict[terr]["boarders"]:
                    for terr_b in t_dict:
                        if terr_b == bt and t_dict[terr_b]["occupier"] == p_name:
                            neighbors.append([bt, t_dict[terr_b]["occupier"], t_dict[terr_b]["troops"]])
                if len(neighbors) > 0:
                    transfer_dict.update({terr: neighbors})
        return transfer_dict


class Prompts:
    @staticmethod
    # Call to prompt for and validate the users requested number of players.
    # Example: p_count = Prompts.player_count()
    def player_count():
        while True:
            p_count = input("\nEnter a number from 2 to 6 in order to set the number of players:\n")
            try:
                p_count = int(p_count)
                if 2 <= p_count <= 6:
                    return p_count
                raise ValueError
            except ValueError:
                print("\nError: {} is an invalid entry for player count.\n".format(p_count))

    @staticmethod
    def goes_first(player_in_play, high_roll):
        print("\n{} had the highest roll of [{}] and goes first.\n".format(player_in_play, high_roll))

    @staticmethod
    def dice_roll(player_name, rolls):
        print("{} rolls: [{}]".format(player_name, rolls))

    @staticmethod
    def tied_rollers(winners_list, high_roll):
        winners = ""
        for winner in winners_list:
            if winners == "":
                winners += winner[1]
            else:
                winners += (" & " + winner[1])
        print("\n{} tied the highest roll of [{}]\n".format(winners, high_roll))
        return winners_list

    @staticmethod
    def display_terrs(t_dict, hide_occ=False, player=None, troop_min=0, attack=False, transfer=False):
        conts = CreateDict.continents()
        for cont in conts:
            bonus = conts[cont]
            print("\n{}\nContinent bonus: {} troops per turn".format(cont, bonus))
            print("-----------------")
            for terr in t_dict:
                if t_dict[terr]["cont"] == cont:
                    occ = t_dict[terr]["occupier"]
                    troops = t_dict[terr]["troops"]
                    boarders = ""
                    for b in t_dict[terr]["boarders"]:
                        if attack:
                            if boarders == "" and t_dict[b]["occupier"] != player:
                                s = "{} ({} troops: {})".format(b, t_dict[b]["occupier"], t_dict[b]["troops"])
                                boarders += s
                            elif t_dict[b]["occupier"] != player:
                                s = ", {} ({} troops: {})".format(b, t_dict[b]["occupier"], t_dict[b]["troops"])
                                boarders += s
                        elif transfer:
                            if boarders == "" and t_dict[b]["occupier"] == player:
                                s = "{} ({} troops: {})".format(b, t_dict[b]["occupier"], t_dict[b]["troops"])
                                boarders += s
                            elif t_dict[b]["occupier"] == player:
                                s = ", {} ({} troops: {})".format(b, t_dict[b]["occupier"], t_dict[b]["troops"])
                                boarders += s
                        elif boarders == "":
                            s = "{} ({} troops: {})".format(b, t_dict[b]["occupier"], t_dict[b]["troops"])
                            boarders += s
                        else:
                            s = ", {} ({} troops: {})".format(b, t_dict[b]["occupier"], t_dict[b]["troops"])
                            boarders += s
                    if hide_occ:
                        if occ is None:
                            print("{}{}Occupier: {}{}Troops: {}{}Boarders: {}".format(
                                terr,
                                " " * (17 - len(terr)),
                                occ,
                                " " * (10 - len(str(occ))),
                                troops,
                                " " * (3 - len(str(troops))),
                                boarders))
                    elif player is not None:
                        if attack:
                            btag = "Hostile"
                            if occ == player and troops >= troop_min and len(boarders) > 0:
                                print("{}{}Occupier: {}{}Troops: {}{}{} Boarders: {}".format(
                                    terr,
                                    " " * (17 - len(terr)),
                                    occ,
                                    " " * (10 - len(str(occ))),
                                    troops,
                                    " " * (3 - len(str(troops))),
                                    btag,
                                    boarders))
                        elif transfer:
                            btag = "Friendly"
                            if occ == player and troops >= troop_min and len(boarders) > 0:
                                print("{}{}Occupier: {}{}Troops: {}{}{} Boarders: {}".format(
                                    terr,
                                    " " * (17 - len(terr)),
                                    occ,
                                    " " * (10 - len(str(occ))),
                                    troops,
                                    " " * (3 - len(str(troops))),
                                    btag,
                                    boarders))
                        else:
                            btag = ""
                            if occ == player and troops >= troop_min:
                                print("{}{}Occupier: {}{}Troops: {}{}{} Boarders: {}".format(
                                    terr,
                                    " " * (17 - len(terr)),
                                    occ,
                                    " " * (10 - len(str(occ))),
                                    troops,
                                    " " * (3 - len(str(troops))),
                                    btag,
                                    boarders))

                    else:
                        print("{}{}Occupier: {}{}Troops: {}{}Boarders: {}".format(
                            terr,
                            " " * (17 - len(terr)),
                            occ,
                            " " * (10 - len(str(occ))),
                            troops,
                            " " * (3 - len(str(troops))),
                            boarders))

    @staticmethod
    def claim_terr(p_dict, t_dict, pnp):
        claimable = []
        for t in t_dict:
            if t_dict[t]["occupier"] is None:
                claimable.append(t)
        p_name = p_dict[pnp]["name"]
        while True:
            try:
                claim = input("\n{} enter a territory name to claim it \n".format(p_name))
                if claim in claimable:
                    print("{} claims {}".format(p_name, claim))
                    return claim
                raise ValueError
            except ValueError:
                print("\nError: {} is not a claimable territory name.\n".format(claim))

    @staticmethod
    def select_terr(t_dict, p_name):
        selectable = []
        for t in t_dict:
            if t_dict[t]["occupier"] == p_name:
                selectable.append(t)
        while True:
            try:
                selection = input("\n{} enter a territory name to supply with additional troops \n".format(p_name))
                if selection in selectable:
                    return selection
                raise ValueError
            except ValueError:
                print("\nError: {} is not a territory under your control.\n".format(selection))

    @staticmethod
    def troop_level(p_dict, pnp, p_name, target, minimum=1):
        troop_cap = p_dict[pnp]["troops"]
        while True:
            try:
                level = input(
                    "\n{} Enter the amount of troops you would like to transfer to {} [Min: {} Max: {}]\n".format(p_name,
                                                                                                                target,
                                                                                                                minimum,
                                                                                                                troop_cap))
                level = int(level)
                if minimum <= level <= troop_cap:
                    print("\n{} troops transferred to {}\n".format(level, target))
                    return level
                raise ValueError
            except ValueError:
                print("\nError: {} is not a valid amount of troops\n".format(level))

    @staticmethod
    def star_trade(stars, p_name):
        stars_out, troops_in = 0, 0
        confirm = input(
            "\n{}, you have {} stars available. Would you like to exchange them [Y/N]\n".format(p_name, stars))
        if confirm == "YES" or confirm == "YES" or confirm == "yes" or confirm == "y" or confirm == "Yes":
            exchange_map = CreateDict.star_exchange_rate()
            print("Stars available to trade: {}".format(stars))
            for i in exchange_map:
                print("{} star for {} troops".format(i, exchange_map[i]))
            trade_in = True
            while trade_in:
                try:
                    s = int(input("\nEnter the amount of stars you would like to trade in: \n"))
                    if 0 <= s <= stars:
                        stars_out = s
                        troops_in = (2 * s) - 1
                        return stars_out, troops_in
                    raise ValueError
                except ValueError:
                    print("\nError: {} is not a valid entry.\n".format(s))
        else:
            return stars_out, troops_in

    @staticmethod
    def load_autosave():
        confirm = input("\nAn autosave file was found would you like to load it? [Y/N]\n(Warning: Starting a new game "
                        "will overwrite the autosave file)\n")
        if confirm == "No" or confirm == "NO" or confirm == "no" or confirm == "n" or confirm == "N":
            return False
        else:
            return True

    @staticmethod
    def transfer(transfer_dict, name):
        while True:
            try:
                request = input(
                    "\n{} please enter a territory to transfer troops from or enter DONE to end the reinforcement phase.\n".format(
                        name))
                if request == "D" or request == "d" or request == "DONE" or request == "Done" or request == "done":
                    print("\nEnding reinforcement phase..\n")
                    return request, 0
                for terr in transfer_dict:
                    if terr == request:
                        print("\n{} can reinforce:\n--------------".format(request))
                        b_list = []
                        for b in transfer_dict[terr]:
                            b_list.append(b[0])
                            print("{}{}troops: {}".format(b[0], " " * (17 - len(b[0])), b[2]))
                        while True:
                            try:
                                request_b = input("\n{} please enter a territory to transfer troops to.\n".format(name))
                                if request_b in b_list:
                                    return request, request_b
                                raise ValueError
                            except ValueError:
                                print(
                                    "\nError: {} is not a valid territory name that you can transfer troops to.\n".format(
                                        request_b))
                raise ValueError
            except ValueError:
                print("\nError: {} is not a valid territory name that you can transfer troops to.\n".format(request))

    @staticmethod
    def transfer_count(terr_out, terr_in, t_dict, p_name):
        transfer_cap = t_dict[terr_out]["troops"] - 1
        while True:
            try:
                request = input("\n{} can transfer a maximum of {} troops from {} to {}. \n Enter how many troops you "
                                "want to transfer:\n".format(p_name, transfer_cap, terr_out, terr_in))
                request = int(request)
                if 0 <= request <= transfer_cap:
                    return request
                raise ValueError
            except ValueError:
                print(
                    "\nError: {} is not a valid amount of troops that you can transfer.\n".format(request))

    @staticmethod
    def attacker(attacker_dict, name):
        while True:
            try:
                request = input(
                    "\n{} please enter a territory to attack from or enter DONE to end attack phase.\n".format(
                        name))
                if request == "D" or request == "d" or request == "DONE" or request == "Done" or request == "done":
                    print("\nEnding attack phase..\n")
                    return request, 0

                for terr in attacker_dict:
                    if terr == request:
                        print("\n{} can attack:\n--------------".format(request))
                        b_list = []
                        for b in attacker_dict[terr]:
                            b_list.append(b[0])
                            print("{}{}occupier: {} troops: {}".format(b[0], " " * (17 - len(b[0])), b[1], b[2]))
                        while True:
                            try:
                                request_b = input("\n{} please enter a territory to attack.\n".format(name))
                                if request_b in b_list:
                                    return request, request_b
                                raise ValueError
                            except ValueError:
                                print("\nError: {} is not a valid territory name that you can attack.\n".format(
                                    request_b))
                raise ValueError
            except ValueError:
                print("\nError: {} is not a valid territory name that you can attack from.\n".format(request))

    @staticmethod
    def attacker_force(att_terr, def_terr, t_dict, p_name):
        attacker_cap = t_dict[att_terr]["troops"] - 1
        while True:
            try:
                attackers = input("\n{} can attack {} with a maximum of {} troops from {}. \n Enter how many troops you "
                                  "want to send on this attack\n".format(p_name, def_terr, attacker_cap, att_terr))
                attackers = int(attackers)
                if 0 <= attackers <= attacker_cap:
                    return attackers
                raise ValueError
            except ValueError:
                print(
                    "\nError: {} is not a valid amount of troops that you can use for this attack.\n".format(attackers))


def pnp_turner(pnp, p_count):
    if pnp == p_count:
        pnp = 1
    else:
        pnp += 1
    return pnp


def banked_troops(p_dict):
    for pid in p_dict:
        if p_dict[pid]["troops"] > 0:
            return True
    return False


def unclaimed_terrs(terr_dict):
    for terr in terr_dict:
        if terr_dict[terr]["occupier"] is None:
            return True
    return False


def roll_to_go_first(player_dict):
    rollers = []
    for pid in player_dict:
        rollers.append([player_dict[pid].get("id"), player_dict[pid].get("name"), None])
    while True:
        high_roll = 0
        for p in range(0, len(rollers)):
            p_name = rollers[p][1]
            roll = np.random.randint(1, 7)
            Prompts.dice_roll(p_name, roll)
            rollers[p][2] = roll
            if roll > high_roll:
                high_roll = roll
        winners = []
        for item in rollers:
            if item[2] == high_roll:
                winners.append(item)
        if len(winners) == 1:
            Prompts.goes_first(winners[0][1], high_roll)
            return winners[0][0]
        else:
            rollers = Prompts.tied_rollers(winners, high_roll)


def claim_territories(terr_dict):
    p_count = Prompts.player_count()
    player_dict = CreateDict.players(p_count)
    pnp = roll_to_go_first(player_dict)
    while unclaimed_terrs(terr_dict):
        Prompts.display_terrs(terr_dict, hide_occ=True)
        claim = Prompts.claim_terr(player_dict, terr_dict, pnp)
        terr_dict[claim]["occupier"] = player_dict[pnp]["name"]
        player_dict[pnp]["territories"] += 1
        terr_dict[claim]["troops"] += 1
        player_dict[pnp]["troops"] -= 1
        pnp = pnp_turner(pnp, p_count)
    return terr_dict, player_dict, pnp, p_count


def deploy_additional_troops(t_dict, p_dict, pnp, player_max=6, turner=True, battle=False):
    while banked_troops(p_dict):
        if p_dict[pnp]["troops"] > 0:
            p_name = p_dict[pnp]["name"]
            Prompts.display_terrs(t_dict, player=p_name)
            deploy_target = Prompts.select_terr(t_dict, p_name)
            if battle:
                troop_target = Prompts.troop_level(p_dict, pnp, p_name, deploy_target, minimum=0)
            else:
                troop_target = Prompts.troop_level(p_dict, pnp, p_name, deploy_target)
            t_dict[deploy_target]["troops"] += troop_target
            p_dict[pnp]["troops"] -= troop_target
        if turner:
            pnp = pnp_turner(pnp, player_max)
    return t_dict, p_dict


def no_winner(t_dict):
    winner = None
    for t in t_dict:
        if winner is None:
            winner = t_dict[t]["occupier"]
        elif t_dict[t]["occupier"] != winner:
            return True
    return False


def cont_bonus(p_dict, t_dict, pnp):
    bonus = 0
    conts = CreateDict.continents()
    p_name = p_dict[pnp]["name"]
    temp = {}
    for cont in conts:
        temp.update({cont: {}})
        for terr in t_dict:
            if t_dict[terr]["cont"] == cont:
                temp[cont].update({terr: dict(occupier=t_dict[terr]["occupier"])})
    for cont in temp:
        owner = True
        for terr in temp[cont]:
            if temp[cont][terr]["occupier"] != p_name:
                owner = False
                break
        if owner:
            bonus += conts[cont]
    p_dict[pnp]["troops"] += bonus
    return p_dict


def star_trade_in(p_dict, pnp):
    stars = p_dict[pnp]["stars"]
    p_name = p_dict[pnp]["name"]
    if stars > 0:
        stars_out, troops_in = Prompts.star_trade(stars, p_name)
        p_dict[pnp]["stars"] -= stars_out
        p_dict[pnp]["troops"] += troops_in
    return p_dict


def add_banked_troops(p_dict, t_dict, pnp):
    p_dict[pnp]["troops"] = p_dict[pnp]["territories"] // 3
    if p_dict[pnp]["troops"] < 3:
        p_dict[pnp]["troops"] = 3
    p_dict = cont_bonus(p_dict, t_dict, pnp)
    p_dict = star_trade_in(p_dict, pnp)
    return p_dict


def battle(t_dict, p_dict, att_terr, def_terr, attackers):
    t_dict[att_terr]["troops"] -= attackers
    wave = 1
    while attackers > 0 and t_dict[def_terr]["troops"] > 0:
        print("Wave: {}".format(wave))
        wave += 1
        print("Attacking Troops: {} Defending Troops: {}".format(attackers, t_dict[def_terr]["troops"]))
        if attackers >= 3 and t_dict[def_terr]["troops"] >= 2:
            a_rolls = np.random.randint(1, 7, size=3)
            d_rolls = np.random.randint(1, 7, size=2)
        elif attackers == 2 and t_dict[def_terr]["troops"] >= 2:
            a_rolls = np.random.randint(1, 7, size=2)
            d_rolls = np.random.randint(1, 7, size=2)
        elif attackers == 1 and t_dict[def_terr]["troops"] >= 2:
            a_rolls = np.random.randint(1, 7, size=1)
            d_rolls = np.random.randint(1, 7, size=2)
        elif attackers == 1 and t_dict[def_terr]["troops"] == 1:
            a_rolls = np.random.randint(1, 7, size=1)
            d_rolls = np.random.randint(1, 7, size=1)
        elif attackers == 2 and t_dict[def_terr]["troops"] == 1:
            a_rolls = np.random.randint(1, 7, size=2)
            d_rolls = np.random.randint(1, 7, size=1)
        elif attackers >= 3 and t_dict[def_terr]["troops"] == 1:
            a_rolls = np.random.randint(1, 7, size=3)
            d_rolls = np.random.randint(1, 7, size=1)
        a_rolls = np.sort(a_rolls)[::-1]
        a_survivors = len(a_rolls)
        d_rolls = np.sort(d_rolls)[::-1]
        print("Attacker Rolls: {}".format(a_rolls))
        print("Defender Rolls: {}".format(d_rolls))
        for i in range(0, min([len(a_rolls), len(d_rolls)])):
            if a_rolls[i] > d_rolls[i]:
                t_dict[def_terr]["troops"] -= 1
            else:
                attackers -= 1
                a_survivors -= 1
    return t_dict, p_dict, attackers, a_survivors


def get_loser_id(loser_name, p_dict):
    for p in p_dict:
        if p_dict[p]["name"] == loser_name:
            return p_dict[p]["id"]


def battle_report(t_dict, p_dict, attackers, a_survivors, pnp, deck, earned_card, att_terr, def_terr, p_name):
    if t_dict[def_terr]["troops"] == 0:
        print("{} captured {}!".format(p_name, def_terr))
        if not earned_card:
            card_i = np.random.randint(0, len(deck))
            card = deck[card_i]
            deck.pop(card_i)
            p_dict[pnp]["stars"] += card[1]
            print(
                "\n{} draws the {} card! {} star(s) have been added to their bank.\n".format(
                    p_name, card[0], card[1]))
            earned_card = True
        loser_name = t_dict[def_terr]["occupier"]
        loser_id = get_loser_id(loser_name, p_dict)
        p_dict[loser_id]["territories"] -= 1
        loser_stars = 0
        if p_dict[loser_id]["territories"] <= 0:
            loser_stars = p_dict[loser_id]["stars"]
            print("{} lost their last territory. {} collects an additional {} stars from {}'s bank".format(loser_name,
                                                                                                           p_name,
                                                                                                           loser_stars,
                                                                                                           loser_name))
        t_dict[def_terr]["occupier"] = p_name
        p_dict[pnp]["territories"] += 1
        p_dict[pnp]["stars"] += loser_stars
        transfer_min = a_survivors
        transfer_max = (attackers - transfer_min)
        print("{} troops survived the final invasion wave and must stay in {}.".format(transfer_min, def_terr))
        print("{} has {} reserve invasion troops that can be transferred to {}".format(p_name, transfer_max, def_terr))
        if transfer_max > 0:
            while True:
                try:
                    transfer_request = int(input(
                        "Enter how many additional troops you would like to transfer (Max = {}) \n".format(
                            transfer_max)))
                    if 0 > transfer_request > transfer_max:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid input!")
        else:
            transfer_request = 0
        t_dict[att_terr]["troops"] += attackers - (transfer_request + transfer_min)
        t_dict[def_terr]["troops"] = transfer_request + transfer_min
        print("Troops transferred. {} now has {} troops in {} and {} remain in {}".format(p_name,
                                                                                          t_dict[def_terr]["troops"],
                                                                                          def_terr,
                                                                                          t_dict[att_terr]["troops"],
                                                                                          att_terr))
    elif attackers == 0:
        print("Player {} failed to capture {}!".format(p_name, def_terr))
    return t_dict, p_dict, deck, earned_card


def attack_stage(t_dict, p_dict, pnp, deck):
    can_attack = True
    earned_card = False
    while can_attack:
        attacker_dict = CreateDict.attacker(t_dict, p_dict, pnp)
        if len(attacker_dict) > 0:
            p_name = p_dict[pnp]["name"]
            Prompts.display_terrs(t_dict, player=p_name, troop_min=2, attack=True)
            att_terr, def_terr = Prompts.attacker(attacker_dict, p_name)
            if def_terr == 0:
                can_attack = False
            else:
                attackers = Prompts.attacker_force(att_terr, def_terr, t_dict, p_name)
                t_dict, p_dict, attackers, a_survivors = battle(t_dict, p_dict, att_terr, def_terr, attackers)
                t_dict, p_dict, deck, earned_card = battle_report(t_dict, p_dict, attackers, a_survivors, pnp, deck,
                                                                  earned_card, att_terr, def_terr, p_name)
        else:
            print("{} has no valid territories to attack from, skipping attack phase.".format(p_name))
            can_attack = False
    return t_dict, p_dict, deck


def fortify_stage(t_dict, p_dict, pnp):
    transfer_dict = CreateDict.transfer(t_dict, p_dict, pnp)
    p_name = p_dict[pnp]["name"]
    if len(transfer_dict) > 0:
        Prompts.display_terrs(t_dict, player=p_name, troop_min=2, transfer=True)
        terr_out, terr_in = Prompts.transfer(transfer_dict, p_name)
        if terr_in != 0:
            transfer_count = Prompts.transfer_count(terr_out, terr_in, t_dict, p_name)
            t_dict[terr_out]["troops"] -= transfer_count
            t_dict[terr_in]["troops"] += transfer_count
    else:
        print("{} has no valid territories to transfer troops from, skipping fortify phase.".format(p_name))
    return t_dict, p_dict


def play(t_dict, p_dict, pnp, p_count, deck):
    while no_winner(t_dict):
        if p_dict[pnp]["territories"] > 0:
            auto_save_save(t_dict, p_dict, pnp, p_count, deck)
            p_dict = add_banked_troops(p_dict, t_dict, pnp)
            t_dict, p_dict = deploy_additional_troops(t_dict, p_dict, pnp, turner=False, battle=True)
            t_dict, p_dict, deck = attack_stage(t_dict, p_dict, pnp, deck)
            t_dict, p_dict = fortify_stage(t_dict, p_dict, pnp)
        pnp = pnp_turner(pnp, p_count)
    winner = t_dict["JAPAN"]["occupier"]
    print("{} won the game!".format(winner))


def auto_save_load():
    try:
        pickle_in = open("autosave.pickle", "rb")
        confirm = Prompts.load_autosave()
        if confirm:
            game_state = pickle.load(pickle_in)
            return game_state[0], game_state[1], game_state[2], game_state[3], game_state[4]
        raise FileNotFoundError

    except FileNotFoundError:
        t_dict, p_dict, pnp, p_count, deck = None, None, None, None, None
        game_state = [t_dict, p_dict, pnp, p_count, deck]
        pickle_out = open("autosave.pickle", "wb")
        pickle.dump(game_state, pickle_out)
        pickle_out.close()
        return t_dict, p_dict, pnp, p_count, deck


def auto_save_save(t_dict, p_dict, pnp, p_count, deck):
    game_state = [t_dict, p_dict, pnp, p_count, deck]
    pickle_out = open("autosave.pickle", "wb")
    pickle.dump(game_state, pickle_out)
    pickle_out.close()


def main():
    t_dict, p_dict, pnp, p_count, deck = auto_save_load()
    if pnp is None:
        t_dict = CreateDict.territories()
        deck = Deck.set_up(t_dict)
        t_dict, p_dict, pnp, p_count = claim_territories(t_dict)
        t_dict, p_dict = deploy_additional_troops(t_dict, p_dict, pnp, player_max=p_count)
    play(t_dict, p_dict, pnp, p_count, deck)


main()
