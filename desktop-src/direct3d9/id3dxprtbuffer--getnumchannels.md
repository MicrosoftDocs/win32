---
description: Retrieves the number of color channels used in memory to store samples.
ms.assetid: dd1e3590-78e1-41a2-9f15-79389d9a210a
title: ID3DXPRTBuffer::GetNumChannels method (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXPRTBuffer.GetNumChannels
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXPRTBuffer::GetNumChannels method

Retrieves the number of color channels used in memory to store samples.

## Syntax


```C++
UINT GetNumChannels();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**UINT**](../winprog/windows-data-types.md)**

Returns the number of color channels used in memory to store samples. The value generally will be either 1 to represent luminance values, or 3 to represent RGB values.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPRTBuffer](id3dxprtbuffer.md)
</dt> </dl>

 

 
