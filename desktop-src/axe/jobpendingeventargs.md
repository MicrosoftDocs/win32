---
title: JobPendingEventArgs structure
description: This structure defines the event arguments that are passed to an IJobPendingEventHandler OnJobPending event.
ms.assetid: 5D90F0B3-8F2D-4769-93D4-35C54871E250
keywords:
- JobPendingEventArgs structure Access Execution Engine
topic_type:
- apiref
api_name:
- JobPendingEventArgs
api_location:
- AxeHosting.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# JobPendingEventArgs structure

This structure defines the event arguments that are passed to an IJobPendingEventHandler::OnJobPending event.

## Syntax


```C++
struct JobPendingEventArgs {
  DWORD     Size;
  const Job *Job;
  DWORD     Timeout;
};
```



## Members

<dl> <dt>

**Size**
</dt> <dd>

The number of bytes in the structure. Used to detect different versions of structure. This is set to sizeof( JobPendingEventArgs ) by the AXE engine.

</dd> <dt>

**Job**
</dt> <dd>

A pointer to the Job object that has been queued for execution. The Job object is owned by the AXE engine and should not be deleted.

</dd> <dt>

**Timeout**
</dt> <dd>

The amount of time the engine will wait for a job running within another engine to finish.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |



 

 





