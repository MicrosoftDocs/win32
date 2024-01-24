---
description: Converts degrees into radians.
ms.assetid: 450806bd-db2f-47be-ae80-c261088b1bb8
title: D3DXToRadian (D3dx9math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXToRadian
api_type:
- HeaderDef
api_location:
- d3dx9math.h
---

# D3DXToRadian

> [!Note]
> The D3DX utility library is deprecated. We recommend that you use [DirectXMath](../dxmath/pg-xnamath-migration-d3dx.md) instead.

Converts degrees into radians.

``` syntax
#define D3DXToRadian(degree) ((degree) * (D3DX_PI / 180.0f))
```

## Parameters



| Parameter                                                           | Description                                              |
|---------------------------------------------------------------------|----------------------------------------------------------|
| <span id="degree"></span><span id="DEGREE"></span>degree<br/> | The value, in degrees, to convert to radians.<br/> |



 

## Return Value

The macro returns the degree value in radians.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9math.h</dt> </dl> |



## See also

<dl> <dt>

[Macros](dx9-graphics-reference-d3dx-macros.md)
</dt> <dt>

[**D3DXToDegree**](d3dxtodegree.md)
</dt> <dt>

[D3DX\_PI](other-d3dx-constants.md)
</dt> </dl>

 

 
