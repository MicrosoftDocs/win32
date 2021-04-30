---
title: RegistrationInfo.Version property
description: For scripting, gets or sets the version number of the task.
ms.assetid: '5f200948-b4ff-495c-9578-2a93b34fd75b'
keywords:
- Version property Task Scheduler
- Version property Task Scheduler , RegistrationInfo object
- RegistrationInfo object Task Scheduler , Version property
topic_type:
- apiref
api_name:
- RegistrationInfo.Version
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# RegistrationInfo.Version property

For scripting, gets or sets the version number of the task.

## Syntax


```VB
RegistrationInfo.Version As String
```



## Property value

The version number of the task.

## Remarks

When reading or writing XML for a task, the version number of the task is specified using the [**Version**](taskschedulerschema-version-registrationinfotype-element.md) element of the Task Scheduler schema.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





