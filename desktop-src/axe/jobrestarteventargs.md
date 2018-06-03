---
title: JobRestartEventArgs structure
description: This structure defines the event arguments that are passed to an IJobRestartEventHandler OnJobRestart event.
ms.assetid: C5A2C3E1-F91E-4339-859C-423915F8CDBF
keywords:
- JobRestartEventArgs structure Access Execution Engine
topic_type:
- apiref
api_name:
- JobRestartEventArgs
api_location:
- AxeHosting.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# JobRestartEventArgs structure

This structure defines the event arguments that are passed to an IJobRestartEventHandler::OnJobRestart event.

## Syntax


```C++
struct JobRestartEventArgs {
  DWORD     Size;
  const Job *Job;
};
```



## Members

<dl> <dt>

**Size**
</dt> <dd>

The number of bytes in the structure. Used to detect different versions of structure.

</dd> <dt>

**Job**
</dt> <dd>

A pointer to the Job object that has been queued for execution. The Job object is owned by the AXE engine and should not be deleted.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |



 

 





