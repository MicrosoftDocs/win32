---
Description: 'Creates an empty skin mesh object using a flexible vertex format (FVF) code.'
ms.assetid: '72e27850-0102-4121-a397-16f2e0220b93'
title: D3DXCreateSkinInfoFVF function
---

# D3DXCreateSkinInfoFVF function

Creates an empty skin mesh object using a flexible vertex format (FVF) code.

## Syntax


```C++
HRESULT D3DXCreateSkinInfoFVF(
  _In_  DWORD          NumVertices,
  _In_  DWORD          FVF,
  _In_  DWORD          NumBones,
  _Out_ LPD3DXSKININFO *ppSkinInfo
);
```



## Parameters

<dl> <dt>

*NumVertices* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

Number of vertices for the skin mesh.

</dd> <dt>

*FVF* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

Combination of [D3DFVF](d3dfvf.md) that describes the vertex format for the returned skin mesh.

</dd> <dt>

*NumBones* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

Number of bones for the skin mesh.

</dd> <dt>

*ppSkinInfo* \[out\]
</dt> <dd>

Type: **[**LPD3DXSKININFO**](id3dxskininfo.md)\***

Address of a pointer to an [**ID3DXSkinInfo**](id3dxskininfo.md) interface, representing the created skin information object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Remarks

Use [**SetBoneInfluence**](id3dxskininfo--setboneinfluence.md) to populate the empty skin mesh object returned by this method.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Mesh Functions](dx9-graphics-reference-d3dx-functions-mesh.md)
</dt> <dt>

[**SetBoneInfluence**](id3dxskininfo--setboneinfluence.md)
</dt> </dl>

 

 




