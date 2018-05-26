---
title: InputPatch
description: Represents an array of control points that are available to the hull shader as inputs.
ms.assetid: a2eeb45a-85b2-4ed0-b071-fcbb8abf4f2d
keywords:
- InputPatch HLSL
topic_type:
- apiref
api_name:
- InputPatch
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# InputPatch

Represents an array of control points that are available to the hull shader as inputs.



| Method                                                      | Description                         |
|-------------------------------------------------------------|-------------------------------------|
| [**Operator\[\]**](sm5-object-inputpatch-operatorindex.md) | Gets a read-only resource variable. |



 

The InputPatch class also supports the following properties:



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
|        | x    |        | x        |       |         |



 

## See also

<dl> <dt>

[Shader Model 5 Objects](d3d11-graphics-reference-sm5-objects.md)
</dt> </dl>

 

 




