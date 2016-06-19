__author__ = 'Hernan Y.Ke'
class Alert:
    def __init__(self, desc, rule, action):
        self.desc = desc
        self.rule = rule
        self.action = action

    def connect(self, exchange):
        self.exchange = exchange
        dependent_stocks = self.rule.depends_on()
        for stock in dependent_stocks:
            exchange[stock].updated.connect(self.check_rule)

    def check_rule(self, stock):
        if self.rule.matches(self.exchange):
            self.action.execute(self.desc)
