---
title: Texture2DMSArray::GetSamplePosition function
description: Gets the position of the specified sample. | Texture2DMSArray::GetSamplePosition function
ms.assetid: e04717be-58b0-4242-87dd-d769834ae1c2
keywords:
- GetSamplePosition function HLSL
topic_type:
- apiref
api_name:
- GetSamplePosition
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Texture2DMSArray::GetSamplePosition function

Gets the position of the specified sample.

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

Type: **[**int**](/windows/desktop/WinProg/windows-data-types)**

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

 

 
