---
title: TextureCube::TextureCube GatherCmp methods
description: Samples and compares a texture and returns all components.
ms.assetid: EEC90CF8-9479-45D7-A9CE-74FC8DC3B1B5
keywords:
- GatherCmp methods HLSL
topic_type:
- apiref
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_name: 
api_location: 
---

# TextureCube::GatherCmp methods

For four texel values of a [**TextureCube**](texturecube.md) that would be used in a bi-linear filtering operation, returns their comparison against a compare value.

See the documentation on [gather4_c](./gather4-c--sm5---asm-.md) for more information describing the underlying DXBC instruction.

### Overload list



| Method                                                                       | Description                                                                                                      |
|:-----------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------|
| [**GatherCmp(S,float,float,uint)**](tcube-gathercmp-s-float-float-uint-.md) | Samples and compares a texture and returns all four components along with status about the operation.<br/> |



## See also

<dl> <dt>

[**TextureCube**](texturecube.md)
</dt> </dl>

 

