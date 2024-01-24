from Date import Date
import sys


def read_celebrity_data(file_name):
    celebrity_data = []
    with open(file_name, 'r') as file:
        for line in file:
            data = line.strip().split(':')
            first_name, last_name, dob, dod = data
            celebrity_data.append((first_name, last_name, dob, dod))
    return celebrity_data


def process_celebrity_data(celebrity_data):
    data = []

    for celeb in celebrity_data:
        first_name, last_name, dob, dod = celeb
        m_dob, d_dob, y_dob = dob.split("/")

        dob_date = Date(int(m_dob), int(d_dob), int(y_dob))

        if dod is not None and dod != "":
            m_dod, d_dod, y_dod = dod.split("/")
            dod_date = Date(int(m_dod), int(d_dod), int(y_dod))
        else:
            dod_date = None

        if dod_date and dob_date.after(dod_date):
            print(f"BAD DATA: {first_name}:{last_name}:{dob}:{dod}")
        else:
            num_days_alive = (dod_date.days_between(dob_date)) if dod_date else Date.today().days_between(dob_date)
            data.append([first_name, last_name, dob_date, dod_date, num_days_alive])

    sorted_data = sorted(data, key=lambda x: x[4])

    max_lengths = {1: 0, 2: 0, 3: 0, 4: 0}
    for dat in sorted_data:
        max_lengths[1] = max(max_lengths[1], len(dat[0]))
        max_lengths[2] = max(max_lengths[2], len(dat[1]))
        max_lengths[3] = max(max_lengths[3], len(str(dat[2])))
        max_lengths[4] = max(max_lengths[4], len(str(dat[3])) if dod else 0)

    print(
        f"{'FNAME':<{max_lengths[1] + 2}}{'LNAME':<{max_lengths[2] + 2}}{'DOB':<{max_lengths[3] + 5}}{'DAY':<13}{'DOD':<{max_lengths[4] + 5}}{'DAY':<13}{'NUM_DAYS':<20}")

    print(
        "------------------------------------------------------------------------------------------------------")

    for dat in sorted_data:
        print(
            f"{dat[0]:<{max_lengths[1] + 2}}{dat[1]:<{max_lengths[2] + 2}}{str(dat[2]):<{max_lengths[3] + 5}}{dat[2].day_of_weekS():<13}{str(dat[3]):<{max_lengths[4] + 5}}{dat[3].day_of_weekS() if dat[3] is not None else 'ALIVE':<13}{int(dat[4]):<20}")

    print(
        "-----------------------------------------------------------------------------------------------------")


def main():
    input_file = sys.argv[1]
    celebrity_data = read_celebrity_data(input_file)
    process_celebrity_data(celebrity_data)


if __name__ == "__main__":
    main()
