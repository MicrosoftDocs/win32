---
title: ActionCollection.Create method
description: For scripting, creates and adds a new action to the collection.
ms.assetid: f33542e1-ee49-4696-b2ab-c48a9b5440d4
keywords:
- Create method Task Scheduler
- Create method Task Scheduler , ActionCollection object
- ActionCollection object Task Scheduler , Create method
topic_type:
- apiref
api_name:
- ActionCollection.Create
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ActionCollection.Create method

For scripting, creates and adds a new action to the collection.

## Syntax


```VB
ActionCollection.Create( _
  ByVal type _
)
```



## Parameters

<dl> <dt>

*type* \[in\]
</dt> <dd>

This parameter is set to one of the following [**TASK\_ACTION\_TYPE**](/windows/desktop/api/taskschd/ne-taskschd-task_action_type) enumeration constants.



| Value                                                                                                                                                                                                                                                   | Meaning                                                                                                                                                                                                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TASK_ACTION_EXEC"></span><span id="task_action_exec"></span><dl> <dt>**TASK\_ACTION\_EXEC**</dt> <dt>0</dt> </dl>                          | The action performs a command-line operation. For example, the action could run a script, launch an executable, or, if the name of a document is provided, find its associated application and launch the application with the document.<br/> |
| <span id="TASK_ACTION_COM_HANDLER"></span><span id="task_action_com_handler"></span><dl> <dt>**TASK\_ACTION\_COM\_HANDLER**</dt> <dt>5</dt> </dl>    | The action fires a handler.<br/>                                                                                                                                                                                                              |
| <span id="TASK_ACTION_SEND_EMAIL"></span><span id="task_action_send_email"></span><dl> <dt>**TASK\_ACTION\_SEND\_EMAIL**</dt> <dt>6</dt> </dl>       | This action sends email message.<br/>                                                                                                                                                                                                         |
| <span id="TASK_ACTION_SHOW_MESSAGE"></span><span id="task_action_show_message"></span><dl> <dt>**TASK\_ACTION\_SHOW\_MESSAGE**</dt> <dt>7</dt> </dl> | This action shows a message box.<br/>                                                                                                                                                                                                         |



 

</dd> </dl>

## Return value

An [**Action**](action.md) object that represents the new action.

## Remarks

You cannot add more than 32 actions to the collection.

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

[**ActionCollection**](actioncollection.md)
</dt> <dt>

[**Action**](action.md)
</dt> <dt>

[**ExecAction**](execaction.md)
</dt> <dt>

[**EmailAction**](emailaction.md)
</dt> <dt>

[**ShowMessageAction**](showmessageaction.md)
</dt> <dt>

[**ComHandlerAction**](comhandleraction.md)
</dt> </dl>

 

 





