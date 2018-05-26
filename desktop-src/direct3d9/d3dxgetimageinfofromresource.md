---
Description: Retrieves information about a given image in a resource.
ms.assetid: 1f811b1e-f0bd-4f64-a4c9-caf899470940
title: D3DXGetImageInfoFromResource function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXGetImageInfoFromResource function

Retrieves information about a given image in a resource.

## Syntax


```C++
HRESULT D3DXGetImageInfoFromResource(
  _In_ HMODULE        hSrcModule,
  _In_ LPCTSTR        pSrcFile,
  _In_ D3DXIMAGE_INFO *pSrcInfo
);
```



## Parameters

<dl> <dt>

*hSrcModule* \[in\]
</dt> <dd>

Type: **[**HMODULE**](winprog.windows_data_types)**

Module where the resource is loaded. Set this parameter to **NULL** to specify the module associated with the image that the operating system used to create the current process.

</dd> <dt>

*pSrcFile* \[in\]
</dt> <dd>

Type: **[**LPCTSTR**](winprog.windows_data_types)**

Pointer to a string that specifies the filename. If the compiler settings require Unicode, the data type LPCTSTR resolves to LPCWSTR. Otherwise, the string data type resolves to LPCSTR. See Remarks.

</dd> <dt>

*pSrcInfo* \[in\]
</dt> <dd>

Type: **[**D3DXIMAGE\_INFO**](d3dximage-info.md)\***

Pointer to a [**D3DXIMAGE\_INFO**](d3dximage-info.md) structure to be filled with the description of the data in the source file.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be the following: D3DERR\_INVALIDCALL

## Remarks

The compiler setting also determines the function version. If Unicode is defined, the function call resolves to D3DXGetImageInfoFromResourceW. Otherwise, the function call resolves to D3DXGetImageInfoFromResourceA because ANSI strings are being used.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9tex.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>  |



## See also

<dl> <dt>

[Texture Functions in D3DX 9](dx9-graphics-reference-d3dx-functions-texture.md)
</dt> <dt>

[**D3DXGetImageInfoFromFile**](d3dxgetimageinfofromfile.md)
</dt> <dt>

[**D3DXGetImageInfoFromFileInMemory**](d3dxgetimageinfofromfileinmemory.md)
</dt> </dl>

 

 




