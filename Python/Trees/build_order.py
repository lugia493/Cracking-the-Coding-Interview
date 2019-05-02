'''
Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of projects,
where the second project is dependent on the first project). All of a project's dependencies must be built 
before the project is. Find a build order that will allow the projects to be built. 
If there is no valid build order, return an error.

EXAMPLE
Input:
projects: a, b, c, d, e, f
dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)

Output:
f, e, a, b, d, c
'''

def buildMatrix(project,dep):
    matrix = []
    for i in range(0, len(project)):
        row = []
        for j in range(0, len(project)):
            row.append(0)
        matrix.append(row)

    for tup in dep:
        col = project.index(tup[0])
        row = project.index(tup[1])
        matrix[row][col] = 1
    return matrix

def buildOrder(project, dep):
    matrix = buildMatrix(project,dep)
    
    for row in matrix:

project = ['a','b','c','d','e','f']
dep = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
buildOrder(project, dep)