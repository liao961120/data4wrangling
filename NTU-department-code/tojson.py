#%%
import json

INPUT = "NTU_dept_code.txt"
OUT = """
data/name2code.json
data/code2name.json
data/name2std.json
data/dept2college.json
"""
COLLEGE = """
1,文學院
2,理學院
3,社科院
4,醫學院
5,工學院
6,生農學院
7,管理學院
8,公衛學院
9,電資學院
A,法律學院
B,生科學院
E,進修推廣學院
H,共同教育中心
I,國際學院
K,重點科技研究學院
Z,創新設計學院
"""
COLLEGE = dict(
    l.strip().split(",") for l in COLLEGE.strip().split("\n")
)
OUT = [ l.strip() for l in OUT.strip().split("\n") ]

################
def write_json(obj, fp):
    with open(fp, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)


name2code = {}
code2name = {}
name2std  = {}
dept2coll = {}
with open(INPUT, encoding="utf-8") as f:
    for line in f:
        code, names = line.strip().split('\t')
        code = code[:3]
        names = names.split(',')
        additional = []
        for nm in names:
            if nm.endswith("系"): additional.append(nm[:-1])
        names = names + additional
        std, n_std = names[0], list(set(names[1:]))

        ### code2name
        if code not in code2name:
            code2name[code] = {
                'std': std,
                'others': set(n_std)
            }
        else:
            code2name[code]['others'].update(names)

        ### name2code / name2std / dept2coll
        for nm in names:
            if nm not in name2code: name2code[nm] = code
            if nm not in name2std: name2std[nm] = std
            if nm not in dept2coll:
                college = COLLEGE.get(code[0], "")
                dept2coll[nm] = college
            

for k in code2name: code2name[k]['others'] = list(code2name[k]['others'])


write_json(name2code, OUT[0])
write_json(code2name, OUT[1])
write_json(name2std , OUT[2])
write_json(dept2coll, OUT[3])
