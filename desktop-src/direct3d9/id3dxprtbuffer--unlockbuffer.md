---
Description: Ends the lifespan of the ppData pointer returned by ID3DXPRTBufferLockBuffer.
ms.assetid: 25464566-8a93-48a4-93fa-17828861f98c
title: ID3DXPRTBufferUnlockBuffer method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXPRTBuffer::UnlockBuffer method

Ends the lifespan of the ppData pointer returned by [**ID3DXPRTBuffer::LockBuffer**](id3dxprtbuffer--lockbuffer.md).

## Syntax


```C++
HRESULT UnlockBuffer();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPRTBuffer](id3dxprtbuffer.md)
</dt> </dl>

 

 




