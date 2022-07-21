import random

NSTUDENTS = 100
NRACES = 100
TOP=10

rnd = random.Random(31315)

fnames = [
    "Adam",
    "Alexander",
    "Ali",
    "Angelo",
    "Anton",
    "Arnaud",
    "Aron",
    "Arthur",
    "Baljit",
    "Ben",
    "Boris",
    "Bram",
    "Brent",
    "Brick",
    "Bryan",
    "Cisse",
    "Dennis",
    "Dieter",
    "Elias",
    "Emilien",
    "Evert",
    "Firas",
    "Frederik",
    "Gillis",
    "Gregory",
    "Guillaume",
    "Hans",
    "Hendrik",
    "Igor",
    "Jakub",
    "Jasper",
    "Jelle",
    "Jens",
    "Jonas",
    "Joni",
    "Joran",
    "Jorian",
    "Jowan",
    "Jurgen",
    "Kasper",
    "Kjell",
    "Kobe",
    "Koen",
    "Kyanii",
    "Laurens",
    "Lennert",
    "Liam",
    "Liena",
    "Lorenzo",
    "Lucas",
    "Lukas",
    "Maarten",
    "Marlene",
    "Mathias",
    "Mathieu",
    "Matthias",
    "Mattias",
    "Maxim",
    "Merijn",
    "Michiel",
    "Mieke",
    "Milan",
    "Mirte",
    "Natan",
    "Nicky",
    "Nicolas",
    "Niels",
    "Niko",
    "Nona",
    "Obim",
    "Othello",
    "Phonkrit",
    "Pieterjan",
    "Preda",
    "Rafael",
    "Rainier",
    "Rick",
    "Rik",
    "Rishad",
    "Robbe",
    "Robin",
    "Roel",
    "Ruben",
    "Rubin",
    "Sam",
    "Sascha",
    "Sigfried",
    "Stanislas",
    "Stijn",
    "Szymon",
    "Sebastien",
    "Thao",
    "Thomas",
    "Timo",
    "Tom",
    "Tuan",
    "Ward",
    "Wout",
    "Wouter",
    "Xavier",
    "Yago",
    "Yang-Yee",
    "Yarne",
    "Yenthe",
    "Younes",
    "Yves"
]

lnames = [
  "Abdo",
  "Aert",
  "Ahmed",
  "Ausloos",
  "Ausloos",
  "Bastiaans",
  "Beddegenoodts",
  "Bijloos",
  "Bogers",
  "Bottu",
  "Braem",
  "Brouns",
  "Bruynseels",
  "Catalano",
  "Claes",
  "Clarysse",
  "Coget",
  "Coremans",
  "Dauwe",
  "De Baets",
  "De Clercq",
  "De Houwer",
  "De Ruysscher",
  "De Sutter",
  "Delarbre",
  "Demol",
  "Descendre",
  "Desmet",
  "Devos",
  "Dierckx",
  "Drabs",
  "Dubois",
  "Engels",
  "Freier",
  "Gataev",
  "Geerinckx",
  "Geldhof",
  "Gervais",
  "Gocmen",
  "Govaers",
  "Hamelryck",
  "Hendrickx",
  "Hendrix",
  "Hoek",
  "Hons",
  "Jacques",
  "Janssen",
  "Janssens",
  "Jeetun",
  "Jemuce",
  "Juste",
  "Kerckhofs",
  "Laporte",
  "Lemeire",
  "Lemmens",
  "Leurquin",
  "Liesenborgs",
  "Lowis",
  "Luypaert",
  "Madugba",
  "Man",
  "Meeus",
  "Melin",
  "Mergaerts",
  "Meyer",
  "Michiels",
  "Michils",
  "Morren",
  "Mounnadi",
  "Mustafa",
  "Nidecki",
  "Nowak",
  "Paeps",
  "Palmans",
  "Pasteels",
  "Paulus",
  "Pauwels",
  "Pechovitch",
  "Pesa",
  "Ramaekers",
  "Rizkallah",
  "Roden",
  "Roets",
  "Romeo",
  "Rubbens",
  "Rummens",
  "Rutten",
  "Scherens",
  "Sebrechts",
  "Seldeslachts",
  "Sels",
  "Sewnarain",
  "Singh",
  "Sol",
  "Spleesters",
  "Sterckx",
  "Symons",
  "Taverniers",
  "Temmerman",
  "Theunis",
  "Thiry",
  "Van Braeckel",
  "Van Briel",
  "Van de Velde",
  "Van den Cruijce",
  "Van der Zwalmen",
  "Van Eetvelt",
  "Van Gansen",
  "Van Grunderbeek",
  "Van Hoof",
  "Van Oosterwyck",
  "van Roekel",
  "Vanden Bosch",
  "Vanden Driesch",
  "Vandenplas",
  "Vanderborght",
  "Vanherf",
  "Vanheusden",
  "Vanluyten",
  "Vavedin",
  "Veelaert",
  "Venneman",
  "Vermeerbergen",
  "Verrycken",
  "Waem",
  "Wandzel",
  "Warlop",
  "Winderickx",
  "Wojtas"
]

def random_name():
    fname = rnd.choice(fnames)
    lname = rnd.choice(lnames)
    return f'{fname} {lname}'

students = set()

while len(students) < NSTUDENTS:
    students.add(random_name())

students = sorted(list(students))
scores = { student: 0 for student in students }
data = []

for _ in range(0, NRACES):
    rnd.shuffle(students)

    for student, score in zip(students, range(NSTUDENTS, 0, -1)):
        scores[student] += score
        data.append(student)

top_n = sorted(scores.items(), key=lambda p: p[1])[0:TOP+1]
top_n_scores = [ score for name, score in top_n ]

if len(set(top_n_scores)) != len(top_n_scores):
    print("ERROR: Duplicates in scores!")
else:
    with open('input.txt', 'w') as file:
        for datum in data:
            print(datum, file=file)