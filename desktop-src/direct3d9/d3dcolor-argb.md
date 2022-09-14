---
description: Initializes a color with the supplied alpha, red, green, and blue values.
ms.assetid: e862ba1b-fdcf-4058-8835-e58b4fc5e21a
title: D3DCOLOR_ARGB macro (D3d9types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DCOLOR_ARGB
api_type: 
- HeaderDef
api_location: 
- D3d9types.h
---

# D3DCOLOR\_ARGB macro

Initializes a color with the supplied alpha, red, green, and blue values.

## Syntax


```C++
D3DCOLOR D3DCOLOR_ARGB(
   int a,
   int r,
   int g,
   int b
);
```



## Parameters

<dl> <dt>

*a* 
</dt> <dd>

Alpha component of the color. This value must be in the range 0 through 255.

</dd> <dt>

*r* 
</dt> <dd>

Red component of the color. This value must be in the range 0 through 255.

</dd> <dt>

*g* 
</dt> <dd>

Green component of the color. This value must be in the range 0 through 255.

</dd> <dt>

*b* 
</dt> <dd>

Blue component of the color. This value must be in the range 0 through 255.

</dd> </dl>

## Return value

Returns the [D3DCOLOR](d3dcolor.md) value that corresponds to the supplied ARGB values.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3d9types.h</dt> </dl> |



## See also

<dl> <dt>

[Macros](dx9-graphics-reference-d3d-macros.md)
</dt> <dt>

[**D3DCOLOR\_RGBA**](d3dcolor-rgba.md)
</dt> <dt>

[**D3DCOLOR\_XRGB**](d3dcolor-xrgb.md)
</dt> </dl>

 

 




