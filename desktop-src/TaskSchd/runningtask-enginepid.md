---
title: RunningTask.EnginePID property
description: For scripting, gets the process ID for the engine (process) which is running the task.
ms.assetid: 'cb8a0f2f-ebe3-4f52-8fbd-b0cebb539728'
keywords:
- EnginePID property Task Scheduler
- EnginePID property Task Scheduler , RunningTask object
- RunningTask object Task Scheduler , EnginePID property
topic_type:
- apiref
api_name:
- RunningTask.EnginePID
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# RunningTask.EnginePID property

For scripting, gets the process ID for the engine (process) which is running the task.

This property is read-only.

## Syntax


```VB
RunningTask.EnginePID As Integer
```



## Property value

The process ID for the engine which is running the task.

## Remarks

The process ID returned by this property cannot be appended directly to a string. The returned value needs to be converted to an integer value first by calling the [CInt](/previous-versions//fctcwhw9(v=vs.85)) function on the returned value.


```VB
ProcessId = cint(RunningTask.EnginePID)
wscript.echo "Process Id of Engine is " & "ProcessId
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



 

