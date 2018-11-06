---
Description: Gets the maximum face influences in a triangle mesh with the specified index buffer.
ms.assetid: 72dc2440-87df-461e-80d0-9ad9b1e4d8ee
title: ID3DXSkinInfo::GetMaxFaceInfluences method
ms.topic: article
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- ID3DXSkinInfo.GetMaxFaceInfluences
api_type:
- COM
api_location:
- d3dx9.lib
- d3dx9.dll
---

# ID3DXSkinInfo::GetMaxFaceInfluences method

Gets the maximum face influences in a triangle mesh with the specified index buffer.

## Syntax


```C++
HRESULT GetMaxFaceInfluences(
  [in] LPDIRECT3DINDEXBUFFER9 pIB,
  [in] DWORD                  NumFaces,
  [in] DWORD                  *maxFaceInfluences
);
```



## Parameters

<dl> <dt>

*pIB* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DINDEXBUFFER9**](https://msdn.microsoft.com/library/Bb205865(v=VS.85).aspx)**

Pointer to the index buffer that contains the mesh index data.

</dd> <dt>

*NumFaces* \[in\]
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

Number of faces in the mesh.

</dd> <dt>

*maxFaceInfluences* \[in\]
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)\***

Pointer to the maximum face influences.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/en-us/library/Bb401631(v=MSDN.10).aspx)**

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

 

 




