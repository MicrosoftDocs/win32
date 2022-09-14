---
title: Translating tevdef
description: The following code example is an IRIS GL texture-environment definition that specifies the TV\_DECAL texture-environment parameter
ms.assetid: bb4c8231-8102-4ecb-a5d2-c41243c2682d
keywords:
- IRIS GL porting,texture
- porting from IRIS GL,texture
- porting to OpenGL from IRIS GL,texture
- OpenGL porting from IRIS GL,texture
- texture
- IRIS GL porting,tevdef
- porting from IRIS GL,tevdef
- porting to OpenGL from IRIS GL,tevdef
- OpenGL porting from IRIS GL,tevdef
- tevdef
ms.topic: article
ms.date: 05/31/2018
---

# Translating tevdef

The following code example is an IRIS GL texture-environment definition that specifies the TV\_DECAL texture-environment parameter:


```C++
float tevprops[] = {TV_DECAL, TV_NULL}; 
 
tevdef(1, 0, tevprops);
```



and the same code translated to OpenGL:


```C++
glTexEnvfv(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL);
```



The following table lists the IRIS GL texture-environment parameters and their equivalent OpenGL parameters.



| IRIS GL parameter     | OpenGL parameter             |
|-----------------------|------------------------------|
| TV\_MODULATE          | GL\_MODULATE                 |
| TV\_DECAL             | GL\_DECAL                    |
| TV\_BLEND             | GL\_BLEND                    |
| TV\_COLOR             | GL\_TEXTURE\_ENV\_COLOR      |
| TV\_ALPHA             | No direct OpenGL equivalent. |
| TV\_COMPONENT\_SELECT | No direct OpenGL equivalent. |



 

For more information about texture-environment parameters, see [**glTexEnv**](gltexenv-functions.md).

 

 




