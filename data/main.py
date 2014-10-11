from . import tools, prepare
from .states import (fishing, leaderboard, menu, cooler_screen,
                                title_screen, catch_window, creel_screen, fish_screen,
                                tournament_info, intro, stats_screen)                               


def main():
    run_it = tools.Control(prepare.ORIGINAL_CAPTION)
    state_dict = {"TITLE": title_screen.TitleScreen(),
                        "FISHING": fishing.Fishing(),
                        "MENU": menu.Menu(),
                        "COOLER_SCREEN": cooler_screen.CoolerScreen(),
                        "LEADERBOARD": leaderboard.Leaderboard(),
                        "CATCH_WINDOW": catch_window.CatchWindow(),
                        "CREEL_SCREEN": creel_screen.CreelScreen(),
                        "FISH_SCREEN": fish_screen.FishScreen(),
                        "TOURNAMENT_INFO": tournament_info.TournamentInfo(),
                        "INTRO": intro.Intro(), 
                        "STATS_SCREEN": stats_screen.StatsScreen()}
                        
    run_it.setup_states(state_dict, "TITLE")
    run_it.main()
