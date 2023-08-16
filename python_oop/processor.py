# https://ark.intel.com/content/www/us/en/ark.html#@PanelLabel122139

class Processor:

    # Class attribute
    species = "Last generation"

    def __init__(self, company_name:str, panel_label:str, generation:str) -> None:
        self.company_name = company_name
        self.panel_label:str = panel_label
        self.generation = generation


intel_core_i3 = Processor("Intel","Core i3", "10th")
intel_core_i5 = Processor("Intel","Core i5", "11th")
intel_core_i7 = Processor("Intel","Core i7", "12th")
intel_core_i9 = Processor("Intel","Core i9", "13th")

print(intel_core_i3)
print(intel_core_i5)
print(intel_core_i7)
print(intel_core_i9)