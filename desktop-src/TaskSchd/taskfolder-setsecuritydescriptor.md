---
title: TaskFolder.SetSecurityDescriptor property
description: For scripting, sets the security descriptor for the folder.
ms.assetid: 54f8a37b-87ac-449c-8e03-aeacd27e8c97
keywords:
- SetSecurityDescriptor property Task Scheduler
- SetSecurityDescriptor property Task Scheduler , TaskFolder object
- TaskFolder object Task Scheduler , SetSecurityDescriptor property
topic_type:
- apiref
api_name:
- TaskFolder.SetSecurityDescriptor
api_location:
- taskschd.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# TaskFolder.SetSecurityDescriptor property

For scripting, sets the security descriptor for the folder.

## Syntax


```VB
TaskFolder.SetSecurityDescriptor( _
  ByVal sddl, _
  ByVal flags _
)
```



## Property value

## Remarks

You can specify the access control list (ACL) in the security descriptor for a task folder in order to allow or deny certain users and groups access to a task folder.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[**RegisteredTask.SetSecurityDescriptor**](registeredtask-setsecuritydescriptor.md)
</dt> <dt>

[**TaskFolder.GetSecurityDescriptor**](taskfolder-getsecuritydescriptor.md)
</dt> </dl>

 

 





