class Conversion:


    def csgo_to_valorant(self, current_sensitivity):
        final_sensitivity = current_sensitivity/3.18
        return final_sensitivity

    def valorant_to_csgo(self, current_sensitivity):
        final_sensitivity = current_sensitivity * 3.18
        return final_sensitivity
        