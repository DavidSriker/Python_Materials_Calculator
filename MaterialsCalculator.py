import re

# Table of elements
TABLE_OF_ELEMENTS = {'H': 1.008, 'He': 4.003, 'Li': 6.941, 'Be': 9.012, 'B': 10.811, 'C': 12.011,
                     'N': 14.007, 'O': 15.999, 'F': 18.998, 'Ne': 20.18, 'Na': 22.99, 'Mg': 24.305,
                     'Al': 26.982, 'Si': 28.086, 'P': 30.974, 'S': 32.065, 'Cl': 35.453, 'Ar': 39.948,
                     'K': 39.098, 'Ca': 40.078, 'Sc': 44.956, 'Ti': 47.867, 'V': 50.942, 'Cr': 51.996,
                     'Mn': 54.938, 'Fe': 55.845, 'Co': 58.933, 'Ni': 58.693, 'Cu': 63.546, 'Zn': 65.39,
                     'Ga': 69.723, 'Ge': 72.64, 'As': 74.922, 'Se': 78.96, 'Br': 79.904, 'Kr': 83.8,
                     'Rb': 85.468, 'Sr': 87.62, 'Y': 88.906, 'Zr': 91.224, 'Nb': 92.906, 'Mo': 95.94,
                     'Tc': 98, 'Ru': 101.07, 'Rh': 102.906, 'Pd': 106.42, 'Ag': 107.868, 'Cd': 112.411,
                     'In': 114.818, 'Sn': 118.71, 'Sb': 121.76, 'Te': 127.6, 'I': 126.905, 'Xe': 131.293,
                     'Cs': 132.906, 'Ba': 137.327, 'La': 138.906, 'Ce': 140.116, 'Pr': 140.908, 'Nd': 144.24,
                     'Pm': 145, 'Sm': 150.36, 'Eu': 151.964, 'Gd': 157.25, 'Tb': 158.925, 'Dy': 162.5,
                     'Ho': 164.93, 'Er': 167.259, 'Tm': 168.934, 'Yb': 173.04, 'Lu': 174.967, 'Hf': 178.49,
                     'Ta': 180.948, 'W': 183.84, 'Re': 186.207, 'Os': 190.23, 'Ir': 192.217, 'Pt': 195.078,
                     'Au': 196.967, 'Hg': 200.59, 'Tl': 204.383, 'Pb': 207.2, 'Bi': 208.98, 'Po': 209, 'At': 210,
                     'Rn': 222, 'Fr': 223, 'Ra': 226, 'Ac': 227, 'Th': 232.038, 'Pa': 231.036, 'U': 238.029,
                     'Np': 237, 'Pu': 244, 'Am': 243, 'Cm': 247, 'Bk': 247, 'Cf': 251, 'Es': 252, 'Fm': 257,
                     'Md': 258, 'No': 259, 'Lr': 262, 'Rf': 261, 'Db': 262, 'Sg': 266, 'Bh': 264, 'Hs': 277, 'Mt': 268
                     }

IGNORED_ELEMENTS = {'H', 'O', 'C', 'N'}


class materialCalc():
    def __init__(self):
        self.product = ""
        self.product_elements = []
        self.product_elements_amount = []
        self.product_quantity = 0.0
        self.product_molar_mass = 0.0
        self.product_mole = 0.0
        self.reactants = []
        self.reactants_elements = dict()
        self.reactants_elements_amount = dict()
        self.reactants_molar_mass = dict()
        self.reactants_quantity = dict()
        self.units = ""
        self.initiation()
        self.calculation()
        self.printResults()

    def isValidElement(self, elem):
        return elem in TABLE_OF_ELEMENTS

    def elementDecomposition(self, formula):
        splitted_str = re.findall(r'[A-Z][a-z]?[0-9]*[.]?[0-9]*', formula)
        elements_list = []
        quantity_list = []
        for sub_str in splitted_str:
            elem, amount = sub_str.partition(re.findall(r'[A-Z][a-z]?', sub_str)[0])[1:]
            if self.isValidElement(elem):
                elements_list.append(elem)
                if amount == '':
                    quantity_list.append(1.0)
                else:
                    quantity_list.append(float(amount))
        if len(splitted_str) == len(elements_list) and len(splitted_str) == len(quantity_list):
            return elements_list, quantity_list
        else:
            return [], []

    def checkInput(self, in_str, check_flag='f'):
        formula_pattern = re.compile('^[A-Z][a-zA-Z0-9]+$')
        amount_formula = re.compile('^[0-9]+.?[0-9]*$')
        if check_flag == 'f':  # formula check
            valid_formula = False
            if bool(formula_pattern.match(in_str)):
                valid_formula = True
                elements_list, quantity_list = self.elementDecomposition(in_str)
                for elem in elements_list:
                    valid_formula = valid_formula and self.isValidElement(elem)
            return valid_formula
        elif check_flag == 'q':  # amount check
            return bool(amount_formula.match(in_str))

    def getProductData(self):
        proceed = True
        while proceed:
            print("Please provide the desired product formula: ")
            self.product = input()
            if self.checkInput(self.product):
                print("Please provide the desired product amount: ")
                self.product_amount = input()
                if self.checkInput(self.product_amount, 'q'):
                    self.product_amount = float(self.product_amount)
                    print("product: ", self.product, " amount: ", self.product_amount)
                    print("is this correct? [y/n]")
                    ans = input()
                    if ans == 'y':
                        proceed = False
                else:
                    print("The quantity entered is invalid")
            else:
                print("The product entered is invalid")
        return

    def getMassUnits(self):
        proceed = True
        units = ['gram', 'milli-gram']
        while proceed:
            print("Which unit of measure for the amount entered:")
            for i, u in enumerate(units):
                print(i + 1, "-", u)
            choice = input()
            try:
                choice = int(choice)
                if (choice in range(1, len(units) + 1)):
                    self.units = units[(choice + 1) % len(units)]
                    proceed = False
            except:
                print("The value entered is incorrect")
        return

    def getReactantsData(self):
        proceed = True
        total_num_reactants = 0
        print("How many reactants there is? ")
        while proceed:
            print("answer: ")
            total_num_reactants = input()
            try:
                total_num_reactants = int(total_num_reactants)
                proceed = False
            except:
                print("please enter a natural number")

        num_reactants = total_num_reactants
        while num_reactants > 0:
            print("Please enter the", 1 + (total_num_reactants - num_reactants),
                  "reactant out of", total_num_reactants, ":")
            reactant = input()
            if self.checkInput(reactant):
                num_reactants -= 1
                self.reactants.append(reactant)
            else:
                print("The reactant entered is invalid")
        return

    def calculateMolarMass(self, elements, elements_amount):
        mass = 0.0
        for idx, elem in enumerate(elements):
            mass += TABLE_OF_ELEMENTS[elem] * elements_amount[idx]
        return mass

    def setMolarMasses(self):
        self.product_molar_mass = self.calculateMolarMass(self.product_elements, self.product_elements_amount)
        for r in self.reactants:
            self.reactants_molar_mass[r] = self.calculateMolarMass(self.reactants_elements[r],
                                                                   self.reactants_elements_amount[r])
        return

    def isReactionValid(self):
        products = set(self.product_elements)
        reactants_desired_elements = set()
        for r in self.reactants:
            r_elements = set(self.reactants_elements[r])
            common_elements = products.intersection(r_elements)
            common_elements = common_elements.difference(IGNORED_ELEMENTS)
            num_common_elements = len(common_elements)
            if num_common_elements == 0:
                print("The reactant", r, "is unnecessary")
            elif num_common_elements > 1:
                print("The reactant", r, "has to many relevant elements")
            else:
                reactants_desired_elements.union(common_elements)
        return len(reactants_desired_elements.difference(products)) == 0

    def getAmountOfElement(self, element, elements_list, elements_amount_list):
        for idx, elem in enumerate(elements_list):
            if elem == element:
                return elements_amount_list[idx]

    def initiation(self):
        self.getProductData()
        self.getMassUnits()
        self.getReactantsData()
        # once all entered is valid -> decompose to elements and calculate the molar mass
        self.product_elements, self.product_elements_amount = self.elementDecomposition(self.product)
        for r in self.reactants:
            self.reactants_elements[r], self.reactants_elements_amount[r] = self.elementDecomposition(r)
        self.setMolarMasses()
        if not self.isReactionValid():
            print("The reaction is not valid, exiting!")
            exit()

    def calculation(self):
        if self.units == 'milli-gram':
            self.product_amount /= 1000

        self.product_mole = self.product_amount / self.product_molar_mass
        products = set(self.product_elements)
        for r in self.reactants:
            r_elements = set(self.reactants_elements[r])
            common_elements = products.intersection(r_elements)
            common_elements = common_elements.difference(IGNORED_ELEMENTS)

            if len(common_elements) == 1:
                common_elements = common_elements.pop()
                # product moles of element
                p_moles = self.getAmountOfElement(common_elements, self.product_elements,
                                                      self.product_elements_amount)
                r_moles = self.getAmountOfElement(common_elements, self.reactants_elements[r],
                                                      self.reactants_elements_amount[r])
                self.reactants_quantity[r] = (p_moles / r_moles) * self.product_mole * self.reactants_molar_mass[r]
                if self.units == 'milli-gram':
                    self.reactants_quantity[r] *= 1000
            else:
                self.reactants_quantity[r] = 0.0
        return

    def printResults(self):
        print("<===========================================>")
        print("The amount of each reactant is as follows:")
        for idx, r in enumerate(self.reactants):
            print(idx, ":", r, "-", self.reactants_quantity[r], self.units)
        print("<===========================================>")
        return


if __name__ == '__main__':
    materialCalc()