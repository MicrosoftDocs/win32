---
Description: Save a texture to memory.
ms.assetid: be541b99-6d07-480e-8f28-b7fc44566e7d
title: D3DX10SaveTextureToMemory function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DX10SaveTextureToMemory function

Save a texture to memory.

## Syntax


```C++
HRESULT D3DX10SaveTextureToMemory(
  _In_  ID3D10Resource           *pSrcTexture,
  _In_  D3DX10_IMAGE_FILE_FORMAT DestFormat,
  _Out_ LPD3D10BLOB              *ppDestBuf,
  _In_  UINT                     Flags
);
```



## Parameters

<dl> <dt>

*pSrcTexture* \[in\]
</dt> <dd>

Type: **[**ID3D10Resource**](/windows/win32/D3D10/nn-d3d10-id3d10resource?branch=master)\***

Pointer to the texture to be saved. See [**ID3D10Resource Interface**](/windows/win32/D3D10/nn-d3d10-id3d10resource?branch=master).

</dd> <dt>

*DestFormat* \[in\]
</dt> <dd>

Type: **[**D3DX10\_IMAGE\_FILE\_FORMAT**](d3dx10-image-file-format.md)**

The format the texture will be saved as. See [**D3DX10\_IMAGE\_FILE\_FORMAT**](d3dx10-image-file-format.md).

</dd> <dt>

*ppDestBuf* \[out\]
</dt> <dd>

Type: **[**LPD3D10BLOB**](/windows/win32/D3DCommon/nn-d3dcommon-id3d10blob?branch=master)\***

Address of a pointer to the memory containing the saved texture. See [**ID3D10Blob Interface**](/windows/win32/D3DCommon/nn-d3dcommon-id3d10blob?branch=master).

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Optional.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The return value is one of the values listed in [Direct3D 10 Return Codes](d3d10-graphics-reference-returnvalues.md).

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10Tex.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>  |



## See also

<dl> <dt>

[Texture Functions in D3DX 10](d3d10-graphics-reference-d3dx10-functions-texturing.md)
</dt> <dt>

[General Purpose Functions](d3d10-graphics-reference-d3dx10-functions-general-purpose.md)
</dt> </dl>

 

 




