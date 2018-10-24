---
title: GetDimensions function
description: Returns the dimensions of the resource.
ms.assetid: a15f1808-296d-43ac-80c0-5cbec0bcb801
keywords:
- GetDimensions function HLSL
topic_type:
- apiref
api_name:
- GetDimensions
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
api_location: 
---

# GetDimensions function

Returns the dimensions of the resource.

## Syntax

``` syntax
void GetDimensions(
  in  UINT MipLevel,
  out UINT Width,
  out UINT Elements,
  out UINT NumberOfLevels
);
```

## Parameters

<dl> <dt>

*MipLevel* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

Optional. Mipmap level (must be specified if *NumberOfLevels* is used).

</dd> <dt>

*Width* \[out\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

The resource width, in texels.

</dd> <dt>

*Elements* \[out\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

The number of elements in the array.

</dd> <dt>

*NumberOfLevels* \[out\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

The number of mipmap levels (requires *MipLevel* also).

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

This is a list of the overloaded versions of this method.


```
void GetDimensions(UINT MipLevel, 
  out UINT Width,
  out UINT Elements,
  out UINT NumberOfLevels);

void GetDimensions (out UINT Width,
  out UINT Elements);

void GetDimensions(UINT MipLevel,
  out float Width,
  out UINT Elements,
  out float NumberOfLevels);

void GetDimensions(out float Width,
  out UINT Elements);
```



This function is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          | x     | x       |



 

## See also

<dl> <dt>

[Texture1DArray](sm5-object-texture1darray.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




