---
title: Iteration SetTraceLink method
description: Sets the trace link for the Iteration.
ms.assetid: 75C9F225-DB22-42F3-83CE-5F4B9B79E691
keywords:
- SetTraceLink method Access Execution Engine
- SetTraceLink method Access Execution Engine , Iteration interface
- Iteration interface Access Execution Engine , SetTraceLink method
topic_type:
- apiref
api_name:
- Iteration.SetTraceLink
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

# Iteration::SetTraceLink method

Sets the trace link for the **Iteration**.

## Syntax


```C++
virtual HRESULT SetTraceLink(
  [in] LPCWSTR traceLink
) = 0;
```



## Parameters

<dl> <dt>

*traceLink* \[in\]
</dt> <dd>

The trace link.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The trace link is the value of element **Iteration/Trace/Link**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Iteration**](iteration-struct.md)
</dt> </dl>

 

 





