---
title: RegistrationInfo.Date property
description: For scripting, gets or sets the date and time when the task is registered.
ms.assetid: 'b9a41413-954f-447c-8fce-f99c81fec40a'
keywords: ["Date property Task Scheduler", "Date property Task Scheduler , RegistrationInfo object", "RegistrationInfo object Task Scheduler , Date property"]
topic_type:
- apiref
api_name:
- RegistrationInfo.Date
api_location:
- taskschd.dll
api_type:
- COM
---

# RegistrationInfo.Date property

For scripting, gets or sets the date and time when the task is registered.

## Syntax


```VB
RegistrationInfo.Date As String
```



## Property value

The registration date of the task.

## Remarks

When reading or writing XML for a task, the registration date is specified using the [**Date**](taskschedulerschema-date-registrationinfotype-element.md) element of the Task Scheduler schema.

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

 

 





