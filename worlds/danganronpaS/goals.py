from worlds.danganronpaS.data import characters


##def set_goal(world):
##    goal = world.options.goal.value
##    player = world.player

##    if goal == 0:
##        region = world.get_region("Secret of the School")
##        world.multiworld.completion_condition[player] = lambda state: state.can_reach(region, player)
##    elif goal == 1:
##        region = world.get_region("Arena of Despair")
##        world.multiworld.completion_condition[player] = lambda state: state.can_reach(region, player)
##    elif goal == 2:
##        required_fragments = world.options.fragments
##        ExtraFragments = ["Monodam Hope Fragment", "Monokid Hope Fragment","Monotaro Hope Fragment","Monophanie Hope Fragment","Monosuke Hope Fragment",]
##        world.multiworld.completion_condition[player] = lambda state: (sum(1 for character in characters if state.has(f"{character} Hope Fragment", player)) + sum(1 for fragments in ExtraFragments if state.has(fragments,player))) >= required_fragments