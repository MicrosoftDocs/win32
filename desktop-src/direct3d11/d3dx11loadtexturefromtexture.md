---
title: D3DX11LoadTextureFromTexture function
description: Note The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps. Note Instead of using this function, we recommend that you use the DirectXTex library, Resize, Convert, Compress, Decompress, and/or CopyRectangle. Load a texture from a texture.
ms.assetid: '4e673f73-531d-4df8-8542-798e4e70c481'
keywords: ["D3DX11LoadTextureFromTexture function Direct3D 11"]
topic_type:
- apiref
api_name:
- D3DX11LoadTextureFromTexture
api_location:
- D3DX11.lib
- D3DX11.dll
api_type:
- LibDef
---

# D3DX11LoadTextureFromTexture function

> [!Note]  
> The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.

 

> [!Note]  
> Instead of using this function, we recommend that you use the [DirectXTex](http://go.microsoft.com/fwlink/p/?linkid=248926) library, **Resize**, **Convert**, **Compress**, **Decompress**, and/or **CopyRectangle**.

 

Load a texture from a texture.

## Syntax


```C++
HRESULT D3DX11LoadTextureFromTexture(
   ID3D11DeviceContext      *pContext,
   ID3D11Resource           *pSrcTexture,
   D3DX11_TEXTURE_LOAD_INFO *pLoadInfo,
   ID3D11Resource           *pDstTexture
);
```



## Parameters

<dl> <dt>

*pContext* 
</dt> <dd>

Type: **[**ID3D11DeviceContext**](id3d11devicecontext.md)\***

A pointer to an [**ID3D11DeviceContext**](id3d11devicecontext.md) object.

</dd> <dt>

*pSrcTexture* 
</dt> <dd>

Type: **[**ID3D11Resource**](id3d11resource.md)\***

Pointer to the source texture. See [**ID3D11Resource**](id3d11resource.md).

</dd> <dt>

*pLoadInfo* 
</dt> <dd>

Type: **[**D3DX11\_TEXTURE\_LOAD\_INFO**](d3dx11-texture-load-info.md)\***

Pointer to texture loading parameters. See [**D3DX11\_TEXTURE\_LOAD\_INFO**](d3dx11-texture-load-info.md).

</dd> <dt>

*pDstTexture* 
</dt> <dd>

Type: **[**ID3D11Resource**](id3d11resource.md)\***

Pointer to the destination texture. See [**ID3D11Resource**](id3d11resource.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The return value is one of the values listed in [Direct3D 11 Return Codes](d3d11-graphics-reference-returnvalues.md).

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX11tex.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX11.lib</dt> </dl>  |



## See also

<dl> <dt>

[D3DX Functions](d3d11-graphics-reference-d3dx11-functions.md)
</dt> </dl>

 

 





