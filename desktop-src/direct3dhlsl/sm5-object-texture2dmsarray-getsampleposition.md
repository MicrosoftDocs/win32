---
title: GetSamplePosition function
description: Samples a texture and returns all four components.
ms.assetid: e04717be-58b0-4242-87dd-d769834ae1c2
keywords:
- GetSamplePosition function HLSL
topic_type:
- apiref
api_name:
- GetSamplePosition
api_type:
- NA
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
api_location: 
---

# GetSamplePosition function

Samples a texture and returns all four components.

## Syntax

``` syntax
float2 GetSamplePosition(
  in int sampleindex
);
```

## Parameters

<dl> <dt>

*sampleindex* \[in\]
</dt> <dd>

Type: **[**int**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

The zero-based index of a sample location.

</dd> </dl>

## Return value

Type: **float2**

A sample location.

## Remarks

This function is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
| x      | x    | x      | x        | x     | x       |



 

## See also

<dl> <dt>

[Texture2DMSArray](sm5-object-texture2dmsarray.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




