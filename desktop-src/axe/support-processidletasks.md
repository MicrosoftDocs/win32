---
title: Support ProcessIdleTasks method
description: Requests the system run the maintenance tasks scheduled to run when the system is idle. This prevents the maintenance tasks from running during the assessment.
ms.assetid: 890BBC71-38CC-49B4-8A29-A585592D09A0
keywords:
- ProcessIdleTasks method Access Execution Engine
- ProcessIdleTasks method Access Execution Engine , Support interface
- Support interface Access Execution Engine , ProcessIdleTasks method
topic_type:
- apiref
api_name:
- Support.ProcessIdleTasks
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

# Support::ProcessIdleTasks method

Requests the system run the maintenance tasks scheduled to run when the system is idle. This prevents the maintenance tasks from running during the assessment.

## Syntax


```C++
virtual HRESULT ProcessIdleTasks(
  [out] HANDLE *idleTasksHandle
) const = 0;
```



## Parameters

<dl> <dt>

*idleTasksHandle* \[out\]
</dt> <dd>

The handle to the idle tasks.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

This method enables an assessment to request that the operating system to perform maintenance tasks usually run when the system is idle. Maintenance tasks such as disk defragmentation can take extremely long times, and running them beforehand is less likely to interfere with the assessment.

Managed code uses the [**Support.ProcessIdleTasks**](axe-support_processidletasks_om) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Support**](support.md)
</dt> </dl>

 

 





