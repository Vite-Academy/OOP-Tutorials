# https://ark.intel.com/content/www/us/en/ark.html#@PanelLabel122139

from product import Product
class Processor(Product):

    # Class attribute
    species = "Last generation"

    def __init__(self, name:str, company_name:str, panel_label:str, generation:str) -> None:
        self._name = name
        self._company_name = company_name
        self._panel_label = panel_label
        self._generation = generation
    
    def get_panel_label(self):
        return self._panel_label

    
intel_core_i3 = Processor("Intel® Core™ i3-1305U Processor","Intel","Core i3", "10th")
intel_core_i5 = Processor("Intel® Core™ i5-1334U Processor","Intel","Core i5", "11th")
intel_core_i7 = Processor("Intel® Core™ i7-1355U Processor","Intel","Core i7", "12th")
intel_core_i9 = Processor("Intel® Core™ i9-13900KS Processor","Intel","Core i9", "13th")

# print(intel_core_i3) # <__main__.Processor object at 0x7fe2b4e42410>
# print(intel_core_i5) # <__main__.Processor object at 0x7fe2b4e42450>
# print(intel_core_i7) # <__main__.Processor object at 0x7fe2b4e42490>
# print(intel_core_i9) # <__main__.Processor object at 0x7fe2b4e424d0>


# print(id(intel_core_i3)) # 140007546971216
# print(id(intel_core_i5)) # 139655362782288
# print(id(intel_core_i7)) # 140120257209488
# print(id(intel_core_i9)) # 139642534503632


# print(Processor.species) # Last generation
# print(intel_core_i3.species) # Last generation

print(intel_core_i3.get_name())
print(intel_core_i3.get_panel_label())