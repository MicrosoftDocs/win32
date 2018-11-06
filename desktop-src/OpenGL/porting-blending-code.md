---
title: Porting Blending Code
description: In IRIS GL, when drawing to both front and back buffers, blending is done by reading one of the buffers, blending with that color, and then writing the result to both buffers. In OpenGL, however, each buffer is read in turn, blended, and then written.
ms.assetid: 18334c6b-586d-44a3-aa95-d10589ba99f4
keywords:
- IRIS GL porting,blending
- porting from IRIS GL,blending
- porting to OpenGL from IRIS GL,blending
- OpenGL porting from IRIS GL,blending
- blending
ms.topic: article
ms.date: 05/31/2018
---

# Porting Blending Code

In IRIS GL, when drawing to both front and back buffers, blending is done by reading one of the buffers, blending with that color, and then writing the result to both buffers. In OpenGL, however, each buffer is read in turn, blended, and then written.

The following table lists IRIS GL blending functions and their equivalent OpenGL functions.



| IRIS GL function  | OpenGL function                            | Meaning                     |
|-------------------|--------------------------------------------|-----------------------------|
|                   | [**glEnable**](glenable.md) ( GL\_BLEND ) | Turns on blending.          |
| **blendfunction** | [**glBlendFunc**](glblendfunc.md)         | Specifies a blend function. |



 

The OpenGL **glBlendFunc** function and the IRIS GL **blendfunction** function are almost identical. The following table lists IRIS GL blend factors and their OpenGL equivalents.



| IRIS GL          | OpenGL                     | Notes             |
|------------------|----------------------------|-------------------|
| BF\_ZERO         | GL\_ZERO                   |                   |
| BF\_ONE          | GL\_ONE                    |                   |
| BF\_SA           | GL\_SRC\_ALPHA             |                   |
| BF\_MSA          | GL\_ONE\_MINUS\_SRC\_ALPHA |                   |
| BF\_DA           | GL\_DST\_ALPHA             |                   |
| BF\_MDA          | GL\_ONE\_MINUS\_DST\_ALPHA |                   |
| BF\_SC           | GL\_SRC\_COLOR             |                   |
| BF\_MSC          | GL\_ONE\_MINUS\_SRC\_COLOR | Destination only. |
| BF\_DC           | GL\_DST\_COLOR             | Source only.      |
| BF\_MDC          | GL\_ONE\_MINUS\_DST\_COLOR | Source only.      |
| BF\_MIN\_SA\_MDA | GL\_SRC\_ALPHA\_SATURATE   |                   |



 

??

 

 




