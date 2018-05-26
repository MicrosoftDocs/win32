---
title: Iteration GetTraceFile method
description: Returns the trace file name for the Iteration.
ms.assetid: 3B02B3D7-ABFF-4720-872E-6C71BA022086
keywords:
- GetTraceFile method Access Execution Engine
- GetTraceFile method Access Execution Engine , Iteration interface
- Iteration interface Access Execution Engine , GetTraceFile method
topic_type:
- apiref
api_name:
- Iteration.GetTraceFile
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

# Iteration::GetTraceFile method

Returns the trace file name for the **Iteration**.

## Syntax


```C++
virtual HRESULT GetTraceFile(
  [out] LPCWSTR *traceFile
) const = 0;
```



## Parameters

<dl> <dt>

*traceFile* \[out\]
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

 

 





