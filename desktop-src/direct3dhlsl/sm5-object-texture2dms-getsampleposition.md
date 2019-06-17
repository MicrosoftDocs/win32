---
title: GetSamplePosition function
description: Returns the sample position for the sample index provided.
ms.assetid: b7821112-9b40-4302-b5c1-03bab531a0ab
keywords:
- GetSamplePosition function HLSL
topic_type:
- apiref
api_name:
- GetSamplePosition
api_type:
- NA
ms.topic: article
ms.date: 05/31/2018
api_location: 
---

# GetSamplePosition function

Returns the sample position for the sample index provided.

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

Type: **[**int**](https://docs.microsoft.com/windows/desktop/WinProg/windows-data-types)**

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

[Texture2DMS](sm5-object-texture2dms.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




