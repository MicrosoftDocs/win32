---
title: Action.Type property
description: For scripting, gets the type of the action.
ms.assetid: 6a0bca3d-9016-4167-9f6e-2cc95bafdb95
keywords:
- Type property Task Scheduler
- Type property Task Scheduler , Action object
- Action object Task Scheduler , Type property
topic_type:
- apiref
api_name:
- Action.Type
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Action.Type property

For scripting, gets the type of the action.

## Syntax


```VB
Action.Type As Integer
```



## Property value

This property returns one of the following [**TASK\_ACTION\_TYPE**](/windows/desktop/api/taskschd/ne-taskschd-task_action_type) enumeration constants.



| Value                                                                                                                                                                                                                                                   | Meaning                                                                                                                                                                                                                                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TASK_ACTION_EXEC"></span><span id="task_action_exec"></span><dl> <dt>**TASK\_ACTION\_EXEC**</dt> <dt>0</dt> </dl>                          | This action performs a command-line operation. For example, the action could run a script, launch an executable, or, if the name of a document is provided, find its associated application and launch the application with the document.<br/> |
| <span id="TASK_ACTION_COM_HANDLER"></span><span id="task_action_com_handler"></span><dl> <dt>**TASK\_ACTION\_COM\_HANDLER**</dt> <dt>5</dt> </dl>    | This action fires a handler.<br/>                                                                                                                                                                                                              |
| <span id="TASK_ACTION_SEND_EMAIL"></span><span id="task_action_send_email"></span><dl> <dt>**TASK\_ACTION\_SEND\_EMAIL**</dt> <dt>6</dt> </dl>       | This action sends an email message.<br/>                                                                                                                                                                                                       |
| <span id="TASK_ACTION_SHOW_MESSAGE"></span><span id="task_action_show_message"></span><dl> <dt>**TASK\_ACTION\_SHOW\_MESSAGE**</dt> <dt>7</dt> </dl> | This action shows a message box.<br/>                                                                                                                                                                                                          |



 

## Remarks

The action type is defined when the action is created and cannot be changed later. For information on creating an action, see [**ActionCollection.Create**](actioncollection-create.md).

For information on how actions and tasks work together, see [Task Actions](task-actions.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[**TASK\_ACTION\_TYPE**](/windows/desktop/api/taskschd/ne-taskschd-task_action_type)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> <dt>

[**Action**](action.md)
</dt> </dl>

 

 





