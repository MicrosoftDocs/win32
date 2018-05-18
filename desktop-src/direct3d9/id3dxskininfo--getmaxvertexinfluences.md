---
Description: 'Gets the maximum number of influences for any vertex in the mesh.'
ms.assetid: '012168e8-30e5-4571-b793-647ab23df068'
title: 'ID3DXSkinInfo::GetMaxVertexInfluences method'
---

# ID3DXSkinInfo::GetMaxVertexInfluences method

Gets the maximum number of influences for any vertex in the mesh.

## Syntax


```C++
HRESULT GetMaxVertexInfluences(
  [in] DWORD *maxVertexInfluences
);
```



## Parameters

<dl> <dt>

*maxVertexInfluences* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)\***

Pointer to the maximum vertex influence.

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

 

 




