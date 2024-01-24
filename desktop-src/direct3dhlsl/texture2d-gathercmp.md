---
title: Texture2D::Texture2D GatherCmp methods
description: Samples and compares a Texture2D and returns all components.
ms.assetid: 'd520b113-77af-486e-8d3d-8276f72df18f'
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

# Texture2D::GatherCmp methods

For four texel values of a [**Texture2D**](sm5-object-texture2d.md) that would be used in a bi-linear filtering operation, returns their comparison against a compare value.

See the documentation on [gather4_c](./gather4-c--sm5---asm-.md) for more information describing the underlying DXBC instruction.

### Overload list



| Method                                                                             | Description                                                                                                      |
|:-----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------|
| [**GatherCmp(S,float,float,int)**](sm5-object-texture2d-gathercmp.md)             | Samples and compares a texture and returns all four components.<br/>                                       |
| [**GatherCmp(S,float,float,int,uint)**](t2d-gathercmp-s-float-float-int-uint-.md) | Samples and compares a texture and returns all four components along with status about the operation.<br/> |



## See also

<dl> <dt>

[Texture2D](sm5-object-texture2d.md)
</dt> </dl>

 

