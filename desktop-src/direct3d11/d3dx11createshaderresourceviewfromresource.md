---
title: D3DX11CreateShaderResourceViewFromResource function
description: Note The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps. Note Instead of using this function, we recommend that you use resource functions, then these DirectXTK library (runtime), CreateXXXTextureFromMemory (where XXX is DDS or WIC)DirectXTex library (tools), LoadFromXXXMemory (where XXX is WIC, DDS, or TGA; WIC doesnt support DDS and TGA; D3DX 9 supported TGA as a common art source format for games) then CreateShaderResourceView Create a shader-resource view from a resource.
ms.assetid: 64620e6d-fc0d-4411-8744-d9d8ffe6ccb8
keywords:
- D3DX11CreateShaderResourceViewFromResource function Direct3D 11
topic_type:
- apiref
api_name:
- D3DX11CreateShaderResourceViewFromResource
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

# D3DX11CreateShaderResourceViewFromResource function

> [!Note]  
> The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.

 

> [!Note]  
> Instead of using this function, we recommend that you use [resource functions](https://msdn.microsoft.com/library/windows/desktop/ff468902), then these:
>
> -   [DirectXTK](http://go.microsoft.com/fwlink/p/?linkid=248929) library (runtime), **CreateXXXTextureFromMemory** (where XXX is DDS or WIC)
> -   [DirectXTex](http://go.microsoft.com/fwlink/p/?linkid=248926) library (tools), **LoadFromXXXMemory** (where XXX is WIC, DDS, or TGA; WIC doesn't support DDS and TGA; D3DX 9 supported TGA as a common art source format for games) then **CreateShaderResourceView**

 

Create a shader-resource view from a resource.

## Syntax


```C++
HRESULT D3DX11CreateShaderResourceViewFromResource(
  _In_  ID3D11Device             *pDevice,
  _In_  HMODULE                  hSrcModule,
  _In_  LPCTSTR                  pSrcResource,
  _In_  D3DX11_IMAGE_LOAD_INFO   *pLoadInfo,
  _In_  ID3DX11ThreadPump        *pPump,
  _Out_ ID3D11ShaderResourceView **ppShaderResourceView,
  _Out_ HRESULT                  *pHResult
);
```



## Parameters

<dl> <dt>

*pDevice* \[in\]
</dt> <dd>

Type: **[**ID3D11Device**](/windows/win32/D3D11/nn-d3d11-id3d11device?branch=master)\***

A pointer to the device (see [**ID3D11Device**](/windows/win32/D3D11/nn-d3d11-id3d11device?branch=master)) that will use the resource.

</dd> <dt>

*hSrcModule* \[in\]
</dt> <dd>

Type: **[**HMODULE**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

Handle to the resource module containing the shader-resource view. HMODULE can be obtained with [GetModuleHandle Function](http://msdn.microsoft.com/library/ms683199.aspx).

</dd> <dt>

*pSrcResource* \[in\]
</dt> <dd>

Type: **[**LPCTSTR**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

Name of the shader resource view in hSrcModule. If the compiler settings require Unicode, the data type LPCTSTR resolves to LPCWSTR. Otherwise, the data type resolves to LPCSTR.

</dd> <dt>

*pLoadInfo* \[in\]
</dt> <dd>

Type: **[**D3DX11\_IMAGE\_LOAD\_INFO**](d3dx11-image-load-info.md)\***

Optional. Identifies the characteristics of a texture (see [**D3DX11\_IMAGE\_LOAD\_INFO**](d3dx11-image-load-info.md)) when the data processor is created; set this to **NULL** to read the characteristics of a texture when the texture is loaded.

</dd> <dt>

*pPump* \[in\]
</dt> <dd>

Type: **[**ID3DX11ThreadPump**](id3dx11threadpump.md)\***

A pointer to a thread pump interface (see [**ID3DX11ThreadPump Interface**](id3dx11threadpump.md)). If **NULL** is specified, this function will behave synchronously and will not return until it is finished.

</dd> <dt>

*ppShaderResourceView* \[out\]
</dt> <dd>

Type: **[**ID3D11ShaderResourceView**](/windows/win32/D3D11/nn-d3d11-id3d11shaderresourceview?branch=master)\*\***

Address of a pointer to the shader-resource view (see [**ID3D11ShaderResourceView**](/windows/win32/D3D11/nn-d3d11-id3d11shaderresourceview?branch=master)).

</dd> <dt>

*pHResult* \[out\]
</dt> <dd>

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)\***

A pointer to the return value. May be **NULL**. If *pPump* is not **NULL**, then *pHResult* must be a valid memory location until the asynchronous execution completes.

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

 

 





