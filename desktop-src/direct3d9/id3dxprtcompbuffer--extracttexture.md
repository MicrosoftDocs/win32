---
Description: Extracts the per-sample principal component analysis (PCA) projection coefficients from an ID3DXPRTCompBuffer compressed data buffer and adds the data to an IDirect3DTexture9 object.
ms.assetid: 2159e57d-b8e5-421f-b20a-ac58b29e3c45
title: ID3DXPRTCompBufferExtractTexture method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXPRTCompBuffer::ExtractTexture method

Extracts the per-sample principal component analysis (PCA) projection coefficients from an [**ID3DXPRTCompBuffer**](id3dxprtcompbuffer.md) compressed data buffer and adds the data to an [**IDirect3DTexture9**](/windows/win32/d3d9helper/nn-d3d9-idirect3dtexture9?branch=master) object.

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

Type: **[**UINT**](winprog.windows_data_types)**

Starting value of the buffer coefficient from which to extract texture data.

</dd> <dt>

*NumPCA* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Number of PCA coefficients to extract from the buffer.

</dd> <dt>

*pTexture* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DTEXTURE9**](/windows/win32/d3d9helper/nn-d3d9-idirect3dtexture9?branch=master)**

Pointer to an [**IDirect3DTexture9**](/windows/win32/d3d9helper/nn-d3d9-idirect3dtexture9?branch=master) texture object that will store PCA coefficients.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

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

 

 




