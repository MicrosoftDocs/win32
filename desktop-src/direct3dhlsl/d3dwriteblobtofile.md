---
title: D3DWriteBlobToFile function
description: Writes a memory blob to a file on disk.
ms.assetid: F21FF3B4-5F69-4C93-9F93-6A12324A664A
keywords:
- D3DWriteBlobToFile function HLSL
topic_type:
- apiref
api_name:
- D3DWriteBlobToFile
api_location:
- D3DCompiler_47.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D3DWriteBlobToFile function

> [!Note]  
> You can use this API to develop your Windows Store apps, but you can't use it in apps that you submit to the Windows Store.

 

Writes a memory blob to a file on disk.

## Syntax

``` syntax
HRESULT WINAPI D3DWriteBlobToFile(
  in ID3DBlob pBlob,
  in LPCWSTR pFileName,
  in BOOL bOverwrite
);
```

## Parameters

<dl> <dt>

*pBlob* \[in\]
</dt> <dd>

Type: **[**ID3DBlob**](https://msdn.microsoft.com/library/windows/desktop/ff728743)\***

A pointer to a [**ID3DBlob**](https://msdn.microsoft.com/library/windows/desktop/ff728743) interface that contains the memory blob to write to the file that the *pFileName* parameter specifies.

</dd> <dt>

*pFileName* \[in\]
</dt> <dd>

Type: **LPCWSTR**

A pointer to a constant null-terminated string that contains the name of the file to which to write.

</dd> <dt>

*bOverwrite* \[in\]
</dt> <dd>

Type: **[**BOOL**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

A Boolean value that specifies whether to overwrite information in the *pFileName* file. TRUE specifies to overwrite information and FALSE specifies not to overwrite information.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/windows/desktop/aa383751#hresult)**

Returns one of the [Direct3D 11 return codes](https://msdn.microsoft.com/library/windows/desktop/ff476174).

## Remarks

> [!Note]  
> The D3dcompiler\_44.dll or later version of the file contains the **D3DWriteBlobToFile** compiler function.

 

## Requirements



|                    |                                                                                                |
|--------------------|------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3Dcompiler.h</dt> </dl>       |
| Library<br/> | <dl> <dt>D3DCompiler.lib</dt> </dl>     |
| DLL<br/>     | <dl> <dt>D3DCompiler\_47.dll</dt> </dl> |



## See also

<dl> <dt>

[Functions](dx-graphics-d3dcompiler-reference-functions.md)
</dt> </dl>

 

 





