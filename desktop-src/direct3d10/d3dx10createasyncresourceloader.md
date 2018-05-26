---
Description: Create an asynchronous-resource loader.
ms.assetid: 1b3eb21c-4ba6-4910-b2f0-2ffa4ae50e47
title: D3DX10CreateAsyncResourceLoader function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DX10CreateAsyncResourceLoader function

Create an asynchronous-resource loader.

## Syntax


```C++
HRESULT D3DX10CreateAsyncResourceLoader(
  _In_  HMODULE           hSrcModule,
  _In_  LPCTSTR           pSrcResource,
  _Out_ ID3DX10DataLoader **ppDataLoader
);
```



## Parameters

<dl> <dt>

*hSrcModule* \[in\]
</dt> <dd>

Type: **[**HMODULE**](winprog.windows_data_types)**

Handle to the resource module. Use [GetModuleHandle Function](http://msdn.microsoft.com/en-us/library/ms683199.aspx) to get the handle.

</dd> <dt>

*pSrcResource* \[in\]
</dt> <dd>

Type: **[**LPCTSTR**](winprog.windows_data_types)**

Name of the resource in hSrcModule. If the compiler settings require Unicode, the data type LPCTSTR resolves to LPCWSTR. Otherwise, the data type resolves to LPCSTR.

</dd> <dt>

*ppDataLoader* \[out\]
</dt> <dd>

Type: **[**ID3DX10DataLoader**](id3dx10dataloader.md)\*\***

The address of a pointer to the asynchronous-data processor (see [**ID3DX10DataProcessor Interface**](id3dx10dataprocessor.md)).

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The return value is one of the values listed in [Direct3D 10 Return Codes](d3d10-graphics-reference-returnvalues.md).

## Requirements



|                   |                                                                                          |
|-------------------|------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3DX10Async.h</dt> </dl> |



## See also

<dl> <dt>

[General Purpose Functions](d3d10-graphics-reference-d3dx10-functions-general-purpose.md)
</dt> </dl>

 

 




