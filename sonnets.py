import pandas as pd
df = pd.read_csv('sonnets.csv')
df['vowellink'] = df['text'].replace({r"([aá] [Aaá])":r"[\1]",r"([eé] [Eeé])":r"[\1]",r"([ií] [Iií])":r"[\1]",r"([oó] [Ooó])":r"[\1]",r"([uú] [Uuú])":r"[\1]"}, regex=True)
df['stop'] = df['text'].replace({r"(  [BVDGbvdg])":r"[\1]",r"([?¿¡!,.:;] [BVDGbvdg])":r"[\1]",r"([¿¡][BVDGbvdg])":r"[\1]",r"([nm][bvdg])":r"[\1]",r"([nm] [bvdg])":r"[\1]"},regex=True)
df['trill'] = df['text'].replace({"(rr)":r"[\1]",r"( [rR])":r"[\1]", r"([¿¡][rR])":r"[\1]", r"(nr)":r"[\1]"},regex=True )
df['sonorization'] = df['text'].replace({r"([sz][nmbvdlr])":r"[\1]", r"([sz] [nmbvdlr])":r"[\1]",r"([sz] g[aourl])":r"[\1]",r"([sz]g[aourl])":r"[\1]"},regex=True )
df['vowellink_count'] = df.vowellink.str.lower().str.count(r'\[*\]')
df['stop_count'] = df.stop.str.lower().str.count(r'\[*\]')
df['trill_count'] = df.trill.str.lower().str.count(r'\[*\]')
df['sonorization_count'] = df.sonorization.str.lower().str.count(r'\[*\]')
df['tag_sum'] = df['stop_count'] + df['trill_count'] + df['sonorization_count']
df.to_csv('sonnets_tagged.csv', encoding='utf-8-sig', index = False)
