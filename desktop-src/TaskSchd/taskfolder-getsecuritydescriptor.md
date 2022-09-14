---
title: TaskFolder.GetSecurityDescriptor property
description: For scripting, gets the security descriptor for the folder.
ms.assetid: 'ebf8dc7f-32b7-45bf-9ee5-36df674a1530'
keywords:
- GetSecurityDescriptor property Task Scheduler
- GetSecurityDescriptor property Task Scheduler , TaskFolder object
- TaskFolder object Task Scheduler , GetSecurityDescriptor property
topic_type:
- apiref
api_name:
- TaskFolder.GetSecurityDescriptor
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# TaskFolder.GetSecurityDescriptor property

For scripting, gets the security descriptor for the folder.

## Syntax


```VB
TaskFolder.GetSecurityDescriptor( _
  ByVal securityInformation, _
  ByRef pSddl _
)
```



## Property value

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[**TaskFolder.SetSecurityDescriptor**](taskfolder-setsecuritydescriptor.md)
</dt> <dt>

[**RegisteredTask.SetSecurityDescriptor**](registeredtask-setsecuritydescriptor.md)
</dt> </dl>

 

 





