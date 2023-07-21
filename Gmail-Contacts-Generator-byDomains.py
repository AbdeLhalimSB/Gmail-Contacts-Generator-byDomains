import random
import csv

def generate_random_name():
    first_names = [
        "Emma", "Liam", "Olivia", "Noah", "Ava", "Isabella", "Sophia", "Mia", "Jackson",
        "Aiden", "Lucas", "Lily", "Zoe", "Layla", "Elijah", "Carter", "Abigail", "Emily",
        "Mason", "Ella", "Scarlett", "Aria", "Grace", "Victoria", "Nora", "Camila", "Mateo",
        "Luna", "Hannah", "Ariana", "James", "Ethan", "Michael", "Alexander", "David", "Benjamin"
    ]

    

    random_name = random.choice(first_names)
    return random_name


def generate_random_usa_phone_number():
    area_code = random.randint(100, 999)
    exchange_code = random.randint(100, 999)
    subscriber_number = random.randint(1000, 9999)

    return f"+1{area_code}{exchange_code}{subscriber_number}"

def generate_random_job_title():
    job_titles = [
        "Software Engineer", "Data Scientist", "Product Manager", "UX Designer",
        "Marketing Specialist", "Sales Representative", "Financial Analyst",
        "Human Resources Manager", "Graphic Designer", "Content Writer",
        "Project Manager", "Business Analyst", "Customer Support Specialist",
        "Operations Manager", "Quality Assurance Tester", "IT Administrator",
        "Social Media Manager", "Research Assistant", "Event Coordinator",
        "Network Engineer", "Accountant", "Web Developer", "Systems Analyst",
        "Digital Marketing Manager", "UI Designer", "Video Editor",
        "Operations Research Analyst", "Public Relations Specialist",
        "Supply Chain Manager", "Software Architect", "Technical Writer",
        "Database Administrator", "Data Engineer", "Mobile App Developer",
        "Machine Learning Engineer", "Financial Planner", "Technical Support Specialist"
    ]

    random_job_title = random.choice(job_titles)
    return random_job_title

def generate_random_birthday():
    month = random.randint(1, 12)
    if month in [4, 6, 9, 11]:
        day = random.randint(1, 30)
    elif month == 2:
        day = random.randint(1, 28)
    else:
        day = random.randint(1, 31)
    year = random.randint(0, 99)
    
    birthday = f"{month:02d}/{day:02d}/{year:02d}"
    return birthday

streets = [
    "Maple Street", "Oak Avenue", "Cedar Lane", "Elm Road", "Pine Drive",
    "Birch Court", "Willow Way", "Cherry Street", "Spruce Lane", "Hickory Avenue",
    "Sycamore Road", "Juniper Drive", "Magnolia Court", "Cypress Lane", "Alder Street",
    "Beech Avenue", "Aspen Road", "Mulberry Court", "Chestnut Lane", "Redwood Drive"
]

cities = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
    "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose",
    "Austin", "Jacksonville", "San Francisco", "Columbus", "Indianapolis",
    "Fort Worth", "Charlotte", "Seattle", "Denver", "Washington"
]

states = [
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
    "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
    "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
    "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
    "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
]

def generate_random_us_address():
    street_number = random.randint(1, 9999)
    street_name = random.choice(streets)
    city = random.choice(cities)
    state = random.choice(states)
    zip_code = f"{random.randint(10000, 99999)}-{random.randint(1000, 9999)}"
    
    address = f"{street_number} {street_name}\n{city}, {state} {zip_code}"
    return address

first_words = [
    "Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", "Eta", "Theta", "Iota", "Kappa",
    "Lambda", "Mu", "Nu", "Xi", "Omicron", "Pi", "Rho", "Sigma", "Tau", "Upsilon", "Phi",
    "Chi", "Psi", "Omega", "Aegis", "Aurora", "Apex", "Equinox", "Horizon", "Vortex", "Zenith",
    "Nimbus", "Pinnacle", "Quasar", "Spectrum", "Terra", "Voyager", "Zen", "Infinite", "Unity"
]

second_words = [
    "Technologies", "Solutions", "Systems", "Innovations", "Services", "Dynamics", "Enterprises",
    "Networks", "Labs", "Ventures", "Global", "Digital", "InfoTech", "Tech", "Automation", "Insights",
    "Analytics", "Cyber", "Matrix", "Logic", "NexGen", "Synergy", "Link", "Forge", "Sphere", "Fusion",
    "Genius", "Pro", "Edge", "Intellect", "Vantage", "Compass", "Synchron", "Bright", "Stratus", "Exo"
]

def generate_random_organization_name():
    first_word = random.choice(first_words)
    second_word = random.choice(second_words)
    
    separator = " " if random.random() < 0.5 else ""
    
    organization_name = f"{first_word}{separator}{second_word}"
    return organization_name

def generate_random_street():
    return random.choice(streets)

def generate_random_city():
    return random.choice(cities)

def generate_random_zipcode():
    return f"{random.randint(10000, 99999)}-{random.randint(1000, 9999)}"

def generate_random_data_for_domains(input_file, output_file):
    with open(input_file, 'r') as domains_file:
        domains = domains_file.read().splitlines()

    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Birthday', 'Group Membership', 'E-mail 1 - Value','Phone 1 - Value','Address 1 - Formatted','Address 1 - Street','Address 1 - City','Address 1 - PO Box','Address 1 - Country','Organization 1 - Name','Organization 1 - Title']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for domain in domains:
            name = generate_random_name()
            phone = generate_random_usa_phone_number()
            job_title = generate_random_job_title()
            writer.writerow({'Name': name, 'Birthday': generate_random_birthday(), 'Group Membership': 'import ::: * myContacts', 'E-mail 1 - Value': domain,'Phone 1 - Value':phone,'Address 1 - Formatted':generate_random_us_address(),'Address 1 - Street':generate_random_street(),'Address 1 - City':generate_random_city(),'Address 1 - PO Box':generate_random_zipcode(),'Address 1 - Country':'US','Organization 1 - Name':generate_random_organization_name(),'Organization 1 - Title':job_title})

generate_random_data_for_domains('domains.txt', 'random_data.csv')
