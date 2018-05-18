---
Description: 'Sets the index of the mesh face to which each texel belongs.'
ms.assetid: '45d931bc-fb8b-48da-b30d-99d5dc183494'
title: 'ID3DXTextureGutterHelper::SetFaceMap method'
---

# ID3DXTextureGutterHelper::SetFaceMap method

Sets the index of the mesh face to which each texel belongs.

## Syntax


```C++
HRESULT SetFaceMap(
  [in] UINT *pFaceData
);
```



## Parameters

<dl> <dt>

*pFaceData* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)\***

Pointer to the index of the mesh face to which each texel belongs.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned.D3DERR\_INVALIDCALL

## Remarks

The mesh face data input to this method is valid only for valid (non-class 0) texels. [**ID3DXTextureGutterHelper::GetGutterMap**](id3dxtexturegutterhelper--getguttermap.md) will return non-zero values for valid texels.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXTextureGutterHelper](id3dxtexturegutterhelper.md)
</dt> </dl>

 

 




