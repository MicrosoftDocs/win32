---
title: Iteration SetTraceFile method
description: Sets the trace file name for the Iteration.
ms.assetid: A0D475E0-615A-48FB-B058-94B5D9386878
keywords:
- SetTraceFile method Access Execution Engine
- SetTraceFile method Access Execution Engine , Iteration interface
- Iteration interface Access Execution Engine , SetTraceFile method
topic_type:
- apiref
api_name:
- Iteration.SetTraceFile
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

# Iteration::SetTraceFile method

Sets the trace file name for the **Iteration**.

## Syntax


```C++
virtual HRESULT SetTraceFile(
  [in] LPCWSTR traceFile
) = 0;
```



## Parameters

<dl> <dt>

*traceFile* \[in\]
</dt> <dd>

The trace file name.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The trace file name is the value of element **Iteration/Trace/File**.

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

 

 





