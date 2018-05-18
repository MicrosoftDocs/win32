---
Description: 'Create a shader-resource view from a file.'
ms.assetid: '97aa848b-e24c-4ebd-8819-b9741ea12b60'
title: D3DX10CreateShaderResourceViewFromFile function
---

# D3DX10CreateShaderResourceViewFromFile function

Create a shader-resource view from a file.

## Syntax


```C++
HRESULT D3DX10CreateShaderResourceViewFromFile(
  _In_  ID3D10Device             *pDevice,
  _In_  LPCTSTR                  pSrcFile,
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

Type: **[**ID3D10Device**](id3d10device.md)\***

A pointer to the device (see [**ID3D10Device Interface**](id3d10device.md)) that will use the resource.

</dd> <dt>

*pSrcFile* \[in\]
</dt> <dd>

Type: **[**LPCTSTR**](winprog.windows_data_types)**

Name of the file that contains the shader-resource view. If the compiler settings require Unicode, the data type LPCTSTR resolves to LPCWSTR. Otherwise, the data type resolves to LPCSTR.

</dd> <dt>

*pLoadInfo* \[in\]
</dt> <dd>

Type: **[**D3DX10\_IMAGE\_LOAD\_INFO**](d3dx10-image-load-info.md)\***

Optional. Identifies the characteristics of a texture (see [**D3DX10\_IMAGE\_LOAD\_INFO**](d3dx10-image-load-info.md)) when the data processor is created; set this to **NULL** to read the characteristics of a texture when the texture is loaded.

</dd> <dt>

*pPump* \[in\]
</dt> <dd>

Type: **[**ID3DX10ThreadPump**](id3dx10threadpump.md)\***

Pointer to a thread-pump interface (see [**ID3DX10ThreadPump Interface**](id3dx10threadpump.md)). If **NULL** is specified, this function will behave synchronously and will not return until it is finished.

</dd> <dt>

*ppShaderResourceView* \[out\]
</dt> <dd>

Type: **[**ID3D10ShaderResourceView**](id3d10shaderresourceview.md)\*\***

Address of a pointer to the shader-resource view (see [**ID3D10ShaderResourceView Interface**](id3d10shaderresourceview.md)).

</dd> <dt>

*pHResult* \[out\]
</dt> <dd>

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)\***

A pointer to the return value. May be **NULL**. If *pPump* is not **NULL**, then *pHResult* must be a valid memory location until the asynchronous execution completes.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The return value is one of the values listed in [Direct3D 10 Return Codes](d3d10-graphics-reference-returnvalues.md).

## Remarks

For a list of supported image formats, see [**D3DX10\_IMAGE\_FILE\_FORMAT**](d3dx10-image-file-format.md).

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

 

 




