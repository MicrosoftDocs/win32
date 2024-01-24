---
title: TaskService.HighestVersion property
description: For scripting, indicates the highest version of Task Scheduler that a computer supports.
ms.assetid: 'b4e55e46-6f33-4224-811b-06bf218dd1ac'
keywords:
- HighestVersion property Task Scheduler
- HighestVersion property Task Scheduler , TaskService object
- TaskService object Task Scheduler , HighestVersion property
topic_type:
- apiref
api_name:
- TaskService.HighestVersion
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# TaskService.HighestVersion property

For scripting, indicates the highest version of Task Scheduler that a computer supports.

## Syntax


```VB
TaskService.HighestVersion As Integer
```



## Property value

The highest version of Task Scheduler that a computer supports. The highest version is a value that is split into MajorVersion/MinorVersion on the 16-bit boundary. The Task Scheduler service returns 1 for the major version and 2 for the minor version. Use the [CLng](/previous-versions//ck4c5842(v=vs.85)) function to get the integer value of the property.

## Examples

The following code shows how to use the [CLng](/previous-versions//ck4c5842(v=vs.85)) function to get the value of the **HighestVersion** property.


```VB
wscript.echo service.HighestVersion
Test = clng( service.HighestVersion )
If Test <> 65538  Then
    wscript.echo "Fail"

Else
    wscript.echo "Pass"
End If
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



 

