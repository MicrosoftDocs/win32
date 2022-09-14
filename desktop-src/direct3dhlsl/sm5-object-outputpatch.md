---
title: OutputPatch
description: OutputPatch
ms.assetid: 24841938-6c84-4e1f-ba8a-a81b589bdd51
keywords:
- OutputPatch HLSL
topic_type:
- apiref
api_name:
- OutputPatch
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# OutputPatch

Represents an array of output control points that are available to the hull shader's patch-constant function as well as the domain shader.



| Method                                                       | Description                         |
|--------------------------------------------------------------|-------------------------------------|
| [**Operator\[\]**](sm5-object-outputpatch-operatorindex.md) | Gets a read-only resource variable. |



 

In addition, the InputPatch class supports the following properties:



| Properties | Type | Description                   |
|------------|------|-------------------------------|
| Length     | uint | The number of control points. |



 

## Minimum Shader Model

This object is supported in the following shader models.



| Shader Model                                                                | Supported |
|-----------------------------------------------------------------------------|-----------|
| [Shader Model 5](d3d11-graphics-reference-sm5.md) and higher shader models | yes       |



 

This object is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        | x    | x      |          |       |         |



 

## See also

<dl> <dt>

[Shader Model 5 Objects](d3d11-graphics-reference-sm5-objects.md)
</dt> </dl>

 

 




