# Stadium capacity lookup by stadium name
# Source: https://en.wikipedia.org/wiki/List_of_FIFA_World_Cup_stadiums

STADIUM_CAPACITY = {
    # 1930 Uruguay
    'Estadio Centenario': 90000,
    'Estadio Gran Parque Central': 20000,
    'Estadio Pocitos': 1000,

    # 1934 Italy
    'Stadio San Siro': 55000,
    'Stadio Littoriale': 50100,
    'Stadio Nazionale PNF': 47300,
    'Stadio Giovanni Berta': 47290,
    'Stadio Giorgio Ascarelli': 40000,
    'Stadio Luigi Ferraris': 36703,
    'Stadio Benito Mussolini': 28140,
    'Stadio Littorio': 8000,

    # 1938 France
    'Stade Olympique de Colombes': 60000,
    'Parc des Princes': 48712,
    'Stade Velodrome': 48000,
    'Parc Lescure': 34694,
    'Stade de la Meinau': 30000,
    'Stade Municipal': 22000,
    'Velodrome Municipal': 21684,
    'Stade Victor Boucquey': 15000,
    'Stade du Fort Carre': 7000,

    # 1950 Brazil
    'Estadio do Maracana': 96000,
    'Estadio do Pacaembu': 60000,
    'Estadio Sete de Setembro': 30000,
    'Estadio Durival de Britto': 10000,
    'Estadio dos Eucaliptos': 20000,
    'Estadio Ilha do Retiro': 20000,

    # 1954 Switzerland
    'Wankdorf Stadium': 64600,
    'St. Jakob Stadium': 54800,
    'Stade Olympique de la Pontaise': 50300,
    'Charmilles Stadium': 35997,
    'Cornaredo Stadium': 35800,
    'Hardturm Stadium': 34800,

    # 1958 Sweden
    'Rasunda Stadium': 52400,
    'Ullevi': 53500,
    'Malmo Stadion': 30000,
    'Olympia': 27000,
    'Tunavallen': 20000,
    'Idrottsparken': 20000,
    'Jernvallen': 20000,
    'Rimnersvallen': 17778,
    'Ryavallen': 15000,
    'Orjans Vall': 15000,
    'Eyravallen': 13000,
    'Arosvallen': 10000,

    # 1962 Chile
    'Estadio Nacional': 66660,
    'Estadio Sausalito': 18037,
    'Estadio Braden Copper Co.': 18000,
    'Estadio Carlos Dittborn': 17786,

    # 1966 England
    'Wembley Stadium': 98600,
    'White City Stadium': 76567,
    'Old Trafford': 58000,
    'Villa Park': 52000,
    'Goodison Park': 50151,
    'Hillsborough Stadium': 42730,
    'Roker Park': 40310,
    'Ayresome Park': 40000,

    # 1970 Mexico
    'Estadio Azteca': 107247,
    'Estadio Jalisco': 71100,
    'Estadio Cuauhtemoc': 35563,
    'Estadio Luis Dosal': 26900,
    'Estadio Nou Camp': 23609,

    # 1974 West Germany
    'Olympiastadion': 77573,
    'Olympiastadion Berlin': 86000,
    'Neckarstadion': 72200,
    'Parkstadion': 72000,
    'Rheinstadion': 70100,
    'Waldstadion': 62200,
    'Volksparkstadion': 61300,
    'Niedersachsenstadion': 60400,
    'Westfalenstadion': 53600,

    # 1978 Argentina
    'Estadio Monumental': 74624,
    'Jose Amalfitani Stadium': 49318,
    'Estadio Cordoba': 46986,
    'Estadio Jose Maria Minella': 43542,
    'Estadio Gigante de Arroyito': 41654,
    'Estadio Ciudad de Mendoza': 34954,

    # 1982 Spain
    'Camp Nou': 97679,
    'Santiago Bernabeu': 90800,
    'Vicente Calderon': 65695,
    'Ramon Sanchez Pizjuan': 68110,
    'Benito Villamarin': 50253,
    'Martínez Valero': 53290,
    'Luis Casanova': 47542,
    'San Mames': 46223,
    'El Molinon': 45153,
    'La Romareda': 41806,
    'Sarrià': 40400,
    'La Rosaleda': 34411,
    'Riazor': 34190,
    'Balaidos': 33000,
    'Jose Zorrilla': 29990,
    'Jose Rico Perez': 28421,
    'Carlos Tartiere': 23500,

    # 1986 Mexico (Azteca already listed)
    'Estadio Olimpico Universitario': 72212,
    'Estadio Universitario': 43780,
    'Estadio La Corregidora': 38576,
    'Estadio Neza 86': 34536,
    'Estadio Tecnologico': 33805,
    'Estadio Nemesio Diez': 32612,
    'Estadio Sergio Leon Chavez': 31336,
    'Estadio Tres de Marzo': 30015,

    # 1990 Italy
    'Stadio Olimpico': 84800,
    'San Siro': 83407,
    'Stadio San Paolo': 83311,
    'Stadio delle Alpi': 71362,
    'Stadio San Nicola': 58270,
    'Stadio Comunale': 49000,
    'Stadio Luigi Ferraris 1990': 44800,
    'Stadio Sant Elia': 44200,
    'Stadio Marc Antonio Bentegodi': 43216,
    'Stadio Friuli': 42311,
    'Stadio Renato Dall Ara': 41200,
    'Stadio La Favorita': 40632,

    # 1994 USA
    'Rose Bowl': 91794,
    'Stanford Stadium': 80906,
    'Pontiac Silverdome': 77557,
    'Giants Stadium': 75338,
    'Cotton Bowl': 63998,
    'Soldier Field': 63117,
    'Citrus Bowl': 61219,
    'Foxboro Stadium': 53644,
    'Robert F. Kennedy Memorial Stadium': 53142,

    # 1998 France
    'Stade de France': 80000,
    'Stade Velodrome 1998': 60000,
    'Parc des Princes 1998': 48875,
    'Stade de Gerland': 44000,
    'Stade Felix-Bollaert': 41300,
    'Stade de la Beaujoire': 39500,
    'Stadium de Toulouse': 37000,
    'Stade Geoffroy-Guichard': 36000,
    'Parc Lescure 1998': 35200,
    'Stade de la Mosson': 34000,

    # 2002 South Korea/Japan
    'Seoul World Cup Stadium': 63961,
    'International Stadium Yokohama': 72327,
    'Saitama Stadium 2002': 63000,
    'Daegu World Cup Stadium': 68014,
    'Busan Asiad Stadium': 55982,
    'Shizuoka Ecopa Stadium': 50600,
    'Nagai Stadium': 50000,
    'Incheon Munhak Stadium': 52179,
    'Miyagi Stadium': 49000,
    'Ulsan Munsu Football Stadium': 43550,
    'Oita Stadium': 43000,
    'Niigata Stadium': 42300,
    'Suwon World Cup Stadium': 43188,
    'Gwangju World Cup Stadium': 42880,
    'Jeonju World Cup Stadium': 42391,
    'Kashima Soccer Stadium': 42000,
    'Kobe Wing Stadium': 42000,
    'Jeju World Cup Stadium': 42256,
    'Sapporo Dome': 42000,
    'Daejeon World Cup Stadium': 40407,

    # 2006 Germany
    'Olympiastadion 2006': 72000,
    'Westfalenstadion 2006': 65000,
    'Allianz Arena': 66000,
    'Gottlieb-Daimler-Stadion': 52000,
    'Arena AufSchalke': 52000,
    'Volksparkstadion 2006': 50000,
    'Commerzbank-Arena': 48000,
    'RheinEnergieStadion': 45000,
    'Niedersachsenstadion 2006': 43000,
    'Zentralstadion': 43000,
    'Fritz-Walter-Stadion': 46000,
    'Max-Morlock-Stadion': 41000,

    # 2010 South Africa
    'FNB Stadium': 84490,
    'Cape Town Stadium': 64100,
    'Moses Mabhida Stadium': 62760,
    'Ellis Park Stadium': 55686,
    'Loftus Versfeld Stadium': 42858,
    'Nelson Mandela Bay Stadium': 42486,
    'Peter Mokaba Stadium': 41733,
    'Mbombela Stadium': 40929,
    'Free State Stadium': 40911,
    'Royal Bafokeng Stadium': 38646,

    # 2014 Brazil
    'Estadio do Maracana 2014': 74738,
    'Estadio Nacional': 69432,
    'Arena de Sao Paulo': 63321,
    'Estadio Castelao': 60348,
    'Estadio Mineirao': 58259,
    'Arena Fonte Nova': 51708,
    'Estadio Beira-Rio': 43394,
    'Arena Pernambuco': 42583,
    'Arena Pantanal': 41112,
    'Arena da Amazonia': 40549,
    'Arena das Dunas': 39971,
    'Arena da Baixada': 39631,

    # Encoding fixes and alternate names
    'Littorale': 50100,
    'Stade Velodrome': 48000,
    'Cavee Verte': 15000,
    'Fort Carree': 7000,
    'Maracana': 96000,
    'Estadio Jornalista Mario Filho': 96000,
    'Durival de Brito': 10000,
    'Independencia': 30000,
    'Comunale di Cornaredo': 35800,
    'Jarnvallen': 20000,
    'Estadio El Teniente-Codelco': 18000,
    'Estadio El Teniente': 18000,
    'Estadio Centenario Montevideo': 90000,
    'Azteca': 107247,
    'Maracana - Estadio Jornalista Mario Filho': 96000,
    # Encoding fixes round 2
    'Stade Velodrome Marseille': 48000,
    'Nou Camp Leon': 23609,
    'Estadio Jose Maria Minella': 43542,
    'Arroyito': 41654,
    'Estadio Olimpico Chateau Carreras': 46986,
    'San Martin': 35000,
    'Estadio Municipal de Balaidos': 33000,
    'Nuevo Estadio': 40000,
    'Sarria': 40400,
    # Final fixes
    'Giuseppe Meazza': 83407,
    'Estadio Olimpico Universitario': 72212,
    'Estadio Corregidora': 38576,
    'Estadio Irapuato': 31336,
    'Estadio Olimpico Chateau Carreras': 46986,
    'Estadio Municipal de Balaidos': 33000,
    'Nou Camp Estadio Leon': 23609,
    'Estadio Jose Maria Minella': 43542,
    'Maracana Estadio Jornalista Mario Filho': 96000,
}

def get_capacity(stadium_name):
    if not isinstance(stadium_name, str):
        return None
    
    # Try exact match
    if stadium_name in STADIUM_CAPACITY:
        return STADIUM_CAPACITY[stadium_name]
    
    # Clean the name — remove special chars for fuzzy matching
    import unicodedata
    def clean(s):
        return ''.join(c for c in unicodedata.normalize('NFD', s)
                      if unicodedata.category(c) != 'Mn').lower()
    
    clean_input = clean(stadium_name)
    
    # Try cleaned match
    for key in STADIUM_CAPACITY:
        if clean(key) == clean_input:
            return STADIUM_CAPACITY[key]
    
    # Try partial match
    for key in STADIUM_CAPACITY:
        if clean(key) in clean_input or clean_input in clean(key):
            return STADIUM_CAPACITY[key]
    
    return None