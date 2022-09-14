---
title: Principal.DisplayName property
description: For scripting, gets or sets the name of the principal..
ms.assetid: '73caf263-f597-4bea-ae89-32f9919d7a70'
keywords:
- DisplayName property Task Scheduler
- DisplayName property Task Scheduler , Principal object
- Principal object Task Scheduler , DisplayName property
topic_type:
- apiref
api_name:
- Principal.DisplayName
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Principal.DisplayName property

For scripting, gets or sets the name of the principal..

## Syntax


```VB
Principal.DisplayName As String
```



## Property value

The name of the principal.

## Remarks

When reading or writing XML for a task, the display name for a principal is specified in the [**DisplayName**](taskschedulerschema-displayname-principaltype-element.md) element of the Task Scheduler schema.

When setting this property value, the value can be text that is retrieved from a resource .dll file. A specialized string is used to reference the text from the resource file. The format of the string is $(@ \[Dll\], \[ResourceID\]) where \[Dll\] is the path to the .dll file that contains the resource and \[ResourceID\] is the identifier for the resource text. For example, setting this property value to $(@ %SystemRoot%\\System32\\ResourceName.dll, -101) will set the property to the value of the resource text with an identifier equal to -101 in the %SystemRoot%\\System32\\ResourceName.dll file.

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
</dt> <dt>

[**Principal**](principal.md)
</dt> </dl>

 

 





