---
title: Activity SetTrace method
description: Sets Trace settings of the Activity.
ms.assetid: B3E4BBA4-142B-4B3A-B4DA-A64A911B33DC
keywords:
- SetTrace method Access Execution Engine
- SetTrace method Access Execution Engine , Activity interface
- Activity interface Access Execution Engine , SetTrace method
topic_type:
- apiref
api_name:
- Activity.SetTrace
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

# Activity::SetTrace method

Sets [**Trace**](trace-struct.md) settings of the **Activity**.

## Syntax


```C++
virtual HRESULT SetTrace(
  [in]            LPCWSTR traceFile,
  [in, optional]  LPCWSTR traceLink,
  [in, optional]  LPCWSTR traceName,
  [in, optional]  LPCWSTR traceTooltip,
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

The **Trace** that this method sets.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

**Activity** objects hold data from **Iteration/Activities/Activity** elements.

The **Trace** holds values from element **Activity/Trace**.

The trace file name is the value of element **Activity/Trace/File**.

The trace link is the value of element **Activity/Trace/Link**.

The trace name is the value of element **Activity/Trace/Description/Name**.

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

 

 





