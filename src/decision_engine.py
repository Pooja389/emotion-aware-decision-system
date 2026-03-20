def decide_action(state, intensity, energy, stress, time_of_day):

    # overload
    if intensity >= 5 or (stress >= 5 and energy <= 2):
        return "grounding", "now"

    # High stress
    if stress >= 4:
        if energy <= 2:
            return "box_breathing", "now"
        return "journaling", "within_15_min"

    # Low energy
    if energy <= 2:
        if time_of_day in ["morning", "afternoon"]:
            return "light_planning", "within_15_min"
        return "rest", "tonight"

    # High energy + good state
    if state in ["focused", "calm"] and energy >= 4:
        return "deep_work", "now"

    # Restless / distracted
    if state in ["restless", "distracted"]:
        return "movement", "within_15_min"

    # Night handling
    if time_of_day == "night" and stress >= 3:
        return "sound_therapy", "tonight"

    return "pause", "within_15_min"