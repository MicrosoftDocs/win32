---
title: Engine RemovePendingRebootJob method
description: Removes an abandoned task that restarts job execution upon a system restart so that other jobs can be executed.
ms.assetid: b91ad602-1e5c-4469-9ee4-29bee2d7ba03
keywords:
- RemovePendingRebootJob method Access Execution Engine
- RemovePendingRebootJob method Access Execution Engine , Engine interface
- Engine interface Access Execution Engine , RemovePendingRebootJob method
topic_type:
- apiref
api_name:
- Engine.RemovePendingRebootJob
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

# Engine::RemovePendingRebootJob method

Removes an abandoned task that restarts job execution upon a system restart so that other jobs can be executed.

## Syntax


```C++
virtual HRESULT RemovePendingRebootJob() = 0;
```



## Parameters

This method has no parameters.

## Return value

If successful, the method returns **S\_OK**.

If an internal error occurs the method returns **AXE\_E\_INTERNAL\_ERROR**. See the log files for information on the exact failure.

If a job is running, the method returns **AXE\_E\_JOB\_RUNNING**. The pending reboot registration cannot be removed while a job is running.

If the job was not terminated, the method returns **AXE\_E\_TERMINATE\_FAILED**.

## Remarks

Managed code uses the [**Engine.RemovePendingRebootJob \| removePendingRebootJob**](https://www.bing.com/search?q=**Engine.RemovePendingRebootJob \| removePendingRebootJob**) method

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Engine**](engine-if.md)
</dt> <dt>

[**ExecuteJob**](engine-executejob.md)
</dt> <dt>

[**JobExecutionInfo**](jobexecutioninfo.md)
</dt> </dl>

 

 





