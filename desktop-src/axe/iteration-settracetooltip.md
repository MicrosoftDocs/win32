---
title: Iteration SetTraceToolTip method
description: Sets the trace tooltip for the Iteration.
ms.assetid: 'D7F7D77D-6DB4-40BC-97F5-783EA86B9957'
keywords: ["SetTraceToolTip method Access Execution Engine", "SetTraceToolTip method Access Execution Engine , Iteration interface", "Iteration interface Access Execution Engine , SetTraceToolTip method"]
topic_type:
- apiref
api_name:
- Iteration.SetTraceToolTip
api_location:
- AxeCore.dll
api_type:
- COM
---

# Iteration::SetTraceToolTip method

Sets the trace tooltip for the **Iteration**.

## Syntax


```C++
virtual HRESULT SetTraceToolTip(
  [in] LPCWSTR traceToolTip
) = 0;
```



## Parameters

<dl> <dt>

*traceToolTip* \[in\]
</dt> <dd>

The trace tooltip.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

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

 

 





