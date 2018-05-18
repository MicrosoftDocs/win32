---
Description: 'Sets the vertex declaration.'
ms.assetid: 'cbb802ac-f0ba-41e6-8c67-a787982f975f'
title: 'ID3DXSkinInfo::SetDeclaration method'
---

# ID3DXSkinInfo::SetDeclaration method

Sets the vertex declaration.

## Syntax


```C++
HRESULT SetDeclaration(
  [in] const D3DVERTEXELEMENT9 *pDeclaration
);
```



## Parameters

<dl> <dt>

*pDeclaration* \[in\]
</dt> <dd>

Type: **const [**D3DVERTEXELEMENT9**](d3dvertexelement9.md)\***

Pointer to an array of [**D3DVERTEXELEMENT9**](d3dvertexelement9.md) elements.

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
</dt> <dt>

[**ID3DXSkinInfo::GetDeclaration**](id3dxskininfo--getdeclaration.md)
</dt> </dl>

 

 




