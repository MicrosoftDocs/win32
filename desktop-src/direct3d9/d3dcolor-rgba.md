---
description: Initializes a color with the supplied red, green, blue, and alpha values.
ms.assetid: 87d322f1-4a26-42fd-a1c3-7be220cecf0f
title: D3DCOLOR_RGBA macro (D3d9types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DCOLOR_RGBA
api_type: 
- HeaderDef
api_location: 
- D3d9types.h
---

# D3DCOLOR\_RGBA macro

Initializes a color with the supplied red, green, blue, and alpha values.

## Syntax


```C++
D3DCOLOR D3DCOLOR_RGBA(
   int r,
   int g,
   int b,
   int a
);
```



## Parameters

<dl> <dt>

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

</dd> <dt>

*a* 
</dt> <dd>

Alpha component of the color. This value must be in the range 0 through 255.

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
</dt> <dt>

[**D3DCOLOR\_ARGB**](d3dcolor-argb.md)
</dt> <dt>

[**D3DCOLOR\_XRGB**](d3dcolor-xrgb.md)
</dt> </dl>

 

 




