---
title: Principal.RunLevel property
description: For scripting, gets or sets the identifier that is used to specify the privilege level that is required to run the tasks that are associated with the principal.
ms.assetid: '2ec3d93e-9eef-4590-842c-edfc9232bcdf'
keywords:
- RunLevel property Task Scheduler
- RunLevel property Task Scheduler , Principal object
- Principal object Task Scheduler , RunLevel property
topic_type:
- apiref
api_name:
- Principal.RunLevel
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Principal.RunLevel property

For scripting, gets or sets the identifier that is used to specify the privilege level that is required to run the tasks that are associated with the principal.

This property is read/write.

## Syntax


```VB
Principal.RunLevel As Integer
```



## Property value

The identifier that is used to specify the privilege level that is required to run the tasks that are associated with the principal.



| Value                                                                                                                                                                                                                                         | Meaning                                                       |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| <span id="TASK_RUNLEVEL_LUA"></span><span id="task_runlevel_lua"></span><dl> <dt>**TASK\_RUNLEVEL\_LUA**</dt> <dt>0</dt> </dl>             | Tasks will be run with the least privileges (LUA).<br/> |
| <span id="TASK_RUNLEVEL_HIGHEST"></span><span id="task_runlevel_highest"></span><dl> <dt>**TASK\_RUNLEVEL\_HIGHEST**</dt> <dt>1</dt> </dl> | Tasks will be run with the highest privileges.<br/>     |



 

## Remarks

If a task is registered using the Builtin\\Administrator account or the Local System or Local Service accounts, then the **RunLevel** property will be ignored. The property value will also be ignored if User Account Control (UAC) is turned off.

If a task is registered using the Administrators group for the security context of the task, then you must also set the [**RunLevel**](/windows/desktop/api/taskschd/nf-taskschd-iprincipal-get_runlevel) property to **TASK\_RUNLEVEL\_HIGHEST** if you want to run the task. For more information, see [Security Contexts for Tasks](security-contexts-for-running-tasks.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[**Principal**](principal.md)
</dt> </dl>

 

 





