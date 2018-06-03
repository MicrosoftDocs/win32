---
title: Support CreateResultSnippet method
description: Creates a result snippet.
ms.assetid: 9ADB730A-6584-429A-BB56-127186953387
keywords:
- CreateResultSnippet method Access Execution Engine
- CreateResultSnippet method Access Execution Engine , Support interface
- Support interface Access Execution Engine , CreateResultSnippet method
topic_type:
- apiref
api_name:
- Support.CreateResultSnippet
api_location:
- AxeCore.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Support::CreateResultSnippet method

Creates a result snippet.

## Syntax


```C++
virtual HRESULT CreateResultSnippet(
  [out] ResultSnippet **resultsFile
) = 0;
```



## Parameters

<dl> <dt>

*resultsFile* \[out\]
</dt> <dd>

A double pointer to receive the new results snippet.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Support**](support.md)
</dt> </dl>

 

 





