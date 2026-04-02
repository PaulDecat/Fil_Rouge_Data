from __future__ import annotations

try:
    from scripts.election_data import PROCESSED_FILE, build_dataset, describe_sources, save_processed_dataset
except ModuleNotFoundError:
    from election_data import PROCESSED_FILE, build_dataset, describe_sources, save_processed_dataset


def main() -> None:
    print('=' * 50)
    print('ANALYSE ELECTIONS PRESIDENTIELLES FRANCAISES (2002-2022)')
    print('=' * 50)

    sources = describe_sources()
    print('\nSources detectees:')
    for source_name, available in sources.items():
        status = 'OK' if available else 'MANQUANT'
        print(f'- {source_name}: {status}')

    df = build_dataset()
    output_file = save_processed_dataset(PROCESSED_FILE)

    print('\nStatistiques globales:')
    print(f'- lignes: {len(df)}')
    print(f"- annees: {sorted(df['annee'].unique().tolist())}")
    print(f"- tours: {sorted(df['tour'].unique().tolist())}")
    print(f'- sortie: {output_file}')

    print('\nResume par source:')
    print(df.groupby(['annee', 'source']).size().to_string())

    print('\nTop 2022 tour 1:')
    sample = df[(df['annee'] == 2022) & (df['tour'] == 1) & (df['niveau_geo'] == 'national')][['candidat', 'parti', 'voix', '%exp']].head(12)
    print(sample.to_string(index=False))


if __name__ == '__main__':
    main()