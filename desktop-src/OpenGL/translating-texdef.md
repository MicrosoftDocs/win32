---
title: Translating texdef
description: The following code example is an IRIS GL texture definition
ms.assetid: bb2d257d-ee74-4a65-b364-c7a97bccaa78
keywords:
- IRIS GL porting,texture
- porting from IRIS GL,texture
- porting to OpenGL from IRIS GL,texture
- OpenGL porting from IRIS GL,texture
- texture
- IRIS GL porting,texdef
- porting from IRIS GL,texdef
- porting to OpenGL from IRIS GL,texdef
- OpenGL porting from IRIS GL,texdef
- texdef
ms.topic: article
ms.date: 05/31/2018
---

# Translating texdef

The following code example is an IRIS GL texture definition:


```C++
float texprops[] = { TX_MINFILTER, TX_POINT, 
                         TX_MAGFILTER, TX_POINT, 
                         TX_WRAP_S, TX_REPEAT, 
                         TX_WRAP_T, TX_REPEAT, 
                         TX_NULL }; 
 
textdef2d(1, 1, 6, 6, granite_texture, 7, texprops);
```



In the preceding example, **texdef** specifies the TX\_POINT filter as both the magnification and the minimizing filter, and TX\_REPEAT as the wrapping mechanism. It also specifies the texture image: **granite\_texture**.

In OpenGL, [**glTexImage**](glteximage1d.md) specifies the image and [glTexParameter](gltexparameter-functions.md) sets the property. To translate IRIS GL texture definitions, replace the **textdef** function with **glTexImage** and one or more calls to **glTexParameter**.

The preceding IRIS GL code looks like this when translated to OpenGL:


```C++
GLfloat nearest[] = {GL_NEAREST}; 
GLfloat repeat = {GL_REPEAT}; 
glTexParameterfv( GL_TEXTURE_1D, GL_TEXTURE_MIN_FILTER, nearest); 
glTexParameterfv( GL_TEXTURE_1D, GL_TEXTURE_MAGILTER, nearest); 
glTexParameterfv( GL_TEXTURE_1D, GL_TEXTURE_WRAP_S, repeat); 
glTexParameterfv( GL_TEXTURE_1D, GL_TEXTURE_WRAP_T, nearest); 
glTexImage1D( GL_TEXTURE_1D, 0, 1, 6, 0, GL_RGB, GL_UNSIGNED_SHORT, granite_texture);
```



The following table lists the IRIS GL texture parameters and their equivalent OpenGL parameters.



| IRIS GL texture parameter | OpenGL texture parameter                                  |
|---------------------------|-----------------------------------------------------------|
| TX\_MINFILTER             | GL\_TEXTURE\_MIN\_FILTER                                  |
| TX\_MAGFILTER             | GL\_TEXTURE\_MAG\_FILTER                                  |
| TX\_WRAP, TX\_WRAP\_S     | GL\_TEXTURE\_WRAP\_S                                      |
| TX\_WRAP, TX\_WRAP\_T     | GL\_TEXTURE\_WRAP\_TGL\_TEXTURE\_BORDER\_COLOR<br/> |



 

The following table lists the possible values of the IRIS GL texture parameters and their equivalent OpenGL parameters.



| IRIS GL texture parameter | OpenGL texture parameter     |
|---------------------------|------------------------------|
| TX\_POINT                 | GL\_NEAREST                  |
| TX\_BILINEAR              | GL\_LINEAR                   |
| TX\_MIPMAP\_POINT         | GL\_NEAREST\_MIPMAP\_NEAREST |
| TX\_MIPMAP\_BILINEAR      | GL\_LINEAR\_MIPMAP\_NEAREST  |
| TX\_MIPMAP\_LINEAR        | GL\_NEAREST\_MIPMAP\_LINEAR  |
| TX\_TRILINEAR             | GL\_LINEAR\_MIPMAP\_LINEAR   |



 

 

 





