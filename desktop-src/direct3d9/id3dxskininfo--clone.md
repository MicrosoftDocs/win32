---
Description: Clones a skin info object.
ms.assetid: 82d0a78a-95f3-4b09-bc1a-b4bc663e0850
title: ID3DXSkinInfoClone method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXSkinInfo::Clone method

Clones a skin info object.

## Syntax


```C++
HRESULT Clone(
  [in, out] LPD3DXSKININFO *ppSkinInfo
);
```



## Parameters

<dl> <dt>

*ppSkinInfo* \[in, out\]
</dt> <dd>

Type: **[**LPD3DXSKININFO**](id3dxskininfo.md)\***

Address of a pointer to an [**ID3DXSkinInfo**](id3dxskininfo.md) object, which will contain the cloned object if the method is successful.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXSkinInfo](id3dxskininfo.md)
</dt> </dl>

 

 




