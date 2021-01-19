from unittest import TestCase
from unittest.mock import patch, call


def get_p_b():
    for p in range(2, 7):
        for b in range(p + 1):
            yield p, b


def get_p_b_pp():
    for p, b in get_p_b():
        for pp in range(1, p + 1):
            yield p, b, pp


class TestCreateDict(TestCase):

    def setUp(self):
        from risk_2 import CreateDict
        self.cd = CreateDict

    def test_territories(self):
        t_dict = self.cd.territories()
        self.assertIsInstance(t_dict, dict)
        self.assertTrue(len(t_dict) == 42)
        for v in t_dict.values():
            self.assertTrue(len(v) == 5)

    def test_players(self):
        for p, b in get_p_b():
            p_dict = self.cd.players(p, b)
            self.assertEqual(len(p_dict), p)
            bots = 0
            for player in p_dict.values():
                if player["bot"]:
                    bots += 1
            self.assertEqual(bots, b)

    def test_continents(self):
        continents = self.cd.continents()
        self.assertIsInstance(continents, dict)
        self.assertEqual(len(continents), 6)

    def test_star_exchange_rate(self):
        ser = self.cd.star_exchange_rate()
        self.assertIsInstance(ser, dict)

    def random_td_pd(self, p, b):
        from random import randint
        td = self.cd.territories()
        pd = self.cd.players(p, b)
        for t in td:
            td[t]["troops"] = randint(1, 2)
            td[t]["occupier"] = pd[randint(1, p)]["name"]
        return td, pd

    def test_attacker(self):
        for p, b, pp in get_p_b_pp():
            td, pd = self.random_td_pd(p, b)
            attack_dict = self.cd.attacker(t_dict=td, p_dict=pd, pnp=pp)
            self.assertIsInstance(attack_dict, dict)
            for c in attack_dict:
                name = pd[pp]["name"]
                self.assertNotIn(name, [x[1] for x in attack_dict[c]])
                self.assertEqual(td[c]["occupier"], name)
                self.assertGreater(td[c]["troops"], 1)

    def test_transfer(self):
        for p, b, pp in get_p_b_pp():
            td, pd = self.random_td_pd(p, b)
            transfer_dict = self.cd.transfer(td, pd, pp)
            self.assertIsInstance(transfer_dict, dict)
            for c in transfer_dict:
                name = pd[pp]["name"]
                self.assertIn(name, [x[1] for x in transfer_dict[c]])
                self.assertEqual(td[c]["occupier"], name)
                self.assertGreater(td[c]["troops"], 1)


class TestDeck(TestCase):
    def setUp(self):
        from risk_2 import CreateDict, Deck
        self.t = CreateDict.territories()
        self.deck = Deck(self.t)

    def test_pop(self):
        l1 = len(self.deck)
        first = self.deck[0]
        popped = self.deck.pop(0)
        l2 = len(self.deck)
        self.assertEqual(first, popped)
        self.assertIs(first, popped)
        self.assertEqual(l1, l2 + 1)

    def test_draw_card(self):
        l = len(self.deck)
        for i in range(1, l + 2):
            deck, card = self.deck.draw_card()
            self.assertEqual(deck, self.deck.deck)
            self.assertIsInstance(deck, type(self.deck.deck))
            self.assertEqual(len(deck), len(self.deck))
            self.assertEqual(len(deck), l - i if i <= l else 0)
            self.assertIsInstance(card[0], str)
            self.assertIsInstance(card[1], int)
            if i == l + 1:
                self.assertEqual(card[1], 0)
            else:
                self.assertGreater(card[1], 0)
            self.assertNotIn(card, deck)


ps = iter([str(p) for p, _ in get_p_b()])
bs = iter([str(b) for _, b in get_p_b()])


def mock_valid_input_p_count(prompt):
    if "number of players:" in prompt.lower():
        return next(ps)
    if "number of bots:" in prompt.lower():
        return next(bs)


def get_ips_iter():
    return iter(["", "-1", "0", "1", "7", "nonnumerical_str", "\n", " ", "6"])


def get_ibs_iter():
    return iter(["", "7", "nonnumerical_str", "\n", " ", "6"])


ips = get_ips_iter()
ibs = get_ibs_iter()


def mock_invalid_input_p_count(prompt):
    if "number of players:" in prompt.lower():
        return next(ips)
    if "number of bots:" in prompt.lower():
        return next(ibs)


def get_wl_iter():
    ns = [f"Player {n}" for n in range(1, 7)]
    return iter([[n for n in ns[:x]] for x in range(1, 7)])


def random_td_pd(p, b):
    from risk_2 import CreateDict
    from random import randint
    td = CreateDict.territories()
    pd = CreateDict.players(p, b)
    for t in td:
        td[t]["troops"] = randint(1, 2)
        td[t]["occupier"] = pd[randint(1, p)]["name"]
    for p in pd:
        pd[p]["stars"] = randint(1, 10)
    return td, pd


def get_c_iter():
    from risk_2 import CreateDict
    return iter([c for c in CreateDict.territories()])


class TestPrompts(TestCase):
    def setUp(self):
        from risk_2 import Prompts
        self.p = Prompts

    def test_player_count(self):
        with patch('builtins.input', mock_valid_input_p_count):
            while not StopIteration:
                p, b = self.p.player_count()
                self.assertIsInstance(p, int)
                self.assertIsInstance(b, int)
                self.assertTrue(2 <= p <= 6)
                self.assertTrue(0 <= b <= p)

        with patch('builtins.input', mock_invalid_input_p_count), patch('sys.stdout') as out:
            p, b = self.p.player_count()
            self.assertEqual(p, 6)
            self.assertEqual(b, 6)
            errs = []
            for e in get_ips_iter():
                if e != "6":
                    errs.append(call.write(f"\nError: {e} is an invalid entry for player count.\n"))
                    errs.append(call.write('\n'))
            for e in get_ibs_iter():
                if e != "6":
                    errs.append(call.write(f"\nError: {e} is an invalid entry for bot count.\n"))
                    errs.append(call.write('\n'))
            out.assert_has_calls(errs)

    def test_goes_first(self):
        with patch('sys.stdout') as out:
            self.p.goes_first(1, 6)
        out.assert_has_calls([call.write("\n1 had the highest roll of [6] and goes first.\n")])

    def test_dice_roll(self):
        with patch('sys.stdout') as out:
            self.p.dice_roll("Player 1", 6)
        out.assert_has_calls([call.write("Player 1 rolls: [6]")])

    def test_tied_rollers(self):
        for wl in get_wl_iter():
            with patch('sys.stdout') as out:
                self.p.tied_rollers(wl, 6)
            out.assert_has_calls([call.write(f"\n{' & '.join(wl).strip(' & ')} tied the highest roll of [6]\n")])
            # print(out.mock_calls)

    def test_display_terrs(self):
        from risk_2 import CreateDict
        import re
        for p, b, pp in get_p_b_pp():
            t_dict = CreateDict.territories()
            p_dict = CreateDict.players(p, b)
            p_name = p_dict[pp]["name"]
            with patch('sys.stdout') as out:
                self.p.display_terrs(t_dict, player=p_name, troop_min=2, attack=True)
            self.assertEqual(len(out.mock_calls), 6 * 4)
            with patch('sys.stdout') as out:
                self.p.display_terrs(t_dict, hide_occ=True)
            self.assertEqual(len(out.mock_calls), (6 * 4) + (42 * 2))
            with patch('sys.stdout') as out:
                self.p.display_terrs(t_dict, player=p_name)
            self.assertEqual(len(out.mock_calls), (6 * 4))
            with patch('sys.stdout') as out:
                self.p.display_terrs(t_dict, player=p_name, troop_min=2, transfer=True)
            self.assertEqual(len(out.mock_calls), (6 * 4))
            t_dict, p_dict = random_td_pd(p, b)
            with patch('sys.stdout') as out:
                self.p.display_terrs(t_dict, player=p_name, troop_min=2, attack=True)
            for c in [
                re.split(
                    r'\s{2,}', str(s).lstrip("call.write('").rstrip("')")
                ) for s in out.mock_calls if "Occupier:" in str(s)
            ]:
                self.assertEqual(t_dict[c[0]]["occupier"], c[1].lstrip("Occupier: "))
                self.assertGreater(t_dict[c[0]]["troops"], 1)
                self.assertEqual(t_dict[c[0]]["troops"], int(c[2].lstrip("Troops: ")))
            with patch('sys.stdout') as out:
                self.p.display_terrs(t_dict, hide_occ=True)
            self.assertEqual(len(out.mock_calls), 6 * 4)
            with patch('sys.stdout') as out:
                self.p.display_terrs(t_dict, player=p_name)
            for c in [
                re.split(
                    r'\s{2,}', str(s).lstrip("call.write('").rstrip("')")
                ) for s in out.mock_calls if "Occupier:" in str(s)
            ]:
                self.assertEqual(t_dict[c[0]]["occupier"], c[1].lstrip("Occupier: "))
            with patch('sys.stdout') as out:
                self.p.display_terrs(t_dict, player=p_name, troop_min=2, transfer=True)
            for c in [
                re.split(
                    r'\s{2,}', str(s).lstrip("call.write('").rstrip("')")
                ) for s in out.mock_calls if "Occupier:" in str(s)
            ]:
                self.assertEqual(t_dict[c[0]]["occupier"], c[1].lstrip("Occupier: "))
                self.assertGreater(t_dict[c[0]]["troops"], 1)

    def test_claim_terr(self):
        from risk_2 import CreateDict
        for p, b, pp in get_p_b_pp():
            player_dict = CreateDict.players(p, b)
            terr_dict = CreateDict.territories()
            c_iter = get_c_iter()

            def mock_valid_input_claim_terr(prompt):
                if "enter a territory name to claim it" in prompt.lower():
                    n = next(c_iter)
                    return n

            for c in terr_dict:
                with patch('builtins.input', mock_valid_input_claim_terr), patch('sys.stdout') as out:
                    claim = self.p.claim_terr(player_dict, terr_dict, pp)
                    self.assertIn(f"Player {pp} claims {claim}", str(out.mock_calls))
                if not player_dict[pp]["bot"]:
                    self.assertEqual(claim, c)

    def test_select_terr(self):
        for p, b, pp in get_p_b_pp():
            t_dict, p_dict = random_td_pd(p, b)
            valid_c_ls = [c for c in t_dict if t_dict[c]["occupier"] == p_dict[pp]["name"]]
            c_iter = iter(valid_c_ls)

            def mock_valid_input_transfer_terrs(prompt):
                return next(c_iter)

            while not StopIteration:
                with patch("builtins.input", mock_valid_input_transfer_terrs):
                    deploy_target = self.p.select_terr(p_dict, t_dict, p_dict[pp]["name"], pp)
                    self.assertIsInstance(deploy_target, str)
                    self.assertIn(deploy_target, t_dict)
            invalid_iter = iter(["INVALID INPUT"] + [valid_c_ls[0]])
            with patch("builtins.input", lambda _: next(invalid_iter)), patch("sys.stdout") as out:
                self.p.select_terr(p_dict, t_dict, p_dict[pp]["name"], pp)
            if not p_dict[pp]["bot"]:
                self.assertIn("Error: INVALID INPUT is not a territory under your control.", str(out.mock_calls))

    def test_troop_level(self):
        for p, b, pp in get_p_b_pp():
            t_dict, p_dict = random_td_pd(p, b)
            pn = p_dict[pp]["name"]
            mt = p_dict[pp]["troops"]
            for t in t_dict:
                for i in range(mt + 1):
                    def mock_valid_troop_level_input(prompt):
                        if f"{pn} Enter the amount of troops you would like to transfer to {t} [Min: 0 Max: {mt}]" in prompt:
                            return i
                        self.fail()

                    with patch("builtins.input", mock_valid_troop_level_input), patch("sys.stdout") as out:
                        troop_target = self.p.troop_level(p_dict, pp, pn, t, minimum=0)
                    if not p_dict[pp]["bot"]:
                        self.assertEqual(troop_target, i)
                    else:
                        self.assertTrue(0 <= troop_target <= mt)
                    self.assertIn(f"{troop_target} troops transferred to {t}", str(out.mock_calls))
            invalid_ls = ["-1", "Nonumerical", "420.69", str(mt + 1), "  ", "/n", "1"]
            invalid_iter = iter(invalid_ls)

            def mock_invalid_troop_input(prompt):
                return next(invalid_iter)

            if not p_dict[pp]["bot"]:
                with patch("builtins.input", mock_invalid_troop_input), patch("sys.stdout") as out:
                    troop_target = self.p.troop_level(p_dict, pp, pn, t, minimum=0)
                self.assertEqual(troop_target, 1)
                for bad_input in iter(invalid_ls[:-1]):
                    self.assertIn(f"Error: {bad_input} is not a valid amount of troops", str(out.mock_calls))
            quick_check_ls = ["0", "1"]
            quick_check_iter = iter(quick_check_ls)
            with patch("builtins.input", lambda _: next(quick_check_iter)), patch("sys.stdout") as out:
                troop_target = self.p.troop_level(p_dict, pp, pn, t)
            if not p_dict[pp]["bot"]:
                self.assertEqual(troop_target, 1)
                self.assertIn(f"Error: 0 is not a valid amount of troops", str(out.mock_calls))
            self.assertIsInstance(troop_target, int)

    def test_star_trade(self):
        y_ls = ["Y", "Yes", "yes", "y", "YES"]
        ex_ls = ["N", "BLAHH", "0"]
        for p, b, pp in get_p_b_pp():
            t_dict, p_dict = random_td_pd(p, b)
            valid_stars_ls = [str(x) for x in range(p_dict[pp]["stars"] + 1)]
            valid_stars_iter = iter(valid_stars_ls)
            y_iter = iter(y_ls * 2)
            star_check = 0

            def mock_valid_star_input(prompt):
                if "Would you like to exchange them [Y/N]" in prompt:
                    return next(y_iter)
                if "Enter the amount of stars you would like to trade in:" in prompt:
                    return next(valid_stars_iter)

            while not StopIteration:
                with patch("builtins.input", mock_valid_star_input), patch("sys.stdout"):
                    stars_out, troops_in = self.p.star_trade(p_dict[pp]["stars"], p_dict[pp]["name"], p_dict, pp)
                self.assertIsInstance(stars_out, int)
                self.assertIsInstance(troops_in, int)
                if not p_dict[pp]["bot"]:
                    self.assertEqual(stars_out, star_check)
            ex_input_iter = iter(ex_ls)

            def mock_exit_input(prompt):
                return next(ex_input_iter)

            while not StopIteration:
                with patch("builtins.input", mock_exit_input), patch("sys.stdout"):
                    stars_out, troops_in = self.p.star_trade(p_dict[pp]["stars"], p_dict[pp]["name"], p_dict, pp)
                if not p_dict[pp]["bot"]:
                    self.assertEqual(stars_out, 0)
                    self.assertEqual(troops_in, 0)

            invalid_in_ls = ["-1", str(p_dict[pp]["stars"] + 1), "NONUMERICAL", "\n", "0"]
            invalid_in_iter = iter(invalid_in_ls)

            def mock_invalid_star_input(prompt):
                if "Would you like to exchange them [Y/N]" in prompt:
                    return "Y"
                if "Enter the amount of stars you would like to trade in:" in prompt:
                    return next(invalid_in_iter)
                self.fail()

            with patch("builtins.input", mock_invalid_star_input), patch("sys.stdout") as out:
                stars_out, troops_in = self.p.star_trade(p_dict[pp]["stars"], p_dict[pp]["name"], p_dict, pp)
                if not p_dict[pp]["bot"]:
                    self.assertEqual(stars_out, 0)
                    self.assertEqual(troops_in, 0)
                    self.assertIn("is not a valid entry.", str(out.mock_calls))

    def test_load_autosave(self):
        for y in ("Y", "y", "YES", "Yes", "yes"):
            with patch("builtins.input", lambda _: y):
                confirm = self.p.load_autosave()
                self.assertTrue(confirm)
        for n in ("N", "No", "NO", "no", "n"):
            with patch("builtins.input", lambda _: n):
                confirm = self.p.load_autosave()
                self.assertFalse(confirm)

    # def test_transfer(self):
    #     self.fail()
#
#     def test_transfer_count(self):
#         self.fail()
#
#     def test_attacker(self):
#         self.fail()
#
#     def test_attacker_force(self):
#         self.fail()
#
#
# class TestGameFunctions(TestCase):
#     def test_pnp_turner(self):
#         self.fail()
#
#     def test_banked_troops(self):
#         self.fail()
#
#     def test_unclaimed_terrs(self):
#         self.fail()
#
#     def test_roll_to_go_first(self):
#         self.fail()
#
#     def test_claim_territories(self):
#         self.fail()
#
#     def test_deploy_additional_troops(self):
#         self.fail()
#
#     def test_no_winner(self):
#         self.fail()
#
#     def test_cont_bonus(self):
#         self.fail()
#
#     def test_star_trade_in(self):
#         self.fail()
#
#     def test_add_banked_troops(self):
#         self.fail()
#
#     def test_battle(self):
#         self.fail()
#
#     def test_get_loser_id(self):
#         self.fail()
#
#     def test_battle_report(self):
#         self.fail()
#
#     def test_attack_stage(self):
#         self.fail()
#
#     def test_fortify_stage(self):
#         self.fail()
#
#     def test_play(self):
#         self.fail()
#
#     def test_auto_save_save(self):
#         self.fail()
#
#     def test_auto_save_load(self):
#         self.fail()
#
#     def test_main(self):
#         self.fail()
