---
title: D3DReadFileToBlob function
description: Reads a file that is on disk into memory.
ms.assetid: 7CFB1BA6-7C36-4BDB-9705-781CCC2E7DB2
keywords:
- D3DReadFileToBlob function HLSL
topic_type:
- apiref
api_name:
- D3DReadFileToBlob
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

# D3DReadFileToBlob function

> [!Note]  
> You can use this API to develop your Windows Store apps, but you can't use it in apps that you submit to the Windows Store.

 

Reads a file that is on disk into memory.

## Syntax

``` syntax
HRESULT WINAPI D3DReadFileToBlob(
  in  LPCWSTR pFileName,
  out ID3DBlob ppContents
);
```

## Parameters

<dl> <dt>

*pFileName* \[in\]
</dt> <dd>

A pointer to a constant null-terminated string that contains the name of the file to read into memory.

</dd> <dt>

*ppContents* \[out\]
</dt> <dd>

A pointer to a variable that receives a pointer to the [**ID3DBlob**](https://msdn.microsoft.com/library/windows/desktop/ff728743) interface that contains information that **D3DReadFileToBlob** read from the *pFileName* file. You can use this **ID3DBlob** interface to access the file information and pass it to other compiler functions.

</dd> </dl>

## Return value

Returns one of the [Direct3D 11 return codes](https://msdn.microsoft.com/library/windows/desktop/ff476174).

## Remarks

> [!Note]  
> The D3dcompiler\_44.dll or later version of the file contains the **D3DReadFileToBlob** compiler function.

 

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

 

 





