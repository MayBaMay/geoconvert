# Some country names are close to each other,
# so let us make sure we never confuse them.
special_countries = {
    "demokratische republik kongo": "CD",  # de
    "democratic republic of congo": "CD",  # en
    "democratic republic of the congo": "CD",  # en
    "congo the democratic republic of the": "CD",  # en
    "congo dem republic": "CD",  # en
    "congo democratic republic of": "CD",  # en
    "republique democratique du congo": "CD",  # fr
    "republica democratica do congo": "CD",  # pt
    "rdc": "CD",
    "rd congo": "CD",
    "kinshasa": "CD",
    "brazzaville": "CG",
    # Keep as last country, to make sure we never mistake it for CD
    "republik kongo": "CG",  # de
    "republica do congo": "CG",  # pt
    "congo": "CG",  # en, fr
    # Make sure we never mistake it for GN (Guinea)
    "aquatorialguinea": "GQ",  # es
    "equatorial guinea": "GQ",  # de / en
    "guinea bissau": "GW",  # en / de
    "guinea ecuatorial": "GQ",  # es
    "pap new guinea": "PG",  # en
    "papua neuguinea": "PG",  # de
    "papua new guinea": "PG",  # en
    "papua nueva guinea": "PG",  # es
    # Make sure we never mistake it for JE (Jersey)
    "new jersey": "US",
    # Make sure we never mistake it for SD (Sudan)
    "south sudan": "SS",  # en
    "sudsudan": "SS",  # de
    "sudan del sur": "SS",  # es
    # Make sure we never mistake some countries for IS (Iceland)
    # We would mistake them because Iceland spells Island in German.
    "bouvet island": "BV",  # en
    "christmas island": "CX",  # en
    "heard island": "HM",  # en
    "norfolk island": "NF",  # en
}


countries_fr = {
    **special_countries,
    **{
        "afghanistan": "AF",
        "afrique du sud": "ZA",
        "aland": "AX",
        "albanie": "AL",
        "algerie": "DZ",
        "allemagne": "DE",
        "andorre": "AD",
        "angola": "AO",
        "anguilla": "AI",
        "antarctique": "AQ",
        "antigua et barbuda": "AG",
        "antigue et barbude": "AG",
        "antilles neerlandaises": "AN",
        "arabie saoudite": "SA",
        "argentine": "AR",
        "armenie": "AM",
        "aruba": "AW",
        "australie": "AU",
        "autriche": "AT",
        "azerbaidjan": "AZ",
        "bahamas": "BS",
        "bahrein": "BH",
        "bangladesh": "BD",
        "barbade": "BB",
        "belarus": "BY",
        "belgique": "BE",
        "belize": "BZ",
        "benin": "BJ",
        "bermudes": "BM",
        "bhoutan": "BT",
        "bolivie": "BO",
        "bonaire saint eustache et saba": "BQ",
        "bosnie herzegovine": "BA",
        "botswana": "BW",
        "bouvet": "BV",
        "bresil": "BR",
        "brunei darussalam": "BN",
        "bulgarie": "BG",
        "burkina faso": "BF",
        "burundi": "BI",
        "caimanes": "KY",
        "cambodge": "KH",
        "cameroun": "CM",
        "canada": "CA",
        "cap vert": "CV",
        "centrafrique": "CF",
        "centrafricaine": "CF",
        "chili": "CL",
        "chine": "CN",
        "christmas": "CX",
        "chypre": "CY",
        "cocos keeling": "CC",
        "colombie": "CO",
        "comores": "KM",
        "cook": "CK",
        "coree": "KR",
        "costa rica": "CR",
        "cote d'ivoire": "CI",
        "croatie": "HR",
        "cuba": "CU",
        "curacao": "CW",
        "danemark": "DK",
        "djibouti": "DJ",
        "dominicaine": "DO",
        "dominique": "DM",
        "egypte": "EG",
        "el salvador": "SV",
        "emirats arabes unis": "AE",
        "equateur": "EC",
        "erythree": "ER",
        "espagne": "ES",
        "estonie": "EE",
        "eswatini": "SZ",
        "etats unis": "US",
        "ethiopie": "ET",
        "falkland": "FK",
        "feroe": "FO",
        "fidji": "FJ",
        "finlande": "FI",
        "france": "FR",
        "gabon": "GA",
        "gambie": "GM",
        "georgie": "GE",
        "georgie du sud et les iles sandwich du sud": "GS",
        "ghana": "GH",
        "gibraltar": "GI",
        "grece": "GR",
        "grenade": "GD",
        "groenland": "GL",
        "guadeloupe": "GP",
        "guam": "GU",
        "guatemala": "GT",
        "guernesey": "GG",
        "guinee": "GN",
        "guinee bissau": "GW",
        "guinee equatoriale": "GQ",
        "guyana": "GY",
        "guyane francaise": "GF",
        "haiti": "HT",
        "heard": "HM",
        "honduras": "HN",
        "hong kong": "HK",
        "hongrie": "HU",
        "ile de man": "IM",
        "iles mineures eloignees des etats unis": "UM",
        "iles vierges britanniques": "VG",
        "iles vierges des etats unis": "VI",
        "inde": "IN",
        "indonesie": "ID",
        "iran": "IR",
        "iraq": "IQ",
        "irlande": "IE",
        "islande": "IS",
        "israel": "IL",
        "italie": "IT",
        "jamaique": "JM",
        "japon": "JP",
        "jersey": "JE",
        "jordanie": "JO",
        "kazakhstan": "KZ",
        "kenya": "KE",
        "kirghizistan": "KG",
        "kiribati": "KI",
        "kosovo": "KO",
        "koweit": "KW",
        "lao": "LA",
        "laos": "LA",
        "lesotho": "LS",
        "lettonie": "LV",
        "liban": "LB",
        "liberia": "LR",
        "libye": "LY",
        "libyenne": "LY",
        "liechtenstein": "LI",
        "lituanie": "LT",
        "luxembourg": "LU",
        "macao": "MO",
        "macedoine": "MK",
        "madagascar": "MG",
        "malaisie": "MY",
        "malawi": "MW",
        "maldives": "MV",
        "mali": "ML",
        "malte": "MT",
        "mariannes du nord": "MP",
        "maroc": "MA",
        "marshall": "MH",
        "martinique": "MQ",
        "maurice": "MU",
        "mauritanie": "MR",
        "mayotte": "YT",
        "mexique": "MX",
        "micronesie": "FM",
        "moldova": "MD",
        "monaco": "MC",
        "mongolia": "MN",
        "mongolie": "MN",
        "montenegro": "ME",
        "montserrat": "MS",
        "mozambique": "MZ",
        "myanmar": "MM",
        "birmanie": "MM",
        "namibie": "NA",
        "nauru": "NR",
        "nepal": "NP",
        "nicaragua": "NI",
        "niger": "NE",
        "nigeria": "NG",
        "niue": "NU",
        "norfolk": "NF",
        "norvege": "NO",
        "nouvelle caledonie": "NC",
        "nouvelle zelande": "NZ",
        "ocean indien": "IO",
        "oman": "OM",
        "ouganda": "UG",
        "ouzbekistan": "UZ",
        "pakistan": "PK",
        "palaos": "PW",
        "palestinien occupe": "PS",
        "palestine": "PS",
        "territoires autonomes palestiniens": "PS",
        "panama": "PA",
        "papouasie nouvelle guinee": "PG",
        "paraguay": "PY",
        "pays bas": "NL",
        "perou": "PE",
        "philippines": "PH",
        "pitcairn": "PN",
        "pologne": "PL",
        "polynesie francaise": "PF",
        "porto rico": "PR",
        "portugal": "PT",
        "qatar": "QA",
        "reunion": "RE",
        "roumanie": "RO",
        "royaume uni": "GB",
        "russie": "RU",
        "rwanda": "RW",
        "sahara occidental": "EH",
        "saint barthelemy": "BL",
        "saint kitts et nevis": "KN",
        "saint marin": "SM",
        "saint martin": "MF",
        "saint pierre et miquelon": "PM",
        "saint vincent et les grenadines": "VC",
        "sainte helene": "SH",
        "sainte lucie": "LC",
        "salomon": "SB",
        "samoa": "WS",
        "samoa americaines": "AS",
        "sao tome et principe": "ST",
        "sao tome principe": "ST",
        "senegal": "SN",
        "serbie": "RS",
        "seychelles": "SC",
        "sierra leone": "SL",
        "singapour": "SG",
        "sint maarten": "SX",
        "slovaquie": "SK",
        "slovenie": "SI",
        "somalie": "SO",
        "soudan": "SD",
        "soudan du sud": "SS",
        "sri lanka": "LK",
        "suede": "SE",
        "suisse": "CH",
        "suriname": "SR",
        "surinam": "SR",
        "svalbard et ile jan mayen": "SJ",
        "swaziland": "SZ",
        "syrienne": "SY",
        "tadjikistan": "TJ",
        "taiwan": "TW",
        "tanzania": "TZ",
        "tanzanie": "TZ",
        "tchad": "TD",
        "tcheque": "CZ",
        "terres australes francaises": "TF",
        "thailande": "TH",
        "timor leste": "TL",
        "togo": "TG",
        "tokelau": "TK",
        "tonga": "TO",
        "trinite et tobago": "TT",
        "tunisie": "TN",
        "turkmenistan": "TM",
        "turks et caiques": "TC",
        "turquie": "TR",
        "turkiye": "TR",
        "tuvalu": "TV",
        "ukraine": "UA",
        "uruguay": "UY",
        "vanuatu": "VU",
        "vatican": "VA",
        "venezuela": "VE",
        "viet nam": "VN",
        "vietnam": "VN",
        "wallis et futuna": "WF",
        "yemen": "YE",
        "zambie": "ZM",
        "zimbabwe": "ZW",
    },
}


countries_en = {
    **special_countries,
    **{
        "afghanistan": "AF",
        "albania": "AL",
        "algeria": "DZ",
        "american samoa": "AS",
        "andorra": "AD",
        "angola": "AO",
        "anguilla": "AI",
        "antarctica": "AQ",
        "antigua and barbuda": "AG",
        "argentina": "AR",
        "armenia": "AM",
        "aruba": "AW",
        "australia": "AU",
        "austria": "AT",
        "azerbaijan": "AZ",
        "bahamas": "BS",
        "bahrain": "BH",
        "bangladesh": "BD",
        "barbados": "BB",
        "belarus": "BY",
        "belgium": "BE",
        "belize": "BZ",
        "benin": "BJ",
        "bermuda": "BM",
        "bhutan": "BT",
        "bolivia": "BO",
        "bolivia plurinational state of": "BO",
        "bonaire saint eustatius and saba": "BQ",
        "bosnia and herzegovina": "BA",
        "bosnia herzegovina": "BA",
        "botswana": "BW",
        "bouvet island": "BV",
        "brazil": "BR",
        "britain": "GB",
        "british indian ocean territory": "IO",
        "brunei darussalam": "BN",
        "bulgaria": "BG",
        "burkina faso": "BF",
        "burundi": "BI",
        "cambodia": "KH",
        "cameroon": "CM",
        "canada": "CA",
        "cape verde": "CV",
        "cayman islands": "KY",
        "central african republic": "CF",
        "chad": "TD",
        "chile": "CL",
        "china": "CN",
        "christmas island": "CX",
        "cocos keeling islands": "CC",
        "colombia": "CO",
        "comoros": "KM",
        "cook islands": "CK",
        "costa rica": "CR",
        "cote d'ivoire": "CI",
        "ivory coast": "CI",
        "croatia": "HR",
        "cuba": "CU",
        "curacao": "CW",
        "cyprus": "CY",
        "czech republic": "CZ",
        "czechia": "CZ",
        "denmark": "DK",
        "djibouti": "DJ",
        "dominica": "DM",
        "dominican republic": "DO",
        "ecuador": "EC",
        "egypt": "EG",
        "el salvador": "SV",
        "eritrea": "ER",
        "estonia": "EE",
        "eswatini": "SZ",
        "ethiopia": "ET",
        "falkland islands malvinas": "FK",
        "faroe islands": "FO",
        "fiji": "FJ",
        "finland": "FI",
        "france": "FR",
        "french guiana": "GF",
        "french polynesia": "PF",
        "french southern territories": "TF",
        "gabon": "GA",
        "gambia": "GM",
        "georgia": "GE",
        "germany": "DE",
        "ghana": "GH",
        "gibraltar": "GI",
        "greece": "GR",
        "greenland": "GL",
        "grenada": "GD",
        "guadeloupe": "GP",
        "guam": "GU",
        "guatemala": "GT",
        "guernsey": "GG",
        "guinea": "GN",
        "guyana": "GY",
        "haiti": "HT",
        "heard island": "HM",
        "holy see": "VA",
        "honduras": "HN",
        "hong kong": "HK",
        "hungary": "HU",
        "iceland": "IS",
        "india": "IN",
        "indonesia": "ID",
        "iran": "IR",
        "iraq": "IQ",
        "ireland": "IE",
        "isle of man": "IM",
        "israel": "IL",
        "italy": "IT",
        "jamaica": "JM",
        "japan": "JP",
        "jersey": "JE",
        "jordan": "JO",
        "kazakhstan": "KZ",
        "kenya": "KE",
        "kiribati": "KI",
        "kosovo": "KO",
        "korea": "KR",
        "kuwait": "KW",
        "kyrgyz republic": "KG",
        "kyrgyzstan": "KG",
        "lao people's democratic republic": "LA",
        "lao pdr": "LA",
        "lao": "LA",
        "laos": "LA",
        "latvia": "LV",
        "lebanon": "LB",
        "lesotho": "LS",
        "liberia": "LR",
        "libya": "LY",
        "libyan arab jamahiriya": "LY",
        "liechtenstein": "LI",
        "lithuania": "LT",
        "luxembourg": "LU",
        "macao": "MO",
        "macedonia": "MK",
        "madagascar": "MG",
        "malawi": "MW",
        "malaysia": "MY",
        "maldives": "MV",
        "mali": "ML",
        "malta": "MT",
        "marocco": "MA",
        "marshall islands": "MH",
        "martinique": "MQ",
        "mauritania": "MR",
        "mauritius": "MU",
        "mayotte": "YT",
        "mexico": "MX",
        "micronesia": "FM",
        "moldova": "MD",
        "monaco": "MC",
        "mongolia": "MN",
        "montenegro": "ME",
        "montserrat": "MS",
        "morocco": "MA",
        "mozambique": "MZ",
        "myanmar": "MM",
        "namibia": "NA",
        "nauru": "NR",
        "nepal": "NP",
        "netherlands": "NL",
        "netherlands antilles": "AN",
        "new caledonia": "NC",
        "new zealand": "NZ",
        "nicaragua": "NI",
        "niger": "NE",
        "nigeria": "NG",
        "niue": "NU",
        "norfolk island": "NF",
        "northern mariana islands": "MP",
        "norway": "NO",
        "oman": "OM",
        "pakistan": "PK",
        "palau": "PW",
        "state of palestine": "PS",
        "palestine state of": "PS",
        "palestinian territory": "PS",
        "palestinian territories": "PS",
        "west bank": "PS",
        "panama": "PA",
        "paraguay": "PY",
        "peru": "PE",
        "philippines": "PH",
        "pitcairn": "PN",
        "poland": "PL",
        "portugal": "PT",
        "puerto rico": "PR",
        "qatar": "QA",
        "reunion": "RE",
        "romania": "RO",
        "russia": "RU",
        "russian federation": "RU",
        "rwanda": "RW",
        "saint barthelemy": "BL",
        "saint helena": "SH",
        "saint kitts and nevis": "KN",
        "saint lucia": "LC",
        "saint martin": "MF",
        "saint pierre and miquelon": "PM",
        "saint vincent and the grenadines": "VC",
        "samoa": "WS",
        "san marino": "SM",
        "sao tome and principe": "ST",
        "sao tome principe": "ST",
        "saudi arabia": "SA",
        "senegal": "SN",
        "serbia": "RS",
        "seychelles": "SC",
        "sierra leone": "SL",
        "singapore": "SG",
        "sint maarten": "SX",
        "slovakia": "SK",
        "slovenia": "SI",
        "solomon islands": "SB",
        "somalia": "SO",
        "south africa": "ZA",
        "south georgia and the south sandwich islands": "GS",
        "southern africa": "ZA",
        "spain": "ES",
        "sri lanka": "LK",
        "sudan": "SD",
        "suriname": "SR",
        "svalbard and jan mayen": "SJ",
        "swaziland": "SZ",
        "sweden": "SE",
        "switzerland": "CH",
        "swiss": "CH",
        "syria": "SY",
        "syrian arab republic": "SY",
        "taiwan": "TW",
        "taiwan province of china": "TW",
        "tajikistan": "TJ",
        "tanzania": "TZ",
        "tanzania united republic of": "TZ",
        "thailand": "TH",
        "timor leste": "TL",
        "togo": "TG",
        "tokelau": "TK",
        "tonga": "TO",
        "trinidad and tobago": "TT",
        "tunisia": "TN",
        "turkey": "TR",
        "turkiye": "TR",
        "turkmenistan": "TM",
        "turks and caicos islands": "TC",
        "tuvalu": "TV",
        "uganda": "UG",
        "ukraine": "UA",
        "united arab emirates": "AE",
        "united kingdom": "GB",
        "usa": "US",
        "united states": "US",
        "united states minor outlying islands": "UM",
        "uruguay": "UY",
        "uzbekistan": "UZ",
        "vanuatu": "VU",
        "venezuela": "VE",
        "venezuela bolivarian republic of": "VE",
        "viet nam": "VN",
        "vietnam": "VN",
        "virgin islands british": "VG",
        "virgin islands us": "VI",
        "wallis and futuna": "WF",
        "western sahara": "EH",
        "yemen": "YE",
        "zambia": "ZM",
        "zimbabwe": "ZW",
        "aland islands": "AX",
    },
}


countries_de = {
    **special_countries,
    **{
        "agypten": "EG",
        "athiopien": "ET",
        "afghanistan": "AF",
        "albanien": "AL",
        "algerien": "DZ",
        "andorra": "AD",
        "angola": "AO",
        "antigua und barbuda": "AG",
        "argentinien": "AR",
        "armenien": "AM",
        "aserbaidschan": "AZ",
        "australien": "AU",
        "bahamas": "BS",
        "bahrain": "BH",
        "bangladesch": "BD",
        "barbados": "BB",
        "belgien": "BE",
        "belize": "BZ",
        "benin": "BJ",
        "bhutan": "BT",
        "bolivien": "BO",
        "bosnien und herzegowina": "BA",
        "botswana": "BW",
        "brasilien": "BR",
        "brunei": "BN",
        "bulgarien": "BG",
        "burkina faso": "BF",
        "burundi": "BI",
        "chile": "CL",
        "costa rica": "CR",
        "danemark": "DK",
        "deutschland": "DE",
        "dominica": "DM",
        "dominikanische republik": "DO",
        "dschibuti": "DJ",
        "ecuador": "EC",
        "el salvador": "SV",
        "elfenbeinkuste": "CI",
        "eritrea": "ER",
        "estland": "EE",
        "eswatini": "SZ",
        "fidschi": "FJ",
        "finnland": "FI",
        "frankreich": "FR",
        "gabun": "GA",
        "gambia": "GM",
        "georgien": "GE",
        "ghana": "GH",
        "grenada": "GD",
        "griechenland": "GR",
        "guatemala": "GT",
        "guinea": "GN",
        "guyana": "GY",
        "haiti": "HT",
        "honduras": "HN",
        "indien": "IN",
        "indonesien": "ID",
        "irak": "IQ",
        "iran": "IR",
        "irland": "IE",
        "island": "IS",
        "israel": "IL",
        "italien": "IT",
        "jamaika": "JM",
        "japan": "JP",
        "jemen": "YE",
        "jordanien": "JO",
        "kambodscha": "KH",
        "kamerun": "CM",
        "kanada": "CA",
        "kap verde": "CV",
        "kasachstan": "KZ",
        "katar": "QA",
        "kenia": "KE",
        "kirgisistan": "KG",
        "kiribati": "KI",
        "kolumbien": "CO",
        "komoren": "KM",
        "korea nord": "KP",
        "korea sud": "KR",
        "kroatien": "HR",
        "kuba": "CU",
        "kuwait": "KW",
        "laos": "LA",
        "lesotho": "LS",
        "lettland": "LV",
        "libanon": "LB",
        "liberia": "LR",
        "libyen": "LY",
        "liechtenstein": "LI",
        "litauen": "LT",
        "luxemburg": "LU",
        "madagaskar": "MG",
        "malawi": "MW",
        "malaysia": "MY",
        "malediven": "MV",
        "mali": "ML",
        "malta": "MT",
        "marokko": "MA",
        "marshallinseln": "MH",
        "mauretanien": "MR",
        "mauritius": "MU",
        "mazedonien": "MK",
        "mexiko": "MX",
        "mikronesien": "FM",
        "moldawien": "MD",
        "monaco": "MC",
        "mongolei": "MN",
        "montenegro": "ME",
        "mosambik": "MZ",
        "myanmar": "MM",
        "namibia": "NA",
        "nauru": "NR",
        "nepal": "NP",
        "neuseeland": "NZ",
        "nicaragua": "NI",
        "niederlande": "NL",
        "niger": "NE",
        "nigeria": "NG",
        "norwegen": "NO",
        "osterreich": "AT",
        "oman": "OM",
        "osttimor": "TL",
        "pakistan": "PK",
        "palastina": "PS",
        "palau": "PW",
        "panama": "PA",
        "paraguay": "PY",
        "peru": "PE",
        "philippinen": "PH",
        "polen": "PL",
        "portugal": "PT",
        "republik china": "TW",
        "ruanda": "RW",
        "rumanien": "RO",
        "russland": "RU",
        "salomonen": "SB",
        "sambia": "ZM",
        "samoa": "WS",
        "san marino": "SM",
        "sao tome und principe": "ST",
        "saudi arabien": "SA",
        "schweden": "SE",
        "schweiz": "CH",
        "senegal": "SN",
        "serbien": "RS",
        "seychellen": "SC",
        "sierra leone": "SL",
        "simbabwe": "ZW",
        "singapur": "SG",
        "slowakei": "SK",
        "slowenien": "SI",
        "somalia": "SO",
        "spanien": "ES",
        "sri lanka": "LK",
        "st kitts und nevis": "KN",
        "st lucia": "LC",
        "st vincent und die grenadinen": "VC",
        "sudan": "SD",
        "sudafrika": "ZA",
        "suriname": "SR",
        "swasiland": "SZ",
        "syrien": "SY",
        "tadschikistan": "TJ",
        "tansania": "TZ",
        "thailand": "TH",
        "togo": "TG",
        "tonga": "TO",
        "trinidad und tobago": "TT",
        "tschad": "TD",
        "tschechien": "CZ",
        "turkei": "TR",
        "tunesien": "TN",
        "turkmenistan": "TM",
        "tuvalu": "TV",
        "uganda": "UG",
        "ukraine": "UA",
        "ungarn": "HU",
        "uruguay": "UY",
        "usbekistan": "UZ",
        "vanuatu": "VU",
        "vatikanstadt": "VA",
        "venezuela": "VE",
        "vereinigte arabische emirate": "AE",
        "vereinigte staaten": "US",
        "vereinigtes konigreich": "GB",
        "vietnam": "VN",
        "volksrepublik china": "CN",
        "weirussland": "BY",
        "zentralafrikanische republik": "CF",
        "zypern": "CY",
    },
}


countries_pt = {
    **special_countries,
    **{
        "afeganistao": "AF",
        "africa do sul": "ZA",
        "ilhas aland": "AX",
        "albania": "AL",
        "alemanha": "DE",
        "andorra": "AD",
        "angola": "AO",
        "anguilla": "AI",
        "antartida": "AQ",
        "antigua e barbuda": "AG",
        "arabia saudita": "SA",
        "argelia": "DZ",
        "argentina": "AR",
        "armenia": "AM",
        "aruba": "AW",
        "australia": "AU",
        "austria": "AT",
        "azerbaijao": "AZ",
        "bahamas": "BS",
        "bahrein": "BH",
        "bangladesh": "BD",
        "barbados": "BB",
        "belgica": "BE",
        "belize": "BZ",
        "benim": "BJ",
        "bermudas": "BM",
        "bielorrussia": "BY",
        "bolivia": "BO",
        "paises baixos caribenhos": "BQ",
        "bosnia e herzegovina": "BA",
        "botswana": "BW",
        "ilha bouvet": "BV",
        "brasil": "BR",
        "brunei": "BN",
        "bulgaria": "BG",
        "burkina faso": "BF",
        "burundi": "BI",
        "butao": "BT",
        "cabo verde": "CV",
        "camboja": "KH",
        "camaroes": "CM",
        "canada": "CA",
        "ilhas cayman": "KY",
        "cazaquistao": "KZ",
        "republica centro africana": "CF",
        "chade": "TD",
        "chequia": "CZ",
        "chile": "CL",
        "china": "CN",
        "chipre": "CY",
        "ilha do natal": "CX",
        "ilhas cocos keeling": "CC",
        "colombia": "CO",
        "comores": "KM",
        "ilhas cook": "CK",
        "coreia do sul": "KR",
        "coreia do norte": "KP",
        "costa do marfim": "CI",
        "costa rica": "CR",
        "croacia": "HR",
        "cuba": "CU",
        "curacao": "CW",
        "dinamarca": "DK",
        "djibouti": "DJ",
        "dominica": "DM",
        "republica dominicana": "DO",
        "egito": "EG",
        "el salvador": "SV",
        "emirados arabes unidos": "AE",
        "equador": "EC",
        "eritreia": "ER",
        "eslovaquia": "SK",
        "eslovenia": "SI",
        "espanha": "ES",
        "estados unidos": "US",
        "estonia": "EE",
        "etiopia": "ET",
        "ilhas feroe": "FO",
        "fiji": "FJ",
        "filipinas": "PH",
        "finlandia": "FI",
        "franca": "FR",
        "gabao": "GA",
        "gambia": "GM",
        "gana": "GH",
        "georgia": "GE",
        "ilhas georgia do sul e sandwich do sul": "GS",
        "gibraltar": "GI",
        "grecia": "GR",
        "granada": "GD",
        "gronelandia": "GL",
        "guadalupe": "GP",
        "guam": "GU",
        "guatemala": "GT",
        "guernsey": "GG",
        "guiana": "GY",
        "guiana francesa": "GF",
        "guine bissau": "GW",
        "guine": "GN",
        "guine equatorial": "GQ",
        "haiti": "HT",
        "ilha heard e ilhas mcdonald": "HM",
        "honduras": "HN",
        "hong kong": "HK",
        "hungria": "HU",
        "iemen": "YE",
        "india": "IN",
        "indonesia": "ID",
        "iraque": "IQ",
        "irao": "IR",
        "irlanda": "IE",
        "islandia": "IS",
        "israel": "IL",
        "italia": "IT",
        "jamaica": "JM",
        "japao": "JP",
        "jersey": "JE",
        "jordania": "JO",
        "kiribati": "KI",
        "kuwait": "KW",
        "laos": "LA",
        "lesoto": "LS",
        "letonia": "LV",
        "libano": "LB",
        "liberia": "LR",
        "libia": "LY",
        "liechtenstein": "LI",
        "lituania": "LT",
        "luxemburgo": "LU",
        "macau": "MO",
        "macedonia do norte": "MK",
        "madagascar": "MG",
        "malasia": "MY",
        "malawi": "MW",
        "maldivas": "MV",
        "mali": "ML",
        "malta": "MT",
        "ilhas malvinas": "FK",
        "ilha de man": "IM",
        "marianas setentrionais": "MP",
        "marrocos": "MA",
        "ilhas marshall": "MH",
        "martinica": "MQ",
        "mauricia": "MU",
        "mauritania": "MR",
        "mayotte": "YT",
        "ilhas menores distantes dos estados unidos": "UM",
        "mexico": "MX",
        "mianmar": "MM",
        "estados federados da micronesia": "FM",
        "mocambique": "MZ",
        "moldavia": "MD",
        "monaco": "MC",
        "mongolia": "MN",
        "montenegro": "ME",
        "montserrat": "MS",
        "namibia": "NA",
        "nauru": "NR",
        "nepal": "NP",
        "nicaragua": "NI",
        "niger": "NE",
        "nigeria": "NG",
        "niue": "NU",
        "ilha norfolk": "NF",
        "noruega": "NO",
        "nova caledonia": "NC",
        "nova zelandia": "NZ",
        "oma": "OM",
        "paises baixos": "NL",
        "palau": "PW",
        "palestina": "PS",
        "panama": "PA",
        "papua nova guine": "PG",
        "paquistao": "PK",
        "paraguai": "PY",
        "peru": "PE",
        "pitcairn": "PN",
        "polinesia francesa": "PF",
        "polonia": "PL",
        "porto rico": "PR",
        "portugal": "PT",
        "catar": "QA",
        "quenia": "KE",
        "quirguistao": "KG",
        "reino unido": "GB",
        "reuniao": "RE",
        "romenia": "RO",
        "ruanda": "RW",
        "russia": "RU",
        "saara ocidental": "EH",
        "samoa americana": "AS",
        "samoa": "WS",
        "saint pierre e miquelon": "PM",
        "ilhas salomao": "SB",
        "san marino": "SM",
        "santa helena ascensao e tristao da cunha": "SH",
        "santa lucia": "LC",
        "sao bartolomeu": "BL",
        "sao cristovao e nevis": "KN",
        "sao martinho": "MF",
        "sao tome e principe": "ST",
        "sao vicente e granadinas": "VC",
        "senegal": "SN",
        "serra leoa": "SL",
        "servia": "RS",
        "seicheles": "SC",
        "singapura": "SG",
        "siria": "SY",
        "somalia": "SO",
        "sri lanka": "LK",
        "essuatini": "SZ",
        "sudao": "SD",
        "sudao do sul": "SS",
        "suecia": "SE",
        "suica": "CH",
        "suriname": "SR",
        "svalbard e jan mayen": "SJ",
        "tailandia": "TH",
        "taiwan": "TW",
        "tajiquistao": "TJ",
        "tanzania": "TZ",
        "terras austrais e antarticas francesas": "TF",
        "territorio britanico do oceano indico": "IO",
        "timor leste": "TL",
        "togo": "TG",
        "toquelau": "TK",
        "tonga": "TO",
        "trinidad e tobago": "TT",
        "tunisia": "TN",
        "turks e caicos": "TC",
        "turquemenistao": "TM",
        "turquia": "TR",
        "tuvalu": "TV",
        "ucrania": "UA",
        "uganda": "UG",
        "uruguai": "UY",
        "uzbequistao": "UZ",
        "vanuatu": "VU",
        "vaticano": "VA",
        "venezuela": "VE",
        "vietna": "VN",
        "ilhas virgens americanas": "VI",
        "ilhas virgens britanicas": "VG",
        "wallis e futuna": "WF",
        "zambia": "ZM",
        "zimbabwe": "ZW",
    },
}


countries_es = {
    **special_countries,
    **{
        "afganistan": "AF",
        "sudafrica": "ZA",
        "islas aland": "AX",
        "albania": "AL",
        "alemania": "DE",
        "andorra": "AD",
        "angola": "AO",
        "anguila": "AI",
        "antartida": "AQ",
        "antigua y barbuda": "AG",
        "arabia saudita": "SA",
        "argelia": "DZ",
        "argentina": "AR",
        "armenia": "AM",
        "aruba": "AW",
        "australia": "AU",
        "austria": "AT",
        "azerbaiyan": "AZ",
        "bahamas": "BS",
        "bahrein": "BH",
        "bangladesh": "BD",
        "barbados": "BB",
        "belgica": "BE",
        "belice": "BZ",
        "benin": "BJ",
        "bermudas": "BM",
        "bielorrusia": "BY",
        "bolivia": "BO",
        "caribe neerlandes": "BQ",
        "bosnia y herzegovina": "BA",
        "botswana": "BW",
        "isla bouvet": "BV",
        "brasil": "BR",
        "brunido": "BN",
        "bulgaria": "BG",
        "burkina faso": "BF",
        "burundi": "BI",
        "butan": "BT",
        "butao": "BT",
        "cabo verde": "CV",
        "camboya": "KH",
        "camerun": "CM",
        "canada": "CA",
        "islas caiman": "KY",
        "kazajstan": "KZ",
        "republica centroafricana": "CF",
        "chad": "TD",
        "cheki": "CZ",
        "chile": "CL",
        "china": "CN",
        "chipre": "CY",
        "isla de navidad": "CX",
        "islas cocos keeling": "CC",
        "colombia": "CO",
        "comores": "KM",
        "islas cook": "CK",
        "corea del sur": "KR",
        "corea del norte": "KP",
        "costa de marfil": "CI",
        "costa rica": "CR",
        "croacia": "HR",
        "cuba": "CU",
        "curacao": "CW",
        "curazao": "CW",
        "dinamarca": "DK",
        "djibouti": "DJ",
        "dominica": "DM",
        "republica dominicana": "DO",
        "egipto": "EG",
        "el salvador": "SV",
        "emiratos arabes unidos": "AE",
        "ecuador": "EC",
        "eritrea": "ER",
        "eslovaquia": "SK",
        "eslovenia": "SI",
        "espana": "ES",
        "estados unidos": "US",
        "estonia": "EE",
        "etiopia": "ET",
        "islas feroe": "FO",
        "fiji": "FJ",
        "fiyi": "FJ",
        "filipinas": "PH",
        "finlandia": "FI",
        "francia": "FR",
        "gabon": "GA",
        "gambia": "GM",
        "ghana": "GH",
        "georgia": "GE",
        "islas georgia del sur y islas sandwich del sur": "GS",
        "islas georgia del sur y sandwich del sur": "GS",
        "gibraltar": "GI",
        "grecia": "GR",
        "granada": "GD",
        "groenlandia": "GL",
        "guadalupe": "GP",
        "guam": "GU",
        "guatemala": "GT",
        "guernsey": "GG",
        "guayana": "GY",
        "guayana francesa": "GF",
        "guinea": "GN",
        "haiti": "HT",
        "islas heard y mcdonald": "HM",
        "heard y mcdonald": "HM",
        "honduras": "HN",
        "hong kong": "HK",
        "hungria": "HU",
        "yemen": "YE",
        "india": "IN",
        "indonesia": "ID",
        "irak": "IQ",
        "iran": "IR",
        "irlanda": "IE",
        "islandia": "IS",
        "israel": "IL",
        "italia": "IT",
        "jamaica": "JM",
        "japon": "JP",
        "jersey": "JE",
        "jordan": "JO",
        "kiribati": "KI",
        "kuwait": "KW",
        "laos": "LA",
        "lesoto": "LS",
        "letonia": "LV",
        "libano": "LB",
        "liberia": "LR",
        "libia": "LY",
        "liechtenstein": "LI",
        "lituania": "LT",
        "luxemburgo": "LU",
        "macao": "MO",
        "macedonia del norte": "MK",
        "madagascar": "MG",
        "malasia": "MY",
        "malawi": "MW",
        "maldivas": "MV",
        "mali": "ML",
        "malta": "MT",
        "islas malvinas": "FK",
        "isla de man": "IM",
        "marianas del norte": "MP",
        "marruecos": "MA",
        "islas marshall": "MH",
        "martinica": "MQ",
        "mauricio": "MU",
        "mauritania": "MR",
        "mayotte": "YT",
        "islas ultramarinas menores de los estados unidos": "UM",
        "ultramarinas menores de los estados unidos": "UM",
        "mexico": "MX",
        "myanmar": "MM",
        "estados federados de micronesia": "FM",
        "mozambique": "MZ",
        "moldavia": "MD",
        "monaco": "MC",
        "mongolia": "MN",
        "montenegro": "ME",
        "montserrat": "MS",
        "namibia": "NA",
        "nauru": "NR",
        "nepal": "NP",
        "nicaragua": "NI",
        "niger": "NE",
        "nigeria": "NG",
        "niue": "NU",
        "isla norfolk": "NF",
        "norfolk": "NF",
        "noruega": "NO",
        "nueva caledonia": "NC",
        "nueva zelanda": "NZ",
        "oman": "OM",
        "paises bajos": "NL",
        "palaos": "PW",
        "palestina": "PS",
        "panama": "PA",
        "pakistan": "PK",
        "paraguay": "PY",
        "peru": "PE",
        "pitcairn": "PN",
        "islas pitcairn": "PN",
        "polinesia francesa": "PF",
        "polonia": "PL",
        "puerto rico": "PR",
        "portugal": "PT",
        "katar": "QA",
        "qatar": "QA",
        "kenia": "KE",
        "kirguistan": "KG",
        "reino unido": "GB",
        "reunion": "RE",
        "rumania": "RO",
        "ruanda": "RW",
        "rusia": "RU",
        "sahara occidental": "EH",
        "samoa americana": "AS",
        "samoa": "WS",
        "san pedro y miquelon": "PM",
        "islas salomon": "SB",
        "san marino": "SM",
        "santa elena ascension y tristan de acuna": "SH",
        "santa lucia": "LC",
        "san bartolome": "BL",
        "san cristobal y nieves": "KN",
        "san martin": "MF",
        "santo tome y principe": "ST",
        "san vicente y las granadinas": "VC",
        "senegal": "SN",
        "sierra leona": "SL",
        "serbia": "RS",
        "seychelles": "SC",
        "singapur": "SG",
        "siria": "SY",
        "somalia": "SO",
        "sri lanka": "LK",
        "esuatini": "SZ",
        "sudan": "SD",
        "suecia": "SE",
        "suiza": "CH",
        "surinam": "SR",
        "svalbard y jan mayen": "SJ",
        "tailandia": "TH",
        "taiwan": "TW",
        "tayikistan": "TJ",
        "tanzania": "TZ",
        "tierras australes y antarticas francesas": "TF",
        "territorio britanico del oceano indico": "IO",
        "timor oriental": "TL",
        "togo": "TG",
        "tokelau": "TK",
        "tonga": "TO",
        "trinidad y tobago": "TT",
        "tunez": "TN",
        "turcas y caicos": "TC",
        "islas turcas y caicos": "TC",
        "turkmenistan": "TM",
        "turquia": "TR",
        "tuvalu": "TV",
        "ucrania": "UA",
        "uganda": "UG",
        "uruguay": "UY",
        "uzbekistan": "UZ",
        "vanuatu": "VU",
        "vaticano": "VA",
        "venezuela": "VE",
        "vietnam": "VN",
        "islas virgenes americanas": "VI",
        "islas virgenes britanicas": "VG",
        "wallis y futuna": "WF",
        "zambia": "ZM",
        "zimbabue": "ZW",
    },
}


language_to_country_names = {
    "de": countries_de,
    "en": countries_en,
    "fr": countries_fr,
    "pt": countries_pt,
    "es": countries_es,
}


# Association from a country code to another country code.
# These territories generally have a code but are not considered as an
# independent country and actually and depend
# from another country.
country_territories = {
    "FR": frozenset(
        ["RE", "TF", "BL", "YT", "WF", "NC", "PF", "PM", "MQ", "GF", "MF", "GP"]
    ),
    "NL": frozenset(["SX", "BQ", "CW"]),
    "NO": frozenset(["BV", "SJ"]),
    "NZ": frozenset(["TK"]),
    "PS": frozenset(["GZ"]),
    "UK": frozenset(["SH", "FK", "GS", "IO"]),
}


# country_territories reciprocal
territory_to_country = {
    territory: country
    for country, territories in country_territories.items()
    for territory in territories
}
