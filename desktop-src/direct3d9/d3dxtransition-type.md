---
description: Defines the transition style between values of a mesh animation.
ms.assetid: 4416ef28-ba6b-47ca-be7d-831daad619e5
title: D3DXTRANSITION_TYPE enumeration (D3dx9anim.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXTRANSITION_TYPE
api_type: 
- HeaderDef
api_location: 
- d3dx9anim.h
---

# D3DXTRANSITION\_TYPE enumeration

Defines the transition style between values of a mesh animation.

## Syntax


```C++
typedef enum D3DXTRANSITION_TYPE { 
  D3DXTRANSITION_LINEAR         = 0x000,
  D3DXTRANSITION_EASEINEASEOUT  = 0x001,
  D3DXTRANSITION_FORCE_DWORD    = 0x7fffffff
} D3DXTRANSITION_TYPE, *LPD3DXTRANSITION_TYPE;
```



## Constants

<dl> <dt>

<span id="D3DXTRANSITION_LINEAR"></span><span id="d3dxtransition_linear"></span>**D3DXTRANSITION\_LINEAR**
</dt> <dd>

Linear transition between values.

</dd> <dt>

<span id="D3DXTRANSITION_EASEINEASEOUT"></span><span id="d3dxtransition_easeineaseout"></span>**D3DXTRANSITION\_EASEINEASEOUT**
</dt> <dd>

Ease-in, ease-out spline transition between values.

</dd> <dt>

<span id="D3DXTRANSITION_FORCE_DWORD"></span><span id="d3dxtransition_force_dword"></span>**D3DXTRANSITION\_FORCE\_DWORD**
</dt> <dd>

Forces this enumeration to compile to 32 bits in size. Without this value, some compilers would allow this enumeration to compile to a size other than 32 bits. This value is not used.

</dd> </dl>

## Remarks

The calculation for the ramp from ease in to ease out is calculated as follows:

<dl> Q(t) = 2(x - y)t³ + 3(y - x)t² + x  
</dl>

where the ramp is a function Q(t) with the following properties:

-   Q(t) is a cubic spline.
-   Q(t) interpolates between x and y as t ranges from 0 to 1.
-   Q(t) is horizontal when t = 0 and t = 1.

Mathematically, this translates into:

<dl> Q(t) = At³ + Bt² + Ct + D (and therefore, Q'(t) = 3At² + 2Bt + C)  
2a) Q(0) = x  
2b) Q(1) = y  
3a) Q'(0) = 0  
3b) Q'(1) = 0  
</dl>

Solving for A, B, C, D:

<dl> D = x (from 2a)  
C = 0 (from 3a)  
3A + 2B = 0 (from 3b)  
A + B = y - x (from 2b and D = x)  
</dl>

Therefore:

<dl> A = 2(x - y), B = 3(y - x), C = 0, D = x  
</dl>

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9anim.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Enumerations](dx9-graphics-reference-d3dx-enums.md)
</dt> </dl>

 

 




