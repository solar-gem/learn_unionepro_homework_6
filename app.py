from flask import Flask, render_template
import database.DAO.equipmentDAO as request_equipment

app = Flask(__name__)


@app.route('/')
def index():

    data_equipment = request_equipment.getEquipment()
    return render_template('equipment.html', data_equipment=data_equipment)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
