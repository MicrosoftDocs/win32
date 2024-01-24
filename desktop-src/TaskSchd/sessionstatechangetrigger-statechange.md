---
title: SessionStateChangeTrigger.StateChange property
description: For scripting, gets or sets the kind of Terminal Server session change that would trigger a task launch.
ms.assetid: 'ae1460c7-2939-4fcb-b7fc-edc859596bc4'
keywords:
- StateChange property Task Scheduler
- StateChange property Task Scheduler , SessionStateChangeTrigger object
- SessionStateChangeTrigger object Task Scheduler , StateChange property
topic_type:
- apiref
api_name:
- SessionStateChangeTrigger.StateChange
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SessionStateChangeTrigger.StateChange property

For scripting, gets or sets the kind of Terminal Server session change that would trigger a task launch.

## Syntax


```VB
SessionStateChangeTrigger.StateChange As Integer
```



## Property value

The kind of Terminal Server session change that triggers a task to launch.

The possible values are from the [**TASK\_SESSION\_STATE\_CHANGE\_TYPE**](/windows/desktop/api/taskschd/ne-taskschd-task_session_state_change_type) enumeration.



| Value                                                                                                                                                                                                                                               | Meaning                                                                                                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TASK_CONSOLE_CONNECT"></span><span id="task_console_connect"></span><dl> <dt>**TASK\_CONSOLE\_CONNECT**</dt> <dt>1</dt> </dl>          | Terminal Server console connection state change. For example, when you connect to a user session on the local computer by switching users on the computer. <br/>                           |
| <span id="TASK_CONSOLE_DISCONNECT"></span><span id="task_console_disconnect"></span><dl> <dt>**TASK\_CONSOLE\_DISCONNECT**</dt> <dt>2</dt> </dl> | Terminal Server console disconnection state change. For example, when you disconnect to a user session on the local computer by switching users on the computer.<br/>                      |
| <span id="TASK_REMOTE_CONNECT"></span><span id="task_remote_connect"></span><dl> <dt>**TASK\_REMOTE\_CONNECT**</dt> <dt>3</dt> </dl>             | Terminal Server remote connection state change. For example, when a user connects to a user session by using the Remote Desktop Connection program from a remote computer.<br/>            |
| <span id="TASK_REMOTE_DISCONNECT"></span><span id="task_remote_disconnect"></span><dl> <dt>**TASK\_REMOTE\_DISCONNECT**</dt> <dt>4</dt> </dl>    | Terminal Server remote disconnection state change. For example, when a user disconnects from a user session while using the Remote Desktop Connection program from a remote computer.<br/> |
| <span id="TASK_SESSION_LOCK"></span><span id="task_session_lock"></span><dl> <dt>**TASK\_SESSION\_LOCK**</dt> <dt>7</dt> </dl>                   | Terminal Server session locked state change. For example, this state change causes the task to run when the computer is locked. <br/>                                                      |
| <span id="TASK_SESSION_UNLOCK"></span><span id="task_session_unlock"></span><dl> <dt>**TASK\_SESSION\_UNLOCK**</dt> <dt>8</dt> </dl>             | Terminal Server session unlocked state change. For example, this state change causes the task to run when the computer is unlocked.<br/>                                                   |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



 

 





