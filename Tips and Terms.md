# Resources
- https://www.ursinaengine.org/entity_basics.html#Rotation
- https://www.ursinaengine.org/api_reference.html#EditorCamera

# Terms
- from ursina import *: Imports all functions and classes from the Ursina game engine.
- app = Ursina(): Initializes the Ursina application; required before creating any entities.
- window.fullscreen = True or false: A setting to toggle the game fullscreen mode (True or False).
- def update(): Defines the update loop, which runs every frame; used to update game logic.
- .rotation_x or y: Example, cube.rotation_y or x: The rotation angle of the cube around the Y-axis or X-axis.
- time.dt: The time delta between frames (used for smooth movement).
- .position: Example, cube.position: The 3D position of the cube in the scene.
- .forward: Example, cube.forward: A vector pointing in the direction the cube is facing.
- Entity: A base class for any visible or interactive object in Ursina.
- model: Example, model='cube': Specifies the 3D model shape of the entity.
- color=color.rgb(): Example, color=color.rgb(255, 0, 0): Sets the entity's color using RGB values (red in this case).
- texture: Example, texture='brick': Applies a brick texture to the surface of the model.
- position=(0, 0, 0): Sets the entity’s starting position in 3D space.
- rotation=(0, 0, 0): Sets the entity’s initial rotation angles (X, Y, Z).
- scale=(0, 0, 0): Sets the entity’s size along the X, Y, and Z axes.
- parent: Eaxample, parent=cube: Makes this entity a child of cube, inheriting its transformations. Example 2: model='sphere': Sets the model of the second entity to a sphere shape.
- EditorCamera(): Enables a free-moving camera for inspecting the scene in the editor.
- app.run(): Starts the game loop, rendering the scene and calling update() every frame.

# Example
```
from ursina import *

app = Ursina()
window.fullscreen =  True

def update():
    cube.rotation_y +=  50 * time.dt
    cube.rotation_x += 50 * time.dt
    cube.position += cube.forward * time.dt

cube = Entity(model = 'cube',
                color = color.rgb (255, 0, 0),
                texture = 'brick',

                position = (0, 0, 0),

                rotation = (10, 1, 8),

                scale = (2, 2, 2)

             )

cube2 = Entity(parent=cube,
               model = 'sphere',
               position = (1, 1, 1),
)

EditorCamera()

app. run()
```

# Tips
'x' is horizontal. <br>
'y' is vertical. <br>
'z' is forward and backward. It's going in and out. <br><br>


The position of the entity can be formatted differently. <br>
Example 1:
```
x = 0,
y = 0,
z = 0,
```
Example 2: As a tuple
```
position = (0, 0, 0),
```
Eaxmple 3:
```
position = Vec3(0, 0, 0),
```
<br><br>


Same format for rotation.
Example 1:
```
rotation_x = 0,
rotation_y = 0,
rotation_z = 0,
```
Example 2:
```
rotation = (0, 0, 0,),
```
<br><br>


Scale <br>
Example 1:
```
scale_x = 4,
scale_y = 4,
scale_z = 4,
```
Example 2:
```
scale = (4, 4, 4),
```
Example 3: Keep the proportions the same.
```
scale = 4,
```
<br><br>


Use * time.dt for frames. Frames should be 60 fps. <br>
Example: 
```
entity.rotation_y += 50 * time.dt
```
<br><br>


Bring an entity forward. <br>
Example 1:
```
entity.position += entity.forward * time.dt
```
Example 2: Use Vec3
```
entity.position += Vec3(1, 0, 0) * time.dt
```





