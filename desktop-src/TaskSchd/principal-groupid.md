---
title: Principal.GroupId property
description: For scripting, gets or sets the identifier of the user group that is required to run the tasks that are associated with the principal.
ms.assetid: 'df4bffa3-ee38-49cd-bec7-28edda48a953'
keywords: ["GroupId property Task Scheduler", "GroupId property Task Scheduler , Principal object", "Principal object Task Scheduler , GroupId property"]
topic_type:
- apiref
api_name:
- Principal.GroupId
api_location:
- taskschd.dll
api_type:
- COM
---

# Principal.GroupId property

For scripting, gets or sets the identifier of the user group that is required to run the tasks that are associated with the principal.

## Syntax


```VB
Principal.GroupId As String
```



## Property value

The identifier of the user group that is associated with this principal.

## Remarks

Do not set this property if a user identifier is specified in the [**UserId**](principal-userid.md) property.

When reading or writing XML for a task, the group identifier for a principal is specified in the [**GroupId**](taskschedulerschema-groupid-principaltype-element.md) element of the Task Scheduler schema.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[**UserId**](principal-userid.md)
</dt> <dt>

[**Principal**](principal.md)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





