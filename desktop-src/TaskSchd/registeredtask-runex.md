---
title: RegisteredTask.RunEx method
description: For scripting, runs the registered task immediately using specified flags and a session identifier.
ms.assetid: '427bb51b-ddb1-4e47-9313-297366ba5ab7'
keywords:
- RunEx method Task Scheduler
- RunEx method Task Scheduler , RegisteredTask object
- RegisteredTask object Task Scheduler , RunEx method
topic_type:
- apiref
api_name:
- RegisteredTask.RunEx
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# RegisteredTask.RunEx method

For scripting, runs the registered task immediately using specified flags and a session identifier.

## Syntax


```VB
RegisteredTask.RunEx( _
  ByVal params, _
  ByVal flags, _
  ByVal sessionID, _
  ByRef runningTask _
)
```



## Parameters

<dl> <dt>

*params* \[in\]
</dt> <dd>

The parameters used as values in the task actions. To not specify any parameter values for the task actions, set this parameter to **Nothing**. Otherwise, a single string value or an array of string values can be specified.

The string values that you specify are paired with names and stored as name-value pairs. If you specify a single string value, then Arg0 will be the name assigned to the value. The value can be used in the task action where the $(Arg0) variable is used in the action properties.

If you pass in values such as "0", "100", and "250" as an array of string values, then "0" will replace the $(Arg0) variables, "100" will replace the $(Arg1) variables, and "250" will replace the $(Arg2) variables used in the action properties.

A maximum of 32 string values can be specified.

For more information and a list of action properties that can use $(Arg0), $(Arg1), ..., $(Arg32) variables in their values, see [Task Actions](task-actions.md).

</dd> <dt>

*flags* \[in\]
</dt> <dd>

A [TASK\_RUN\_FLAGS](/windows/desktop/api/taskschd/ne-taskschd-task_run_flags) constant that defines how the task is run.

</dd> <dt>

*sessionID* \[in\]
</dt> <dd>

The terminal server session in which you want to launch the task.

If the TASK\_RUN\_USE\_SESSION\_ID constant (0x4) is not passed into the *flags* parameter, then the value specified in this parameter is ignored. If the TASK\_RUN\_USE\_SESSION\_ID constant is passed into the *flags* parameter and the sessionID value is less than or equal to 0, then an invalid argument error will be returned.

If the TASK\_RUN\_USE\_SESSION\_ID constant is passed into the *flags* parameter and the sessionID value is a valid session ID greater than 0 and if no value is specified for the *user* parameter, then the Task Scheduler service will try to launch the task interactively as the user who is logged on to the specified session.

If the TASK\_RUN\_USE\_SESSION\_ID constant is passed into the *flags* parameter and the sessionID value is a valid session ID greater than 0 and if a user is specified in the *user* parameter, then the Task Scheduler service will try to launch the task interactively as the user who is specified in the *user* parameter.

</dd> <dt>

*runningTask* \[out\]
</dt> <dd>

A [**RunningTask**](runningtask.md) object that defines the new instance of the task.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This method will return without error, but the task will not run if the [**TaskSettings.AllowDemandStart**](tasksettings-allowdemandstart.md) property is set to false for the registered task.

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
</dt> </dl>

 

 





