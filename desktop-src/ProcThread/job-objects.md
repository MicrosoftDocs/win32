---
description: A job object allows groups of processes to be managed as a unit. Job objects are namable, securable, sharable objects that control attributes of the processes associated with them.
ms.assetid: 59296384-5e78-44dd-8019-f1df6668928b
title: Job Objects
ms.topic: article
ms.date: 05/31/2018
---

# Job Objects

A *job object* allows groups of processes to be managed as a unit. Job objects are namable, securable, sharable objects that control attributes of the processes associated with them. Operations performed on a job object affect all processes associated with the job object. Examples include enforcing limits such as working set size and process priority or terminating all processes associated with a job.

-   [Creating Jobs](#creating-jobs)
-   [Managing Processes in Jobs](#managing-processes-in-jobs)
-   [Job Limits and Notifications](#job-limits-and-notifications)
-   [Resource Accounting for Jobs](#resource-accounting-for-jobs)
-   [Managing Job Objects](#managing-job-objects)
-   [Managing a Process Tree that Uses Job Objects](#managing-a-process-tree-that-uses-job-objects)

## Creating Jobs

To create a job object, use the [**CreateJobObject**](/windows/desktop/api/WinBase/nf-winbase-createjobobjecta) function. When the job is created, no processes are associated with the job.

To associate a process with a job, use the [**AssignProcessToJobObject**](/windows/win32/api/jobapi2/nf-jobapi2-assignprocesstojobobject) function. After a process is associated with a job, the association cannot be broken. A process can be associated with more than one job in a hierarchy of nested jobs. For more information, see [Nested Jobs](nested-jobs.md).

**Windows 7, Windows Server 2008 R2, Windows XP with SP3, Windows Server 2008, Windows Vista and Windows Server 2003:** A process can be associated with only one job. Jobs cannot be nested. The ability to nest jobs was added in Windows 8 and Windows Server 2012.

You can specify a security descriptor for a job object when you call the [**CreateJobObject**](/windows/desktop/api/WinBase/nf-winbase-createjobobjecta) function. For more information, see [Job Object Security and Access Rights](job-object-security-and-access-rights.md).

## Managing Processes in Jobs

After a process is associated with a job, by default any child processes it creates using [**CreateProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa) are also associated with the job. (Child processes created using [**Win32\_Process.Create**](../cimwin32prov/create-method-in-class-win32-process.md) are not associated with the job.) This default behavior can be changed by setting the extended limit JOB\_OBJECT\_LIMIT\_BREAKAWAY\_OK or JOB\_OBJECT\_LIMIT\_SILENT\_BREAKAWAY\_OK for the job.

-   If the job has the extended limit JOB\_OBJECT\_LIMIT\_BREAKAWAY\_OK and the parent process was created with the CREATE\_BREAKAWAY\_FROM\_JOB flag, then child processes of the parent process are not associated with the job.
-   If the job has the extended limit JOB\_OBJECT\_LIMIT\_SILENT\_BREAKAWAY\_OK, then child processes of any parent process associated with the job are not associated with the job. It is not necessary for parent processes to be created with the CREATE\_BREAKAWAY\_FROM\_JOB flag.

If the job is nested, the breakaway settings of parent jobs in the hierarchy affect whether child processes are associated with another job in the hierarchy. For more information, see [Nested Jobs](nested-jobs.md).

To determine if a process is running in a job, use the [**IsProcessInJob**](/windows/win32/api/jobapi/nf-jobapi-isprocessinjob) function.

To terminate all processes currently associated with a job object, use the [**TerminateJobObject**](/windows/win32/api/jobapi2/nf-jobapi2-terminatejobobject) function.

## Job Limits and Notifications

A job can enforce limits such as working set size, process priority, and end-of-job time limit on each process that is associated with the job. If a process associated with a job attempts to increase its working set size or process priority from the limit established by the job, the function calls succeed but are silently ignored. A job can also set limits that trigger a notification when they are exceeded but allow the job to continue to run.

To set limits for a job, use the [**SetInformationJobObject**](/windows/win32/api/jobapi2/nf-jobapi2-setinformationjobobject) function. For a list of possible limits that can be set for a job, see the following topics:

-   [**JOBOBJECT\_BASIC\_LIMIT\_INFORMATION**](/windows/desktop/api/WinNT/ns-winnt-jobobject_basic_limit_information)
-   [**JOBOBJECT\_BASIC\_UI\_RESTRICTIONS**](/windows/desktop/api/WinNT/ns-winnt-jobobject_basic_ui_restrictions)
-   [**JOBOBJECT\_CPU\_RATE\_CONTROL\_INFORMATION**](/windows/desktop/api/Winnt/ns-winnt-jobobject_cpu_rate_control_information)
-   [**JOBOBJECT\_EXTENDED\_LIMIT\_INFORMATION**](/windows/desktop/api/WinNT/ns-winnt-jobobject_extended_limit_information)
-   [**JOBOBJECT\_NOTIFICATION\_LIMIT\_INFORMATION**](/windows/desktop/api/WinNT/ns-winnt-jobobject_notification_limit_information)

Security limits must be set individually for each process associated with a job object. For more information, see [Process Security and Access Rights](process-security-and-access-rights.md).

**Windows XP with SP3 and Windows Server 2003:** The [**SetInformationJobObject**](/windows/win32/api/jobapi2/nf-jobapi2-setinformationjobobject) function can be used to set security limitations for all processes associated with a job object. Starting with Windows Vista, security limits must be set individually for each process associated with a job object.

If the job is nested, parent jobs in the hierarchy influence the limit that is enforced for the job. For more information, see [Nested Jobs](nested-jobs.md).

If the job has an associated I/O completion port, it can receive notifications when certain job limits are exceeded. The system sends messages to the completion port when a limit is exceeded or certain other events occur. To associate a completion port with a job, use the [**SetInformationJobObject**](/windows/win32/api/jobapi2/nf-jobapi2-setinformationjobobject) function with the job object information class **JobObjectAssociateCompletionPortInformation** and a pointer to a [**JOBOBJECT\_ASSOCIATE\_COMPLETION\_PORT**](/windows/desktop/api/WinNT/ns-winnt-jobobject_associate_completion_port) structure. It is best to do this when the job is inactive, to reduce the chance of missing notifications for processes whose states change during the association of the completion port.

All messages are sent directly from the job as if the job had called the [**PostQueuedCompletionStatus**](/windows/win32/api/ioapiset/nf-ioapiset-postqueuedcompletionstatus) function. A thread must monitor the completion port using the [**GetQueuedCompletionStatus**](/windows/win32/api/ioapiset/nf-ioapiset-getqueuedcompletionstatus) function to pick up the messages. Note that, with the exception of limits set with the **JobObjectNotificationLimitInformation** information class, delivery of messages to the completion port is not guaranteed; failure of a message to arrive does not necessarily mean that the event did not occur. Notifications for limits set with **JobObjectNotificationLimitInformation** are guaranteed to arrive at the completion port. For a list of possible messages, see [**JOBOBJECT\_ASSOCIATE\_COMPLETION\_PORT**](/windows/desktop/api/WinNT/ns-winnt-jobobject_associate_completion_port).

## Resource Accounting for Jobs

The job object records basic accounting information for all its associated processes, including those that have terminated. To retrieve this accounting information, use the [**QueryInformationJobObject**](/windows/win32/api/jobapi2/nf-jobapi2-queryinformationjobobject) function. For a list of the accounting information that is maintained for a job, see the following topics:

-   [**JOBOBJECT\_BASIC\_ACCOUNTING\_INFORMATION**](/windows/desktop/api/WinNT/ns-winnt-jobobject_basic_accounting_information)
-   [**JOBOBJECT\_BASIC\_AND\_IO\_ACCOUNTING\_INFORMATION**](/windows/desktop/api/WinNT/ns-winnt-jobobject_basic_and_io_accounting_information)

If the job object is nested, accounting information for each child job is aggregated in its parent job. For more information, see [Nested Jobs](nested-jobs.md).

## Managing Job Objects

The state of a job object is set to signaled when all of its processes are terminated because the specified end-of-job time limit has been exceeded. Use [**WaitForSingleObject**](/windows/win32/api/synchapi/nf-synchapi-waitforsingleobject) or [**WaitForSingleObjectEx**](/windows/win32/api/synchapi/nf-synchapi-waitforsingleobjectex) to monitor the job object for this event.

To obtain a handle for an existing job object, use the [**OpenJobObject**](/windows/desktop/api/WinBase/nf-winbase-openjobobjecta) function and specify the name given to the object when it was created. Only named job objects can be opened.

To close a job object handle, use the [**CloseHandle**](/windows/win32/api/handleapi/nf-handleapi-closehandle) function. The job is destroyed when its last handle has been closed and all associated processes have been terminated. However, if the job has the JOB\_OBJECT\_LIMIT\_KILL\_ON\_JOB\_CLOSE flag specified, closing the last job object handle terminates all associated processes and then destroys the job object itself. If a nested job has the JOB\_OBJECT\_LIMIT\_KILL\_ON\_JOB\_CLOSE flag specified, closing the last job object handle terminates all processes associated with the job and its child jobs in the hierarchy.

## Managing a Process Tree that Uses Job Objects

Starting with Windows 8 and Windows Server 2012, an application can use [nested jobs](nested-jobs.md) to manage a process tree that uses more than one job object. However, an application that must run on Windows 7, Windows Server 2008 R2, or earlier versions of Windows that do not support nested jobs must manage the process tree in other ways.

If a tool must manage a process tree that uses job objects and it is not possible to use nested jobs, both the tool and the members of the process tree must cooperate. Use one of the following options:

-   Use the JOB\_OBJECT\_LIMIT\_SILENT\_BREAKAWAY\_OK limit. If the tool uses this limit, it cannot monitor an entire process tree. The tool can monitor only the processes it adds to the job. If these processes create child processes, they are not associated with the job. In this option, child processes can be associated with other job objects.
-   Use the JOB\_OBJECT\_LIMIT\_BREAKAWAY\_OK limit. If the tool uses this limit, it can monitor the entire process tree, except for those processes that any member of the tree explicitly breaks away from the tree. A member of the tree can create a child process in a new job object by calling the [**CreateProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa) function with the CREATE\_BREAKAWAY\_FROM\_JOB flag, then calling the [**AssignProcessToJobObject**](/windows/win32/api/jobapi2/nf-jobapi2-assignprocesstojobobject) function. Otherwise, the member must handle cases in which **AssignProcessToJobObject** fails.

    The CREATE\_BREAKAWAY\_FROM\_JOB flag has no effect if the tree is not being monitored by the tool. Therefore, this is the preferred option, but it requires advance knowledge of the processes being monitored.

-   Prevent breakaways of any kind by setting neither the JOB\_OBJECT\_LIMIT\_BREAKAWAY\_OK nor the JOB\_OBJECT\_LIMIT\_SILENT\_BREAKAWAY\_OK limit. In this option, the tool can monitor the entire process tree. However, if a child process attempts to associate itself or another child process with a job by calling [**AssignProcessToJobObject**](/windows/win32/api/jobapi2/nf-jobapi2-assignprocesstojobobject), the call will fail. If the process was designed to be associated with a specific job, this failure may prevent the process from working properly.

 

 
