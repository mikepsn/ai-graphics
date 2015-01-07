    # Each vertex is made of a point in 3D space.
class Vertex:
    x, y, z : Float

    # An object is made up an array  of vertices, and a list of faces.
    # Each face is a list of indices into  the vertex array
class SimpleObject:
    vertices : [Vertex] 
    faces : [[Integer]]  

    # Simplest possible scene is made up a list of objects.
class SimpleScene: 
    objects : [SimpleObject] 
