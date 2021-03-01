from mortgage import Loan

class Engine(object):

    """Docstring for Engine. """

    def __init__(
        self, purchase_price, appraised_price, down_pct, interest,
        property_tax=6000, rent=1700, months=60, appreciation=.05,
        vacancy=.05, management=0.06, closing_cost=.015,
        insurrance=100, capital_expenditure=.05, repair=.03, hoa=25):
        """
        Parameters
        ----------
        purchase_price : TODO
        appraised_price : TODO
        down_pct : TODO
        sell_at : TODO, optional
        appreciation : TODO, optional
        vacancy : TODO, optional
        management : TODO, optional
        property_tax : TODO, optional
        closing_cost : TODO, optional
        insurrance : TODO, optional
        capital_expenditure : TODO, optional
        repair : TODO, optional


        """
        if purchase_price < appraised_price:
            raise ValueError('Purchase price should be larger than bank appraised price.')

        self._purchase_price = purchase_price
        self._appraised_price = appraised_price
        self._down_pct = down_pct
        self._interest = interest
        self._rent = rent
        self._months = months
        self._appreciation = appreciation
        self._vacancy = vacancy
        self._management = management
        self._property_tax = property_tax
        self._closing_cost = closing_cost
        self._insurrance = insurrance
        self._capital_expenditure = capital_expenditure
        self._repair = repair
        self._hoa = hoa
        self._loan = Loan(self.loan_amount, self._interest, term=30)

    @property
    def years(self):
        return self._months / 12

    @property
    def loan_amount(self):
        return self._appraised_price * (1 - self._down_pct)

    @property
    def inital_investment(self):
        val = self._appraised_price * (self._down_pct + self._closing_cost) \
            + (self._purchase_price - self._appraised_price)
        return val

    @property
    def monthly_cash_flow(self):
        return self._rent * (1 - self._vacancy - self._management
                             - self._capital_expenditure - self._repair) \
                - self._hoa - float(self._loan.monthly_payment) \
                - self._property_tax / 12 - self._insurrance

    @property
    def resale_value(self):
        return self._purchase_price * (1 + self._appreciation)**self.years

    @property
    def payoff_at_sale(self):
        return float(self._loan.schedule(self._months).balance)

    @property
    def profit_from_sale(self):
        return self.resale_value * (1 - 0.06) - self.payoff_at_sale

    @property
    def net_profit(self):
        return self.profit_from_sale + 60 * self.monthly_cash_flow \
            - self.inital_investment

    def annual_return(self, type='compound'):
        if type == 'compound':
            return (self.net_profit / self.inital_investment + 1)**(1 / self.years) - 1
        if type == 'average':
            return self.net_profit / self.inital_investment / self.years

        raise NotImplementedError

