---
title: Texture2DArray::Texture2DArray GatherCmp methods
description: Samples and compares a Texture2DArray and returns all components.
ms.assetid: '5b2892f0-be62-4fb2-978e-aabb8ae96e67'
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

# Texture2DArray::GatherCmp methods

For four texel values of a [**Texture2DArray**](sm5-object-texture2darray.md) that would be used in a bi-linear filtering operation, returns their comparison against a compare value.

See the documentation on [gather4_c](./gather4-c--sm5---asm-.md) for more information describing the underlying DXBC instruction.

### Overload list



| Method                                                                             | Description                                                                                                      |
|:-----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------|
| [**GatherCmp(S,float,float,int)**](sm5-object-texture2darray-gathercmp.md)        | Samples and compares a texture and returns all four components.<br/>                                       |
| [**GatherCmp(S,float,float,int,uint)**](t2d-gathercmp-s-float-float-int-uint-.md) | Samples and compares a texture and returns all four components along with status about the operation.<br/> |



## See also

<dl> <dt>

[Texture2DArray](sm5-object-texture2darray.md)
</dt> </dl>

 

