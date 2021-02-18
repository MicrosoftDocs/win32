---
title: Texture2DArray::Texture2DArray Gather methods
description: Samples a Texture2DArray and returns all four components.
ms.assetid: 'eea1dd00-0061-4601-a218-979eb0ecd36d'
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

# Texture2DArray::Gather methods

Returns the four texel values of a [**Texture2DArray**](sm5-object-texture2darray.md) that would be used in a bi-linear filtering operation.

See the documentation on [gather4](./gather4--sm5---asm-.md) for more information describing the underlying DXBC instruction.

### Overload list



| Method                                                                | Description                                                                                                               |
|:----------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------|
| [**Gather(S,float,int)**](sm5-object-texture2darray-gather.md)        | Returns the four texel values that would be used in a bi-linear filtering operation.<br/>                                 |
| [**Gather(S,float,int,uint)**](t2darray-gather-s-float-int-uint-.md)  | Returns the four texel values that would be used in a bi-linear filtering operation, along with tile-mapping status.<br/> |



## See also

<dl> <dt>

[Texture2DArray](sm5-object-texture2darray.md)
</dt> </dl>

 

