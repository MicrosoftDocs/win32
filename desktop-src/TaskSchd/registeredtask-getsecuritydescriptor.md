---
title: RegisteredTask.GetSecurityDescriptor method
description: For scripting, gets the security descriptor that is used as credentials for the registered task.
ms.assetid: 474d62a5-9ec7-40f7-b26e-54923f8ebe1e
keywords:
- GetSecurityDescriptor method Task Scheduler
- GetSecurityDescriptor method Task Scheduler , RegisteredTask object
- RegisteredTask object Task Scheduler , GetSecurityDescriptor method
topic_type:
- apiref
api_name:
- RegisteredTask.GetSecurityDescriptor
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

# RegisteredTask.GetSecurityDescriptor method

For scripting, gets the security descriptor that is used as credentials for the registered task.

## Syntax


```VB
sddl = .GetSecurityDescriptor( _
  ByVal securityInformation _
)
```



## Parameters

<dl> <dt>

*securityInformation* 
</dt> <dd>

The security information from [**SECURITY\_INFORMATION**](https://msdn.microsoft.com/library/windows/desktop/aa379573).

</dd> </dl>

## Return value

The security descriptor for the registered task.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[**RegisteredTask**](registeredtask.md)
</dt> <dt>

[**TaskFolder.GetSecurityDescriptor**](taskfolder-getsecuritydescriptor.md)
</dt> <dt>

[**RegisteredTask.SetSecurityDescriptor**](registeredtask-setsecuritydescriptor.md)
</dt> </dl>

 

 





