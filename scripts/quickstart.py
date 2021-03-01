import argparse

from housera.engine import Engine


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p', '--purchase_price', required=True, dest='purchase_price', type=float
    )
    parser.add_argument(
        '--appraised-price', required=True, dest='appraised_price', type=float
    )
    parser.add_argument(
        '--down-pct', required=True, dest='down_pct', type=float
    )
    parser.add_argument(
        '-i', '--interest', required=True, dest='interest', type=float
    )
    parser.add_argument(
        '-r', '--rent', required=True, dest='rent', type=float
    )
    parser.add_argument(
        '--property-tax', required=True, dest='property_tax', type=float
    )
    parser.add_argument(
        '--hoa', required=True, dest='hoa', type=float
    )
    parser.add_argument(
        '--appreciation', required=True, dest='appreciation', type=float
    )

    args = parser.parse_args()

    investment = Engine(**args.__dict__)
    print('Inital investment:', investment.inital_investment)
    print('Monthly Cash Flow:', investment.monthly_cash_flow)
    print('Average Annual Return', investment.annual_return('average'))
    print('Compound Annual Return', investment.annual_return('compound'))


if __name__ == "__main__":
    main()
