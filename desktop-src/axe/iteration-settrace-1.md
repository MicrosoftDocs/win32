---
title: Iteration SetTrace method
description: Sets values for the Trace object of the Iteration.
ms.assetid: AD8A6FC0-3029-4006-9817-967E30B50C3F
keywords:
- SetTrace method Access Execution Engine
- SetTrace method Access Execution Engine , Iteration interface
- Iteration interface Access Execution Engine , SetTrace method
topic_type:
- apiref
api_name:
- Iteration.SetTrace
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

# Iteration::SetTrace method

Sets values for the [**Trace**](trace-struct.md) object of the **Iteration**.

## Syntax


```C++
virtual HRESULT SetTrace(
  [in]            LPCWSTR traceFile,
  [in, optional]  LPCWSTR traceLink,
  [out, optional] Trace   **trace
) = 0;
```



## Parameters

<dl> <dt>

*traceFile* \[in\]
</dt> <dd>

The trace file name.

</dd> <dt>

*traceLink* \[in, optional\]
</dt> <dd>

The trace link.

</dd> <dt>

*trace* \[out, optional\]
</dt> <dd>

The **Trace** object.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **Trace** object holds information from element **Iteration/Trace**.

The trace file name is the value of element **Iteration/Trace/File**.

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

 

 





