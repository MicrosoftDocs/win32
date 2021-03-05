---
title: TextureCube::TextureCube Gather methods
description: Returns the four texel values that would be used in a bi-linear filtering operation.
ms.assetid: 4891A62A-9D54-4F7E-92C2-9CDDF1453671
keywords:
- Gather methods HLSL
topic_type:
- apiref
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_name: 
api_location: 
---

# TextureCube::Gather methods

Returns the four texel values that would be used in a bi-linear filtering operation.

See the documentation on [gather4](./gather4--sm5---asm-.md) for more information describing the underlying DXBC instruction.

### Overload list



| Method                                                     | Description                                                                                                              |
|:-----------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------|
| [**Gather(S,float)**](dx-graphics-hlsl-to-gather.md)      | Samples a texture and returns the four samples (red component only) that are used for bilinear interpolation.<br/> |
| [**Gather(S,float,uint)**](tcube-gather-s-float-uint-.md) | Samples a texture and returns all four components along with status about the operation.<br/>                      |



## See also

<dl> <dt>

[**TextureCube**](texturecube.md)
</dt> </dl>

 

