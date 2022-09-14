---
title: RegistrationInfo.SecurityDescriptor property
description: For scripting, gets or sets the security descriptor of the task.
ms.assetid: 'e03607f0-c2a0-4aa1-a2b0-915b03aae968'
keywords:
- SecurityDescriptor property Task Scheduler
- SecurityDescriptor property Task Scheduler , RegistrationInfo object
- RegistrationInfo object Task Scheduler , SecurityDescriptor property
topic_type:
- apiref
api_name:
- RegistrationInfo.SecurityDescriptor
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# RegistrationInfo.SecurityDescriptor property

For scripting, gets or sets the security descriptor of the task. If a different security descriptor is supplied during task registration, it will supersede the security descriptor set with this property.

## Syntax


```VB
RegistrationInfo.SecurityDescriptor As String
```



## Property value

The security descriptor that is associated with the task.

## Remarks

When reading or writing XML for a task, the security descriptor of the task is specified using the [**SecurityDescriptor**](taskschedulerschema-securitydescriptor-registrationinfotype-element.md) element of the Task Scheduler schema.

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

 

 





