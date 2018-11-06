---
title: D3DX11CreateTextureFromResource function
description: Note The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps. Note Instead of using this function, we recommend that you use resource functions, then these DirectXTK library (runtime), CreateXXXTextureFromMemory (where XXX is DDS or WIC)DirectXTex library (tools), LoadFromXXXMemory (where XXX is WIC, DDS, or TGA; WIC doesn't support DDS and TGA; D3DX 9 supported TGA as a common art source format for games) then CreateTexture Create a texture from another resource.
ms.assetid: 2b62239a-c19b-4d4f-9fd2-afcd87ba0fac
keywords:
- D3DX11CreateTextureFromResource function Direct3D 11
topic_type:
- apiref
api_name:
- D3DX11CreateTextureFromResource
api_location:
- D3DX11.lib
- D3DX11.dll
api_type:
- LibDef
ms.topic: article
ms.date: 05/31/2018
---

# D3DX11CreateTextureFromResource function

> [!Note]  
> The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.

 

> [!Note]  
> Instead of using this function, we recommend that you use [resource functions](https://msdn.microsoft.com/library/windows/desktop/ff468902), then these:
>
> -   [DirectXTK](http://go.microsoft.com/fwlink/p/?linkid=248929) library (runtime), **CreateXXXTextureFromMemory** (where XXX is DDS or WIC)
> -   [DirectXTex](http://go.microsoft.com/fwlink/p/?linkid=248926) library (tools), **LoadFromXXXMemory** (where XXX is WIC, DDS, or TGA; WIC doesn't support DDS and TGA; D3DX 9 supported TGA as a common art source format for games) then **CreateTexture**

 

Create a texture from another resource.

## Syntax


```C++
HRESULT D3DX11CreateTextureFromResource(
  _In_  ID3D11Device           *pDevice,
  _In_  HMODULE                hSrcModule,
  _In_  LPCTSTR                pSrcResource,
  _In_  D3DX11_IMAGE_LOAD_INFO *pLoadInfo,
  _In_  ID3DX11ThreadPump      *pPump,
  _Out_ ID3D11Resource         **ppTexture,
  _Out_ HRESULT                *pHResult
);
```



## Parameters

<dl> <dt>

*pDevice* \[in\]
</dt> <dd>

Type: **[**ID3D11Device**](/windows/desktop/api/D3D11/nn-d3d11-id3d11device)\***

A pointer to the device (see [**ID3D11Device**](/windows/desktop/api/D3D11/nn-d3d11-id3d11device)) that will use the resource.

</dd> <dt>

*hSrcModule* \[in\]
</dt> <dd>

Type: **[**HMODULE**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

A handle to the source resource. HMODULE can be obtained with [GetModuleHandle Function](http://msdn.microsoft.com/library/ms683199.aspx).

</dd> <dt>

*pSrcResource* \[in\]
</dt> <dd>

Type: **[**LPCTSTR**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

A string that contains the name of the source resource. If the compiler settings require Unicode, the data type LPCTSTR resolves to LPCWSTR. Otherwise, the data type resolves to LPCSTR.

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

*ppTexture* \[out\]
</dt> <dd>

Type: **[**ID3D11Resource**](/windows/desktop/api/D3D11/nn-d3d11-id3d11resource)\*\***

The address of a pointer to the texture resource (see [**ID3D11Resource**](/windows/desktop/api/D3D11/nn-d3d11-id3d11resource)).

</dd> <dt>

*pHResult* \[out\]
</dt> <dd>

Type: **[**HRESULT**](https://msdn.microsoft.com/en-us/library/Bb401631(v=MSDN.10).aspx)\***

A pointer to the return value. May be **NULL**. If *pPump* is not **NULL**, then *pHResult* must be a valid memory location until the asynchronous execution completes.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/en-us/library/Bb401631(v=MSDN.10).aspx)**

The return value is one of the values listed in [Direct3D 11 Return Codes](d3d11-graphics-reference-returnvalues.md).

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX11.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX11.lib</dt> </dl> |



## See also

<dl> <dt>

[D3DX Functions](d3d11-graphics-reference-d3dx11-functions.md)
</dt> </dl>

 

 





