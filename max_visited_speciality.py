def max_visited_speciality(patient_medical_speciality_list, medical_speciality):
    # Dictionary to count visits for each speciality code
    speciality_count = {}

    # Iterate over speciality codes (at odd indices)
    for i in range(1, len(patient_medical_speciality_list), 2):
        code = patient_medical_speciality_list[i]
        if code in speciality_count:
            speciality_count[code] += 1
        else:
            speciality_count[code] = 1

    # Find the speciality code with the maximum count
    max_code = max(speciality_count, key=speciality_count.get)

    # Return the full name of the speciality using the dictionary
    return medical_speciality[max_code]
