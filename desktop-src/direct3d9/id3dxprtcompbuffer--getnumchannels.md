---
Description: Retrieves the number of color channels used in memory to store samples.
ms.assetid: 8b033cda-feec-4e74-a4c4-ea44b5fb12c7
title: ID3DXPRTCompBuffer::GetNumChannels method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ID3DXPRTCompBuffer::GetNumChannels method

Retrieves the number of color channels used in memory to store samples.

## Syntax


```C++
UINT GetNumChannels();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**UINT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Returns the number of color channels used in memory to store samples. The value generally will be either 1 to represent luminance values, or 3 to represent RGB values.

## Remarks

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPRTCompBuffer](id3dxprtcompbuffer.md)
</dt> </dl>

 

 




