---
title: Porting Depth Cueing and Fog Commands
description: Porting Depth Cueing and Fog Commands
ms.assetid: 16982d11-88a1-4a35-960f-28f10491e0ac
keywords:
- IRIS GL porting,depth cueing
- porting from IRIS GL,depth cueing
- porting to OpenGL from IRIS GL,depth cueing
- OpenGL porting from IRIS GL,depth cueing
- IRIS GL porting,fog
- porting from IRIS GL,fog
- porting to OpenGL from IRIS GL,fog
- OpenGL porting from IRIS GL,fog
- depth cueing
- fog
ms.topic: article
ms.date: 05/31/2018
---

# Porting Depth Cueing and Fog Commands

When porting depth-cueing and fog commands, keep the following points in mind:

-   The IRIS GL call, **fogvertex**, sets a mode and the parameters affecting that mode. In OpenGL, you call [**glFog**](glfog.md) once to set the mode, and then again twice or more to set various parameters.
-   In OpenGL, depth cueing is not a separate feature. Use linear fog instead of depth cueing. (This section gives an example of how to do this.) The following IRIS GL functions have no direct OpenGL equivalent:

    **depthcue**

    **lRGBrange**

    **lshaderange**

    **getdcm**

-   To adjust fog quality, use [**glHint**](glhint.md)( GL\_FOG\_HINT ).

The following table lists the IRIS GL functions for managing fog and their equivalent OpenGL functions.



| IRIS GL function         | OpenGL function                                     | Meaning                           |
|--------------------------|-----------------------------------------------------|-----------------------------------|
| **fogvertex**            | [**glFog**](glfog.md)                              | Sets various fog parameters.      |
| **fogvertex**( FG\_ON )  | [**glEnable**](glenable.md) ( GL\_FOG )            | Turns on fog.                     |
| **fogvertex**( FG\_OFF ) | [**glDisable**](gldisable.md) ( GL\_FOG )          | Turns off fog.                    |
| **depthcue**             | [**glFog**](glfog.md) ( GL\_FOG\_MOD, GL\_LINEAR ) | Uses linear fog for depth cueing. |



 

The following table lists the parameters you can pass to **glFog**.



| Fog parameter    | Meaning                       | Default                  |
|------------------|-------------------------------|--------------------------|
| GL\_FOG\_DENSITY | Fog density.                  | 1.0                      |
| GL\_FOG\_START   | Near distance for linear fog. | 0.0                      |
| GL\_FOG\_END     | Far distance for linear fog.  | 1.0                      |
| GL\_FOG\_INDEX   | Fog color index.              | 0.0                      |
| GL\_FOG\_COLOR   | Fog RGBA color.               | (0, 0, 0, 0)             |
| GL\_FOG\_MODE    | Fog mode.                     | See the following table. |



 

The fog-density parameter of OpenGL differs from the one in IRIS GL. They are related as follows:

-   if *fogMode* = EXP2
     

    *openGLfogDensity* = (*irisGLfogDensity* ) ( **sqrt** ( **log** ( 1 / 255 ) ))
-   if *fogMode* = EXP
     

    *openGLfogDensity* = (*irisGLfogDensity* ) ( **log** ( 1 / 255 ) )

where **sqrt** is the square root operation, **log** is the natural logarithm, *irisGLfogDensity* is the IRIS GL fog density, and *openGLfogDensity* is the OpenGL fog density.

To switch between calculating fog in per-pixel mode and per-vertex mode, use [**glHint**](glhint.md)( GL\_FOG\_HINT, *hintMode*). Two hint modes are available:

-   GL\_NICEST per-pixel fog calculation
-   GL\_FASTEST per-vertex fog calculation

The following table lists the IRIS GL fog modes and their OpenGL equivalents.



| IRIS GL fog mode                       | OpenGL fog mode | Hint mode                         | Meaning                                  |
|----------------------------------------|-----------------|-----------------------------------|------------------------------------------|
| FG\_VTX\_EXP,FG\_PIX\_EXP<br/>   | GL\_EXP         | GL\_FASTEST,GL\_NICEST<br/> | Heavy fog mode (default).                |
| FG\_VTX\_EXP2,FG\_PIX\_EXP2<br/> | GL\_EXP2        | GL\_FASTEST,GL\_NICEST<br/> | Haze mode.                               |
| FG\_VTX\_LIN,FG\_PIX\_LIN<br/>   | GL\_LINEAR      | GL\_FASTEST,GL\_NICEST<br/> | Linear fog mode. (Use for depth cueing.) |



 

The following code example demonstrates depth cueing in OpenGL:


```C++
/* 
 *  depthcue.c 
 *  This program draws a wire frame model, which uses 
 *  intensity (brightness) to give clues to distance 
 *  Fog is used to achieve this effect 
 */ 
#include <GL/gl.h> 
#include <GL/glu.h> 
#include "aux.h" 
 
/*  Initialize linear fog for depth cueing 
 */ 
void myinit(void) 
{ 
    GLfloat fogColor[4] = {0.0, 0.0, 0.0, 1.0}; 
 
    glEnable(GL_FOG); 
    glFogi (GL_FOG_MODE, GL_LINEAR); 
    glHint (GL_FOG_HINT, GL_NICEST);  /*  per pixel  */ 
    glFogf (GL_FOG_START, 3.0); 
    glFogf (GL_FOG_END, 5.0); 
    glFogfv (GL_FOG_COLOR, fogColor); 
    glClearColor(0.0, 0.0, 0.0, 1.0); 
 
    glDepthFunc(GL_LEQUAL); 
    glEnable(GL_DEPTH_TEST); 
    glShadeModel(GL_FLAT); 
} 
 
/*  display() draws an icosahedron 
 */ 
void display(void) 
{ 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT); 
    glColor3f (1.0, 1.0, 1.0); 
    auxWireIcosahedron(1.0); 
    glFlush(); 
} 
 
void myReshape(GLsizei w, GLsizei h) 
{ 
    glViewport(0, 0, w, h); 
    glMatrixMode(GL_PROJECTION); 
    glLoadIdentity(); 
    gluPerspective (45.0, (GLfloat) w/(GLfloat) h, 3.0, 5.0); 
    glMatrixMode(GL_MODELVIEW); 
    glLoadIdentity (); 
    glTranslatef (0.0, 0.0, -4.0); /*move object into view*/ 
} 
/*  Main Loop 
 */ 
int main(int argc, char** argv) 
{ 
    auxInitDisplayMode (AUX_SINGLE | AUX_RGBA | AUX_DEPTH); 
    auxInitPosition (0, 0, 400, 400); 
    auxInitWindow (argv[0]); 
    myinit(); 
    auxReshapeFunc (myReshape); 
    auxMainLoop(display); 
}
```



 

 





