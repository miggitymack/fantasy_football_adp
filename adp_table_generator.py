import pandas as pd

#m Cleaning the individual tables

stats_19 = pd.read_csv('stats_19.csv')
dst_19 = pd.read_csv('dst_19.csv', index_col=0)
adp_19 = pd.read_csv('adp_19.csv', index_col=0)
k_19 = pd.read_csv('k_19.csv', index_col=0)

stats_19 = stats_19.drop(stats_19.loc[stats_19.player.isnull()].index) 
dst_19 = dst_19.loc[dst_19.SACK.notnull()]
dst_19 = dst_19.drop(columns=['FPTS', 'FPTS/G', 'OWN', 'G'])
k_19 = k_19.loc[k_19.Player.notnull()]
k_19 = k_19.drop(columns=['FPTS', 'FPTS/G', 'OWN', 'G'])

# functions for cleaning

def format_name (name):
    return ''.join(e.lower() for e in name if e.isalnum())

def format_defense(defense):
    team = defense.split(' ')[-1]
    return team[1:-1]

def format_k (kicker):
    kicker = kicker.split(' ')[0:-1]
    kicker = ''.join(kicker)
    return ''.join(e.lower() for e in kicker if e.isalnum())

#The only player to have a different name from the different tables.
# I changed the adp table name for merging purposes

mahomes = adp_19.loc[adp_19['Name'].str.contains('Mahomes')]
mahomes['Name'] = 'Patrick Mahomes'
adp_19.loc[adp_19['Name'].str.contains('Mahomes')] = mahomes

adp_rename = adp_19.Name.apply(lambda x: format_name(x))
stats_rename = stats_19.player.apply(lambda x: format_name(x))
k_rename = k_19.Player.apply(lambda x: format_k(x))
dst_19['Team'] = dst_19.Player.apply(lambda x: format_defense(x))

adp_19['match_name'] = adp_rename
stats_19['match_name'] = stats_rename
k_19['match_name'] = k_rename

# Merging the tables

adp_join = adp_19.merge(stats_19, how="left", left_on="match_name", right_on="match_name")
adp_join['Team Def'] = adp_join.loc[adp_join['Name'].str.contains('Defense')]['Team']
adp_join = adp_join.merge(dst_19, how="left", left_on="Team Def", right_on="Team")
adp = adp_join.merge(k_19, how="left", left_on="match_name", right_on="match_name")

## Cleaning the merged table

adp['Name'].apply(lambda x: ' '.join(x.split()))
adp['Name'] = adp['Name'].apply(lambda x: ' '.join(x.split()))
adp = adp.drop(columns=['match_name', 'Bye', 'Team Def', 'Player_x', 'Player_y', 'Team_y', 'player', 'pos'])
adp = adp.rename(columns={'Team_x':'Team'})
adp = adp.fillna(0)

dummy_cols = pd.get_dummies(adp[['Position', 'Team']])
adp = adp.merge(dummy_cols, left_on=adp.index, right_on=dummy_cols.index)
adp = adp.drop(columns=['key_0', 'Position', 'Team'])

adp.to_csv('adp_data_19.csv', index=False)