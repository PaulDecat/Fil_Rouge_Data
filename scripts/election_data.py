from __future__ import annotations

from pathlib import Path
import unicodedata

import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / 'data'
RAW_DIR = DATA_DIR / 'raw'
REFERENCE_DIR = DATA_DIR / 'reference'
PROCESSED_DIR = DATA_DIR / 'processed'

REFERENCE_FILE = REFERENCE_DIR / 'presidentielle_2002_2022_reference.csv'
PROCESSED_FILE = PROCESSED_DIR / 'presidentielle_2002_2022_complete.csv'

RAW_2022_FILES = {
    1: RAW_DIR / 'Presidentielle_2022_Resultats_Tour_1_c.txt',
    2: RAW_DIR / 'Presidentielle_2022_Resultats_Tour_2_c.txt',
}

PARTY_2022 = {
    'M. MACRON Emmanuel': 'LREM',
    'Mme LE PEN Marine': 'RN',
    'M. MÉLENCHON Jean-Luc': 'FI',
    'M. ZEMMOUR Éric': 'Rec',
    'Mme PÉCRESSE Valérie': 'LR',
    'M. JADOT Yannick': 'EELV',
    'M. LASSALLE Jean': 'Rés',
    'M. ROUSSEL Fabien': 'PCF',
    'M. DUPONT-AIGNAN Nicolas': 'DLF',
    'Mme HIDALGO Anne': 'PS',
    'M. POUTOU Philippe': 'NPA',
    'Mme ARTHAUD Nathalie': 'LO',
}

DEPARTMENT_TO_REGION = {
    '01': 'Auvergne-Rhone-Alpes', '02': 'Hauts-de-France', '03': 'Auvergne-Rhone-Alpes',
    '04': 'Provence-Alpes-Cote d\'Azur', '05': 'Provence-Alpes-Cote d\'Azur', '06': 'Provence-Alpes-Cote d\'Azur',
    '07': 'Auvergne-Rhone-Alpes', '08': 'Grand Est', '09': 'Occitanie', '10': 'Grand Est',
    '11': 'Occitanie', '12': 'Occitanie', '13': 'Provence-Alpes-Cote d\'Azur', '14': 'Normandie',
    '15': 'Auvergne-Rhone-Alpes', '16': 'Nouvelle-Aquitaine', '17': 'Nouvelle-Aquitaine',
    '18': 'Centre-Val de Loire', '19': 'Nouvelle-Aquitaine', '21': 'Bourgogne-Franche-Comte',
    '22': 'Bretagne', '23': 'Nouvelle-Aquitaine', '24': 'Nouvelle-Aquitaine', '25': 'Bourgogne-Franche-Comte',
    '26': 'Auvergne-Rhone-Alpes', '27': 'Normandie', '28': 'Centre-Val de Loire',
    '29': 'Bretagne', '2A': 'Corse', '2B': 'Corse', '30': 'Occitanie', '31': 'Occitanie',
    '32': 'Occitanie', '33': 'Nouvelle-Aquitaine', '34': 'Occitanie', '35': 'Bretagne',
    '36': 'Centre-Val de Loire', '37': 'Centre-Val de Loire', '38': 'Auvergne-Rhone-Alpes',
    '39': 'Bourgogne-Franche-Comte', '40': 'Nouvelle-Aquitaine', '41': 'Centre-Val de Loire',
    '42': 'Auvergne-Rhone-Alpes', '43': 'Auvergne-Rhone-Alpes', '44': 'Pays de la Loire',
    '45': 'Centre-Val de Loire', '46': 'Occitanie', '47': 'Nouvelle-Aquitaine', '48': 'Occitanie',
    '49': 'Pays de la Loire', '50': 'Normandie', '51': 'Grand Est', '52': 'Grand Est',
    '53': 'Pays de la Loire', '54': 'Grand Est', '55': 'Grand Est', '56': 'Bretagne',
    '57': 'Grand Est', '58': 'Bourgogne-Franche-Comte', '59': 'Hauts-de-France',
    '60': 'Hauts-de-France', '61': 'Normandie', '62': 'Hauts-de-France', '63': 'Auvergne-Rhone-Alpes',
    '64': 'Nouvelle-Aquitaine', '65': 'Occitanie', '66': 'Occitanie', '67': 'Grand Est',
    '68': 'Grand Est', '69': 'Auvergne-Rhone-Alpes', '70': 'Bourgogne-Franche-Comte',
    '71': 'Bourgogne-Franche-Comte', '72': 'Pays de la Loire', '73': 'Auvergne-Rhone-Alpes',
    '74': 'Auvergne-Rhone-Alpes', '75': 'Ile-de-France', '76': 'Normandie',
    '77': 'Ile-de-France', '78': 'Ile-de-France', '79': 'Nouvelle-Aquitaine',
    '80': 'Hauts-de-France', '81': 'Occitanie', '82': 'Occitanie', '83': 'Provence-Alpes-Cote d\'Azur',
    '84': 'Provence-Alpes-Cote d\'Azur', '85': 'Pays de la Loire', '86': 'Nouvelle-Aquitaine',
    '87': 'Nouvelle-Aquitaine', '88': 'Grand Est', '89': 'Bourgogne-Franche-Comte',
    '90': 'Bourgogne-Franche-Comte', '91': 'Ile-de-France', '92': 'Ile-de-France',
    '93': 'Ile-de-France', '94': 'Ile-de-France', '95': 'Ile-de-France', '971': 'Guadeloupe',
    '972': 'Martinique', '973': 'Guyane', '974': 'La Reunion', '976': 'Mayotte',
}

FAMILY_MAPPING = {
    'RPR': 'Droite', 'UMP': 'Droite', 'LR': 'Droite',
    'PS': 'Gauche', 'PRG': 'Gauche',
    'FN': 'Extrême droite', 'RN': 'Extrême droite', 'MNR': 'Extrême droite', 'Rec': 'Extrême droite',
    'PCF': 'Extrême gauche', 'LO': 'Extrême gauche', 'NPA': 'Extrême gauche', 'LCR': 'Extrême gauche', 'PT': 'Extrême gauche',
    'PG': 'Gauche radicale', 'FI': 'Gauche radicale',
    'UDF': 'Centre', 'MoDem': 'Centre',
    'EM': 'Centre', 'LREM': 'Centre',
    'Verts': 'Écologie', 'EELV': 'Écologie',
    'DLF': 'Souverainiste', 'UPR': 'Souverainiste', 'MPF': 'Souverainiste',
    'CPNT': 'Divers', 'CAP21': 'Divers', 'FRS': 'Divers', 'S&P': 'Divers', 'Rés': 'Divers', 'MDC': 'Divers', 'DL': 'Divers'
}


def _normalize_text(value: str) -> str:
    return unicodedata.normalize('NFC', value.strip())


def _candidate_label(sex: str, last_name: str, first_name: str) -> str:
    civility = 'M.' if sex == 'M' else 'Mme'
    return _normalize_text(f'{civility} {last_name} {first_name}')


def _aggregate_level(
    candidate_rows: pd.DataFrame,
    territory_totals: pd.DataFrame,
    tour: int,
    level: str,
    territory_column: str,
    source: str,
) -> pd.DataFrame:
    grouped_votes = candidate_rows.groupby([territory_column, 'candidat'], as_index=False)['voix'].sum()
    merged = grouped_votes.merge(territory_totals, on=territory_column, how='left')
    merged['%ins'] = (merged['voix'] / merged['inscrits'] * 100).round(2)
    merged['%exp'] = (merged['voix'] / merged['exprimes'] * 100).round(2)
    merged['tour'] = tour
    merged['annee'] = 2022
    merged['parti'] = merged['candidat'].map(PARTY_2022)
    merged['famille'] = merged['parti'].map(FAMILY_MAPPING).fillna('Divers')
    merged['niveau_geo'] = level
    merged['territoire'] = merged[territory_column].astype(str)
    merged['source'] = source
    return merged.drop(columns=['inscrits', 'exprimes', territory_column])


def load_reference_history() -> pd.DataFrame:
    if not REFERENCE_FILE.exists():
        raise FileNotFoundError(f'Reference dataset not found: {REFERENCE_FILE}')

    df = pd.read_csv(REFERENCE_FILE)
    df = df[df['annee'] < 2022].copy()
    df['source'] = 'reference_csv'
    return df


def parse_2022_raw_file(file_path: Path, tour: int) -> pd.DataFrame:
    candidate_rows = []
    bureau_rows = []

    with file_path.open('r', encoding='cp1252') as handle:
        next(handle)
        for raw_line in handle:
            line = raw_line.strip()
            if not line:
                continue

            fields = line.split(';')
            if len(fields) < 28:
                continue

            dept_code = fields[0].strip()
            dept_name = _normalize_text(fields[1])
            territory_department = f'{dept_code} - {dept_name}'
            region_name = DEPARTMENT_TO_REGION.get(dept_code, 'Inconnu')

            inscrits = int(fields[7])
            exprimes = int(fields[18])
            bureau_rows.append({
                'territoire_departement': territory_department,
                'territoire_region': region_name,
                'inscrits': inscrits,
                'exprimes': exprimes,
            })

            for index in range(21, len(fields), 7):
                bloc = fields[index:index + 7]
                if len(bloc) < 7:
                    continue

                _, sex, last_name, first_name, voix, _, _ = bloc
                candidate_rows.append({
                    'candidat': _candidate_label(sex, last_name, first_name),
                    'territoire_departement': territory_department,
                    'territoire_region': region_name,
                    'voix': int(voix),
                })

    df_candidates = pd.DataFrame(candidate_rows)
    df_bureaux = pd.DataFrame(bureau_rows)

    total_inscrits = int(df_bureaux['inscrits'].sum())
    total_exprimes = int(df_bureaux['exprimes'].sum())

    national = df_candidates.groupby('candidat', as_index=False)['voix'].sum()
    national['%ins'] = (national['voix'] / total_inscrits * 100).round(2)
    national['%exp'] = (national['voix'] / total_exprimes * 100).round(2)
    national['tour'] = tour
    national['annee'] = 2022
    national['parti'] = national['candidat'].map(PARTY_2022)
    national['famille'] = national['parti'].map(FAMILY_MAPPING).fillna('Divers')
    national['niveau_geo'] = 'national'
    national['territoire'] = 'France'
    national['source'] = 'raw_2022'

    by_department_totals = df_bureaux.groupby('territoire_departement', as_index=False)[['inscrits', 'exprimes']].sum()
    by_region_totals = df_bureaux.groupby('territoire_region', as_index=False)[['inscrits', 'exprimes']].sum()

    department = _aggregate_level(
        candidate_rows=df_candidates,
        territory_totals=by_department_totals,
        tour=tour,
        level='departement',
        territory_column='territoire_departement',
        source='raw_2022',
    )
    region = _aggregate_level(
        candidate_rows=df_candidates,
        territory_totals=by_region_totals,
        tour=tour,
        level='region',
        territory_column='territoire_region',
        source='raw_2022',
    )

    combined = pd.concat([national, department, region], ignore_index=True)
    return combined.sort_values(['niveau_geo', 'voix'], ascending=[True, False]).reset_index(drop=True)


def load_2022_results() -> pd.DataFrame:
    available_raw = [parse_2022_raw_file(path, tour) for tour, path in RAW_2022_FILES.items() if path.exists()]
    if available_raw:
        return pd.concat(available_raw, ignore_index=True)

    if not REFERENCE_FILE.exists():
        raise FileNotFoundError('No 2022 raw files or reference dataset available.')

    fallback = pd.read_csv(REFERENCE_FILE)
    fallback = fallback[fallback['annee'] == 2022].copy()
    fallback['source'] = 'reference_csv'
    return fallback


def build_dataset() -> pd.DataFrame:
    historical = load_reference_history()
    results_2022 = load_2022_results()
    df = pd.concat([historical, results_2022], ignore_index=True)

    numeric_columns = ['voix', '%ins', '%exp', 'tour', 'annee']
    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors='coerce')

    df['tour'] = df['tour'].astype(int)
    df['annee'] = df['annee'].astype(int)
    df['candidat'] = df['candidat'].astype(str).map(_normalize_text)
    df['parti'] = df['parti'].fillna('Inconnu')
    df['famille'] = df['famille'].fillna(df['parti'].map(FAMILY_MAPPING)).fillna('Divers')
    df['niveau_geo'] = df['niveau_geo'].fillna('national')
    df['territoire'] = df['territoire'].fillna('France')

    ordered_columns = [
        'candidat', 'voix', '%ins', '%exp', 'tour', 'annee',
        'parti', 'famille', 'niveau_geo', 'territoire', 'source'
    ]
    df = df[ordered_columns]
    return df.sort_values(['annee', 'tour', 'voix'], ascending=[True, True, False]).reset_index(drop=True)


def save_processed_dataset(output_file: Path | None = None) -> Path:
    target = output_file or PROCESSED_FILE
    target.parent.mkdir(parents=True, exist_ok=True)
    build_dataset().to_csv(target, index=False, encoding='utf-8-sig')
    return target


def describe_sources() -> dict[str, bool]:
    return {
        'reference_csv': REFERENCE_FILE.exists(),
        'raw_2022_tour_1': RAW_2022_FILES[1].exists(),
        'raw_2022_tour_2': RAW_2022_FILES[2].exists(),
    }