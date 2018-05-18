---
Description: 'Gets the maximum face influences in a triangle mesh with the specified index buffer.'
ms.assetid: '72dc2440-87df-461e-80d0-9ad9b1e4d8ee'
title: 'ID3DXSkinInfo::GetMaxFaceInfluences method'
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

Type: **[**LPDIRECT3DINDEXBUFFER9**](idirect3dindexbuffer9.md)**

Pointer to the index buffer that contains the mesh index data.

</dd> <dt>

*NumFaces* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

Number of faces in the mesh.

</dd> <dt>

*maxFaceInfluences* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)\***

Pointer to the maximum face influences.

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

 

 




