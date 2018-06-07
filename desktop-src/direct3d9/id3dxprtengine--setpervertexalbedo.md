---
Description: Sets an albedo value for each mesh vertex, overwriting previous albedo values.
ms.assetid: 5220dfe3-8d41-480c-a850-b9aad3d2bb2f
title: ID3DXPRTEngine::SetPerVertexAlbedo method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ID3DXPRTEngine::SetPerVertexAlbedo method

Sets an albedo value for each mesh vertex, overwriting previous albedo values.

## Syntax


```C++
HRESULT SetPerVertexAlbedo(
  [in] const VOID *pDataIn,
  [in]       UINT NumChannels,
  [in]       UINT Stride
);
```



## Parameters

<dl> <dt>

*pDataIn* \[in\]
</dt> <dd>

Type: **const VOID\***

Pointer to FLOAT albedo data of the first sample.

</dd> <dt>

*NumChannels* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Number of color channels to set. Set to 1 to specify gray materials (R = G = B), or 3 to enable color bleeding effects.

</dd> <dt>

*Stride* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Stride in bytes needed to get to next sample's albedo value. See [Width vs. Pitch (Direct3D 9)](width-vs--pitch.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPRTEngine](id3dxprtengine.md)
</dt> </dl>

 

 




