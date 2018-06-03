---
title: ResultSnippet AddLogFile method
description: Adds a log file to this ResultSnippet.
ms.assetid: 12C8F0E9-07DA-4EA8-8A11-2274E84B53B4
keywords:
- AddLogFile method Access Execution Engine
- AddLogFile method Access Execution Engine , ResultSnippet interface
- ResultSnippet interface Access Execution Engine , AddLogFile method
topic_type:
- apiref
api_name:
- ResultSnippet.AddLogFile
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

# ResultSnippet::AddLogFile method

Adds a log file to this [**ResultSnippet**](resultsnippet.md).

## Syntax


```C++
virtual HRESULT AddLogFile(
  [in] LPCWSTR filePath
) = 0;
```



## Parameters

<dl> <dt>

*filePath* \[in\]
</dt> <dd>

The file path of the log file to add.

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

[**ResultSnippet**](resultsnippet.md)
</dt> </dl>

 

 





