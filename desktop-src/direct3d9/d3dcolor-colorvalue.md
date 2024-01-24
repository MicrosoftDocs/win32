---
description: Initializes a color with the supplied red, green, blue, and alpha floating-point values.
ms.assetid: 61825e33-4150-47cd-97f2-2144434a45e2
title: D3DCOLOR_COLORVALUE macro (D3d9types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DCOLOR_COLORVALUE
api_type: 
- HeaderDef
api_location: 
- D3d9types.h
---

# D3DCOLOR\_COLORVALUE macro

Initializes a color with the supplied red, green, blue, and alpha floating-point values.

## Syntax


```C++
D3DCOLOR D3DCOLOR_COLORVALUE(
   float r,
   float g,
   float b,
   float a
);
```



## Parameters

<dl> <dt>

*r* 
</dt> <dd>

Red component of the color. This value must be a floating-point value in the range 0.0 through 1.0.

</dd> <dt>

*g* 
</dt> <dd>

Green component of the color. This value must be a floating-point value in the range 0.0 through 1.0.

</dd> <dt>

*b* 
</dt> <dd>

Blue component of the color. This value must be a floating-point value in the range 0.0 through 1.0.

</dd> <dt>

*a* 
</dt> <dd>

Alpha component of the color. This value must be a floating-point value in the range 0.0 through 1.0.

</dd> </dl>

## Return value

Returns the [**D3DCOLOR**](d3dcolor.md) value that corresponds to the supplied RGBA values.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3d9types.h</dt> </dl> |



## See also

<dl> <dt>

[Macros](dx9-graphics-reference-d3d-macros.md)
</dt> </dl>

 

 




