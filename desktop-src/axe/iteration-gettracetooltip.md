---
title: Iteration GetTraceToolTip method
description: Returns the trace tooltip for the Iteration.
ms.assetid: 'D2463665-C2EB-4731-B742-EA4BCBA44CB8'
keywords: ["GetTraceToolTip method Access Execution Engine", "GetTraceToolTip method Access Execution Engine , Iteration interface", "Iteration interface Access Execution Engine , GetTraceToolTip method"]
topic_type:
- apiref
api_name:
- Iteration.GetTraceToolTip
api_location:
- AxeCore.dll
api_type:
- COM
---

# Iteration::GetTraceToolTip method

Returns the trace tooltip for the **Iteration**.

## Syntax


```C++
virtual HRESULT GetTraceToolTip(
  [out] const LPCWSTR *traceToolTip
) = 0;
```



## Parameters

<dl> <dt>

*traceToolTip* \[out\]
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

 

 





