class Conversion:


    def csgo_to_valorant(self, csgo_sensitivity):
        final_sensitivity = csgo_sensitivity/3.18
        print("Your valorant sensitivity should be: ", final_sensitivity)

    def valorant_to_csgo(self, valorant_sensitivity):
        final_sensitivity = valorant_sensitivity * 3.18
        print("Your csgo sensitivity should be: ", final_sensitivity)
        