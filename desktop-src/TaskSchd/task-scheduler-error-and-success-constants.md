---
title: Task Scheduler error and success constants (WinError.h)
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
ms.date: 10/29/2024
---

# Task Scheduler error and success constants

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

Example from [C/C++ code example: retrieving task status](c-c-code-example-retrieving-task-status.md).

> [!NOTE] 
> Some Task Scheduler APIs can return system and network error codes (64 for example). You can check the definition of these types of error codes by using the **net helpmsg** command in the command prompt window. For example, the command **net helpmsg 64** returns the message: The specified network name is no longer available.

For more info about events and error messages, see [Events and Errors Message Center](https://www.microsoft.com/technet/support/ee/ee_advanced.aspx).

**SCHED_E_SERVICE_NOT_LOCALSYSTEM**

 The Task Scheduler service must be configured to run in the System account to function properly. Individual tasks may be configured to run in other accounts.

`#define SCHED_E_SERVICE_NOT_LOCALSYSTEM  6200L`

**SCHED_S_TASK_READY**

 The task is ready to run at its next scheduled time.

`#define SCHED_S_TASK_READY               _HRESULT_TYPEDEF_(0x00041300L)`


**SCHED_S_TASK_RUNNING**

 The task is currently running.

`#define SCHED_S_TASK_RUNNING             _HRESULT_TYPEDEF_(0x00041301L)`


**SCHED_S_TASK_DISABLED**

 The task will not run at the scheduled times because it has been disabled.

`#define SCHED_S_TASK_DISABLED            _HRESULT_TYPEDEF_(0x00041302L)`


**SCHED_S_TASK_HAS_NOT_RUN**

 The task has not yet run.

`#define SCHED_S_TASK_HAS_NOT_RUN         _HRESULT_TYPEDEF_(0x00041303L)`


**SCHED_S_TASK_NO_MORE_RUNS**

 There are no more runs scheduled for this task.

`#define SCHED_S_TASK_NO_MORE_RUNS        _HRESULT_TYPEDEF_(0x00041304L)`


**SCHED_S_TASK_NOT_SCHEDULED**

 One or more of the properties that are needed to run this task on a schedule have not been set.

`#define SCHED_S_TASK_NOT_SCHEDULED       _HRESULT_TYPEDEF_(0x00041305L)`


**SCHED_S_TASK_TERMINATED**

 The last run of the task was terminated by the user.

`#define SCHED_S_TASK_TERMINATED          _HRESULT_TYPEDEF_(0x00041306L)`


**SCHED_S_TASK_NO_VALID_TRIGGERS**

 Either the task has no triggers or the existing triggers are disabled or not set.

`#define SCHED_S_TASK_NO_VALID_TRIGGERS   _HRESULT_TYPEDEF_(0x00041307L)`


**SCHED_S_EVENT_TRIGGER**

 Event triggers don't have set run times.

`#define SCHED_S_EVENT_TRIGGER            _HRESULT_TYPEDEF_(0x00041308L)`


**SCHED_E_TRIGGER_NOT_FOUND**

 Trigger not found.

`#define SCHED_E_TRIGGER_NOT_FOUND        _HRESULT_TYPEDEF_(0x80041309L)`


**SCHED_E_TASK_NOT_READY**

 One or more of the properties that are needed to run this task have not been set.

`#define SCHED_E_TASK_NOT_READY           _HRESULT_TYPEDEF_(0x8004130AL)`


**SCHED_E_TASK_NOT_RUNNING**

 There is no running instance of the task.

`#define SCHED_E_TASK_NOT_RUNNING         _HRESULT_TYPEDEF_(0x8004130BL)`


**SCHED_E_SERVICE_NOT_INSTALLED**

 The Task Scheduler Service is not installed on this computer.

`#define SCHED_E_SERVICE_NOT_INSTALLED    _HRESULT_TYPEDEF_(0x8004130CL)`


**SCHED_E_CANNOT_OPEN_TASK**

 The task object could not be opened.

`#define SCHED_E_CANNOT_OPEN_TASK         _HRESULT_TYPEDEF_(0x8004130DL)`


**SCHED_E_INVALID_TASK**

 The object is either an invalid task object or is not a task object.

`#define SCHED_E_INVALID_TASK             _HRESULT_TYPEDEF_(0x8004130EL)`


**SCHED_E_ACCOUNT_INFORMATION_NOT_SET**

 No account information could be found in the Task Scheduler security database for the task indicated.

`#define SCHED_E_ACCOUNT_INFORMATION_NOT_SET _HRESULT_TYPEDEF_(0x8004130FL)`


**SCHED_E_ACCOUNT_NAME_NOT_FOUND**

 Unable to establish existence of the account specified.

`#define SCHED_E_ACCOUNT_NAME_NOT_FOUND   _HRESULT_TYPEDEF_(0x80041310L)`


**SCHED_E_ACCOUNT_DBASE_CORRUPT**

 Corruption was detected in the Task Scheduler security database; the database has been reset.

`#define SCHED_E_ACCOUNT_DBASE_CORRUPT    _HRESULT_TYPEDEF_(0x80041311L)`


**SCHED_E_NO_SECURITY_SERVICES**

 Task Scheduler security services are available only on Windows NT.

`#define SCHED_E_NO_SECURITY_SERVICES     _HRESULT_TYPEDEF_(0x80041312L)`


**SCHED_E_UNKNOWN_OBJECT_VERSION**

 The task object version is either unsupported or invalid.

`#define SCHED_E_UNKNOWN_OBJECT_VERSION   _HRESULT_TYPEDEF_(0x80041313L)`


**SCHED_E_UNSUPPORTED_ACCOUNT_OPTION**

 The task has been configured with an unsupported combination of account settings and run time options.

`#define SCHED_E_UNSUPPORTED_ACCOUNT_OPTION _HRESULT_TYPEDEF_(0x80041314L)`


**SCHED_E_SERVICE_NOT_RUNNING**

 The Task Scheduler Service is not running.

`#define SCHED_E_SERVICE_NOT_RUNNING      _HRESULT_TYPEDEF_(0x80041315L)`


**SCHED_E_UNEXPECTEDNODE**

 The task XML contains an unexpected node.

`#define SCHED_E_UNEXPECTEDNODE           _HRESULT_TYPEDEF_(0x80041316L)`


**SCHED_E_NAMESPACE**

 The task XML contains an element or attribute from an unexpected namespace.

`#define SCHED_E_NAMESPACE                _HRESULT_TYPEDEF_(0x80041317L)`


**SCHED_E_INVALIDVALUE**

 The task XML contains a value which is incorrectly formatted or out of range.

`#define SCHED_E_INVALIDVALUE             _HRESULT_TYPEDEF_(0x80041318L)`


**SCHED_E_MISSINGNODE**

 The task XML is missing a required element or attribute.

`#define SCHED_E_MISSINGNODE              _HRESULT_TYPEDEF_(0x80041319L)`


**SCHED_E_MALFORMEDXML**

 The task XML is malformed.

`#define SCHED_E_MALFORMEDXML             _HRESULT_TYPEDEF_(0x8004131AL)`


**SCHED_S_SOME_TRIGGERS_FAILED**

 The task is registered, but not all specified triggers will start the task, check task scheduler event log for detailed information.

`#define SCHED_S_SOME_TRIGGERS_FAILED     _HRESULT_TYPEDEF_(0x0004131BL)`


**SCHED_S_BATCH_LOGON_PROBLEM**

 The task is registered, but may fail to start. Batch logon privilege needs to be enabled for the task principal.

`#define SCHED_S_BATCH_LOGON_PROBLEM      _HRESULT_TYPEDEF_(0x0004131CL)`


**SCHED_E_TOO_MANY_NODES**

 The task XML contains too many nodes of the same type.

`#define SCHED_E_TOO_MANY_NODES           _HRESULT_TYPEDEF_(0x8004131DL)`


**SCHED_E_PAST_END_BOUNDARY**

 The task cannot be started after the trigger's end boundary.

`#define SCHED_E_PAST_END_BOUNDARY        _HRESULT_TYPEDEF_(0x8004131EL)`


**SCHED_E_ALREADY_RUNNING**

 An instance of this task is already running.

`#define SCHED_E_ALREADY_RUNNING          _HRESULT_TYPEDEF_(0x8004131FL)`


**SCHED_E_USER_NOT_LOGGED_ON**

 The task will not run because the user is not logged on.

`#define SCHED_E_USER_NOT_LOGGED_ON       _HRESULT_TYPEDEF_(0x80041320L)`


**SCHED_E_INVALID_TASK_HASH**

 The task image is corrupt or has been tampered with.

`#define SCHED_E_INVALID_TASK_HASH        _HRESULT_TYPEDEF_(0x80041321L)`


**SCHED_E_SERVICE_NOT_AVAILABLE**

 The Task Scheduler service is not available.

`#define SCHED_E_SERVICE_NOT_AVAILABLE    _HRESULT_TYPEDEF_(0x80041322L)`


**SCHED_E_SERVICE_TOO_BUSY**

 The Task Scheduler service is too busy to handle your request. Please try again later.

`#define SCHED_E_SERVICE_TOO_BUSY         _HRESULT_TYPEDEF_(0x80041323L)`


**SCHED_E_TASK_ATTEMPTED**

 The Task Scheduler service attempted to run the task, but the task did not run due to one of the constraints in the task definition.

`#define SCHED_E_TASK_ATTEMPTED           _HRESULT_TYPEDEF_(0x80041324L)`


**SCHED_S_TASK_QUEUED**

 The Task Scheduler service has asked the task to run.

`#define SCHED_S_TASK_QUEUED              _HRESULT_TYPEDEF_(0x00041325L)`


**SCHED_E_TASK_DISABLED**

 The task is disabled.

`#define SCHED_E_TASK_DISABLED            _HRESULT_TYPEDEF_(0x80041326L)`


**SCHED_E_TASK_NOT_V1_COMPAT**

 The task has properties that are not compatible with previous versions of Windows.

`#define SCHED_E_TASK_NOT_V1_COMPAT       _HRESULT_TYPEDEF_(0x80041327L)`


**SCHED_E_START_ON_DEMAND**

 The task settings do not allow the task to start on demand.

`#define SCHED_E_START_ON_DEMAND          _HRESULT_TYPEDEF_(0x80041328L)`


**SCHED_E_TASK_NOT_UBPM_COMPAT**

 The combination of properties that task is using is not compatible with the scheduling engine.

`#define SCHED_E_TASK_NOT_UBPM_COMPAT     _HRESULT_TYPEDEF_(0x80041329L)`


**SCHED_E_DEPRECATED_FEATURE_USED**

 The task definition uses a deprecated feature.

`#define SCHED_E_DEPRECATED_FEATURE_USED  _HRESULT_TYPEDEF_(0x80041330L)`

## Requirements

| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client | Windows Vista \[desktop apps only\] |
| Minimum supported server | Windows Server 2008 \[desktop apps only\] |
| Header | WinError.h |
