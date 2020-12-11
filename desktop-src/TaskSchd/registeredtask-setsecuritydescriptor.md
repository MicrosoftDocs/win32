---
title: RegisteredTask.SetSecurityDescriptor method
description: For scripting, sets the security descriptor that is used as credentials for the registered task.
ms.assetid: '2dc10df0-5827-4199-940e-865a03a694f5'
keywords:
- SetSecurityDescriptor method Task Scheduler
- SetSecurityDescriptor method Task Scheduler , RegisteredTask object
- RegisteredTask object Task Scheduler , SetSecurityDescriptor method
topic_type:
- apiref
api_name:
- RegisteredTask.SetSecurityDescriptor
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# RegisteredTask.SetSecurityDescriptor method

For scripting, sets the security descriptor that is used as credentials for the registered task.

## Syntax


```VB
RegisteredTask.SetSecurityDescriptor( _
  ByVal sddl, _
  ByVal flags _
)
```



## Parameters

<dl> <dt>

*sddl* \[in\]
</dt> <dd>

The security descriptor that is used as credentials for the registered task.

> [!Note]  
> If the Local System account is denied access to a task, then the Task Scheduler service can produce unexpected results.

 

</dd> <dt>

*flags* \[in\]
</dt> <dd>

Flags that specify how to set the security descriptor. The TASK\_DONT\_ADD\_PRINCIPAL\_ACE flag (0x10) from the [**TASK\_CREATION**](/windows/desktop/api/taskschd/ne-taskschd-task_creation) enumeration can be specified.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

You can specify the access control list (ACL) in the security descriptor for a task in order to allow or deny certain users and groups access to a task.

## Requirements



| Requirement | Value |
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

 

 





