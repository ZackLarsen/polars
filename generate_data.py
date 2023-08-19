"""
This file is used to generate data for the project.
"""

import random

from faker import Faker
import numpy as np
import click
import pyarrow as pa
import pyarrow.parquet as pq


fake = Faker()


@click.command()
@click.option('--n', default=1000, help='Number of patients to generate')
@click.option('--output', default='healthcare_data.parquet', help='Output file path')
@click.option('--seed', default=None, help='Seed for random number generation')

def generate_healthcare_data(n, output, seed=42):
    """
    This function generates realistic healthcare data using the Faker, numpy.random, and random libraries.
    It returns a pyarrow.Table object, where each column represents a field and each row represents a patient.
    """
    if seed is not None:
        random.seed(seed)
        np.random.seed(seed)
    
    data = {
        'patient_id': [str(i).zfill(9) for i in range(n)],
        'first_name': [fake.first_name() for _ in range(n)],
        'last_name': [fake.last_name() for _ in range(n)],
        'gender': np.random.choice(['Male', 'Female'], size=n),
        'age': np.random.normal(50, 20, size=n),
        'address': [fake.address() for _ in range(n)],
        'phone_number': [fake.phone_number() for _ in range(n)],
        'email': [fake.email() for _ in range(n)],
        'blood_type': np.random.choice(['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'], size=n),
        'height_cm': np.random.normal(170, 10, size=n),
        'weight_kg': np.random.normal(70, 15, size=n),
        'bmi': np.random.normal(25, 5, size=n),
        'pulse_bpm': np.random.normal(70, 10, size=n),
        'blood_pressure_mmhg': [f"{np.random.randint(90, 140)}/{np.random.randint(60, 90)}" for _ in range(n)],
        'respiratory_rate_bpm': np.random.normal(16, 2, size=n),
        'temperature_c': np.random.normal(37, 0.5, size=n),
        'oxygen_saturation_pct': np.random.normal(98, 1, size=n),
        'pain_level': np.random.randint(0, 11, size=n),
        'allergies': [fake.words(nb=3) for _ in range(n)],
        'medications': [fake.words(nb=3) for _ in range(n)],
        'medical_history': [fake.sentence(nb_words=10) for _ in range(n)],
        'family_history': [fake.sentence(nb_words=10) for _ in range(n)],
        'social_history': [fake.sentence(nb_words=10) for _ in range(n)],
        'chief_complaint': [fake.sentence(nb_words=10) for _ in range(n)],
        'symptoms': [fake.sentence(nb_words=10) for _ in range(n)],
        'diagnosis': [fake.sentence(nb_words=10) for _ in range(n)],
        'treatment': [fake.sentence(nb_words=10) for _ in range(n)],
        'lab_results': [fake.sentence(nb_words=10) for _ in range(n)],
        'imaging_results': [fake.sentence(nb_words=10) for _ in range(n)],
        'vital_signs': [fake.sentence(nb_words=10) for _ in range(n)],
        'notes': [fake.sentence(nb_words=10) for _ in range(n)],
        'insurance_provider': [fake.company() for _ in range(n)],
        'insurance_id': [fake.random_number(digits=10) for _ in range(n)],
        'emergency_contact_name': [fake.name() for _ in range(n)],
        'emergency_contact_relationship': [fake.word() for _ in range(n)],
        'emergency_contact_phone': [fake.phone_number() for _ in range(n)],
        'primary_care_physician': [fake.name() for _ in range(n)],
        'pcp_phone': [fake.phone_number() for _ in range(n)],
        'last_visit_date': [fake.date_between(start_date='-1y', end_date='today') for _ in range(n)],
        'next_visit_date': [fake.date_between(start_date='today', end_date='+1y') for _ in range(n)],
        'has_high_acuity': np.random.choice([True, False], size=n, p=[0.05, 0.95]),
        'has_moderate_acuity': np.random.choice([True, False], size=n, p=[0.1, 0.9]),
        'needs_stabilization': np.random.choice([True, False], size=n, p=[0.2, 0.8]),
        'current_clinical_risk': np.random.choice(['low', 'moderate', 'high'], size=n, p=[0.7, 0.2, 0.1])
    }

    table = pa.Table.from_pydict(data)
    pq.write_table(table, output)

    click.echo(f"Generated {n} patients and saved to {output}")


if __name__ == '__main__':
    generate_healthcare_data()