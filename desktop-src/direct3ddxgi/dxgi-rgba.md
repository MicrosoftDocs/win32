---
description: DXGI_RGBA structure - Represents a color value with alpha, which is used for transparency.
ms.assetid: 5F9DDDC1-644E-4DA2-8E3D-F157789809E7
title: DXGI_RGBA structure (DXGItype.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DXGI_RGBA
api_type: 
- HeaderDef
api_location: 
- DXGItype.h
---

# DXGI\_RGBA structure

Represents a color value with alpha, which is used for transparency.

## Syntax


```C++
typedef struct _DXGI_RGBA {
  float r;
  float g;
  float b;
  float a;
} DXGI_RGBA;
```



## Members

<dl> <dt>

**r**
</dt> <dd>

Floating-point value that specifies the red component of a color. This value generally is in the range from 0.0 through 1.0. A value of 0.0 indicates the complete absence of the red component, while a value of 1.0 indicates that red is fully present.

</dd> <dt>

**g**
</dt> <dd>

Floating-point value that specifies the green component of a color. This value generally is in the range from 0.0 through 1.0. A value of 0.0 indicates the complete absence of the green component, while a value of 1.0 indicates that green is fully present.

</dd> <dt>

**b**
</dt> <dd>

Floating-point value that specifies the blue component of a color. This value generally is in the range from 0.0 through 1.0. A value of 0.0 indicates the complete absence of the blue component, while a value of 1.0 indicates that blue is fully present.

</dd> <dt>

**a**
</dt> <dd>

Floating-point value that specifies the alpha component of a color. This value generally is in the range from 0.0 through 1.0. A value of 0.0 indicates fully transparent, while a value of 1.0 indicates fully opaque.

</dd> </dl>

## Remarks

You can set the members of this structure to values outside the range of 0 through 1 to implement some unusual effects. Values greater than 1 produce strong lights that tend to wash out a scene. Negative values produce dark lights that actually remove light from a scene.

The DXGItype.h header type-defines **DXGI\_RGBA** as an alias of [**D3DCOLORVALUE**](d3dcolorvalue.md), as follows:


```
typedef D3DCOLORVALUE DXGI_RGBA;
```



You can use **DXGI\_RGBA** with [**IDXGISwapChain1::SetBackgroundColor**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgiswapchain1-setbackgroundcolor), [**IDXGISwapChain1::GetBackgroundColor**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgiswapchain1-getbackgroundcolor), and [**DXGI\_ALPHA\_MODE**](/windows/desktop/api/DXGI1_2/ne-dxgi1_2-dxgi_alpha_mode).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 and Platform Update for Windows 7 \[desktop apps \| UWP apps\]<br/>                        |
| Minimum supported server<br/> | Windows Server 2012 and Platform Update for Windows Server 2008 R2 \[desktop apps \| UWP apps\]<br/> |
| Header<br/>                   | <dl> <dt>DXGItype.h</dt> </dl>                      |



## See also

<dl> <dt>

[DXGI Structures](d3d10-graphics-reference-dxgi-structures.md)
</dt> <dt>

[**D3DCOLORVALUE**](d3dcolorvalue.md)
</dt> <dt>

[**D3DCOLORVALUE (in Direct3D 9)**](../direct3d9/d3dcolorvalue.md)
</dt> </dl>

 

 
