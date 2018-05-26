---
Description: Unmap a buffer.
ms.assetid: 47f125cd-5c0a-4814-93c5-f2f11ce33ea6
title: ID3DX10MeshBufferUnmap method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DX10MeshBuffer::Unmap method

Unmap a buffer.

## Syntax


```C++
HRESULT Unmap();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The return value is one of the values listed in [Direct3D 10 Return Codes](d3d10-graphics-reference-returnvalues.md).

## Remarks



|                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Differences between Direct3D 9 and Direct3D 10:<br/> Unmap() in Direct3D 10 is analogous to resource Unlock() in Direct3D 9.<br/> |



 

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[ID3DX10MeshBuffer](id3dx10meshbuffer.md)
</dt> <dt>

[D3DX Interfaces](d3d10-graphics-reference-d3dx10-interfaces.md)
</dt> </dl>

 

 




