---
description: Save a texture to a file.
ms.assetid: c1718903-039a-4132-b128-82e03078ef62
title: D3DX10SaveTextureToFile function (D3DX10Tex.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DX10SaveTextureToFile
api_type: 
- LibDef
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# D3DX10SaveTextureToFile function

Save a texture to a file.

## Syntax


```C++
HRESULT D3DX10SaveTextureToFile(
  _In_ ID3D10Resource           *pSrcTexture,
  _In_ D3DX10_IMAGE_FILE_FORMAT DestFormat,
  _In_ LPCTSTR                  pDestFile
);
```



## Parameters

<dl> <dt>

*pSrcTexture* \[in\]
</dt> <dd>

Type: **[**ID3D10Resource**](/windows/desktop/api/D3D10/nn-d3d10-id3d10resource)\***

Pointer to the texture to be saved. See [**ID3D10Resource Interface**](/windows/desktop/api/D3D10/nn-d3d10-id3d10resource).

</dd> <dt>

*DestFormat* \[in\]
</dt> <dd>

Type: **[**D3DX10\_IMAGE\_FILE\_FORMAT**](d3dx10-image-file-format.md)**

The format the texture will be saved as (see [**D3DX10\_IMAGE\_FILE\_FORMAT**](d3dx10-image-file-format.md)). D3DX10\_IFF\_DDS is the preferred format since it is the only option that supports all the formats in [**DXGI\_FORMAT**](/windows/win32/api/dxgiformat/ne-dxgiformat-dxgi_format).

</dd> <dt>

*pDestFile* \[in\]
</dt> <dd>

Type: **[**LPCTSTR**](../winprog/windows-data-types.md)**

Name of the destination output file where the texture will be saved. If the compiler settings require Unicode, the data type LPCTSTR resolves to LPCWSTR. Otherwise, the data type resolves to LPCSTR.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

The return value is one of the values listed in [Direct3D 10 Return Codes](d3d10-graphics-reference-returnvalues.md); use the return value to see if the *DestFormat* is supported.

## Remarks

**D3DX10SaveTextureToFile** writes out the extra [**DDS\_HEADER\_DXT10**](../direct3ddds/dds-header-dxt10.md) structure for the input texture only if necessary (for example, because the input texture is in standard RGB (sRGB) format). If **D3DX10SaveTextureToFile** writes out the **DDS\_HEADER\_DXT10** structure, it sets the **dwFourCC** member of the [**DDS\_PIXELFORMAT**](../direct3ddds/dds-pixelformat.md) structure for the texture to **DX10** to indicate the prescense of the **DDS\_HEADER\_DXT10** extended header.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10Tex.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>  |



## See also

<dl> <dt>

[Texture Functions in D3DX 10](d3d10-graphics-reference-d3dx10-functions-texturing.md)
</dt> <dt>

[General Purpose Functions](d3d10-graphics-reference-d3dx10-functions-general-purpose.md)
</dt> </dl>

 

 
