---
title: Security Contexts for Tasks
description: Tasks are registered and run under a specific security context.
ms.assetid: be86eb9f-f6ec-4dce-afe8-e3314a74062a
ms.topic: article
ms.date: 05/31/2018
---

# Security Contexts for Tasks

Tasks are registered and run under a specific security context. Users can create applications that successfully register, update, delete, or run tasks, but the user must supply the correct credentials when a task is registered and the application must be running in a process with the correct privileges.

## Specifying Credentials

You can specify the security context for a task by specifying credentials in the [**ITaskFolder::RegisterTask**](/windows/desktop/api/taskschd/nf-taskschd-itaskfolder-registertask) or [**ITaskFolder::RegisterTaskDefinition**](/windows/desktop/api/taskschd/nf-taskschd-itaskfolder-registertaskdefinition) ([**TaskFolder.RegisterTask**](taskfolder-registertask.md) or [**TaskFolder.RegisterTaskDefinition**](taskfolder-registertaskdefinition.md) for scripting) methods or by assigning a principal to the [**Principal Property of ITaskDefinition**](/windows/desktop/api/taskschd/nf-taskschd-itaskdefinition-get_principal) ([**TaskDefinition.Principal**](taskdefinition-principal.md) for scripting). If a principal is created for a task definition, and then the task definition is registered using the **RegisterTaskDefinition** method with different credentials specified in the method parameters, then the credentials specified in the **RegisterTaskDefinition** method will overwrite the credentials in the principal. If a principal is created for a task definition using XML, and then the XML for the task is registered using the **RegisterTask** method with different credentials specified in the method parameters, then the credentials specified in the **RegisterTask** method will overwrite the credentials in the principal.

You specify a user account or group when registering a task or specifying the principle for a task. The security context of the user account or group is used for the security context of the task. In these methods and properties, you also define the logon type. The logon type is defined by one of the constants in the [**TASK\_LOGON\_TYPE**](/windows/desktop/api/taskschd/ne-taskschd-task_logon_type) enumeration.

Tasks registered with the TASK\_LOGON\_PASSWORD or TASK\_LOGON\_S4U flag will only launch if the specified user has the Logon as Batch privilege enabled. Administrators and Backup Operators group users have this privilege enabled by default.

When you call the [**ITaskService::Connect**](/windows/desktop/api/taskschd/nf-taskschd-itaskservice-connect) ([**TaskService.Connect**](taskservice-connect.md) for scripting) method, any subsequent method calls to the Task Scheduler service will use the credentials that were passed to the **Connect** method. This is important to consider when registering tasks with an interactive logon type. When you register a task with the logon type equal to TASK\_LOGON\_INTERACTIVE\_TOKEN and the task does not have credentials specified in the [**Principal**](/windows/desktop/api/taskschd/nf-taskschd-itaskdefinition-get_principal) property of the task definition, specified in the parameters to [**RegisterTaskDefinition**](/windows/desktop/api/taskschd/nf-taskschd-itaskfolder-registertaskdefinition), or specified in the XML that is passed to [**RegisterTask**](/windows/desktop/api/taskschd/nf-taskschd-itaskfolder-registertask), then the task will be registered with the credentials of the user that called the **Connect** method.

## User Account Control (UAC) Security for Tasks

[User Account Control](https://www.microsoft.com/technet/windowsvista/security/uac.mspx) (UAC) lets users exercise general functionality such as running programs and saving and modifying data without exposing administrative privileges. By default, a task runs with low level privileges when UAC is turned on. Tasks can specify that they will run with elevated privileges or low privileges by setting a privilege level from the [**TASK\_RUNLEVEL\_TYPE**](/windows/win32/api/taskschd/ne-taskschd-task_runlevel_type) enumeration for the [**RunLevel property of IPrincipal**](/windows/desktop/api/taskschd/nf-taskschd-iprincipal-get_runlevel) ([**Principal.RunLevel**](principal-runlevel.md) for scripting). The value of the **RunLevel** property determines the privilege level at which a task's actions will be run. If a task's actions must have elevated privileges to run, then you must set the **RunLevel** property to **TASK\_RUNLEVEL\_HIGHEST**. If a task is registered using the Administrators group for the security context of the task, then you must also set the **RunLevel** property to **TASK\_RUNLEVEL\_HIGHEST** if you want to run the task. If a task is registered using the Builtin\\Administrator account or the Local System or Local Service accounts, then the **RunLevel** property will be ignored. The property value will also be ignored if User Account Control (UAC) is turned off. The value of the **RunLevel** property doesn't affect the permissions needed to run or delete a task.

> [!Note]  
> After upgrading an operating system from Windows XP to Windows Vista, tasks that were registered using the Builtin\\Administrator account on Windows XP will have the [**RunLevel**](/windows/desktop/api/taskschd/nf-taskschd-iprincipal-get_runlevel) property set to **TASK\_RUNLEVEL\_LUA**. This might cause some tasks to fail. You can update this property manually to ensure all the tasks will run.

 

From a low privilege process, you cannot register a task with the [**RunLevel**](/windows/desktop/api/taskschd/nf-taskschd-iprincipal-get_runlevel) property equal to **TASK\_RUNLEVEL\_HIGHEST**, but you can register a task with the **RunLevel** property equal to **TASK\_RUNLEVEL\_LUA**. The task actions will be run with low privileges. You are not allowed to register the task as Builtin/Administrator, Local System, or for a group.

From an elevated privilege process, you can register a task with the [**RunLevel**](/windows/desktop/api/taskschd/nf-taskschd-iprincipal-get_runlevel) property equal to **TASK\_RUNLEVEL\_HIGHEST** or **TASK\_RUNLEVEL\_LUA**. The task will be run with a privilege level decided by the **RunLevel** property unless you are using the Administrator account, in which case the task is run with elevated privileges.

From an elevated process, you can register a Task Scheduler 1.0 task. The Task Scheduler service will set the run level of the task to TASK\_RUNLEVEL\_HIGHEST and the task will run with elevated privileges.

From an low privilege process, you can also register a Task Scheduler 1.0 task. The Task Scheduler service will set the run level of the task to TASK\_RUNLEVEL\_LUA, and the task will run with low privileges. If this task is updated from an elevated process, the run level of the task will remain TASK\_RUNLEVEL\_LUA.

## Security for Registering Tasks

When you register a task from an account that is a member of the Administrators group, then you only need to specify a password while registering the task in the following situations:

-   If you register the task to run under the security context of your account or a different user's account and you use the TASK\_LOGON\_PASSWORD flag in the [**RegisterTask**](/windows/desktop/api/taskschd/nf-taskschd-itaskfolder-registertask) or [**RegisterTaskDefinition**](/windows/desktop/api/taskschd/nf-taskschd-itaskfolder-registertaskdefinition) method.
-   If you register the task to run under the security context of a different user's account and you use the TASK\_LOGON\_S4U flag in the [**RegisterTask**](/windows/desktop/api/taskschd/nf-taskschd-itaskfolder-registertask) or [**RegisterTaskDefinition**](/windows/desktop/api/taskschd/nf-taskschd-itaskfolder-registertaskdefinition) method.

You cannot use a user group as the security context of a task when you register the task using the TASK\_LOGON\_S4U flag or the TASK\_LOGON\_PASSWORD flag in the [**RegisterTask**](/windows/desktop/api/taskschd/nf-taskschd-itaskfolder-registertask) or [**RegisterTaskDefinition**](/windows/desktop/api/taskschd/nf-taskschd-itaskfolder-registertaskdefinition) method.

When you register a task from a user account that is not a member of the Administrators group, then you do not need to specify a password when registering the task if you register the task to run under the security context of your account and you use the S4U or interactive logon type. Otherwise, you need to specify a password when registering the task. Also, you cannot register the task using the Local Service account or by using a group for the task's security context.

## Security for Reading, Updating, Deleting, and Running Tasks

By default, a user who creates a task can read, update, delete, and run the task. A user must have file write permission on a task file to update a task, file read permission on a task file to read a task, delete permission on a task file to delete a task, and file execute permission on a task to run a task using the [**IRegisteredTask::Run**](/windows/desktop/api/taskschd/nf-taskschd-iregisteredtask-run) or [**RunEx**](/windows/desktop/api/taskschd/nf-taskschd-iregisteredtask-runex) methods ([**RegisteredTask.Run**](registeredtask-run.md) and [**RunEx**](registeredtask-runex.md) for scripting). Members of the Administrators group or the SYSTEM account can read, update, delete, and run any tasks. Members of the Users group, the LocalService account, and the NetworkService account can only read, update, delete, and run the tasks that they have created. This default behavior is changed when the DACL of the task file is changed, in which case the DACL defines which users have file write, read, execute, and delete permission. To set permissions for a task file, use the IRegisteredTask.SetSecurityDescriptor method (RegisteredTask.SetSecurityDescriptor for scripting) or set the security descriptor when you register the task using the [**RegisterTask**](/windows/desktop/api/taskschd/nf-taskschd-itaskfolder-registertask) or [**RegisterTaskDefinition**](/windows/desktop/api/taskschd/nf-taskschd-itaskfolder-registertaskdefinition) methods.

A user must have WriteDAC permission in addition to the read/write permissions to update a task if the task update requires a change to the DACL for the task.

## Related topics

<dl> <dt>

[Task Registration Information](task-registration-information.md)
</dt> <dt>

[About The Task Scheduler](about-the-task-scheduler.md)
</dt> <dt>

[Task Security Hardening](task-security-hardening.md)
</dt> <dt>

[**TaskFolder.RegisterTaskDefinition**](taskfolder-registertaskdefinition.md)
</dt> <dt>

[**ITaskFolder::RegisterTaskDefinition**](/windows/desktop/api/taskschd/nf-taskschd-itaskfolder-registertaskdefinition)
</dt> <dt>

[**Principal Property of ITaskDefinition**](/windows/desktop/api/taskschd/nf-taskschd-itaskdefinition-get_principal)
</dt> <dt>

[**TASK\_LOGON\_TYPE**](/windows/desktop/api/taskschd/ne-taskschd-task_logon_type)
</dt> </dl>

 

 




