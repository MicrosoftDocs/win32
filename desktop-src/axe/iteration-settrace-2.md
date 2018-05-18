---
title: Iteration SetTrace method
description: Sets values for the Trace object of the Iteration.
ms.assetid: 'FC7A9EA5-B698-479C-A037-30A62A6070ED'
keywords: ["SetTrace method Access Execution Engine", "SetTrace method Access Execution Engine , Iteration interface", "Iteration interface Access Execution Engine , SetTrace method"]
topic_type:
- apiref
api_name:
- Iteration.SetTrace
api_location:
- AxeCore.dll
api_type:
- COM
---

# Iteration::SetTrace method

Sets values for the [**Trace**](trace-struct.md) object of the **Iteration**.

## Syntax


```C++
virtual HRESULT SetTrace(
  [in]            LPCWSTR traceFile,
  [in, optional]  LPCWSTR traceLink,
  [in, optional]  LPCWSTR traceName,
  [in, optional]  LPCWSTR traceTooltip,
  [out, optional] Trace   **trace
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

*traceName* \[in, optional\]
</dt> <dd>

The trace name.

</dd> <dt>

*traceTooltip* \[in, optional\]
</dt> <dd>

The trace tooltip.

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

The trace name is the value of element **Iteration/Trace/Description/Name**.

The trace tooltip is the value of element **Iteration/Trace/Description/ToolTip**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Iteration**](iteration-struct.md)
</dt> </dl>

 

 





