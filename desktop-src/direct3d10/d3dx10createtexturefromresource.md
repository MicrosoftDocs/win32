---
Description: Create a texture from another resource.
ms.assetid: 9758968a-652f-42bb-8c81-ad7816c57b17
title: D3DX10CreateTextureFromResource function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DX10CreateTextureFromResource function

Create a texture from another resource.

## Syntax


```C++
HRESULT D3DX10CreateTextureFromResource(
  _In_  ID3D10Device           *pDevice,
  _In_  HMODULE                hSrcModule,
  _In_  LPCTSTR                pSrcResource,
  _In_  D3DX10_IMAGE_LOAD_INFO *pLoadInfo,
  _In_  ID3DX10ThreadPump      *pPump,
  _Out_ ID3D10Resource         **ppTexture,
  _Out_ HRESULT                *pHResult
);
```



## Parameters

<dl> <dt>

*pDevice* \[in\]
</dt> <dd>

Type: **[**ID3D10Device**](/windows/win32/D3D10/nn-d3d10-id3d10device?branch=master)\***

A pointer to the device (see [**ID3D10Device Interface**](/windows/win32/D3D10/nn-d3d10-id3d10device?branch=master)) that will use the resource.

</dd> <dt>

*hSrcModule* \[in\]
</dt> <dd>

Type: **[**HMODULE**](winprog.windows_data_types)**

A handle to the source resource. HMODULE can be obtained with [GetModuleHandle Function](http://msdn.microsoft.com/en-us/library/ms683199.aspx).

</dd> <dt>

*pSrcResource* \[in\]
</dt> <dd>

Type: **[**LPCTSTR**](winprog.windows_data_types)**

A string that contains the name of the source resource. If the compiler settings require Unicode, the data type LPCTSTR resolves to LPCWSTR. Otherwise, the data type resolves to LPCSTR.

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

*ppTexture* \[out\]
</dt> <dd>

Type: **[**ID3D10Resource**](/windows/win32/D3D10/nn-d3d10-id3d10resource?branch=master)\*\***

The address of a pointer to the texture resource (see [**ID3D10Resource Interface**](/windows/win32/D3D10/nn-d3d10-id3d10resource?branch=master)).

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

For a list of supported image formats see [**D3DX10\_IMAGE\_FILE\_FORMAT**](d3dx10-image-file-format.md).

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[Texture Functions in D3DX 10](d3d10-graphics-reference-d3dx10-functions-texturing.md)
</dt> <dt>

[General Purpose Functions](d3d10-graphics-reference-d3dx10-functions-general-purpose.md)
</dt> </dl>

 

 




