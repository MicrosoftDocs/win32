---
title: Iteration GetTraceLink method
description: Returns the trace link for the Iteration.
ms.assetid: F17E5DBF-3208-40EE-B5DA-311D63588783
keywords:
- GetTraceLink method Access Execution Engine
- GetTraceLink method Access Execution Engine , Iteration interface
- Iteration interface Access Execution Engine , GetTraceLink method
topic_type:
- apiref
api_name:
- Iteration.GetTraceLink
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

# Iteration::GetTraceLink method

Returns the trace link for the **Iteration**.

## Syntax


```C++
virtual HRESULT GetTraceLink(
  [out] LPCWSTR *traceLink
) const = 0;
```



## Parameters

<dl> <dt>

*traceLink* \[out\]
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

 

 





