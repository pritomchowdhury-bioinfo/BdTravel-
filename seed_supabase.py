import json, pathlib
base=pathlib.Path(__file__).parent
D=json.loads((base/'data/districts-64.json').read_text())
S=json.loads((base/'data/tourist-spots-64.json').read_text())
def esc(v):
    return 'NULL' if v is None else "'"+str(v).replace("'", "''")+"'"
out=['-- Generated seed SQL for BDTravel catalogue','insert into public.districts (name,division,official_portal,directory_status,attractions_status,live_poi_status) values']
rows=[]
for x in D:
    rows.append('('+','.join(map(esc,[x['district'],x['division'],x.get('official_portal'),x.get('directory_status'),x.get('attractions_status'),x.get('live_poi_status')]))+')')
out.append(',\n'.join(rows)+' on conflict (name) do update set division=excluded.division, official_portal=excluded.official_portal;')
out.append('\ninsert into public.tourist_spots (district_id,district,name,coordinates,best_season,estimated_cost_bdt_per_person,activities,food,hotel,transport,safety,nearby_hospital,data_status,source_note)\nselect d.id, s.district, s.spot, s.coordinates, s.best_season, s.estimated_cost_bdt_per_person, s.activities, s.food, s.hotel, s.transport, s.safety, s.nearby_hospital, s.data_status, s.source_note\nfrom (values')
rows=[]
for x in S:
    rows.append('('+','.join(map(esc,[x.get('district'),x.get('spot'),x.get('coordinates'),x.get('best_season'),x.get('estimated_cost_bdt_per_person'),x.get('activities'),x.get('food'),x.get('hotel'),x.get('transport'),x.get('safety'),x.get('nearby_hospital'),x.get('data_status'),x.get('source_note')]))+')')
out.append(',\n'.join(rows)+') as s(district,spot,coordinates,best_season,estimated_cost_bdt_per_person,activities,food,hotel,transport,safety,nearby_hospital,data_status,source_note) join public.districts d on d.name=s.district;')
(base/'supabase-seed-generated.sql').write_text('\n'.join(out),encoding='utf-8')
print('generated',len(D),'districts and',len(S),'spots')
