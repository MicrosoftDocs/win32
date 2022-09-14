---
description: Gets the stipple-pattern scale value.
ms.assetid: cf80ae8c-493d-4f35-b4f9-5981e64cc842
title: ID3DXLine::GetPatternScale method (D3dx9core.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXLine.GetPatternScale
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXLine::GetPatternScale method

Gets the stipple-pattern scale value.

## Syntax


```C++
FLOAT GetPatternScale();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Returns the value used to scale the stipple-pattern. 1.0f is the default value and represents no scaling. A value less than 1.0f shrinks the pattern, and a value greater than 1.0 stretches the pattern.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXLine](id3dxline.md)
</dt> <dt>

[**ID3DXLine::SetPatternScale**](id3dxline--setpatternscale.md)
</dt> </dl>

 

 
