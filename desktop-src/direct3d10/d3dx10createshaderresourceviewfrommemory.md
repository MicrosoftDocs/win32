---
Description: Create a shader-resource view from a file in memory.
ms.assetid: 8316987f-75b4-4cee-a1f2-10bee77a28e6
title: D3DX10CreateShaderResourceViewFromMemory function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DX10CreateShaderResourceViewFromMemory function

Create a shader-resource view from a file in memory.

## Syntax


```C++
HRESULT D3DX10CreateShaderResourceViewFromMemory(
  _In_  ID3D10Device             *pDevice,
  _In_  LPCVOID                  pSrcData,
  _In_  SIZE_T                   SrcDataSize,
  _In_  D3DX10_IMAGE_LOAD_INFO   *pLoadInfo,
  _In_  ID3DX10ThreadPump        *pPump,
  _Out_ ID3D10ShaderResourceView **ppShaderResourceView,
  _Out_ HRESULT                  *pHResult
);
```



## Parameters

<dl> <dt>

*pDevice* \[in\]
</dt> <dd>

Type: **[**ID3D10Device**](/windows/win32/D3D10/nn-d3d10-id3d10device?branch=master)\***

A pointer to the device (see [**ID3D10Device Interface**](/windows/win32/D3D10/nn-d3d10-id3d10device?branch=master)) that will use the resource.

</dd> <dt>

*pSrcData* \[in\]
</dt> <dd>

Type: **[**LPCVOID**](winprog.windows_data_types)**

Pointer to the file in memory that contains the shader-resource view.

</dd> <dt>

*SrcDataSize* \[in\]
</dt> <dd>

Type: **[**SIZE\_T**](winprog.windows_data_types)**

Size of the file in memory.

</dd> <dt>

*pLoadInfo* \[in\]
</dt> <dd>

Type: **[**D3DX10\_IMAGE\_LOAD\_INFO**](d3dx10-image-load-info.md)\***

Optional. Identifies the characteristics of a texture (see [**D3DX10\_IMAGE\_LOAD\_INFO**](d3dx10-image-load-info.md)) when the data processor is created; set this to **NULL** to read the characteristics of a texture when the texture is loaded.

</dd> <dt>

*pPump* \[in\]
</dt> <dd>

Type: **[**ID3DX10ThreadPump**](id3dx10threadpump.md)\***

A pointer to a thread pump interface (see [**ID3DX10ThreadPump Interface**](id3dx10threadpump.md)). If **NULL** is specified, this function will behave synchronously and will not return until it is finished.

</dd> <dt>

*ppShaderResourceView* \[out\]
</dt> <dd>

Type: **[**ID3D10ShaderResourceView**](/windows/win32/d3d10/nn-d3d10-id3d10shaderresourceview?branch=master)\*\***

Address of a pointer to the newly created shader resource view. See [**ID3D10ShaderResourceView Interface**](/windows/win32/d3d10/nn-d3d10-id3d10shaderresourceview?branch=master).

</dd> <dt>

*pHResult* \[out\]
</dt> <dd>

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)\***

A pointer to the return value. May be **NULL**. If *pPump* is not **NULL**, then *pHResult* must be a valid memory location until the asynchronous execution completes.

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

 

 




