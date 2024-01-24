---
title: Principal.LogonType property
description: For scripting, gets or sets the security logon method that is required to run the tasks that are associated with the principal.
ms.assetid: 'ac6fd7a1-00ef-4478-920f-de391a5a2c8c'
keywords:
- LogonType property Task Scheduler
- LogonType property Task Scheduler , Principal object
- Principal object Task Scheduler , LogonType property
topic_type:
- apiref
api_name:
- Principal.LogonType
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Principal.LogonType property

For scripting, gets or sets the security logon method that is required to run the tasks that are associated with the principal.

## Syntax


```VB
Principal.LogonType As Integer
```



## Property value

Set to one of the following [**TASK\_LOGON TYPE**](/windows/desktop/api/taskschd/ne-taskschd-task_logon_type) enumeration constants.



| Value                                                                                                                                                                                                                                                                                                     | Meaning                                                                                                                                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TASK_LOGON_NONE"></span><span id="task_logon_none"></span><dl> <dt>**TASK\_LOGON\_NONE**</dt> <dt>0</dt> </dl>                                                                               | The logon method is not specified. Used for non-NT credentials. <br/>                                                                                                                                                                                                                           |
| <span id="TASK_LOGON_PASSWORD"></span><span id="task_logon_password"></span><dl> <dt>**TASK\_LOGON\_PASSWORD**</dt> <dt>1</dt> </dl>                                                                   | Use a password for logging on the user. The password must be supplied at registration time.<br/>                                                                                                                                                                                                |
| <span id="TASK_LOGON_S4U"></span><span id="task_logon_s4u"></span><dl> <dt>**TASK\_LOGON\_S4U**</dt> <dt>2</dt> </dl>                                                                                  | Use an existing interactive token to run a task. The user must log on using a service for user (S4U) logon. When an S4U logon is used, no password is stored by the system and there is no access to either the network or encrypted files.<br/>                                                |
| <span id="TASK_LOGON_INTERACTIVE_TOKEN"></span><span id="task_logon_interactive_token"></span><dl> <dt>**TASK\_LOGON\_INTERACTIVE\_TOKEN**</dt> <dt>3</dt> </dl>                                       | User must already be logged on. The task will be run only in an existing interactive session.<br/>                                                                                                                                                                                              |
| <span id="TASK_LOGON_GROUP"></span><span id="task_logon_group"></span><dl> <dt>**TASK\_LOGON\_GROUP**</dt> <dt>4</dt> </dl>                                                                            | Group activation. The userId field specifies the group.<br/>                                                                                                                                                                                                                                    |
| <span id="TASK_LOGON_SERVICE_ACCOUNT"></span><span id="task_logon_service_account"></span><dl> <dt>**TASK\_LOGON\_SERVICE\_ACCOUNT**</dt> <dt>5</dt> </dl>                                             | Indicates that a Local System, Local Service, or Network Service account is being used as a security context to run the task.<br/>                                                                                                                                                              |
| <span id="TASK_LOGON_INTERACTIVE_TOKEN_OR_PASSWORD"></span><span id="task_logon_interactive_token_or_password"></span><dl> <dt>**TASK\_LOGON\_INTERACTIVE\_TOKEN\_OR\_PASSWORD**</dt> <dt>6</dt> </dl> | First use the interactive token. If the user is not logged on (no interactive token is available), then the password is used. The password must be specified when a task is registered. This flag is not recommended for new tasks because it is less reliable than TASK\_LOGON\_PASSWORD.<br/> |



 

## Remarks

This property is valid only when a user identifier is specified by the [**UserId**](principal-userid.md) property.

When reading or writing XML for a task, the logon type is specified in the [**&lt;LogonType&gt;**](taskschedulerschema-logontype-principaltype-element.md) element of the Task Scheduler schema.

For a task, that contains a message box action, the message box will be displayed if the task is activated and the task has an interactive logon type. To set the task logon type to interactive, specify 3 (**TASK\_LOGON\_INTERACTIVE\_TOKEN**) or 4 (**TASK\_LOGON\_GROUP**) in the **LogonType** property of the task principal, or in the *logonType* parameter of [**TaskFolder.RegisterTask**](taskfolder-registertask.md) or [**TaskFolder.RegisterTaskDefinition**](taskfolder-registertaskdefinition.md).

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

 

 





