---
title: RegisteredTask.Run method
description: For scripting, runs the registered task immediately.
ms.assetid: '99c8f6ea-6dcf-4f9a-bf61-5191df5958c6'
keywords:
- Run method Task Scheduler
- Run method Task Scheduler , RegisteredTask object
- RegisteredTask object Task Scheduler , Run method
topic_type:
- apiref
api_name:
- RegisteredTask.Run
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# RegisteredTask.Run method

For scripting, runs the registered task immediately.

## Syntax


```VB
RegisteredTask.Run( _
  ByVal params, _
  ByRef ppRunningTask _
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

*ppRunningTask* \[out\]
</dt> <dd>

A [**RunningTask**](runningtask.md) object that defines the new instance of the task.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The **RegisteredTask.Run** function is equivalent to the [**RegisteredTask.RunEx**](registeredtask-runex.md) function with the flags parameter equal to 0 and nothing specified for the user parameter.

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

 

 





