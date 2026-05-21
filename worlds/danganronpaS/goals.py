from typing import TYPE_CHECKING

from rule_builder.rules import HasFromListUnique, CanReachRegion

if TYPE_CHECKING:
    from .world import DanganronpaSWorld

from .items import item_table
from .options import Goal

def set_goal(world: "DanganronpaSWorld"):
    hope_fragments: list[str] = [item_name for item_name in item_table if "Hope Fragment" in item_name]
    hope_fragments += []

    match world.options.goal:
        case Goal.option_school_secret:
            #beat jabberwock boss
            pass
        case Goal.option_graduation:
            # finish story
            world.set_completion_rule(CanReachRegion ("Graduation"))
            pass
        case Goal.option_hope_fragments:
            # macguffin hunt
            world.set_completion_rule(HasFromListUnique(*hope_fragments, count=world.options.fragments.value))
            pass




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