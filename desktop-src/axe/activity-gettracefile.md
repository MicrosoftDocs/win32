---
title: Activity GetTraceFile method
description: Returns the trace file name of the Activity.
ms.assetid: 21EC2A78-CF2E-4547-8B37-1DB5CC58EC46
keywords:
- GetTraceFile method Access Execution Engine
- GetTraceFile method Access Execution Engine , Activity interface
- Activity interface Access Execution Engine , GetTraceFile method
topic_type:
- apiref
api_name:
- Activity.GetTraceFile
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

# Activity::GetTraceFile method

Returns the trace file name of the **Activity**.

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

 

 





