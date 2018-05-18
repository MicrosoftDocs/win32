---
title: Activity SetTraceLink method
description: Sets the trace link of the Activity.
ms.assetid: '2B628DCC-ED2C-48DB-9DB3-F6EAE4FCC4C0'
keywords: ["SetTraceLink method Access Execution Engine", "SetTraceLink method Access Execution Engine , Activity interface", "Activity interface Access Execution Engine , SetTraceLink method"]
topic_type:
- apiref
api_name:
- Activity.SetTraceLink
api_location:
- AxeCore.dll
api_type:
- COM
---

# Activity::SetTraceLink method

Sets the trace link of the **Activity**.

## Syntax


```C++
virtual HRESULT SetTraceLink(
  [in] LPCWSTR traceLink
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

 

 





