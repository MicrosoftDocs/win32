---
title: Porting Functions that Get Matrices and Transformations
description: The following table lists the IRIS GL functions that get the state of matrices and transformations and their OpenGL equivalents.
ms.assetid: 53546bc0-ce1d-47e0-ab5e-5d6789c6db2a
keywords:
- IRIS GL porting,matrices
- porting from IRIS GL,matrices
- porting to OpenGL from IRIS GL,matrices
- OpenGL porting from IRIS GL,matrices
- matrices
- IRIS GL porting,transformations
- porting from IRIS GL,transformations
- porting to OpenGL from IRIS GL,transformations
- OpenGL porting from IRIS GL,transformations
- transformations
ms.topic: article
ms.date: 05/31/2018
---

# Porting Functions that Get Matrices and Transformations

The following table lists the IRIS GL functions that get the state of matrices and transformations and their OpenGL equivalents.



| IRIS GL matrix query                  | OpenGL glGet matrix query         | Meaning                                                         |
|---------------------------------------|-----------------------------------|-----------------------------------------------------------------|
| **getmmode**                          | GL\_MATRIX\_MODE                  | Returns the current matrix mode.                                |
| **getmatrix** in **MVIEWING** mode    | GL\_MODELVIEW\_MATRIX             | Returns a copy of the current model-view matrix.                |
| **getmatrix** in **MPROJECTION** mode | GL\_PROJECTION\_MATRIX            | Returns a copy of the current projection matrix.                |
| **getmatrix** in **MTEXTURE** mode    | GL\_TEXTURE\_MATRIX               | Returns a copy of the current texture matrix.                   |
| Not applicable.                       | GL\_MAX\_MODELVIEW\_STACK\_DEPTH  | Returns maximum supported depth of the model-view matrix stack. |
| Not applicable.                       | GL\_MAX\_PROJECTION\_STACK\_DEPTH | Returns maximum supported depth of the projection matrix stack. |
| Not applicable.                       | GL\_MAX\_TEXTURE\_STACK\_DEPTH    | Returns maximum supported depth of the texture matrix stack.    |
| Not applicable.                       | GL\_MODELVIEW\_STACK\_DEPTH       | Returns number of matrices on the model view stack.             |
| Not applicable.                       | GL\_PROJECTION\_STACK\_DEPTH      | Returns number of matrices on the projection stack.             |
| Not applicable.                       | GL\_TEXTURE\_STACK\_DEPTH         | Returns number of matrices on the texture stack.                |



 

??

 

 




