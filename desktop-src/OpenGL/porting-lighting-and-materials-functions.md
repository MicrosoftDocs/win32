---
title: Porting Lighting and Materials Functions
description: OpenGL functions for lighting and materials differ substantially from the IRIS GL functions. Unlike IRIS GL, OpenGL has separate functions for setting lights, light models and materials.
ms.assetid: de57d041-1ea1-46d0-b584-009608625ea5
keywords:
- IRIS GL porting,lighting
- porting from IRIS GL,lighting
- porting to OpenGL from IRIS GL,lighting
- OpenGL porting from IRIS GL,lighting
- IRIS GL porting,materials
- porting from IRIS GL,materials
- porting to OpenGL from IRIS GL,materials
- OpenGL porting from IRIS GL,materials
- lighting
- materials
ms.topic: article
ms.date: 05/31/2018
---

# Porting Lighting and Materials Functions

OpenGL functions for lighting and materials differ substantially from the IRIS GL functions. Unlike IRIS GL, OpenGL has separate functions for setting lights, light models and materials.

Keep the following points in mind when porting lighting and materials functions:

-   OpenGL has no table of stored definitions. You can use display lists to mimic the IRIS GL def/bind mechanism. For more information on defs and binds, see [Porting Defs, Binds, and Sets](porting-defs--binds--and-sets.md).
-   With OpenGL, attenuation is associated with each light source, rather than the overall lighting model.
-   Diffuse and specular components are separated in OpenGL light sources.
-   OpenGL light sources have an alpha component. When porting your IRIS GL code, set this alpha component to 1.0, indicating 100 percent opaque. The alpha values are then determined by the alpha component of your materials only, so the objects in your scene will look the same as they did in IRIS GL.

The following table lists IRIS GL lighting and materials functions and their equivalent OpenGL functions.



| IRIS GL function                 | OpenGL function                               | Meaning                                                       |
|----------------------------------|-----------------------------------------------|---------------------------------------------------------------|
| **Imdef(DEFLIGHT**, ... **)**    | [glLight](gllight-functions.md)              | Define a light source.                                        |
| **Imdef(DEFLMODEL**, ... **)**   | [glLightModel](gllightmodel-functions.md)    | Define a lighting model.                                      |
| **Imbind**                       | [**glEnable**](glenable.md) ( GL\_LIGHT *i*) | Enable light *i*.                                             |
| **Imbind**                       | **glEnable**( GL\_LIGHTING )                  | Enable lighting.                                              |
| **Imdef(DEFMATERIAL**, ... **)** | [**glMaterial**](glmaterial-functions.md)    | Define a material.                                            |
| **Imcolor**                      | [**glColorMaterial**](glcolormaterial.md)    | Change the effect of color commands while lighting is active. |
|                                  | [**glGetMaterial**](glgetmaterial.md)        | Get material parameters.                                      |



 

The following table lists various IRIS GL material parameters and their equivalent OpenGL parameters.



| Imdef index  | glMaterial parameter                              | Default              | Meaning                                                                                       |
|--------------|---------------------------------------------------|----------------------|-----------------------------------------------------------------------------------------------|
| ALPHA        | GL\_DIFFUSE                                       |                      | The fourth value in the GL\_DIFFUSE parameter specifies the alpha value.                      |
| AMBIENT      | GL\_AMBIENT                                       | (0.2, 0.2, 0.2, 1.0) | Ambient color.                                                                                |
| DIFFUSE      | GL\_DIFFUSE                                       | (0.8, 0.8, 0.8, 1.0) | Diffuse color.                                                                                |
| SPECULAR     | GL\_SPECULAR                                      | (0.0, 0.0, 0.0, 1.0) | Emissive color.                                                                               |
| SHININESS    | GL\_SHININESSGL\_AMBIENT\_AND\_DIFFUSE<br/> | 0.0                  | Specular exponent.Equivalent to calling **glMaterial** twice with the same values.<br/> |
| COLORINDEXES | GL\_COLOR\_INDEXES                                |                      | Color indexes for ambient, diffuse, and specular lighting.                                    |



 

When the first parameter of **Imdef** is DEFMODEL, the equivalent OpenGL translation is the function [**glLightModel**](gllightmodel-functions.md). The exception is when the parameter following DEFMODEL is ATTENUATION: then the equivalent OpenGL function is [**glLight**](gllight-functions.md).

The following table lists the equivalent lighting model parameters for IRIS GL and OpenGL.



| Imdef index | glLightModel parameter          | Default              | Meaning                                          |
|-------------|---------------------------------|----------------------|--------------------------------------------------|
| AMBIENT     | GL\_LIGHT\_MODEL\_AMBIENT       | (0.2, 0.2, 0.2, 1.0) | Ambient color of scene.                          |
| ATTENUATION |                                 |                      | See [**glLight**](gllight-functions.md).        |
| LOCALVIEWER | GL\_LIGHT\_MODEL\_LOCAL\_VIEWER | GL\_FALSE            | Viewer local (**TRUE**) or infinite (**FALSE**). |
| TWOSIDE     | GL\_LIGHTMODEL\_TWO\_SIDE       | GL\_FALSE            | Use two-sided lighting when **TRUE**.            |



 

When the first parameter of **Imdef** is DEFLIGHT, the equivalent OpenGL translation is the [**glLight**](gllight-functions.md) function.

The following table lists the equivalent lighting parameters for IRIS GL and OpenGL.



| Imdef index           | glLight parameter                                                                                 | Default                                                                             | Meaning                                                                        |
|-----------------------|---------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| AMBIENT               | GL\_AMBIENTGL\_DIFFUSE<br/> GL\_SPECULAR<br/>                                         | (0.0, 0.0, 0.0, 1.0)(1.0, 1.0, 1.0, 1.0)<br/> (1.0, 1.0, 1.0, 1.0)<br/> | Ambient intensity.Diffuse intensity.<br/> Specular intensity.<br/> |
| LCOLOR                | No equivalent.                                                                                    |                                                                                     |                                                                                |
| POSITION              | GL\_POSITION                                                                                      | (0.0, 0.0, 1.0, 0.0)                                                                | Position of light.                                                             |
| SPOTDIRECTION         | GL\_SPOT\_DIRECTION                                                                               | (0, 0, 1)                                                                           | Direction of spotlight.                                                        |
| SPOTLIGHT             | GL\_SPOT\_EXPONENTGL\_SPOT\_CUTOFF<br/>                                                     | 0180<br/>                                                                     | Intensity distribution.Maximum spread angle of light source.<br/>        |
| DEFMODEL, ATTENUATION | GL\_CONSTANT\_ATTENUATIONGL\_LINEAR\_ATTENUATION<br/> GL\_QUADRATIC\_ATTENUATION<br/> | (1, 0, 0)                                                                           | Attenuation factors.                                                           |



 

 

 





