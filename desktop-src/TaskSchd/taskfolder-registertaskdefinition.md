---
title: TaskFolder.RegisterTaskDefinition method
description: For scripting, registers (creates) a task in a specified location using the TaskDefinition object to define a task.
ms.assetid: '198c8848-c89d-4883-b111-4ac0b009b7b3'
keywords:
- RegisterTaskDefinition method Task Scheduler
- RegisterTaskDefinition method Task Scheduler , TaskFolder object
- TaskFolder object Task Scheduler , RegisterTaskDefinition method
topic_type:
- apiref
api_name:
- TaskFolder.RegisterTaskDefinition
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# TaskFolder.RegisterTaskDefinition method

For scripting, registers (creates) a task in a specified location using the [**TaskDefinition**](taskdefinition.md) object to define a task.

## Syntax


```VB
TaskFolder.RegisterTaskDefinition( _
  ByVal path, _
  ByVal definition, _
  ByVal flags, _
  ByVal userId, _
  ByVal password, _
  ByVal logonType, _
  [ ByVal sddl ], _
  ByRef task _
)
```



## Parameters

<dl> <dt>

*path* \[in\]
</dt> <dd>

The name of the task. If this value is **Nothing**, the task will be registered in the root task folder and the task name will be a GUID value that is created by the Task Scheduler service.

A task name cannot begin or end with a space character. The '.' character cannot be used to specify the current task folder and the '..' characters cannot be used to specify the parent task folder in the path.

</dd> <dt>

*definition* \[in\]
</dt> <dd>

The definition of the task that is registered.

</dd> <dt>

*flags* \[in\]
</dt> <dd>

A [**TASK\_CREATION**](/windows/desktop/api/taskschd/ne-taskschd-task_creation) constant.



| Value                                                                                                                                                                                                                                                                                 | Meaning                                                                                                                                                                                                                                                                                                                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TASK_VALIDATE_ONLY"></span><span id="task_validate_only"></span><dl> <dt>**TASK\_VALIDATE\_ONLY**</dt> <dt>0x1</dt> </dl>                                                | The Task Scheduler checks the syntax of the XML that describes the task but does not register the task. This constant cannot be combined with the **TASK\_CREATE**, **TASK\_UPDATE**, or **TASK\_CREATE\_OR\_UPDATE** values.<br/>                                                                                                                            |
| <span id="TASK_CREATE"></span><span id="task_create"></span><dl> <dt>**TASK\_CREATE**</dt> <dt>0x2</dt> </dl>                                                                      | The Task Scheduler registers the task as a new task.<br/>                                                                                                                                                                                                                                                                                                     |
| <span id="TASK_UPDATE"></span><span id="task_update"></span><dl> <dt>**TASK\_UPDATE**</dt> <dt>0x4</dt> </dl>                                                                      | The Task Scheduler registers the task as an updated version of an existing task. When a task with a registration trigger is updated, the task will execute after the update occurs.<br/>                                                                                                                                                                      |
| <span id="TASK_CREATE_OR_UPDATE"></span><span id="task_create_or_update"></span><dl> <dt>**TASK\_CREATE\_OR\_UPDATE**</dt> <dt>0x6</dt> </dl>                                      | The Task Scheduler either registers the task as a new task or as an updated version if the task already exists. Equivalent to TASK\_CREATE \| TASK\_UPDATE.<br/>                                                                                                                                                                                              |
| <span id="TASK_DISABLE"></span><span id="task_disable"></span><dl> <dt>**TASK\_DISABLE**</dt> <dt>0x8</dt> </dl>                                                                   | The Task Scheduler disables the existing task.<br/>                                                                                                                                                                                                                                                                                                           |
| <span id="TASK_DONT_ADD_PRINCIPAL_ACE"></span><span id="task_dont_add_principal_ace"></span><dl> <dt>**TASK\_DONT\_ADD\_PRINCIPAL\_ACE**</dt> <dt>0x10</dt> </dl>                  | The Task Scheduler is prevented from adding the allow access-control entry (ACE) for the context principal. When the **TaskFolder.RegisterTaskDefinition** function is called with this flag to update a task, the Task Scheduler service does not add the ACE for the new context principal and does not remove the ACE from the old context principal.<br/> |
| <span id="TASK_IGNORE_REGISTRATION_TRIGGERS"></span><span id="task_ignore_registration_triggers"></span><dl> <dt>**TASK\_IGNORE\_REGISTRATION\_TRIGGERS**</dt> <dt>0x20</dt> </dl> | The Task Scheduler creates the task, but ignores the registration triggers in the task. By ignoring the registration triggers, the task will not execute when it is registered unless a time-based trigger causes it to execute on registration.<br/>                                                                                                         |



 

</dd> <dt>

*userId* \[in\]
</dt> <dd>

The user credentials that are used to register the task. If present, these credentials take priority over the credentials specified in the task definition object pointed to by the *definition* parameter.

> [!Note]  
> If the task is defined as a Task Scheduler 1.0 task, then do not use a group name (rather than a specific user name) in this userId parameter. A task is defined as a Task Scheduler 1.0 task when the [**Compatibility**](tasksettings-compatibility.md) property is set to 1 in the task's settings.

 

</dd> <dt>

*password* \[in\]
</dt> <dd>

The password for the userId that is used to register the task. When the TASK\_LOGON\_SERVICE\_ACCOUNT logon type is used, the password must be an empty **VARIANT** value such as **VT\_NULL** or **VT\_EMPTY**.

</dd> <dt>

*logonType* \[in\]
</dt> <dd>

Defines what logon technique is used to run the registered task.



| Value                                                                                                                                                                                                                                                                                                     | Meaning                                                                                                                                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TASK_LOGON_NONE"></span><span id="task_logon_none"></span><dl> <dt>**TASK\_LOGON\_NONE**</dt> <dt>0</dt> </dl>                                                                               | The logon method is not specified. Used for non-NT credentials. <br/>                                                                                                                                                                                                                           |
| <span id="TASK_LOGON_PASSWORD"></span><span id="task_logon_password"></span><dl> <dt>**TASK\_LOGON\_PASSWORD**</dt> <dt>1</dt> </dl>                                                                   | Use a password for logging on the user. The password must be supplied at registration time.<br/>                                                                                                                                                                                                |
| <span id="TASK_LOGON_S4U"></span><span id="task_logon_s4u"></span><dl> <dt>**TASK\_LOGON\_S4U**</dt> <dt>2</dt> </dl>                                                                                  | Use an existing interactive token to run a task. The user must log on using a service for user (S4U) logon. When an S4U logon is used, no password is stored by the system and there is no access to either the network or to encrypted files.<br/>                                             |
| <span id="TASK_LOGON_INTERACTIVE_TOKEN"></span><span id="task_logon_interactive_token"></span><dl> <dt>**TASK\_LOGON\_INTERACTIVE\_TOKEN**</dt> <dt>3</dt> </dl>                                       | User must already be logged on. The task will be run only in an existing interactive session.<br/>                                                                                                                                                                                              |
| <span id="TASK_LOGON_GROUP"></span><span id="task_logon_group"></span><dl> <dt>**TASK\_LOGON\_GROUP**</dt> <dt>4</dt> </dl>                                                                            | Group activation. The **groupId** field specifies the group.<br/>                                                                                                                                                                                                                               |
| <span id="TASK_LOGON_SERVICE_ACCOUNT"></span><span id="task_logon_service_account"></span><dl> <dt>**TASK\_LOGON\_SERVICE\_ACCOUNT**</dt> <dt>5</dt> </dl>                                             | Indicates that a Local System, Local Service, or Network Service account is being used as a security context to run the task.<br/>                                                                                                                                                              |
| <span id="TASK_LOGON_INTERACTIVE_TOKEN_OR_PASSWORD"></span><span id="task_logon_interactive_token_or_password"></span><dl> <dt>**TASK\_LOGON\_INTERACTIVE\_TOKEN\_OR\_PASSWORD**</dt> <dt>6</dt> </dl> | First use the interactive token. If the user is not logged on (no interactive token is available), then the password is used. The password must be specified when a task is registered. This flag is not recommended for new tasks because it is less reliable than TASK\_LOGON\_PASSWORD.<br/> |



 

</dd> <dt>

*sddl* \[in, optional\]
</dt> <dd>

The security descriptor that is associated with the registered task. You can specify the access control list (ACL) in the security descriptor for a task in order to allow or deny certain users and groups access to a task.

> [!Note]  
> If the Local System account is denied access to a task, then the Task Scheduler service can produce unexpected results.

 

</dd> <dt>

*task* \[out\]
</dt> <dd>

A [**RegisteredTask**](registeredtask.md) object that represents the new task.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

For a task, that contains a message box action, the message box will be displayed if the task is activated and the task has an interactive logon type. To set the task logon type to interactive, specify 3 (**TASK\_LOGON\_INTERACTIVE\_TOKEN**) or 4 (**TASK\_LOGON\_GROUP**) in the [**LogonType**](principal-logontype.md) property of the task principal, or in the *logonType* parameter of [**TaskFolder.RegisterTask**](taskfolder-registertask.md) or **TaskFolder.RegisterTaskDefinition**.

Only a member of the Administrators group can create a task with a boot trigger.

You can successfully register a task with a group specified in the *userId* parameter and 3 (**TASK\_LOGON\_INTERACTIVE\_TOKEN**) specified in the *logonType* parameter of [**TaskFolder.RegisterTask**](taskfolder-registertask.md) or **TaskFolder.RegisterTaskDefinition**, but the task will not run.

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

[**RegisteredTask**](registeredtask.md)
</dt> <dt>

[**TaskFolder**](taskfolder.md)
</dt> </dl>

 

 





