import re
import datetime
class Inspector:
    time = datetime.datetime(1982, 11, 22)
    citizen = {
        'Arstotzka' : {
            'allow' : True,
            'requirement' : set(),
            'vaccination' : set()
            },
        'Antegria' : {
            'allow' : False,
            'requirement' : set(),
            'vaccination' : set()
            },
        'Impor' : {
            'allow' : False,
            'requirement' : set(),
            'vaccination' : set()
            },
        'Kolechia' : {
            'allow' : False,
            'requirement' : set(),
            'vaccination' : set()
            },
        'Obristan' : {
            'allow' : False,
            'requirement' : set(),
            'vaccination' : set()
            },
        'Republia' : {
            'allow' : False,
            'requirement' : set(),
            'vaccination' : set()
            },
        'United Federation' : {
            'allow' : False,
            'requirement' : set(),
            'vaccination' : set()
            }
    }
    wanted = set()

    @classmethod
    def receive_bulletin(cls, bulletin:str):
        cls.time += datetime.timedelta(days=1)
        cls.wanted = set()
        re_nations = 'Arstotzka|Antegria|Impor|Kolechia|Obristan|Republia|United Federation'
        re_requirement = '(passport)|(vaccination)|(ID card)|(access permit)|(work pass)|(grant of asylum)|(diplomatic autorization)| '
        for regulation in bulletin.split('\n'):
            regulation = regulation.split(' ', 1)
            # Updates to the list of nations
            if regulation[0] == 'Allow':
                for nation in re.findall(re_nations, regulation[1]):
                    cls.citizen[nation]['allow'] = True
            elif regulation[0] == 'Deny':
                for nation in re.findall(re_nations, regulation[1]):
                    cls.citizen[nation]['allow'] = False
            # Update to a currently wanted criminal
            elif regulation[0] == 'Wanted':
                cls.wanted.add(regulation[1].split(': ')[-1])
            # Updates to required documents & vaccinations
            else:
                nations = []
                if regulation[0] == 'Citizens':
                    nations = re.findall(re_nations, regulation[1])
                elif regulation[0] == 'Entrants':
                    nations = re_nations.split('|')
                else:
                    nations = re_nations.split('|')[1:]
                reg = list(filter(None, re.split(re_requirement, regulation[1])))
                require = True
                if 'no' in reg:
                    require = False
                for nation in nations:
                    if require:
                        if reg[-1] == 'vaccination':
                            vac_name = ''
                            for i in range(reg.index('require') + 1, reg.index('vaccination')):
                                vac_name += reg[i] + ' '
                            cls.citizen[nation]['vaccination'].add(vac_name[:-1])
                        else:
                            cls.citizen[nation]['requirement'].add(reg[-1].replace(' ', '_'))
                    else:
                        if reg[-1] == 'vaccination':
                            vac_name = ''
                            for i in range(reg.index('require') + 1, reg.index('vaccination')):
                                vac_name += reg[i] + ' '
                            cls.citizen[nation]['vaccination'].remove(vac_name[:-1])
                        else:
                            cls.citizen[nation]['requirement'].remove(reg[-1].replace(' ', '_'))

    @classmethod
    def inspect(cls, paper:str):
        print(paper)
        if not paper:
            return "Entry denied: missing required passport."
        requirement_names = {
            'passport' : 'passport',
            'certificate_of_vaccination' : 'certificate_of_vaccination',
            'ID_card' : 'ID_card',
            'access_permit' : 'access_permit',
            'grant_of_asylum' : 'access_permit',
            'diplomatic_authorization' : 'access_permit',
            'work_pass' : 'work_pass'
            }
        check_requirements = set()
        check_names = {'ID#', 'NATION', 'NAME', 'DOB'}
        msg = {
            'ID#' : 'ID number',
            'NATION' : 'nationality',
            'NAME' : 'name',
            'DOB' : 'date of birth'
            }
        entrant = {}
        worker = False
        message = ""
        for requirement, contents in paper.items():
            check_requirements.add(requirement_names[requirement])
            contents = re.split(': |\n', contents)
            for i in range(0, len(contents), 2):
                name, detail = contents[i], contents[i + 1]
                if name in check_names:
                    if name in entrant:
                        if detail != entrant[name]:
                            return  "Detainment: " + msg[name] + " mismatch."
                    else:
                        entrant[name] = detail
                elif name == 'EXP':
                    t = detail.split('.')
                    if datetime.datetime(int(t[0]), int(t[1]), int(t[2])) <= cls.time:
                        message = "Entry denied: " + re.sub('_', ' ', requirement) + " expired."
                elif name == 'ACCESS':
                    if 'Arstotzka' not in detail:
                        message = 'Entry denied: invalid diplomatic authorization.'
                elif name == 'VACCINES':
                    entrant[name] = detail.split(', ')
                elif name == 'PURPOSE':
                    if detail == 'WORK':
                        worker = True
        entrant_name = entrant['NAME'].split(', ')
        if entrant_name[1] + ' ' + entrant_name[0] in cls.wanted:
            return "Detainment: Entrant is a wanted criminal."
        for req in cls.citizen[entrant['NATION']]['requirement']:
            if req == 'work_pass' and not worker:
                continue
            if req not in check_requirements:
                return "Entry denied: missing required " + re.sub('_', ' ', req) + "."
        if 'VACCINES' in entrant:
            vac_cnt = 0
            for vac in entrant['VACCINES']:
                if vac in cls.citizen[entrant['NATION']]['vaccination']:
                    vac_cnt += 1
            if vac_cnt < len(cls.citizen[entrant['NATION']]['vaccination']):
                message = "Entry denied: missing required vaccination."    
        if message:
            return message
        elif entrant['NATION'] == 'Arstotzka':
            return "Glory to Arstotzka."
        elif not cls.citizen[entrant['NATION']]['allow']:
            return 'Entry denied: citizen of banned nation.'
        else:
            return "Cause no trouble."