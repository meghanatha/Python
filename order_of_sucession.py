'''
print names of royalfamiles in order of their sucession
'''
def get_children_names(parent, family):
    '''
    Returns names of the children by sorting in order of gender and age
    Args:
        parent(str) -> name of the person
        family(dict) -> family of information of royal families
    Returns:
        names(list<str>) -> children names of the parent in order of gender and age
    '''
    children = []
    for name in family:
        if family[name]['parent'] == parent:
            children.append((name, family[name]['gender'], family[name]['year_of_birth']))
    children.sort(key=lambda info: info[2])
    children.sort(key=lambda info: info[1] == 'M', reverse=True)
    children_names = [child[0] for child in children]
    return children_names

def order_of_sucession(root_of_the_generation,family):
    '''
    Its prints names of the family person in order of their sucession
    Args:
        root_of_the_generation(str) -> name of the person
        family(dict) -> family information of royal families

    '''
    if ((not family[root_of_the_generation]['year_of_death'] != '-' )and (not family[root_of_the_generation]['reglion'] == 'Catholic')):
        print(root_of_the_generation)
    children_names_of_the_parent = get_children_names(root_of_the_generation, family)
    for child in children_names_of_the_parent:
        order_of_sucession(child, family)
    
no_of_people = int(input())
family = {}
root_of_the_generation =''
for i in range(no_of_people):
    name, parent, year_of_birth, year_of_death, religion, gender = input().split()
    family[name] = {
        'name': name,
        'parent': parent,
        'year_of_birth': int(year_of_birth),
        'year_of_death': year_of_death,
        'reglion': religion,
        'gender': gender
    }
    if parent == '-':
        root_of_the_generation = name 
order_of_sucession(root_of_the_generation, family)