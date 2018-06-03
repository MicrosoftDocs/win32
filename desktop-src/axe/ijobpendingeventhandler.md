---
title: IJobPendingEventHandler class
description: The IJobPendingEventHandler interface enables a solution to receive notification from the AXE engine when a job is blocked by another currently running job.
ms.assetid: 706B43B6-A429-4398-84E4-E5FA5513AFEF
keywords:
- IJobPendingEventHandler class Access Execution Engine
- IJobPendingEventHandler class Access Execution Engine , described
topic_type:
- apiref
api_name:
- IJobPendingEventHandler
api_location:
- AxeCore.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IJobPendingEventHandler class

The **IJobPendingEventHandler** interface enables a solution to receive notification from the AXE engine when a job is blocked by another currently running job.

## When to implement

An **IJobPendingEventHandler** interface should be implemented by a solution that might attempt to run multiple jobs simultaneously. An interface should be implemented even if each job is controlled by separate instances of the same solution application.

**IJobPendingEventHandler** has these types of members:

-   [Methods](#methods)

### Methods

The **IJobPendingEventHandler** class has these methods.



| Method                                                       | Description                                                                                                 |
|:-------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------|
| [**OnJobPending**](ijobpendingeventhandler-onjobpending.md) | The AXE Core raises this event when the job is blocked because another job is currently running.<br/> |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Execution Solution Interfaces**](execution-solution-interfaces.md)
</dt> </dl>

 

 





