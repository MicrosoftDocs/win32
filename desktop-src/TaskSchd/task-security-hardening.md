---
title: Task Security Hardening
description: Using the tasks security hardening feature will allow task owners to run their tasks with minimum required privileges.
ms.assetid: ba03add5-aa05-4bef-baec-684ca17363bd
ms.topic: article
ms.date: 05/31/2018
---

# Task Security Hardening

Using the tasks security hardening feature will allow task owners to run their tasks with minimum required privileges. Note that this feature is enabled by default and task owners can make further adjustments by using the task process token security identifier type and task required privileges array.

## Task Process Token SID Type and Task Required Privileges Array

Specifying **ProcessTokenSidType** at the task definition level allows task owners to request a task process to run with the "none" SID type or the "unrestricted" SID type. If the field is present in task definition, validation ensures that task UserId contains the name or the corresponding SID string for one of those operating system built-in service accounts: "NETWORK SERVICE" or "LOCAL SERVICE".

The SID type "none" means that the task runs in a process that does not contain a process token SID (no changes will be made to the process token groups list). The task principal account SID (LocalService/NetworkService) in that case has full access to the process token.

The "unrestricted" SID type means that a task SID will be derived from the full task path and will be added to the process token groups list. For example, the \\Microsoft\\Windows\\RAC\\RACTask which runs in the Local Service account, the task SID is derived from the name Microsoft-Windows-RAC-RACTask where a "-" is substituted for a "\\" since "\\" is an invalid user name character. The well known group name for the task SID would be "NT TASK\\\<modified full task path\>" (domainname\\username format). The process token default discretionary access control list (DACL) will also be modified to allow full control for the task SID and local system SID only and read control to the task principal account SID. "schtasks.exe /showsid /tn \<full task path\>" will show the task SID that is corresponding to the task.

When a non-COM task action starts up, the scheduling engine logs on the task principal account, gets the process token and queries the list of privileges that the token has and then compares that with the privileges list specified in RequiredPrivileges. If a privilege is not specified in the latter, then that is marked as SE\_PRIVILEGE\_REMOVED. The executable action will then be started with the resulting token handle by using the CreateProcessAsUser API.

When a COM task action starts up, it must be activated by the taskhost.exe process. The scheduling engine queries the context block of each running taskhost.exe with the same account as the starting task. If it finds that a host process was started with a superset of privileges that the starting task needs, then that task gets hosted in that process. If it does not find such a process, it combines the hardening info of all the tasks that are running in the taskhosts under the task principal account with the specified RequiredPrivileges mask and then starts up a new instance of taskhost.exe.

If RequiredPrivileges is not present in the task definition, the default privileges of task principal account without the SeImpersonatePrivilege will be used for task process. If **ProcessTokenSidType** is not present in the task definition, "unrestricted" is used as the default.

## Related topics

<dl> <dt>

[Task Registration Information](task-registration-information.md)
</dt> <dt>

[About The Task Scheduler](about-the-task-scheduler.md)
</dt> <dt>

[Security Contexts for Tasks](security-contexts-for-running-tasks.md)
</dt> </dl>

 

 




