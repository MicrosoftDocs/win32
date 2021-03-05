---
title: TextureCubeArray::TextureCubeArray GatherCmp methods
description: Samples and compares a texture and returns all components.
ms.assetid: DF2C86F3-B585-47CD-8A0F-A5695A91F89E
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

# TextureCubeArray::GatherCmp methods

For four texel values of a [**TextureCubeArray**](texturecubearray.md) that would be used in a bi-linear filtering operation, returns their comparison against a compare value.

See the documentation on [gather4_c](./gather4-c--sm5---asm-.md) for more information describing the underlying DXBC instruction.

### Overload list



| Method                                                                            | Description                                                                                                      |
|:----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------|
| [**GatherCmp(S,float,float,uint)**](tcubearray-gathercmp-s-float-float-uint-.md) | Samples and compares a texture and returns all four components along with status about the operation.<br/> |



## See also

<dl> <dt>

[**TextureCubeArray**](texturecubearray.md)
</dt> </dl>

 

