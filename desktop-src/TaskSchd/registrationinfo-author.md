---
title: RegistrationInfo.Author property
description: For scripting, gets or sets the author of the task.
ms.assetid: 'ba355a3b-cda3-4d4f-8504-f77f3d9eb21a'
keywords:
- Author property Task Scheduler
- Author property Task Scheduler , RegistrationInfo object
- RegistrationInfo object Task Scheduler , Author property
topic_type:
- apiref
api_name:
- RegistrationInfo.Author
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# RegistrationInfo.Author property

For scripting, gets or sets the author of the task.

## Syntax


```VB
RegistrationInfo.Author As String
```



## Property value

The author of the task.

## Remarks

When reading or writing XML for a task, the task author is specified using the [**Author**](taskschedulerschema-author-registrationinfotype-element.md) element of the Task Scheduler schema.

When setting this property value, the value can be text that is retrieved from a resource .dll file. A specialized string is used to reference the text from the resource file. The format of the string is $(@ \[Dll\], \[ResourceID\]) where \[Dll\] is the path to the .dll file that contains the resource and \[ResourceID\] is the identifier for the resource text. For example, the setting this property value to $(@ %SystemRoot%\\System32\\ResourceName.dll, -101) will set the property to the value of the resource text with an identifier equal to -101 in the %SystemRoot%\\System32\\ResourceName.dll file.

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

 

 





