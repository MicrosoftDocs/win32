---
description: Converts radians into degrees.
ms.assetid: 1b19af39-ca23-4364-9121-f532d7fed099
title: D3DXToDegree (D3dx9math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXToDegree
api_type: 
- HeaderDef
api_location: 
- d3dx9math.h
---

# D3DXToDegree

Converts radians into degrees.

``` syntax
#define D3DXToDegree(radian) ((radian) * (180.0f / D3DX_PI))
```

## Parameters



| Parameter                                                           | Description                                              |
|---------------------------------------------------------------------|----------------------------------------------------------|
| <span id="radian"></span><span id="RADIAN"></span>radian<br/> | The value, in radians, to convert to degrees.<br/> |



 

## Return Value

The macro returns the radian value in degrees.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9math.h</dt> </dl> |



## See also

<dl> <dt>

[Macros](dx9-graphics-reference-d3dx-macros.md)
</dt> <dt>

[**D3DXToRadian**](d3dxtoradian.md)
</dt> <dt>

[D3DX\_PI](other-d3dx-constants.md)
</dt> </dl>

 

 




