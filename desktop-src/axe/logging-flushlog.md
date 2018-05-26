---
title: Logging FlushLog method
description: Commits all accumulated log messages to disk.
ms.assetid: ce9009ee-92dc-4f56-9283-85a1f6afdb9e
keywords:
- FlushLog method Access Execution Engine
- FlushLog method Access Execution Engine , Logging interface
- Logging interface Access Execution Engine , FlushLog method
topic_type:
- apiref
api_name:
- Logging.FlushLog
api_location:
- AxeCore.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Logging::FlushLog method

Commits all accumulated log messages to disk.

## Syntax


```C++
virtual HRESULT FlushLog() = 0;
```



## Parameters

This method has no parameters.

## Return value

If the function succeeds, the return is **S\_OK**.

## Remarks

Axe s ETW session stores log messages in a circular buffer in memory. When the buffer gets full, the log messages are committed to disk. This method forces the buffers to be committed to disk so that the information is not lost.

This method should only be called in situations where there is danger of data being lost due to a loss of power or an unsuccessful shutdown.

Managed code uses the [**Logging.FlushLog**](axe-logging_flushlog_om) method.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>AxeCore.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl> |



## See also

<dl> <dt>

[**Logging**](logging.md)
</dt> </dl>

 

 





