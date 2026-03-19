from datetime import datetime, timedelta



SPECIALTY_CHOICES = [
    ("primary_care", "Medicina general"),
    ("cardiology", "Cardiología"),
    ("pediatrics", "Pediatría"),
    ("surgery", "Cirugía"),
    ("dermatology", "Dermatología"),
    ("obgyn", "Obstetriciaginecología"),
    ("ent", "Otorrinonaringología"),
    ("ge", "Gastroenterología"),
]


def generate_time_choices(start="08:00", end="20:00", step_minutes=30):
    choices = []
    current = datetime.strptime(start, "%H:%M")
    end_time = datetime.strptime(end, "%H:%M")
    
    while current <= end_time:
        value = current.strftime("%H:%M")
        choices.append((value, value))
        current += timedelta(minutes=step_minutes)
        
    return choices

TIME_CHOICES = generate_time_choices()
