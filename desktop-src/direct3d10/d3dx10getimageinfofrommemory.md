---
Description: Get information about an image already loaded into memory.
ms.assetid: 6750116a-ad4f-4102-aba9-6ef32c367be4
title: D3DX10GetImageInfoFromMemory function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DX10GetImageInfoFromMemory function

Get information about an image already loaded into memory.

## Syntax


```C++
HRESULT D3DX10GetImageInfoFromMemory(
  _In_  LPCVOID           pSrcData,
  _In_  SIZE_T            SrcDataSize,
  _In_  ID3DX10ThreadPump *pPump,
  _In_  D3DX10_IMAGE_INFO *pSrcInfo,
  _Out_ HRESULT           *pHResult
);
```



## Parameters

<dl> <dt>

*pSrcData* \[in\]
</dt> <dd>

Type: **[**LPCVOID**](winprog.windows_data_types)**

Pointer to the image in memory.

</dd> <dt>

*SrcDataSize* \[in\]
</dt> <dd>

Type: **[**SIZE\_T**](winprog.windows_data_types)**

Size of the image in memory, in bytes.

</dd> <dt>

*pPump* \[in\]
</dt> <dd>

Type: **[**ID3DX10ThreadPump**](id3dx10threadpump.md)\***

Optional thread pump that can be used to load the info asynchronously. Can be **NULL**. See [**ID3DX10ThreadPump**](id3dx10threadpump.md).

</dd> <dt>

*pSrcInfo* \[in\]
</dt> <dd>

Type: **[**D3DX10\_IMAGE\_INFO**](d3dx10-image-info.md)\***

Information about the image in memory.

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
</dt> </dl>

 

 




