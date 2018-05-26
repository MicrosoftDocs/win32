---
title: D3DX11SaveTextureToFile function
description: Note The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps. Note Instead of using this function, we recommend that you use the DirectXTex library, CaptureTexture then SaveToXXXFile (where XXX is WIC, DDS, or TGA; WIC doesnt support DDS and TGA; D3DX 9 supported TGA as a common art source format for games). For the simplified scenario of creating a screen shot from a render target texture, we recommend that you use the DirectXTK library, SaveDDSTextureToFile or SaveWICTextureToFile. Save a texture to a file.
ms.assetid: da161268-fb68-42dd-ba31-b090a993f369
keywords:
- D3DX11SaveTextureToFile function Direct3D 11
topic_type:
- apiref
api_name:
- D3DX11SaveTextureToFile
api_location:
- D3DX11.lib
- D3DX11.dll
api_type:
- LibDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DX11SaveTextureToFile function

> [!Note]  
> The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.

 

> [!Note]  
> Instead of using this function, we recommend that you use the [DirectXTex](http://go.microsoft.com/fwlink/p/?linkid=248926) library, **CaptureTexture** then **SaveToXXXFile** (where XXX is WIC, DDS, or TGA; WIC doesn't support DDS and TGA; D3DX 9 supported TGA as a common art source format for games). For the simplified scenario of creating a screen shot from a render target texture, we recommend that you use the [DirectXTK](http://go.microsoft.com/fwlink/p/?linkid=248929) library, **SaveDDSTextureToFile** or **SaveWICTextureToFile**.

 

Save a texture to a file.

## Syntax


```C++
HRESULT D3DX11SaveTextureToFile(
       ID3D11DeviceContext      *pContext,
  _In_ ID3D11Resource           *pSrcTexture,
  _In_ D3DX11_IMAGE_FILE_FORMAT DestFormat,
  _In_ LPCTSTR                  pDestFile
);
```



## Parameters

<dl> <dt>

*pContext* 
</dt> <dd>

Type: **[**ID3D11DeviceContext**](/windows/win32/D3D11/nn-d3d11-id3d11devicecontext?branch=master)\***

A pointer to an [**ID3D11DeviceContext**](/windows/win32/D3D11/nn-d3d11-id3d11devicecontext?branch=master) object.

</dd> <dt>

*pSrcTexture* \[in\]
</dt> <dd>

Type: **[**ID3D11Resource**](/windows/win32/D3D11/nn-d3d11-id3d11resource?branch=master)\***

Pointer to the texture to be saved. See [**ID3D11Resource**](/windows/win32/D3D11/nn-d3d11-id3d11resource?branch=master).

</dd> <dt>

*DestFormat* \[in\]
</dt> <dd>

Type: **[**D3DX11\_IMAGE\_FILE\_FORMAT**](d3dx11-image-file-format.md)**

The format the texture will be saved as (see [**D3DX11\_IMAGE\_FILE\_FORMAT**](d3dx11-image-file-format.md)). D3DX11\_IFF\_DDS is the preferred format since it is the only option that supports all the formats in [**DXGI\_FORMAT**](https://msdn.microsoft.com/library/windows/desktop/bb173059).

</dd> <dt>

*pDestFile* \[in\]
</dt> <dd>

Type: **[**LPCTSTR**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

Name of the destination output file where the texture will be saved. If the compiler settings require Unicode, the data type LPCTSTR resolves to LPCWSTR. Otherwise, the data type resolves to LPCSTR.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The return value is one of the values listed in [Direct3D 11 Return Codes](d3d11-graphics-reference-returnvalues.md); use the return value to see if the *DestFormat* is supported.

## Remarks

**D3DX11SaveTextureToFile** writes out the extra [**DDS\_HEADER\_DXT10**](https://msdn.microsoft.com/library/windows/desktop/bb943983) structure for the input texture only if necessary (for example, because the input texture is in standard RGB (sRGB) format). If **D3DX11SaveTextureToFile** writes out the **DDS\_HEADER\_DXT10** structure, it sets the **dwFourCC** member of the [**DDS\_PIXELFORMAT**](https://msdn.microsoft.com/library/windows/desktop/bb943984) structure for the texture to **DX10** to indicate the prescense of the **DDS\_HEADER\_DXT10** extended header.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX11tex.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX11.lib</dt> </dl>  |



## See also

<dl> <dt>

[D3DX Functions](d3d11-graphics-reference-d3dx11-functions.md)
</dt> </dl>

 

 





