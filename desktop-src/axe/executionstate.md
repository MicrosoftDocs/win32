---
title: ExecutionState enumeration
description: Represents the current state of a job or assessment execution.
ms.assetid: 13F91205-35F0-40CE-9C4D-ACCD05F02260
keywords:
- ExecutionState enumeration Access Execution Engine
topic_type:
- apiref
api_name:
- ExecutionState
api_location:
- AxeHosting.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# ExecutionState enumeration

Represents the current state of a job or assessment execution.

## Syntax


```C++
enum ExecutionState {
  None       = 0, 
  NotYetRun  = 1, 
  Running    = 2, 
  Completed  = 3 

};
```



## Constants

<dl> <dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None**
</dt> <dd>

No state is specified. This is an invalid state.

</dd> <dt>

<span id="NotYetRun"></span><span id="notyetrun"></span><span id="NOTYETRUN"></span>**NotYetRun**
</dt> <dd>

The *OnJobBegin* callback for the job or *OnAssessmentBegin* callback for the assessment has not yet been called.

</dd> <dt>

<span id="Running"></span><span id="running"></span><span id="RUNNING"></span>**Running**
</dt> <dd>

The job or assessment has been started. The corresponding *OnJobBegin* or *OnAssessmentBegin* callback has been called, but the *OnJobEnd* or *OnAssessmentEnd* callback has not been called yet.

</dd> <dt>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>**Completed**
</dt> <dd>

The job or assessment has been completed. The *OnJobEnd* or *OnAssessmentEnd* callback for the object has been called.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |



## See also

<dl> <dt>

[**GetStatus**](https://msdn.microsoft.com/library/windows/desktop/hh707403)
</dt> </dl>

 

 





