---
title: Texture3D::GetDimensions function
description: Returns the dimensions of the resource. | Texture3D::GetDimensions function
ms.assetid: 4a08f14f-7489-4ed1-bf94-4f63f1002eab
keywords:
- GetDimensions function HLSL
topic_type:
- apiref
api_name:
- GetDimensions
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Texture3D::GetDimensions function

Returns the dimensions of the resource.

## Syntax

``` syntax
void GetDimensions(
  in  UINT MipLevel,
  out UINT Width,
  out UINT Height,
  out UINT Depth,
  out UINT NumberOfLevels
);
```

## Parameters

<dl> <dt>

*MipLevel* \[in\]
</dt> <dd>

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

Optional. Mipmap level (must be specified if *NumberOfLevels* is used).

</dd> <dt>

*Width* \[out\]
</dt> <dd>

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

The resource width, in texels.

</dd> <dt>

*Height* \[out\]
</dt> <dd>

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

The resource height, in texels.

</dd> <dt>

*Depth* \[out\]
</dt> <dd>

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

The resource depth, in texels.

</dd> <dt>

*NumberOfLevels* \[out\]
</dt> <dd>

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

The number of mipmap levels (requires *MipLevel* also).

</dd> </dl>

## Return value

Nothing

## Remarks

This is a list of the overloaded versions of this method.


```
void GetDimensions(UINT MipLevel, 
  out UINT Width,
  out UINT Height,
  out UINT Depth,
  out UINT NumberOfLevels);

void GetDimensions (out UINT Width,
  out UINT Height,
  out UINT Depth);

void GetDimensions(UINT MipLevel,
  out float Width,
  out float Height,
  out float Depth,
  out float NumberOfLevels);

void GetDimensions(out float Width,
  out float Height,
  out float Depth);
```



This function is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          | x     | x       |



 

## See also

<dl> <dt>

[Texture3D](sm5-object-texture3d.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 
