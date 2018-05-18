---
Description: 'Sets the bone offset matrix.'
ms.assetid: 'f8ac1117-510d-42af-a6bf-422cbaaf6b74'
title: 'ID3DXSkinInfo::SetBoneOffsetMatrix method'
---

# ID3DXSkinInfo::SetBoneOffsetMatrix method

Sets the bone offset matrix.

## Syntax


```C++
HRESULT SetBoneOffsetMatrix(
  [in]       DWORD      Bone,
  [in] const D3DXMATRIX *pBoneTransform
);
```



## Parameters

<dl> <dt>

*Bone* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

Bone number.

</dd> <dt>

*pBoneTransform* \[in\]
</dt> <dd>

Type: **const [**D3DXMATRIX**](d3dxmatrix.md)\***

Pointer to the bone offset matrix.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Remarks

Bone names are returned by [**D3DXLoadMeshFromXof**](d3dxloadmeshfromxof.md).

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXSkinInfo](id3dxskininfo.md)
</dt> <dt>

[**ID3DXSkinInfo::GetBoneOffsetMatrix**](id3dxskininfo--getboneoffsetmatrix.md)
</dt> </dl>

 

 




