from jsonplaceholder import Jsonplaceholder
from flask import Flask,Response,jsonify

app = Flask(__name__)
jph = Jsonplaceholder()
jph.connect()

@app.route('/users/<id>', methods=['GET'] )
def getUserReport(id):
    try:
        user = jph.get_user_by_id(id)
        if user is not None :
            report = jph.get_user_report_from_email( user["body"]["email"] )
            return jsonify ( report )
        else:
            return Response("{'error':'User not found'}", status=404, mimetype='application/json')
    except Exception as e:
        print ( e )
        return Response("{'error':'Internal server error'}", status=503, mimetype='application/json')

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)
