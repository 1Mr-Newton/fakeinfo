from concurrent.futures import ThreadPoolExecutor
import json
import random
from time import perf_counter
from faker import Faker

fake = Faker()
t0 = perf_counter()


def create_job(i):
    job_types = [
        "Software Engineer",
        "Data Scientist",
        "Product Manager",
        "Marketing Specialist",
        "Graphic Designer",
        "Sales Representative",
        "Financial Analyst",
        "Human Resources Manager",
        "Operations Coordinator",
        "Customer Support Specialist",
        "Business Development Executive",
        "Content Writer",
        "UX/UI Designer",
        "Quality Assurance Engineer",
        "Project Manager",
        "Accountant",
        "Research Analyst",
        "Administrative Assistant",
        "Network Engineer",
        "Legal Counsel",
        "Web Developer",
        "Digital Marketing Manager",
        "Database Administrator",
        "Systems Analyst",
        "IT Consultant",
        "Mobile App Developer",
        "Social Media Manager",
        "Data Analyst",
        "Supply Chain Analyst",
        "Event Planner",
        "Public Relations Manager",
        "Technical Writer",
        "Operations Manager",
        "Financial Planner",
        "Software Architect",
        "UI/UX Designer",
        "E-commerce Manager",
        "Business Analyst",
        "Market Research Analyst",
        "Copywriter",
        "Cybersecurity Analyst",
        "Product Owner",
        "IT Project Manager",
        "Data Engineer",
        "HR Generalist",
        "Sales Manager",
        "Front-end Developer",
        "Digital Strategist",
        "UX Researcher",
        "Business Intelligence Analyst",
        "DevOps Engineer",
    ]

    job_descriptions = [
        "Experienced professional with a strong background in {job_type}.",
        "Skilled {job_type} with expertise in problem-solving and collaboration.",
        "Innovative {job_type} with a proven track record of success.",
        "Detail-oriented {job_type} with excellent organizational skills.",
        "Analytical {job_type} with a passion for data-driven decision making.",
        "Creative {job_type} with a keen eye for design and aesthetics.",
        "Results-driven {job_type} with a focus on achieving targets.",
        "Adaptable {job_type} who thrives in a fast-paced environment.",
        "Strategic {job_type} with a deep understanding of market trends.",
        "Motivated {job_type} with strong communication and leadership skills.",
        "Technical {job_type} with proficiency in multiple programming languages.",
        "Customer-focused {job_type} dedicated to delivering exceptional service.",
        "Collaborative {job_type} experienced in cross-functional teamwork.",
        "Expert {job_type} with a strong ability to analyze complex problems.",
        "Skilled {job_type} experienced in managing large-scale projects.",
        "Organized {job_type} with a systematic approach to tasks and deadlines.",
        "Results-oriented {job_type} with a track record of exceeding targets.",
        "Knowledgeable {job_type} with expertise in financial analysis.",
        "Resourceful {job_type} skilled in finding innovative solutions.",
        "Proactive {job_type} with a strong attention to detail.",
        "Team-oriented {job_type} with excellent interpersonal skills.",
        "Passionate {job_type} with a drive for continuous learning.",
        "Adaptive {job_type} with the ability to quickly embrace new technologies.",
        "Strategic thinker with a focus on {job_type} planning and execution.",
        "Experienced {job_type} with a strong background in data analysis.",
        "Detail-oriented {job_type} with a knack for problem-solving.",
        "Motivated {job_type} with a passion for customer satisfaction.",
        "Skilled {job_type} with expertise in digital marketing strategies.",
        "Creative {job_type} with a flair for visual design.",
        "Innovative {job_type} with a talent for product ideation.",
        "Analytical {job_type} with a data-driven approach to decision making.",
        "Collaborative {job_type} with excellent teamwork skills.",
        "Results-oriented {job_type} with a focus on delivering high-quality outcomes.",
        "Proactive {job_type} with the ability to identify and address issues proactively.",
        "Experienced {job_type} with strong project management skills.",
        "Adaptable {job_type} with a proven ability to thrive in changing environments.",
        "Strategic {job_type} with a deep understanding of market dynamics.",
        "Customer-centric {job_type} dedicated to ensuring client satisfaction.",
        "Skilled {job_type} with expertise in web development technologies.",
        "Creative {job_type} with a passion for visual storytelling.",
        "Analytical {job_type} with a strong attention to detail.",
        "Innovative {job_type} with a knack for problem-solving.",
        "Collaborative {job_type} experienced in working with cross-functional teams.",
        "Results-driven {job_type} with a focus on meeting and exceeding goals.",
        "Motivated {job_type} with excellent organizational and time management skills.",
        "Adaptable {job_type} with the ability to thrive in fast-paced environments.",
        "Strategic {job_type} with a data-driven approach to decision making.",
        "Experienced {job_type} with strong interpersonal and communication skills.",
        "Detail-oriented {job_type} with a meticulous approach to work.",
        "Customer-focused {job_type} dedicated to delivering exceptional service experiences.",
    ]

    employment_types = ["Full time", "Part time", "Contract", "Freelance"]

    job_type = random.choice(job_types)
    job_description = random.choice(job_descriptions).format(job_type=job_type)
    job = {
        "id": i,
        "title": job_type,
        "company": fake.company(),
        "description": job_description,
        "employment_type": random.choice(employment_types),
        "location": fake.city(),
        "requirements": fake.paragraph(nb_sentences=2),
        "salary": "${:,.2f}".format(fake.random_int(min=50000, max=150000)),
        "latitude": float(fake.latitude()),
        "longitude": float(fake.longitude()),
    }

    return job


def create_jobs(n):
    with ThreadPoolExecutor() as executor:
        users = list(executor.map(create_job, range(n)))
    return users


def jobs(n):
    us = create_jobs(n)
    results = {
        "jobs": us,
        "total": n,
    }
    return json.dumps(results)


# with open("jobs.json", "w") as f:
#     f.write(jobs(10000))
# print(perf_counter() - t0)


# create_job_data(1000000)
# https://chat.openai.com/share/66d7ac09-6268-400a-a4bb-c77db11a27a5
# https://www.figma.com/file/bpAwwvZNSx5JY7fWQYFros/Jobhuntly---Job-Board-%26-Portal-Web-and-Mobile-UI-Kit-(Community)?type=design&node-id=201%3A4123&mode=design&t=2WZ8qvUm7ORdiJ6E-1
# https://www.figma.com/file/wcWvWiaqUttOpmt6qojlPm/Job-UI-Kit-Free-Template-(Community)?type=design&node-id=2%3A56&mode=design&t=gnema1sUd54gkDFO-1

# locations = [
#         "San Francisco",
#         "New York City",
#         "London",
#         "Berlin",
#         "Toronto",
#         "Sydney",
#         "Chicago",
#         "Seattle",
#         "Los Angeles",
#         "Paris",
#         "Tokyo",
#         "Dubai",
#         "Mumbai",
#         "Singapore",
#         "Stockholm",
#         "Barcelona",
#         "Amsterdam",
#         "Hong Kong",
#         "Zurich",
#         "Dublin",
#     ]
