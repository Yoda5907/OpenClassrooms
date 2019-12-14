class Account:
    """ une classe de gestion d'un compte bancaire
    Cette classe permet de créer un compte bancaire
    et d'eefectuer des opérations de dépôtrs et retrait"""
    _id = 0
    _balance = 100.0
    _currency = "€"
    overdraft = False
    rate = 0.75
    date_joint = ""
    client = None

    def __init__(self, _id, client, _balance = 100.0, _currency="€"):
        self._id = _id
        self.client = client
        self._balance = _balance
        self._currency = _currency
    
    def getId(self):
        return self._id
    def getBalance(self):
        return "{:.2f} {}".format(self._balance, self._currency)
    
    def setId(self, _id):
        """ setter de l'identifiant """
        self._id = _id
    
    def setBalance(self, balance):
        self._balance = balance
        self._updateOverdraft()
    
        
    def deposit(self, value):
        if(isinstance(value, float) and value > 0):
            self._modify_balance(value)
    
    def withdraw(self, value):
        if(isinstance(value, float) and value > 0):
            self._modify_balance( -1 * value)
    
    def _modify_balance(self, value):
        self._balance += value
        self._updateOverdraft()
    
    def _updateOverdraft(self):
        self.overdraft = bool(self._balance < 0)

    def getClientName(self):
        return self.client.getFullName()

class Person:
    _id = 0
    first_name = ""
    last_name = ""
    
    def __init__(self, _id, f, l):
        self._id = _id
        self.first_name = f
        self.last_name = l
    
    def getFullName(self):
        return self.first_name + " " + self.last_name

class Client(Person):
    _id = 0
    date_joint = ""
    #le constructeur doit tenir compte des attributs hérités de Person
    def __init__(self, _id, dj, _idc, f, l):
        #appel au constructeur de la classe mère
        super().__init__(_idc, f, l)
        #initialisation des attibuts propres
        self._id = _id
        self.date_joint = dj
    
    def getDateJoint(self):
        return self.date_joint
