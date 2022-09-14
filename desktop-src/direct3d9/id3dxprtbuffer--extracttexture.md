---
description: Extracts coefficient data from a color channel of the buffer for a specified range of coefficients, and adds the data to an IDirect3DTexture9 object.
ms.assetid: 75854676-706a-4675-857e-4f2f8fc8365b
title: ID3DXPRTBuffer::ExtractTexture method (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- ID3DXPRTBuffer.ExtractTexture
api_type:
- COM
api_location:
- d3dx9.lib
- d3dx9.dll
---

# ID3DXPRTBuffer::ExtractTexture method

Extracts coefficient data from a color channel of the buffer for a specified range of coefficients, and adds the data to an [**IDirect3DTexture9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3dtexture9) object.

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

Type: **[**UINT**](../winprog/windows-data-types.md)**

Buffer color channel from which to extract texture data.

</dd> <dt>

*StartCoefficient* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Starting value of the buffer coefficient from which to extract texture data.

</dd> <dt>

*NumCoefficients* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Number of scalars, beginning at StartCoefficient, from which to extract texture data.

</dd> <dt>

*pTexture* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DTEXTURE9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3dtexture9)**

Pointer to a [**IDirect3DTexture9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3dtexture9) texture object that will store coefficients.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPRTBuffer](id3dxprtbuffer.md)
</dt> </dl>

 

 
