import pytest

from housera import engine


@pytest.fixture
def investment():
    return engine.Engine(330000, 280000, 0.25, 0.032)


def test_loan_amount(investment):
    assert investment.loan_amount == 210000


def test_inital_investment(investment):
    assert investment.inital_investment == 124200


def test_monthly_payment(investment):
    assert float(investment._loan.monthly_payment) == pytest.approx(908.18)


def test_monthly_cash_flow(investment):
    assert investment.monthly_cash_flow == pytest.approx(-156.18)


def test_resale_value(investment):
    assert investment.resale_value == pytest.approx(421172.91)


def test_profit_from_sale(investment):
    assert investment.profit_from_sale == pytest.approx(208524.8)


def test_avg_annual_return(investment):
    assert investment.annual_return('average') == pytest.approx(0.12069, abs=1e-4)


def test_compound_annual_return(investment):
    assert investment.annual_return('compound') == pytest.approx(0.099, abs=1e-3)
