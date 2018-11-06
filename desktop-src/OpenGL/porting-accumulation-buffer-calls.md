---
title: Porting Accumulation Buffer Calls
description: You must allocate your accumulation buffer by requesting the appropriate pixel format with the OpenGL auxInitDisplayMode or ChoosePixelFormat function.
ms.assetid: 523728ce-4aae-4247-a3dc-23864231cad1
keywords:
- IRIS GL porting,accumulation buffers
- porting from IRIS GL,accumulation buffers
- porting to OpenGL from IRIS GL,accumulation buffers
- OpenGL porting from IRIS GL,accumulation buffers
- accumulation buffers OpenGL
ms.topic: article
ms.date: 05/31/2018
---

# Porting Accumulation Buffer Calls

You must allocate your accumulation buffer by requesting the appropriate pixel format with the OpenGL **auxInitDisplayMode** or [**ChoosePixelFormat**](/windows/desktop/api/wingdi/nf-wingdi-choosepixelformat) function. The following table lists IRIS GL functions that affect the accumulation buffer and their equivalent OpenGL functions.



| IRIS GL function       | OpenGL function                                       | Meaning                                                                       |
|------------------------|-------------------------------------------------------|-------------------------------------------------------------------------------|
| **acsize**             | **auxInitDisplayMode** or **ChoosePixelFormat**       | Specifies number of bitplanes per color component in the accumulation buffer. |
| **acbuf**              | [**glAccum**](glaccum.md)                            | Operates on the accumulation buffer.                                          |
|                        | [**glClearAccum**](glclearaccum.md)                  | Sets clear values for accumulation buffer.                                    |
| **acbuf**( AC\_CLEAR ) | [**glClear**](glclear.md) ( GL\_ACCUM\_BUFFER\_BIT ) | Clears the accumulation buffer.                                               |



 

The following table lists the IRIS GL **acbuf** parameters along with the equivalent OpenGL [**glAccum**](glaccum.md) parameters.



| IRIS GL parameter     | OpenGL parameter |
|-----------------------|------------------|
| AC\_ACCUMULATE        | GL\_ACCUM        |
| AC\_CLEAR\_ACCUMULATE | GL\_LOAD         |
| AC\_RETURN            | GL\_RETURN       |
| AC\_MULT              | GL\_MULT         |
| AC\_ADD               | GL\_ADD          |



 

 

 




