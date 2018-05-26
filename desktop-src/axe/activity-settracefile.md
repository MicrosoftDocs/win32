---
title: Activity SetTraceFile method
description: Sets the trace file name of the Activity.
ms.assetid: 312A1D5D-FD2D-47A0-9CD2-076FC707B924
keywords:
- SetTraceFile method Access Execution Engine
- SetTraceFile method Access Execution Engine , Activity interface
- Activity interface Access Execution Engine , SetTraceFile method
topic_type:
- apiref
api_name:
- Activity.SetTraceFile
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

# Activity::SetTraceFile method

Sets the trace file name of the **Activity**.

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

**Activity** objects hold data from **Iteration/Activities/Activity** elements.

The trace file name is the value of element **Activity/Trace/File**.

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

 

 





