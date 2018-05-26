---
title: Activity SetTraceToolTip method
description: Sets the trace tooltip of the Activity.
ms.assetid: DCFB5EE1-F8DB-47CD-B66A-4C6590DF607B
keywords:
- SetTraceToolTip method Access Execution Engine
- SetTraceToolTip method Access Execution Engine , Activity interface
- Activity interface Access Execution Engine , SetTraceToolTip method
topic_type:
- apiref
api_name:
- Activity.SetTraceToolTip
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

# Activity::SetTraceToolTip method

Sets the trace tooltip of the **Activity**.

## Syntax


```C++
virtual HRESULT SetTraceToolTip(
  [in] LPCWSTR traceTooltip
) = 0;
```



## Parameters

<dl> <dt>

*traceTooltip* \[in\]
</dt> <dd>

The trace tooltip.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

**Activity** objects hold data from **Iteration/Activities/Activity** elements.

The trace tooltip is the value of element **Activity/Trace/Description/ToolTip**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Activity**](activity-struct.md)
</dt> </dl>

 

 





