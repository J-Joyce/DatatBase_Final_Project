from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



# Flask application setup
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///peoples_record.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Table model
class users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    role_id = db.Column(db.Integer, nullable=False)

class user_logs(db.Model):
    log_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    action = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class updated (db.Model):
    update_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    field_name = db.Column(db.String(120), nullable=False)
    details = db.Column(db.Text, nullable=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

class roles(db.Model):
    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)

class elections(db.Model):
    election_id = db.Column(db.Integer, primary_key=True)
    election_type = db.Column(db.String(120), nullable=False)
    election_date = db.Column(db.Date, nullable=False)
    voter_turnout = db.Column(db.Float, nullable=False)
    total_votes = db.Column(db.Integer, nullable=False)
    winner = db.Column(db.String(120), nullable=False)

class states(db.Model):
    state_id = db.Column(db.Integer, primary_key=True)
    state_name = db.Column(db.String(120), unique=True, nullable=False)
    population = db.Column(db.Integer, nullable=False)
    registered_voters = db.Column(db.Integer, nullable=False)
    voter_turnout = db.Column(db.Float, nullable=False)
    voter_age_range = db.Column(db.String(50), nullable=False)

class parties(db.Model):
    party_id = db.Column(db.Integer, primary_key=True)
    party_name = db.Column(db.String(120), unique=True, nullable=False)

class counties(db.Model):
    county_id = db.Column(db.Integer, primary_key=True)
    county_name = db.Column(db.String(120), unique=True, nullable=False)
    population = db.Column(db.Integer, nullable=False)
    registered_voters = db.Column(db.Integer, nullable=False)
    senate_number = db.Column(db.String(10), nullable=False)
    house_number = db.Column(db.String(10), nullable=False)
    congress_number = db.Column(db.String(10), nullable=False)

class congress(db.Model):
    congress_id = db.Column(db.Integer, primary_key=True)
    population = db.Column(db.Integer, nullable=False)
    registered_voters = db.Column(db.Integer, nullable=False)
    voter_turnout = db.Column(db.Float, nullable=False)
    election_id = db.Column(db.Integer, db.ForeignKey('elections.election_id'), nullable=False)
    county_id = db.Column(db.Integer, db.ForeignKey('counties.county_id'), nullable=False)
    term_start = db.Column(db.Date, nullable=False)
    term_end = db.Column(db.Date, nullable=False)
    party_id = db.Column(db.Integer, db.ForeignKey('parties.party_id'), nullable=False)

class house(db.Model):
    house_id = db.Column(db.Integer, primary_key=True)
    population = db.Column(db.Integer, nullable=False)
    registered_voters = db.Column(db.Integer, nullable=False)
    voter_turnout = db.Column(db.Float, nullable=False)
    election_id = db.Column(db.Integer, db.ForeignKey('elections.election_id'), nullable=False)
    county_id = db.Column(db.Integer, db.ForeignKey('counties.county_id'), nullable=False)
    term_start = db.Column(db.Date, nullable=False)
    term_end = db.Column(db.Date, nullable=False)
    party_id = db.Column(db.Integer, db.ForeignKey('parties.party_id'), nullable=False)

class senate(db.Model):
    senate_id = db.Column(db.Integer, primary_key=True)
    population = db.Column(db.Integer, nullable=False)
    registered_voters = db.Column(db.Integer, nullable=False)
    voter_turnout = db.Column(db.Float, nullable=False)
    election_id = db.Column(db.Integer, db.ForeignKey('elections.election_id'), nullable=False)
    county_id = db.Column(db.Integer, db.ForeignKey('counties.county_id'), nullable=False)
    term_start = db.Column(db.Date, nullable=False)
    term_end = db.Column(db.Date, nullable=False)
    party_id = db.Column(db.Integer, db.ForeignKey('parties.party_id'), nullable=False)

class federal_senate(db.Model):
    federal_senate_id = db.Column(db.Integer, primary_key=True)
    population = db.Column(db.Integer, nullable=False)
    registered_voters = db.Column(db.Integer, db.ForeignKey("states.registered_voters"), nullable=False)
    voter_turnout = db.Column(db.Float, db.ForeignKey("states.voter_turnout"),  nullable=False)
    election_id = db.Column(db.Integer, db.ForeignKey('elections.election_id'), nullable=False)
    state_id = db.Column(db.Integer, db.ForeignKey('states.state_id'), nullable=False)
    term_start = db.Column(db.Date, nullable=False)
    term_end = db.Column(db.Date, nullable=False)
    party_id = db.Column(db.Integer, db.ForeignKey('parties.party_id'), nullable=False)

class governor(db.Model):
    governor_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), nullable=False)
    party_id = db.Column(db.Integer, db.ForeignKey('parties.party_id'), nullable=False)
    state_id = db.Column(db.Integer, db.ForeignKey('states.state_id'), nullable=False)
    election_id = db.Column(db.Integer, db.ForeignKey('elections.election_id'), nullable=False)
    voter_turnout = db.Column(db.Float, nullable=False)
    term_start = db.Column(db.Date, nullable=False)
    term_end = db.Column(db.Date, nullable=False)

class supreme_court(db.Model):
    supreme_court_id = db.Column(db.Integer, primary_key=True)
    justice_name = db.Column(db.String(120), nullable=False)
    state_id = db.Column(db.Integer, db.ForeignKey('states.state_id'), nullable=False)
    election_id = db.Column(db.Integer, db.ForeignKey('elections.election_id'), nullable=False)
    term_start = db.Column(db.Date, nullable=False)
    term_end = db.Column(db.Date, nullable=True)

class board_of_education(db.Model):
    board_id = db.Column(db.Integer, primary_key=True)
    member_name = db.Column(db.String(120), nullable=False)
    county_id = db.Column(db.Integer, db.ForeignKey('counties.county_id'), nullable=False)
    election_id = db.Column(db.Integer, db.ForeignKey('elections.election_id'), nullable=False)
    term_start = db.Column(db.Date, nullable=False)
    term_end = db.Column(db.Date, nullable=False)

class secretary_of_state(db.Model):
    secretary_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    state_id = db.Column(db.Integer, db.ForeignKey('states.state_id'), nullable=False)
    election_id = db.Column(db.Integer, db.ForeignKey('elections.election_id'), nullable=False)
    party_id = db.Column(db.Integer, db.ForeignKey('parties.party_id'), nullable=False)
    term_start = db.Column(db.Date, nullable=False)
    term_end = db.Column(db.Date, nullable=False)

class ballot_measures(db.Model):
    measure_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    election_id = db.Column(db.Integer, db.ForeignKey('elections.election_id'), nullable=False)
    votes_for = db.Column(db.Integer, nullable=False)
    votes_against = db.Column(db.Integer, nullable=False)
    passed = db.Column(db.Boolean, nullable=False)

class candidates(db.Model):
    candidate_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    party_id = db.Column(db.Integer, db.ForeignKey('parties.party_id'), nullable=False)
    election_id = db.Column(db.Integer, db.ForeignKey('elections.election_id'), nullable=False)
    position = db.Column(db.String(120), nullable=False)

class precincts(db.Model):
    precinct_id = db.Column(db.Integer, primary_key=True)
    county_id = db.Column(db.Integer, db.ForeignKey('counties.county_id'), nullable=False)
    population = db.Column(db.Integer, nullable=False)
    registered_voters = db.Column(db.Integer, nullable=False)
    voter_turnout = db.Column(db.Float, nullable=False)

class election_results(db.Model):
    result_id = db.Column(db.Integer, primary_key=True)
    election_id = db.Column(db.Integer, db.ForeignKey('elections.election_id'), nullable=False)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.candidate_id'), nullable=False)
    votes_received = db.Column(db.Integer, nullable=False)
    percentage_of_total = db.Column(db.Float, nullable=False)
    voter_turnout = db.Column(db.Float, nullable=False)

class elected_officials(db.Model):
    official_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    position = db.Column(db.String(120), nullable=False)
    party_id = db.Column(db.Integer, db.ForeignKey('parties.party_id'), nullable=False)
    election_id = db.Column(db.Integer, db.ForeignKey('elections.election_id'), nullable=False)
    term_start = db.Column(db.Date, nullable=False)
    term_end = db.Column(db.Date, nullable=False)

# crud operations and routes
#create
@app.route('/elections', methods=['POST'])
def create_election():
    data = request.get_json()
    new_election = elections(
        election_type=data['election_type', ""],
        election_date=datetime.strptime(data['election_date'], '%Y-%m-%d').date(),
        voter_turnout=data['voter_turnout', 0],
        total_votes=data['total_votes', 0],
        winner=data['winner', ""]
    )
    db.session.add(new_election)
    db.session.commit()
    return jsonify({'message': 'Election created successfully!'}), 201

#read
@app.route('/elections/<int:election_id>', methods=['GET'])
def get_election(election_id):
    election = elections.query.get_or_404(election_id)
    return jsonify({
        'election_id': election.election_id,
        'election_type': election.election_type,
        'election_date': election.election_date.strftime('%Y-%m-%d'),
        'voter_turnout': election.voter_turnout,
        'total_votes': election.total_votes,
        'winner': election.winner
    })
#update

@app.route('/elections/<int:election_id>', methods=['PUT'])
def update_election(election_id):
    data = request.get_json()
    election = elections.query.get_or_404(election_id)
    election.election_type = data.get('election_type', election.election_type)
    election.election_date = datetime.strptime(data.get('election_date', election.election_date.strftime('%Y-%m-%d')), '%Y-%m-%d').date()
    election.voter_turnout = data.get('voter_turnout', election.voter_turnout)
    election.total_votes = data.get('total_votes', election.total_votes)
    election.winner = data.get('winner', election.winner)
    db.session.commit()
    return jsonify({'message': 'Election updated successfully!'})
#delete

@app.route('/elections/<int:election_id>', methods=['DELETE'])
def delete_election(election_id):
    election = elections.query.get_or_404(election_id)
    db.session.delete(election)
    db.session.commit()
    return jsonify({'message': 'Election deleted successfully!'})

#filter by date range
@app.route('/elections', methods=['GET'])
def filter_elections_by_date():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    query = elections.query
    if start_date:
        query = query.filter(elections.election_date >= datetime.strptime(start_date, '%Y-%m-%d').date())
    if end_date:
        query = query.filter(elections.election_date <= datetime.strptime(end_date, '%Y-%m-%d').date())
    elections_list = query.all()
    result = []
    for election in elections_list:
        result.append({
            'election_id': election.election_id,
            'election_type': election.election_type,
            'election_date': election.election_date.strftime('%Y-%m-%d'),
            'voter_turnout': election.voter_turnout,
            'total_votes': election.total_votes,
            'winner': election.winner
        })
    return jsonify(result)

from flask import render_template

# Homepage route
@app.route('/')
def home():
    return render_template('index.html')

# Tables navigation route
@app.route('/tables')
def tables():
    return render_template('tables.html')

# Generic table view route
@app.route('/table/<table_name>')
def table_view(table_name):
    # Map table names to SQLAlchemy models
    models = {
        'users': users,
        'user_logs': user_logs,
        'updated': updated,
        'roles': roles,
        'elections': elections,
        'states': states,
        'parties': parties,
        'counties': counties,
        'congress': congress,
        'house': house,
        'senate': senate,
        'federal_senate': federal_senate,
        'governor': governor,
        'supreme_court': supreme_court,
        'board_of_education': board_of_education,
        'secretary_of_state': secretary_of_state,
        'ballot_measures': ballot_measures,
        'candidates': candidates,
        'precincts': precincts,
        'election_results': election_results,
        'elected_officials': elected_officials,
    }
    model = models.get(table_name)
    if not model:
        return f"Table '{table_name}' not found.", 404
    records = model.query.all()
    # Get column names
    columns = [col.name for col in model.__table__.columns]
    # Convert records to dicts
    record_dicts = [{col: getattr(r, col) for col in columns} for r in records]
    return render_template('table_view.html', table_name=table_name, display_name=table_name.replace('_', ' ').title(), columns=columns, records=record_dicts)

# API Routes for Add, Update, Delete
@app.route('/api/add/<table_name>', methods=['POST'])
def api_add_record(table_name):
    models = {
        'users': users,
        'user_logs': user_logs,
        'updated': updated,
        'roles': roles,
        'elections': elections,
        'states': states,
        'parties': parties,
        'counties': counties,
        'congress': congress,
        'house': house,
        'senate': senate,
        'federal_senate': federal_senate,
        'governor': governor,
        'supreme_court': supreme_court,
        'board_of_education': board_of_education,
        'secretary_of_state': secretary_of_state,
        'ballot_measures': ballot_measures,
        'candidates': candidates,
        'precincts': precincts,
        'election_results': election_results,
        'elected_officials': elected_officials,
    }
    model = models.get(table_name)
    if not model:
        return jsonify({'error': 'Table not found'}), 404
    
    data = request.get_json()
    try:
        # Convert data types based on column types
        converted_data = {}
        for col_name, col in model.__table__.columns.items():
            if col_name in data:
                value = data[col_name]
                if value is None or value == '':
                    if col.nullable:
                        converted_data[col_name] = None
                    continue
                
                # Type conversion
                if col.type.__class__.__name__ == 'Integer':
                    converted_data[col_name] = int(value)
                elif col.type.__class__.__name__ == 'Float':
                    converted_data[col_name] = float(value)
                elif col.type.__class__.__name__ == 'Boolean':
                    converted_data[col_name] = value.lower() in ['true', '1', 'yes']
                elif col.type.__class__.__name__ == 'Date':
                    converted_data[col_name] = datetime.strptime(value, '%Y-%m-%d').date()
                elif col.type.__class__.__name__ == 'DateTime':
                    converted_data[col_name] = datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
                else:
                    converted_data[col_name] = value
        
        new_record = model(**converted_data)
        db.session.add(new_record)
        db.session.commit()
        return jsonify({'message': 'Record added successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


# ✅ Helper for consistent JSON responses
def json_response(success=True, message=None, error=None, status=200):
    payload = {'success': success}
    if message:
        payload['message'] = message
    if error:
        payload['error'] = error
    return jsonify(payload), status

@app.route('/api/update/<table_name>', methods=['PUT'])
def api_update_record(table_name):
    models = {
        'users': users,
        'user_logs': user_logs,
        'updated': updated,
        'roles': roles,
        'elections': elections,
        'states': states,
        'parties': parties,
        'counties': counties,
        'congress': congress,
        'house': house,
        'senate': senate,
        'federal_senate': federal_senate,
        'governor': governor,
        'supreme_court': supreme_court,
        'board_of_education': board_of_education,
        'secretary_of_state': secretary_of_state,
        'ballot_measures': ballot_measures,
        'candidates': candidates,
        'precincts': precincts,
        'election_results': election_results,
        'elected_officials': elected_officials,
    }
    model = models.get(table_name)
    if not model:
        return json_response(success=False, error='Table not found', status=404)

    data = request.get_json()
    try:
        old_record = data.get('oldRecord')
        new_record_data = data.get('newRecord')

        if not old_record or not new_record_data:
            return json_response(success=False, error='Missing oldRecord or newRecord', status=400)

        # Find the record to update using the primary key
        primary_key = model.__table__.primary_key.columns[0].name
        pk_value = old_record.get(primary_key)

        if not pk_value:
            return json_response(success=False, error=f'Primary key {primary_key} not found', status=400)

        record = model.query.filter_by(**{primary_key: pk_value}).first()

        if not record:
            return json_response(success=False, error=f'Record with {primary_key}={pk_value} not found', status=404)

        # Update fields with type conversion
        for col_name, col in model.__table__.columns.items():
            if col_name in new_record_data:
                value = new_record_data[col_name]

                if value is None or value == '':
                    if col.nullable:
                        setattr(record, col_name, None)
                    continue

                try:
                    # Type conversion
                    if col.type.__class__.__name__ == 'Integer':
                        setattr(record, col_name, int(value))
                    elif col.type.__class__.__name__ == 'Float':
                        setattr(record, col_name, float(value))
                    elif col.type.__class__.__name__ == 'Boolean':
                        setattr(record, col_name, value.lower() in ['true', '1', 'yes'])
                    elif col.type.__class__.__name__ == 'Date':
                        setattr(record, col_name, datetime.strptime(value, '%Y-%m-%d').date())
                    elif col.type.__class__.__name__ == 'DateTime':
                        setattr(record, col_name, datetime.strptime(value, '%Y-%m-%d %H:%M:%S'))
                    else:
                        setattr(record, col_name, value)
                except ValueError as ve:
                    return json_response(success=False, error=f'Invalid value for {col_name}: {str(ve)}', status=400)

        db.session.commit()
        return json_response(message='Record updated successfully!', status=200)

    except Exception as e:
        db.session.rollback()
        import traceback
        print(f"Error in api_update_record: {str(e)}")
        print(traceback.format_exc())
        return json_response(success=False, error=str(e), status=400)

@app.route('/api/delete/<table_name>', methods=['DELETE'])
def api_delete_record(table_name):
    models = {
        'users': users,
        'user_logs': user_logs,
        'updated': updated,
        'roles': roles,
        'elections': elections,
        'states': states,
        'parties': parties,
        'counties': counties,
        'congress': congress,
        'house': house,
        'senate': senate,
        'federal_senate': federal_senate,
        'governor': governor,
        'supreme_court': supreme_court,
        'board_of_education': board_of_education,
        'secretary_of_state': secretary_of_state,
        'ballot_measures': ballot_measures,
        'candidates': candidates,
        'precincts': precincts,
        'election_results': election_results,
        'elected_officials': elected_officials,
    }
    model = models.get(table_name)
    if not model:
        return jsonify({'error': 'Table not found'}), 404
    
    data = request.get_json()
    try:
        # Find the record to delete using the primary key
        primary_key = model.__table__.primary_key.columns[0].name
        pk_value = data.get(primary_key)
        
        if not pk_value:
            return jsonify({'error': f'Primary key {primary_key} not provided'}), 400
        
        record = model.query.filter_by(**{primary_key: pk_value}).first()
        
        if not record:
            return jsonify({'error': f'Record with {primary_key}={pk_value} not found'}), 404
        
        db.session.delete(record)
        db.session.commit()
        return jsonify({'message': 'Record deleted successfully!'}), 200
    except Exception as e:
        db.session.rollback()
        import traceback
        print(f"Error in api_delete_record: {str(e)}")
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 400

# run the app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)