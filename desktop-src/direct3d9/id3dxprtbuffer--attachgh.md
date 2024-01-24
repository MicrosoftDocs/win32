---
description: Associates an ID3DXTextureGutterHelper object with the ID3DXPRTBuffer object.
ms.assetid: 095fea82-ac7a-42fa-990a-084715c73823
title: ID3DXPRTBuffer::AttachGH method (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXPRTBuffer.AttachGH
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXPRTBuffer::AttachGH method

Associates an [**ID3DXTextureGutterHelper**](id3dxtexturegutterhelper.md) object with the [**ID3DXPRTBuffer**](id3dxprtbuffer.md) object.

## Syntax


```C++
HRESULT AttachGH(
  [in] LPD3DXTEXTUREGUTTERHELPER pGH
);
```



## Parameters

<dl> <dt>

*pGH* \[in\]
</dt> <dd>

Type: **[**LPD3DXTEXTUREGUTTERHELPER**](id3dxtexturegutterhelper.md)**

Pointer to the [**ID3DXTextureGutterHelper**](id3dxtexturegutterhelper.md) interface of an object that contains texture gutter data.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK.

## Remarks

The reference count of the [**ID3DXTextureGutterHelper**](id3dxtexturegutterhelper.md) object will automatically be incremented by one. Any existing **ID3DXTextureGutterHelper** pointers will be released.

You must ensure that the number of **ID3DXPRTBuffer::AttachGH** calls matches the number of [**ID3DXPRTBuffer::ReleaseGH**](id3dxprtbuffer--releasegh.md) calls. After calling **ID3DXPRTBuffer::ReleaseGH**, the pGH pointer returned by **ID3DXPRTBuffer::AttachGH** should no longer be used.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPRTBuffer](id3dxprtbuffer.md)
</dt> <dt>

[**ID3DXPRTBuffer::ReleaseGH**](id3dxprtbuffer--releasegh.md)
</dt> </dl>

 

 




