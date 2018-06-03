---
title: RegistrationInfo.Documentation property
description: For scripting, gets or sets any additional documentation for the task.
ms.assetid: ec12b0aa-def4-4ff3-b067-62f989c890d5
keywords:
- Documentation property Task Scheduler
- Documentation property Task Scheduler , RegistrationInfo object
- RegistrationInfo object Task Scheduler , Documentation property
topic_type:
- apiref
api_name:
- RegistrationInfo.Documentation
api_location:
- taskschd.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RegistrationInfo.Documentation property

For scripting, gets or sets any additional documentation for the task.

## Syntax


```VB
RegistrationInfo.Documentation As String
```



## Property value

Any additional documentation that is associated with the task.

## Remarks

When reading or writing XML for a task, the additional documentation for the task is specified using the [**Documentation**](taskschedulerschema-documentation-registrationinfotype-element.md) element of the Task Scheduler schema.

When setting this property value, the value can be text that is retrieved from a resource .dll file. A specialized string is used to reference the text from the resource file. The format of the string is $(@ \[Dll\], \[ResourceID\]) where \[Dll\] is the path to the .dll file that contains the resource and \[ResourceID\] is the identifier for the resource text. For example, the setting this property value to $(@ %SystemRoot%\\System32\\ResourceName.dll, -101) will set the property to the value of the resource text with an identifier equal to -101 in the %SystemRoot%\\System32\\ResourceName.dll file.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





