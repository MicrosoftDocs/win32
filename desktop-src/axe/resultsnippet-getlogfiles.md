---
title: ResultSnippet GetLogFiles method
description: Returns a LogFileCollection object that contains the log files for this ResultSnippet.
ms.assetid: 818CE536-1B0E-423F-B834-8A1FFF4C72E6
keywords:
- GetLogFiles method Access Execution Engine
- GetLogFiles method Access Execution Engine , ResultSnippet interface
- ResultSnippet interface Access Execution Engine , GetLogFiles method
topic_type:
- apiref
api_name:
- ResultSnippet.GetLogFiles
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

# ResultSnippet::GetLogFiles method

Returns a [**LogFileCollection**](logfilecollection.md) object that contains the log files for this [**ResultSnippet**](resultsnippet.md).

## Syntax


```C++
virtual HRESULT GetLogFiles(
  [out] LogFileCollection **logfiles
) = 0;
```



## Parameters

<dl> <dt>

*logfiles* \[out\]
</dt> <dd>

The [**LogFileCollection**](logfilecollection.md) object that this method returns.

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

 

 





