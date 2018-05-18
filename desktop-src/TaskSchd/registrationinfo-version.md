---
title: RegistrationInfo.Version property
description: For scripting, gets or sets the version number of the task.
ms.assetid: 'e2305dbd-bb81-4854-86bd-d0c4f3cf78a1'
keywords: ["Version property Task Scheduler", "Version property Task Scheduler , RegistrationInfo object", "RegistrationInfo object Task Scheduler , Version property"]
topic_type:
- apiref
api_name:
- RegistrationInfo.Version
api_location:
- taskschd.dll
api_type:
- COM
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



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





