# Data Entry Guide - People's Record Database

This guide shows valid examples for entering data into each table.

## Users Table
**Description:** User accounts in the system
**Auto-fields:** user_id (automatically set starting at 1)

### Fields to Enter:
- **email**: Valid email address
  - Example: `john.doe@example.com` or `admin@company.org`
  
- **password**: Password string (store securely in production)
  - Example: `SecurePass123!` or `pwd2024`
  
- **name**: Full name of the user
  - Example: `John Doe` or `Jane Smith`

### Example Entry:
| email | password | name |
|-------|----------|------|
| john.doe@example.com | SecurePass123 | John Doe |
| jane.smith@example.com | MyPassword456 | Jane Smith |

---

## Roles Table
**Description:** User roles/permissions
**Auto-fields:** role_id (auto-generated)

### Fields to Enter:
- **role_name**: Name of the role (must be unique)
  - Example: `Admin`, `Editor`, `Viewer`, `Manager`
  
- **description**: Description of the role
  - Example: `Full system access and administration` or `Can view and edit content`

### Example Entry:
| role_name | description |
|-----------|-------------|
| Admin | Full system access and administration |
| Editor | Can create and edit content |
| Viewer | Read-only access |

---

## Elections Table
**Description:** Election information
**Auto-fields:** election_id (auto-generated)

### Fields to Enter:
- **election_type**: Type of election
  - Example: `Presidential`, `Midterm`, `Local`, `State`
  
- **election_date**: Date of election (format: YYYY-MM-DD)
  - Example: `2024-11-05` or `2024-06-18`
  
- **voter_turnout**: Voter turnout percentage (decimal number)
  - Example: `65.5` or `72.3`
  
- **total_votes**: Total number of votes cast (integer)
  - Example: `150000000` or `5000`
  
- **winner**: Name of the winner
  - Example: `John Smith` or `Democratic Party`

### Example Entry:
| election_type | election_date | voter_turnout | total_votes | winner |
|---------------|---------------|---------------|-------------|--------|
| Presidential | 2024-11-05 | 65.5 | 150000000 | Democratic Party |
| Midterm | 2022-11-08 | 53.0 | 125000000 | Republican Party |

---

## States Table
**Description:** State-level information
**Auto-fields:** state_id (auto-generated)

### Fields to Enter:
- **state_name**: Name of state (must be unique)
  - Example: `California`, `Texas`, `New York`, `Florida`
  
- **population**: State population (integer)
  - Example: `39500000` or `2700000`
  
- **registered_voters**: Number of registered voters (integer)
  - Example: `25000000` or `1500000`
  
- **voter_turnout**: Turnout percentage (decimal)
  - Example: `60.5` or `58.2`
  
- **voter_age_range**: Age range distribution
  - Example: `18-64`, `Mixed` or `18-34: 25%, 35-64: 45%, 65+: 30%`

### Example Entry:
| state_name | population | registered_voters | voter_turnout | voter_age_range |
|------------|------------|-------------------|----------------|-----------------|
| California | 39500000 | 25000000 | 62.5 | 18-64 |
| Texas | 30000000 | 18000000 | 61.0 | Mixed |

---

## Parties Table
**Description:** Political parties
**Auto-fields:** party_id (auto-generated)

### Fields to Enter:
- **party_name**: Name of political party (must be unique)
  - Example: `Democratic Party`, `Republican Party`, `Libertarian Party`, `Green Party`

### Example Entry:
| party_name |
|------------|
| Democratic Party |
| Republican Party |
| Libertarian Party |

---

## Counties Table
**Description:** County-level information
**Auto-fields:** county_id (auto-generated)

### Fields to Enter:
- **county_name**: Name of county (must be unique)
  - Example: `Los Angeles County`, `Cook County`, `Harris County`
  
- **population**: County population (integer)
  - Example: `10000000` or `500000`
  
- **registered_voters**: Registered voters (integer)
  - Example: `6000000` or `250000`
  
- **senate_number**: Senate district number
  - Example: `1` or `25`
  
- **house_number**: House district number
  - Example: `5` or `12`
  
- **congress_number**: Congressional district number
  - Example: `10` or `3`

### Example Entry:
| county_name | population | registered_voters | senate_number | house_number | congress_number |
|-------------|------------|-------------------|---------------|--------------|-----------------|
| Los Angeles County | 10000000 | 6000000 | 1 | 5 | 10 |

---

## Candidates Table
**Description:** Election candidates
**Auto-fields:** candidate_id (auto-generated)

### Fields to Enter:
- **name**: Candidate full name
  - Example: `John Smith` or `Sarah Johnson`
  
- **party_id**: ID of candidate's party (must reference existing party)
  - Example: `1` or `2`
  
- **election_id**: ID of election running in (must reference existing election)
  - Example: `1` or `2`
  
- **position**: Position sought
  - Example: `President`, `Governor`, `Senator`, `Representative`

### Example Entry:
| name | party_id | election_id | position |
|------|----------|-------------|----------|
| John Smith | 1 | 1 | President |
| Sarah Johnson | 2 | 1 | President |

---

## Election Results Table
**Description:** Results for each candidate in elections
**Auto-fields:** result_id (auto-generated)

### Fields to Enter:
- **election_id**: ID of election (must reference existing election)
  - Example: `1` or `2`
  
- **candidate_id**: ID of candidate (must reference existing candidate)
  - Example: `1` or `2`
  
- **votes_received**: Number of votes candidate received (integer)
  - Example: `75000000` or `50000000`
  
- **percentage_of_total**: Percentage of total votes (decimal)
  - Example: `50.5` or `33.3`
  
- **voter_turnout**: Turnout for this result (decimal)
  - Example: `65.5` or `60.0`

### Example Entry:
| election_id | candidate_id | votes_received | percentage_of_total | voter_turnout |
|-------------|--------------|-----------------|---------------------|----------------|
| 1 | 1 | 75000000 | 50.5 | 65.5 |
| 1 | 2 | 73000000 | 49.5 | 65.5 |

---

## Governor Table
**Description:** Governor information
**Auto-fields:** governor_id (auto-generated)

### Fields to Enter:
- **name**: Governor's name
  - Example: `Gavin Newsom` or `Ron DeSantis`
  
- **party_id**: Party ID (must reference existing party)
  - Example: `1` or `2`
  
- **state_id**: State ID (must reference existing state)
  - Example: `1` or `2`
  
- **election_id**: Election ID (must reference existing election)
  - Example: `1` or `2`
  
- **voter_turnout**: Turnout percentage (decimal)
  - Example: `60.5` or `58.2`
  
- **term_start**: When term started (YYYY-MM-DD)
  - Example: `2022-01-10` or `2023-01-09`
  
- **term_end**: When term ends (YYYY-MM-DD)
  - Example: `2026-01-10` or `2027-01-09`

### Example Entry:
| name | party_id | state_id | election_id | voter_turnout | term_start | term_end |
|------|----------|----------|-------------|----------------|------------|----------|
| Gavin Newsom | 1 | 1 | 1 | 60.5 | 2022-01-10 | 2026-01-10 |

---

## Data Entry Tips

1. **Dates**: Always use YYYY-MM-DD format (e.g., 2024-12-25)
2. **Decimals**: Use dot notation (e.g., 65.5 not 65,5)
3. **Integers**: No decimal point (e.g., 1000000 not 1000000.0)
4. **Foreign Keys**: Use the ID number from the referenced table
5. **Unique Fields**: Check that values like emails, state names, and party names don't already exist
6. **Required Fields**: All fields without auto-generation must be filled in

## Notes

- Auto-generated fields (ending in _id) are automatically created when you add a record
- Do NOT manually enter values for auto-generated fields in the Add form
- When editing, primary key fields are read-only to maintain data integrity
- For date fields, use the YYYY-MM-DD format consistently
