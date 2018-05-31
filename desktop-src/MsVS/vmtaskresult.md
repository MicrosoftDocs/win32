---
title: VMTaskResult enumeration
description: The VMTaskResult enumeration specifies the result of a task.
ms.assetid: 62fa0a34-cb9b-4c61-ad42-8e41ee5a503b
keywords:
- VMTaskResult enumeration Virtual Server
topic_type:
- apiref
api_name:
- VMTaskResult
api_location:
- VsComInterfaces.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# VMTaskResult enumeration

The **VMTaskResult** enumeration specifies the result of a task.

## Syntax


```C++
typedef enum  { 
  vmTaskResult_Success                      = 0,
  vmTaskResult_Cancelled                    = 1,
  vmTaskResult_UnexpectedError              = 2,
  vmTaskResult_OutOfMemoryError             = 3,
  vmTaskResult_DiskRelatedError             = 4,
  vmTaskResult_IncompatibleSavedStateError  = 5,
  vmTaskResult_TimeOutError                 = 6,
  vmTaskResult_IllegalValueError            = 7,
  vmTaskResult_ThreadCrashError             = 8
} VMTaskResult;
```



## Constants

<dl> <dt>

<span id="vmTaskResult_Success"></span><span id="vmtaskresult_success"></span><span id="VMTASKRESULT_SUCCESS"></span>**vmTaskResult\_Success**
</dt> <dd>

The task completed normally.

</dd> <dt>

<span id="vmTaskResult_Cancelled"></span><span id="vmtaskresult_cancelled"></span><span id="VMTASKRESULT_CANCELLED"></span>**vmTaskResult\_Cancelled**
</dt> <dd>

The task was canceled.

</dd> <dt>

<span id="vmTaskResult_UnexpectedError"></span><span id="vmtaskresult_unexpectederror"></span><span id="VMTASKRESULT_UNEXPECTEDERROR"></span>**vmTaskResult\_UnexpectedError**
</dt> <dd>

The task aborted due to an unexpected error.

</dd> <dt>

<span id="vmTaskResult_OutOfMemoryError"></span><span id="vmtaskresult_outofmemoryerror"></span><span id="VMTASKRESULT_OUTOFMEMORYERROR"></span>**vmTaskResult\_OutOfMemoryError**
</dt> <dd>

The task aborted because there was insufficient memory to complete the task.

</dd> <dt>

<span id="vmTaskResult_DiskRelatedError"></span><span id="vmtaskresult_diskrelatederror"></span><span id="VMTASKRESULT_DISKRELATEDERROR"></span>**vmTaskResult\_DiskRelatedError**
</dt> <dd>

The task aborted because a disk write error occurred (insufficient disk space or other write error).

</dd> <dt>

<span id="vmTaskResult_IncompatibleSavedStateError"></span><span id="vmtaskresult_incompatiblesavedstateerror"></span><span id="VMTASKRESULT_INCOMPATIBLESAVEDSTATEERROR"></span>**vmTaskResult\_IncompatibleSavedStateError**
</dt> <dd>

The task aborted because the virtual machine could not restore (the saved state was incompatible).

</dd> <dt>

<span id="vmTaskResult_TimeOutError"></span><span id="vmtaskresult_timeouterror"></span><span id="VMTASKRESULT_TIMEOUTERROR"></span>**vmTaskResult\_TimeOutError**
</dt> <dd>

The task aborted because the timeout specified had expired.

</dd> <dt>

<span id="vmTaskResult_IllegalValueError"></span><span id="vmtaskresult_illegalvalueerror"></span><span id="VMTASKRESULT_ILLEGALVALUEERROR"></span>**vmTaskResult\_IllegalValueError**
</dt> <dd>

The task aborted because an illegal preference value was read while the task was processing.

</dd> <dt>

<span id="vmTaskResult_ThreadCrashError"></span><span id="vmtaskresult_threadcrasherror"></span><span id="VMTASKRESULT_THREADCRASHERROR"></span>**vmTaskResult\_ThreadCrashError**
</dt> <dd>

The task aborted because a thread associated with the task crashed.

</dd> </dl>

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



 

 





