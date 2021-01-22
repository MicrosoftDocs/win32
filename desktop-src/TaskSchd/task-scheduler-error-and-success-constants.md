---
title: Task Scheduler Error and Success Constants (WinError.h)
description: If an error occurs, the Task Scheduler APIs can return one of the following error codes as an HRESULT value.
ms.assetid: 54278bbd-7dca-438e-a771-5fcb08c4aa68
keywords:
- Task Scheduler Task Scheduler , reference, error and success constants
topic_type:
- apiref
api_name:
- SCHED_S_TASK_READY
- SCHED_S_TASK_RUNNING
- SCHED_S_TASK_DISABLED
- SCHED_S_TASK_HAS_NOT_RUN
- SCHED_S_TASK_NO_MORE_RUNS
- SCHED_S_TASK_NOT_SCHEDULED
- SCHED_S_TASK_TERMINATED
- SCHED_S_TASK_NO_VALID_TRIGGERS
- SCHED_S_EVENT_TRIGGER
- SCHED_E_TRIGGER_NOT_FOUND
- SCHED_E_TASK_NOT_READY
- SCHED_E_TASK_NOT_RUNNING
- SCHED_E_SERVICE_NOT_INSTALLED
- SCHED_E_CANNOT_OPEN_TASK
- SCHED_E_INVALID_TASK
- SCHED_E_ACCOUNT_INFORMATION_NOT_SET
- SCHED_E_ACCOUNT_NAME_NOT_FOUND
- SCHED_E_ACCOUNT_DBASE_CORRUPT
- SCHED_E_NO_SECURITY_SERVICES
- SCHED_E_UNKNOWN_OBJECT_VERSION
- SCHED_E_UNSUPPORTED_ACCOUNT_OPTION
- SCHED_E_SERVICE_NOT_RUNNING
- SCHED_E_UNEXPECTEDNODE
- SCHED_E_NAMESPACE
- SCHED_E_INVALIDVALUE
- SCHED_E_MISSINGNODE
- SCHED_E_MALFORMEDXML
- SCHED_S_SOME_TRIGGERS_FAILED
- SCHED_S_BATCH_LOGON_PROBLEM
- SCHED_E_TOO_MANY_NODES
- SCHED_E_PAST_END_BOUNDARY
- SCHED_E_ALREADY_RUNNING
- SCHED_E_USER_NOT_LOGGED_ON
- SCHED_E_INVALID_TASK_HASH
- SCHED_E_SERVICE_NOT_AVAILABLE
- SCHED_E_SERVICE_TOO_BUSY
- SCHED_E_TASK_ATTEMPTED
- SCHED_S_TASK_QUEUED
- SCHED_E_TASK_DISABLED
- SCHED_E_TASK_NOT_V1_COMPAT
- SCHED_E_START_ON_DEMAND
api_location:
- WinError.h
api_type:
- HeaderDef
ms.topic: reference
ms.custom: snippet-project
ms.date: 05/31/2018
---

# Task Scheduler Error and Success Constants

If an error occurs, the Task Scheduler APIs can return one of the following error codes as an **HRESULT** value.

The constants that begin with SCHED\_S\_ are success constants, and the constants that begin with SCHED\_E\_ are error constants.

```cpp
  HRESULT phrStatus;
  hr = pITask->GetStatus(&phrStatus);
  
  // Release the ITask interface.
  pITask->Release();
    
  switch(phrStatus)
  {
  case SCHED_S_TASK_READY:
       wprintf(L"  SCHED_S_TASK_READY\n");
       break;
  case SCHED_S_TASK_RUNNING:
       wprintf(L"  SCHED_S_TASK_RUNNING\n");
       break;

  //...
  }
```

Example from [C/C++ Code Example: Retrieving Task Status](c-c-code-example-retrieving-task-status.md).

> [!Note]  
> Some Task Scheduler APIs can return system and network error codes (64 for example). You can check the definition of these types of error codes by using the **net helpmsg** command in the command prompt window. For example, the command **net helpmsg 64** returns the message: The specified network name is no longer available.

 

For more information about events and error messages, see [Events and Errors Message Center](https://www.microsoft.com/technet/support/ee/ee_advanced.aspx).

<dl> <dt>

<span id="SCHED_S_TASK_READY"></span><span id="sched_s_task_ready"></span>**SCHED\_S\_TASK\_READY**
</dt> <dd> <dl> <dt>

0x00041300
</dt> <dt>



The task is ready to run at its next scheduled time.


</dt> </dl> </dd> <dt>

<span id="SCHED_S_TASK_RUNNING"></span><span id="sched_s_task_running"></span>**SCHED\_S\_TASK\_RUNNING**
</dt> <dd> <dl> <dt>

0x00041301
</dt> <dt>



The task is currently running.


</dt> </dl> </dd> <dt>

<span id="SCHED_S_TASK_DISABLED"></span><span id="sched_s_task_disabled"></span>**SCHED\_S\_TASK\_DISABLED**
</dt> <dd> <dl> <dt>

0x00041302
</dt> <dt>



The task will not run at the scheduled times because it has been disabled.


</dt> </dl> </dd> <dt>

<span id="SCHED_S_TASK_HAS_NOT_RUN"></span><span id="sched_s_task_has_not_run"></span>**SCHED\_S\_TASK\_HAS\_NOT\_RUN**
</dt> <dd> <dl> <dt>

0x00041303
</dt> <dt>



The task has not yet run.


</dt> </dl> </dd> <dt>

<span id="SCHED_S_TASK_NO_MORE_RUNS"></span><span id="sched_s_task_no_more_runs"></span>**SCHED\_S\_TASK\_NO\_MORE\_RUNS**
</dt> <dd> <dl> <dt>

0x00041304
</dt> <dt>



There are no more runs scheduled for this task.


</dt> </dl> </dd> <dt>

<span id="SCHED_S_TASK_NOT_SCHEDULED"></span><span id="sched_s_task_not_scheduled"></span>**SCHED\_S\_TASK\_NOT\_SCHEDULED**
</dt> <dd> <dl> <dt>

0x00041305
</dt> <dt>



One or more of the properties that are needed to run this task on a schedule have not been set.


</dt> </dl> </dd> <dt>

<span id="SCHED_S_TASK_TERMINATED"></span><span id="sched_s_task_terminated"></span>**SCHED\_S\_TASK\_TERMINATED**
</dt> <dd> <dl> <dt>

0x00041306
</dt> <dt>



The last run of the task was terminated by the user.


</dt> </dl> </dd> <dt>

<span id="SCHED_S_TASK_NO_VALID_TRIGGERS"></span><span id="sched_s_task_no_valid_triggers"></span>**SCHED\_S\_TASK\_NO\_VALID\_TRIGGERS**
</dt> <dd> <dl> <dt>

0x00041307
</dt> <dt>



Either the task has no triggers or the existing triggers are disabled or not set.


</dt> </dl> </dd> <dt>

<span id="SCHED_S_EVENT_TRIGGER"></span><span id="sched_s_event_trigger"></span>**SCHED\_S\_EVENT\_TRIGGER**
</dt> <dd> <dl> <dt>

0x00041308
</dt> <dt>



Event triggers do not have set run times.


</dt> </dl> </dd> <dt>

<span id="SCHED_E_TRIGGER_NOT_FOUND"></span><span id="sched_e_trigger_not_found"></span>**SCHED\_E\_TRIGGER\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

0x80041309
</dt> <dt>



A task's trigger is not found.


</dt> </dl> </dd> <dt>

<span id="SCHED_E_TASK_NOT_READY"></span><span id="sched_e_task_not_ready"></span>**SCHED\_E\_TASK\_NOT\_READY**
</dt> <dd> <dl> <dt>

0x8004130A
</dt> <dt>



One or more of the properties required to run this task have not been set.


</dt> </dl> </dd> <dt>

<span id="SCHED_E_TASK_NOT_RUNNING"></span><span id="sched_e_task_not_running"></span>**SCHED\_E\_TASK\_NOT\_RUNNING**
</dt> <dd> <dl> <dt>

0x8004130B
</dt> <dt>



There is no running instance of the task.


</dt> </dl> </dd> <dt>

<span id="SCHED_E_SERVICE_NOT_INSTALLED"></span><span id="sched_e_service_not_installed"></span>**SCHED\_E\_SERVICE\_NOT\_INSTALLED**
</dt> <dd> <dl> <dt>

0x8004130C
</dt> <dt>



The Task Scheduler service is not installed on this computer.


</dt> </dl> </dd> <dt>

<span id="SCHED_E_CANNOT_OPEN_TASK"></span><span id="sched_e_cannot_open_task"></span>**SCHED\_E\_CANNOT\_OPEN\_TASK**
</dt> <dd> <dl> <dt>

0x8004130D
</dt> <dt>



The task object could not be opened.


</dt> </dl> </dd> <dt>

<span id="SCHED_E_INVALID_TASK"></span><span id="sched_e_invalid_task"></span>**SCHED\_E\_INVALID\_TASK**
</dt> <dd> <dl> <dt>

0x8004130E
</dt> <dt>



The object is either an invalid task object or is not a task object.


</dt> </dl> </dd> <dt>

<span id="SCHED_E_ACCOUNT_INFORMATION_NOT_SET"></span><span id="sched_e_account_information_not_set"></span>**SCHED\_E\_ACCOUNT\_INFORMATION\_NOT\_SET**
</dt> <dd> <dl> <dt>

0x8004130F
</dt> <dt>



No account information could be found in the Task Scheduler security database for the task indicated.


</dt> </dl> </dd> <dt>

<span id="SCHED_E_ACCOUNT_NAME_NOT_FOUND"></span><span id="sched_e_account_name_not_found"></span>**SCHED\_E\_ACCOUNT\_NAME\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

0x80041310
</dt> <dt>



Unable to establish existence of the account specified.


</dt> </dl> </dd> <dt>

<span id="SCHED_E_ACCOUNT_DBASE_CORRUPT"></span><span id="sched_e_account_dbase_corrupt"></span>**SCHED\_E\_ACCOUNT\_DBASE\_CORRUPT**
</dt> <dd> <dl> <dt>

0x80041311
</dt> <dt>



Corruption was detected in the Task Scheduler security database; the database has been reset.


</dt> </dl> </dd> <dt>

<span id="SCHED_E_NO_SECURITY_SERVICES"></span><span id="sched_e_no_security_services"></span>**SCHED\_E\_NO\_SECURITY\_SERVICES**
</dt> <dd> <dl> <dt>

0x80041312
</dt> <dt>



Task Scheduler security services are available only on Windows NT.


</dt> </dl> </dd> <dt>

<span id="SCHED_E_UNKNOWN_OBJECT_VERSION"></span><span id="sched_e_unknown_object_version"></span>**SCHED\_E\_UNKNOWN\_OBJECT\_VERSION**
</dt> <dd> <dl> <dt>

0x80041313
</dt> <dt>



The task object version is either unsupported or invalid.


</dt> </dl> </dd> <dt>

<span id="SCHED_E_UNSUPPORTED_ACCOUNT_OPTION"></span><span id="sched_e_unsupported_account_option"></span>**SCHED\_E\_UNSUPPORTED\_ACCOUNT\_OPTION**
</dt> <dd> <dl> <dt>

0x80041314
</dt> <dt>



The task has been configured with an unsupported combination of account settings and run time options.


</dt> </dl> </dd> <dt>

<span id="SCHED_E_SERVICE_NOT_RUNNING"></span><span id="sched_e_service_not_running"></span>**SCHED\_E\_SERVICE\_NOT\_RUNNING**
</dt> <dd> <dl> <dt>

0x80041315
</dt> <dt>



The Task Scheduler Service is not running.


</dt> </dl> </dd> <dt>

<span id="SCHED_E_UNEXPECTEDNODE"></span><span id="sched_e_unexpectednode"></span>**SCHED\_E\_UNEXPECTEDNODE**
</dt> <dd> <dl> <dt>

0x80041316
</dt> <dt>



The task XML contains an unexpected node.


</dt> </dl> </dd> <dt>

<span id="SCHED_E_NAMESPACE"></span><span id="sched_e_namespace"></span>**SCHED\_E\_NAMESPACE**
</dt> <dd> <dl> <dt>

0x80041317
</dt> <dt>



The task XML contains an element or attribute from an unexpected namespace.


</dt> </dl> </dd> <dt>

<span id="SCHED_E_INVALIDVALUE"></span><span id="sched_e_invalidvalue"></span>**SCHED\_E\_INVALIDVALUE**
</dt> <dd> <dl> <dt>

0x80041318
</dt> <dt>



The task XML contains a value which is incorrectly formatted or out of range.


</dt> </dl> </dd> <dt>

<span id="SCHED_E_MISSINGNODE"></span><span id="sched_e_missingnode"></span>**SCHED\_E\_MISSINGNODE**
</dt> <dd> <dl> <dt>

0x80041319
</dt> <dt>



The task XML is missing a required element or attribute.


</dt> </dl> </dd> <dt>

<span id="SCHED_E_MALFORMEDXML"></span><span id="sched_e_malformedxml"></span>**SCHED\_E\_MALFORMEDXML**
</dt> <dd> <dl> <dt>

0x8004131A
</dt> <dt>



The task XML is malformed.


</dt> </dl> </dd> <dt>

<span id="SCHED_S_SOME_TRIGGERS_FAILED"></span><span id="sched_s_some_triggers_failed"></span>**SCHED\_S\_SOME\_TRIGGERS\_FAILED**
</dt> <dd> <dl> <dt>

0x0004131B
</dt> <dt>



The task is registered, but not all specified triggers will start the task.


</dt> </dl> </dd> <dt>

<span id="SCHED_S_BATCH_LOGON_PROBLEM"></span><span id="sched_s_batch_logon_problem"></span>**SCHED\_S\_BATCH\_LOGON\_PROBLEM**
</dt> <dd> <dl> <dt>

0x0004131C
</dt> <dt>



The task is registered, but may fail to start. Batch logon privilege needs to be enabled for the task principal.


</dt> </dl> </dd> <dt>

<span id="SCHED_E_TOO_MANY_NODES"></span><span id="sched_e_too_many_nodes"></span>**SCHED\_E\_TOO\_MANY\_NODES**
</dt> <dd> <dl> <dt>

0x8004131D
</dt> <dt>



The task XML contains too many nodes of the same type.


</dt> </dl> </dd> <dt>

<span id="SCHED_E_PAST_END_BOUNDARY"></span><span id="sched_e_past_end_boundary"></span>**SCHED\_E\_PAST\_END\_BOUNDARY**
</dt> <dd> <dl> <dt>

0x8004131E
</dt> <dt>



The task cannot be started after the trigger end boundary.


</dt> </dl> </dd> <dt>

<span id="SCHED_E_ALREADY_RUNNING"></span><span id="sched_e_already_running"></span>**SCHED\_E\_ALREADY\_RUNNING**
</dt> <dd> <dl> <dt>

0x8004131F
</dt> <dt>



An instance of this task is already running.


</dt> </dl> </dd> <dt>

<span id="SCHED_E_USER_NOT_LOGGED_ON"></span><span id="sched_e_user_not_logged_on"></span>**SCHED\_E\_USER\_NOT\_LOGGED\_ON**
</dt> <dd> <dl> <dt>

0x80041320
</dt> <dt>



The task will not run because the user is not logged on.


</dt> </dl> </dd> <dt>

<span id="SCHED_E_INVALID_TASK_HASH"></span><span id="sched_e_invalid_task_hash"></span>**SCHED\_E\_INVALID\_TASK\_HASH**
</dt> <dd> <dl> <dt>

0x80041321
</dt> <dt>



The task image is corrupt or has been tampered with.


</dt> </dl> </dd> <dt>

<span id="SCHED_E_SERVICE_NOT_AVAILABLE"></span><span id="sched_e_service_not_available"></span>**SCHED\_E\_SERVICE\_NOT\_AVAILABLE**
</dt> <dd> <dl> <dt>

0x80041322
</dt> <dt>



The Task Scheduler service is not available.


</dt> </dl> </dd> <dt>

<span id="SCHED_E_SERVICE_TOO_BUSY"></span><span id="sched_e_service_too_busy"></span>**SCHED\_E\_SERVICE\_TOO\_BUSY**
</dt> <dd> <dl> <dt>

0x80041323
</dt> <dt>



The Task Scheduler service is too busy to handle your request. Please try again later.


</dt> </dl> </dd> <dt>

<span id="SCHED_E_TASK_ATTEMPTED"></span><span id="sched_e_task_attempted"></span>**SCHED\_E\_TASK\_ATTEMPTED**
</dt> <dd> <dl> <dt>

0x80041324
</dt> <dt>



The Task Scheduler service attempted to run the task, but the task did not run due to one of the constraints in the task definition.


</dt> </dl> </dd> <dt>

<span id="SCHED_S_TASK_QUEUED"></span><span id="sched_s_task_queued"></span>**SCHED\_S\_TASK\_QUEUED**
</dt> <dd> <dl> <dt>

0x00041325
</dt> <dt>



The Task Scheduler service has asked the task to run.


</dt> </dl> </dd> <dt>

<span id="SCHED_E_TASK_DISABLED"></span><span id="sched_e_task_disabled"></span>**SCHED\_E\_TASK\_DISABLED**
</dt> <dd> <dl> <dt>

0x80041326
</dt> <dt>



The task is disabled.


</dt> </dl> </dd> <dt>

<span id="SCHED_E_TASK_NOT_V1_COMPAT"></span><span id="sched_e_task_not_v1_compat"></span>**SCHED\_E\_TASK\_NOT\_V1\_COMPAT**
</dt> <dd> <dl> <dt>

0x80041327
</dt> <dt>



The task has properties that are not compatible with earlier versions of Windows.


</dt> </dl> </dd> <dt>

<span id="SCHED_E_START_ON_DEMAND"></span><span id="sched_e_start_on_demand"></span>**SCHED\_E\_START\_ON\_DEMAND**
</dt> <dd> <dl> <dt>

0x80041328
</dt> <dt>



The task settings do not allow the task to start on demand.


</dt> </dl> </dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>WinError.h</dt> </dl> |



 

 





