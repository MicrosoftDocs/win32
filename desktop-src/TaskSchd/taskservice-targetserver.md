---
title: TaskService.TargetServer property
description: For scripting, gets the name of the computer that is running the Task Scheduler service that the user is connected to.
ms.assetid: '8b0edf18-2a79-46f2-9b90-2c4726db881e'
keywords:
- TargetServer property Task Scheduler
- TargetServer property Task Scheduler , TaskService object
- TaskService object Task Scheduler , TargetServer property
topic_type:
- apiref
api_name:
- TaskService.TargetServer
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# TaskService.TargetServer property

For scripting, gets the name of the computer that is running the Task Scheduler service that the user is connected to.

## Syntax


```VB
TaskService.TargetServer As String
```



## Property value

The name of the computer that is running the Task Scheduler service that the user is connected to.

## Remarks

This property returns an empty string when the user passes an IP address, Localhost, or '.' as a parameter, and it returns the name of the computer that is running the Task Scheduler service when the user does not pass any parameter value.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



 

 





