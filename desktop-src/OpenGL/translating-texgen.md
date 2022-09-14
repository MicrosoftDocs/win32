---
title: Translating texgen
description: The IRIS GL function texgen is translated to glTexGen for OpenGL.
ms.assetid: ddf398ed-37d4-4fb6-97be-20fe0564cb77
keywords:
- IRIS GL porting,texture
- porting from IRIS GL,texture
- porting to OpenGL from IRIS GL,texture
- OpenGL porting from IRIS GL,texture
- texture
- IRIS GL porting,texgen
- porting from IRIS GL,texgen
- porting to OpenGL from IRIS GL,texgen
- OpenGL porting from IRIS GL,texgen
- texgen
ms.topic: article
ms.date: 05/31/2018
---

# Translating texgen

The IRIS GL function **texgen** is translated to [glTexGen](gltexgen-functions.md) for OpenGL.

With IRIS GL, you call **texgen** twice: once to set the mode and plane equation simultaneously, and once to enable texture-coordinate generation. For example:


```C++
texgen(TX_S, TG_LINEAR, planeParams); 
texgen(TX_S, TG_ON, NULL);
```



With OpenGL, you make three calls: two to **glTexGen** (once to set the mode and once to set the plane equation), and one to [**glEnable**](glenable.md). For example, the OpenGL equivalent to the IRIS GL code above is:


```C++
glTexGen(GL_S, GLTEXTURE_GEN_MODE, modeName); 
glTextGen(GL_S, GL_OBJECT_PLANE, planeParameters); 
glEnable(GL_TEXTURE_GEN_S);
```



The following table lists the IRIS GL texture-coordinate names and their OpenGL equivalents.



| IRIS GL texture coordinate | OpenGL texture coordinate | glEnable argument   |
|----------------------------|---------------------------|---------------------|
| TX\_S                      | GL\_S                     | GL\_TEXTURE\_GEN\_S |
| TX\_T                      | GL\_T                     | GL\_TEXTURE\_GEN\_T |
| TX\_R                      | GL\_R                     | GL\_TEXTURE\_GEN\_R |
| TX\_Q                      | GL\_Q                     | GL\_TEXTURE\_GEN\_Q |



 

The following table lists the IRIS GL texture-generation modes and their equivalent OpenGL texture modes and plane names.



| IRIS GL texture mode | OpenGL texture mode | OpenGL plane name |
|----------------------|---------------------|-------------------|
| TG\_LINEAR           | GL\_OBJECT\_LINEAR  | GL\_OBJECT\_PLANE |
| TG\_CONTOUR          | GL\_EYE\_LINEAR     | GL\_EYE\_PLANE    |
| TG\_SPHEREMAP        | GL\_SPHERE\_MAP     |                   |



 

 

 




