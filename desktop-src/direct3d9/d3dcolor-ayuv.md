---
description: Initializes a color using the (a,y,u,v) values.
ms.assetid: 47b65aab-511a-44c1-ab94-973bc2da7e04
title: D3DCOLOR_AYUV macro (D3d9types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DCOLOR_AYUV
api_type: 
- HeaderDef
api_location: 
- D3d9types.h
---

# D3DCOLOR\_AYUV macro

Initializes a color using the (a,y,u,v) values.

## Syntax


```C++
D3DCOLOR D3DCOLOR_AYUV(
   int a,
   int y,
   int u,
   int v
);
```



## Parameters

<dl> <dt>

*a* 
</dt> <dd>

Alpha component of the color. This value must be in the range 0 through 255.

</dd> <dt>

*y* 
</dt> <dd>

Luminance component of the color. This value must be in the range 0 through 255.

</dd> <dt>

*u* 
</dt> <dd>

Blue brightness of the color. This value must be in the range 0 through 255.

</dd> <dt>

*v* 
</dt> <dd>

Red brightness of the color. This value must be in the range 0 through 255.

</dd> </dl>

## Return value

Returns the [D3DCOLOR](d3dcolor.md) value that corresponds to the supplied ARGB values.

## Remarks

An RGB color can be reduced to 16 bits per pixel by conversion to luminance and color differences with the following equations:


```C++
y (luminance) = 0.299*red + 0.587*green + 0.114*blue
u = blue - luminance
v = red - luminance 
```



## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3d9types.h</dt> </dl> |



## See also

<dl> <dt>

[Macros](dx9-graphics-reference-d3d-macros.md)
</dt> <dt>

[**D3DCOLOR\_ARGB**](d3dcolor-argb.md)
</dt> <dt>

[**D3DCOLOR\_XYUV**](d3dcolor-xyuv.md)
</dt> </dl>

 

 




