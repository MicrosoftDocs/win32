---
Description: Extracts the per-sample principal component analysis (PCA) projection coefficients from an ID3DXPRTCompBuffer compressed data buffer and adds the data to an IDirect3DTexture9 object.
ms.assetid: 2159e57d-b8e5-421f-b20a-ac58b29e3c45
title: ID3DXPRTCompBuffer::ExtractTexture method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- ID3DXPRTCompBuffer.ExtractTexture
api_type:
- COM
api_location:
- d3dx9.lib
- d3dx9.dll
---

# ID3DXPRTCompBuffer::ExtractTexture method

Extracts the per-sample principal component analysis (PCA) projection coefficients from an [**ID3DXPRTCompBuffer**](id3dxprtcompbuffer.md) compressed data buffer and adds the data to an [**IDirect3DTexture9**](https://msdn.microsoft.com/library/Bb205909(v=VS.85).aspx) object.

## Syntax


```C++
HRESULT ExtractTexture(
  [in] UINT               StartPCA,
  [in] UINT               NumPCA,
  [in] LPDIRECT3DTEXTURE9 pTexture
);
```



## Parameters

<dl> <dt>

*StartPCA* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

Starting value of the buffer coefficient from which to extract texture data.

</dd> <dt>

*NumPCA* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

Number of PCA coefficients to extract from the buffer.

</dd> <dt>

*pTexture* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DTEXTURE9**](https://msdn.microsoft.com/library/Bb205909(v=VS.85).aspx)**

Pointer to an [**IDirect3DTexture9**](https://msdn.microsoft.com/library/Bb205909(v=VS.85).aspx) texture object that will store PCA coefficients.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/en-us/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPRTCompBuffer](id3dxprtcompbuffer.md)
</dt> </dl>

 

 




