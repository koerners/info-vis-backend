import pandas as pd
from flask import Flask, request, jsonify
from pytrends.request import TrendReq
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/custom', methods=['POST'])
def get_data():
    try:
        if request.method == 'POST':
            kw_list = []
            for val in request.json.values():
                if len(val) > 50 or len(val) < 1:
                    continue
                kw_list.append(str(val))
            results = pd.DataFrame()

            dates = pd.date_range(start='2020-01-01', end="2021-01-01", freq='M')

            pytrends = TrendReq(hl='de-DE')

            for date in dates:
                d = date.strftime("%Y-%m-%d")
                d_ = date.strftime("%Y-%m-") + "01"


                pytrends.build_payload(kw_list, timeframe=str(d_) + " " + str(d),
                                       geo='DE')

                results = results.append(pytrends.interest_over_time())

            results = results.drop_duplicates()
            results.drop(columns=['isPartial'], inplace=True)

            results = results.resample("1d").median()
            results.interpolate(inplace=True)
            results.reset_index(inplace=True)
            results['date'] = results['date'].dt.strftime('%Y-%m-%d')
            results = results[(results.date == '2020-01-28').idxmax():]

            results = results.to_json(orient="index")

            return jsonify(results)

    except Exception as e:
        print(e)
        return e


if __name__ == '__main__':
    app.run()
