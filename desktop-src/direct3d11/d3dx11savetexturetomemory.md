---
title: D3DX11SaveTextureToMemory function
description: Note The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps. Note Instead of using this function, we recommend that you use the DirectXTex library, CaptureTexture then SaveToXXXMemory (where XXX is WIC, DDS, or TGA; WIC doesn't support DDS and TGA; D3DX 9 supported TGA as a common art source format for games). Save a texture to memory.
ms.assetid: '3b54d8e1-6474-48fd-8348-a3baac406101'
keywords: ["D3DX11SaveTextureToMemory function Direct3D 11"]
topic_type:
- apiref
api_name:
- D3DX11SaveTextureToMemory
api_location:
- D3DX11.lib
- D3DX11.dll
api_type:
- LibDef
---

# D3DX11SaveTextureToMemory function

> [!Note]  
> The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.

 

> [!Note]  
> Instead of using this function, we recommend that you use the [DirectXTex](http://go.microsoft.com/fwlink/p/?linkid=248926) library, **CaptureTexture** then **SaveToXXXMemory** (where XXX is WIC, DDS, or TGA; WIC doesn't support DDS and TGA; D3DX 9 supported TGA as a common art source format for games).

 

Save a texture to memory.

## Syntax


```C++
HRESULT D3DX11SaveTextureToMemory(
        ID3D11DeviceContext      *pContext,
  _In_  ID3D11Resource           *pSrcTexture,
  _In_  D3DX11_IMAGE_FILE_FORMAT DestFormat,
  _Out_ LPD3D10BLOB              *ppDestBuf,
  _In_  UINT                     Flags
);
```



## Parameters

<dl> <dt>

*pContext* 
</dt> <dd>

Type: **[**ID3D11DeviceContext**](id3d11devicecontext.md)\***

A pointer to an [**ID3D11DeviceContext**](id3d11devicecontext.md) object.

</dd> <dt>

*pSrcTexture* \[in\]
</dt> <dd>

Type: **[**ID3D11Resource**](id3d11resource.md)\***

Pointer to the texture to be saved. See [**ID3D11Resource**](id3d11resource.md).

</dd> <dt>

*DestFormat* \[in\]
</dt> <dd>

Type: **[**D3DX11\_IMAGE\_FILE\_FORMAT**](d3dx11-image-file-format.md)**

The format the texture will be saved as. See [**D3DX11\_IMAGE\_FILE\_FORMAT**](d3dx11-image-file-format.md).

</dd> <dt>

*ppDestBuf* \[out\]
</dt> <dd>

Type: **[**LPD3D10BLOB**](https://msdn.microsoft.com/library/windows/desktop/bb173507)\***

Address of a pointer to the memory containing the saved texture.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

Optional.

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

 

 





