---
Description: 'Extracts coefficient data from a color channel of the buffer for a specified range of coefficients, and adds the data to an IDirect3DTexture9 object.'
ms.assetid: '75854676-706a-4675-857e-4f2f8fc8365b'
title: 'ID3DXPRTBuffer::ExtractTexture method'
---

# ID3DXPRTBuffer::ExtractTexture method

Extracts coefficient data from a color channel of the buffer for a specified range of coefficients, and adds the data to an [**IDirect3DTexture9**](idirect3dtexture9.md) object.

## Syntax


```C++
HRESULT ExtractTexture(
  [in] UINT               Channel,
  [in] UINT               StartCoefficient,
  [in] UINT               NumCoefficients,
  [in] LPDIRECT3DTEXTURE9 pTexture
);
```



## Parameters

<dl> <dt>

*Channel* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Buffer color channel from which to extract texture data.

</dd> <dt>

*StartCoefficient* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Starting value of the buffer coefficient from which to extract texture data.

</dd> <dt>

*NumCoefficients* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Number of scalars, beginning at StartCoefficient, from which to extract texture data.

</dd> <dt>

*pTexture* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DTEXTURE9**](idirect3dtexture9.md)**

Pointer to a [**IDirect3DTexture9**](idirect3dtexture9.md) texture object that will store coefficients.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPRTBuffer](id3dxprtbuffer.md)
</dt> </dl>

 

 




