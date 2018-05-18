---
Description: 'Receives a texel class value that indicates texel class according to each texel''s location.'
ms.assetid: '450739a8-e30c-4e56-9560-8cb705a75672'
title: 'ID3DXTextureGutterHelper::GetGutterMap method'
---

# ID3DXTextureGutterHelper::GetGutterMap method

Receives a texel class value that indicates texel class according to each texel's location.

## Syntax


```C++
HRESULT GetGutterMap(
  [in, out] BYTE *pGutterData
);
```



## Parameters

<dl> <dt>

*pGutterData* \[in, out\]
</dt> <dd>

Type: **[**BYTE**](winprog.windows_data_types)\***

Pointer to the texel class. Possible texel classes are as follows. There is no texel class 3.



| Texel Class | Texel Location                                                                                                                                                                                                                                                                                                                                                                |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0           | Invalid point; texel will not be used.                                                                                                                                                                                                                                                                                                                                        |
| 1           | Inside triangle.                                                                                                                                                                                                                                                                                                                                                              |
| 2           | Inside gutter.                                                                                                                                                                                                                                                                                                                                                                |
| 4           | Inside gutter; texel will be evaluated as a full sample in the [**ID3DXTextureGutterHelper::ApplyGuttersFloat**](id3dxtexturegutterhelper--applyguttersfloat.md), [**ID3DXTextureGutterHelper::ApplyGuttersTex**](id3dxtexturegutterhelper--applygutterstex.md), or [**ID3DXTextureGutterHelper::ApplyGuttersPRT**](id3dxtexturegutterhelper--applyguttersprt.md) methods. |



 

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned.D3DERR\_INVALIDCALL

## Remarks

The application must allocate and manage pGutterData, with size given by:


```
texture width * texture height * sizeof(BYTE)
```



Texture width and height are returned by [**ID3DXTextureGutterHelper::GetWidth**](id3dxtexturegutterhelper--getwidth.md) and [**ID3DXTextureGutterHelper::GetHeight**](id3dxtexturegutterhelper--getheight.md).

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXTextureGutterHelper](id3dxtexturegutterhelper.md)
</dt> </dl>

 

 




