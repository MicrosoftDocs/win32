---
title: Activity GetTraceLink method
description: Returns the trace link of the Activity.
ms.assetid: '2BBF6382-514E-4F04-AA2A-C62C7C824F05'
keywords: ["GetTraceLink method Access Execution Engine", "GetTraceLink method Access Execution Engine , Activity interface", "Activity interface Access Execution Engine , GetTraceLink method"]
topic_type:
- apiref
api_name:
- Activity.GetTraceLink
api_location:
- AxeCore.dll
api_type:
- COM
---

# Activity::GetTraceLink method

Returns the trace link of the **Activity**.

## Syntax


```C++
virtual HRESULT GetTraceLink(
  [out] LPCWSTR *traceLink
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

**Activity** objects hold data from **Iteration/Activities/Activity** elements.

The trace link is the value of element **Activity/Trace/Link**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Activity**](activity-struct.md)
</dt> </dl>

 

 





