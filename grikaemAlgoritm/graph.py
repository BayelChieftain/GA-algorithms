from collections import deque

graph = {}
graph['you'] = ['doctor', 'dentist', 'policeman']
graph['doctor'] = ['nurse', 'bob']
graph['dentist'] = ['peggy', 'wiki']
graph['policeman'] = ['pony', 'john']

def person_is_nurse(pers):
    return pers == 'nurse'


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_nurse(person):
                print(person + ' is a nurse!')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

search('you')
