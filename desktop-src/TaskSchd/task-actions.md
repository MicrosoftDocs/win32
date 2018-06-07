---
title: Task Actions
description: The work items performed by a task are called actions. A task can have a single action or a maximum of 32 actions. Be aware that when multiple actions are specified, they are executed sequentially.
ms.assetid: 4cbe739d-4c4e-4469-8289-4be41b93950c
keywords:
- actions Task Scheduler
- actions Task Scheduler , described
- actions Task Scheduler , execute action
- actions Task Scheduler , COM handler action
- execute action Task Scheduler
- COM Handler action Task Scheduler
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Task Actions

The work items performed by a task are called actions. A task can have a single action or a maximum of 32 actions. Be aware that when multiple actions are specified, they are executed sequentially.

## Types of Actions

The following table of actions describes the type of work or actions that can be accomplished by a task.

| Type of Action      | Description                                                             |
|---------------------|-------------------------------------------------------------------------|
| ComHandler Action   | This action fires a COM handler.                                        |
| Exec Action         | This action executes a command-line operation such as starting Notepad. |
| E-mail Action       | This action sends an email when a task is triggered.                    |
| Show Message Action | This action shows a message box with a specified message and title.     |



 

## Specifying Actions

The actions of a task are specified when the task is defined and stored in a collection of actions used by the Task Scheduler service. The following table lists links to reference topics for the APIs and XML elements that are associated with actions.

For more information and examples about how to use the Task Scheduler interfaces, scripting objects, and XML, see [Using the Task Scheduler](using-the-task-scheduler.md).

### Interface APIs for C++ Development



| API                                                                    | Description                                                  |
|------------------------------------------------------------------------|--------------------------------------------------------------|
| [**Actions Property of ITaskDefinition**](/windows/desktop/api/taskschd/nf-taskschd-itaskdefinition-get_actions) | Gets or sets the actions performed by the task.              |
| [**IActionCollection**](/windows/desktop/api/taskschd/nn-taskschd-iactioncollection)                         | Contains the actions performed by the task.                  |
| [**IComHandlerAction**](/windows/desktop/api/taskschd/nn-taskschd-icomhandleraction)                         | Represents an action that fires a handler.                   |
| [**IExecAction**](/windows/desktop/api/taskschd/nn-taskschd-iexecaction)                                     | Represents an action that executes a command-line operation. |
| [**IEmailAction**](/windows/desktop/api/taskschd/nn-taskschd-iemailaction)                                   | Represents an action that sends an email message.            |
| [**IShowMessageAction**](/windows/desktop/api/taskschd/nn-taskschd-ishowmessageaction)                       | Represents an action that shows a message box.               |



 

### Scripting Object APIs for Scripting Development



| API                                                      | Description                                                  |
|----------------------------------------------------------|--------------------------------------------------------------|
| [**TaskDefinition.Actions**](taskdefinition-actions.md) | Gets or sets the actions performed by the task.              |
| [**ActionCollection**](actioncollection.md)             | Contains the actions performed by the task.                  |
| [**ComHandlerAction**](comhandleraction.md)             | Represents an action that fires a handler.                   |
| [**ExecAction**](execaction.md)                         | Represents an action that executes a command-line operation. |
| [**EmailAction**](emailaction.md)                       | Represents an action that sends an email message.            |
| [**ShowMessageAction**](showmessageaction.md)           | Represents an action that shows a message box.               |



 

### XML Elements



| Element                                                                    | Description                                                  |
|----------------------------------------------------------------------------|--------------------------------------------------------------|
| [**Actions**](taskschedulerschema-actions-tasktype-element.md)            | Defines the actions performed by the task.                   |
| [**ComHandler**](taskschedulerschema-comhandler-actiongroup-element.md)   | Represents an action that fires a handler.                   |
| [**Exec**](taskschedulerschema-exec-actiongroup-element.md)               | Represents an action that executes a command-line operation. |
| [**SendEmail**](taskschedulerschema-sendemail-actiongroup-element.md)     | Represents an action that sends an email message.            |
| [**ShowMessage**](taskschedulerschema-showmessage-actiongroup-element.md) | Represents an action that shows a message box.               |



 

## Using Variables in Action Properties

Some action properties that are of type **BSTR** can contain $(Arg0), $(Arg1), ..., $(Arg32) variables in their string values. These variables are replaced with the values that are specified in the *params* parameter of the [**IRegisteredTask::Run**](/windows/desktop/api/taskschd/nf-taskschd-iregisteredtask-run) and [**IRegisteredTask::RunEx**](/windows/desktop/api/taskschd/nf-taskschd-iregisteredtask-runex) methods or are contained within the event trigger for the task. The following table lists the action properties that can use variables in their string values.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Action</th>
<th>Properties</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>COM Handler Action</td>
<td>C++:
<ul>
<li>[<strong>ClassId Property of IComHandlerAction</strong>](/windows/desktop/api/taskschd/nf-taskschd-icomhandleraction-get_classid)</li>
<li>[<strong>Data Property of IComHandlerAction</strong>](/windows/desktop/api/taskschd/nf-taskschd-icomhandleraction-get_data)</li>
</ul>
<br/> Scripting:
<ul>
<li>[<strong>ComHandlerAction.ClassId</strong>](comhandleraction-classid.md)</li>
<li>[<strong>ComHandlerAction.Data</strong>](comhandleraction-data.md)</li>
</ul>
<br/></td>
</tr>
<tr class="even">
<td>Email Action</td>
<td>C++:
<ul>
<li>[<strong>Body Property of IEmailAction</strong>](/windows/desktop/api/taskschd/nf-taskschd-iemailaction-get_body)</li>
<li>[<strong>Server Property of IEmailAction</strong>](/windows/desktop/api/taskschd/nf-taskschd-iemailaction-get_server)</li>
<li>[<strong>Subject Property of IEmailAction</strong>](/windows/desktop/api/taskschd/nf-taskschd-iemailaction-get_subject)</li>
<li>[<strong>To Property of IEmailAction</strong>](/windows/desktop/api/taskschd/nf-taskschd-iemailaction-get_to)</li>
<li>[<strong>Cc Property of IEmailAction</strong>](/windows/desktop/api/taskschd/nf-taskschd-iemailaction-get_cc)</li>
<li>[<strong>Bcc Property of IEmailAction</strong>](/windows/desktop/api/taskschd/nf-taskschd-iemailaction-get_bcc)</li>
<li>[<strong>ReplyTo Property of IEmailAction</strong>](/windows/desktop/api/taskschd/nf-taskschd-iemailaction-get_replyto)</li>
<li>[<strong>From Property of IEmailAction</strong>](/windows/desktop/api/taskschd/nf-taskschd-iemailaction-get_from)</li>
</ul>
<br/> Scripting:
<ul>
<li>[<strong>EmailAction.Body</strong>](emailaction-body.md)</li>
<li>[<strong>EmailAction.Server</strong>](emailaction-server.md)</li>
<li>[<strong>EmailAction.Subject</strong>](emailaction-subject.md)</li>
<li>[<strong>EmailAction.To</strong>](emailaction-to.md)</li>
<li>[<strong>EmailAction.Cc</strong>](emailaction-cc.md)</li>
<li>[<strong>EmailAction.Bcc</strong>](emailaction-bcc.md)</li>
<li>[<strong>EmailAction.ReplyTo</strong>](emailaction-replyto.md)</li>
<li>[<strong>EmailAction.From</strong>](emailaction-from.md)</li>
</ul>
<br/></td>
</tr>
<tr class="odd">
<td>Exec Action</td>
<td>C++:
<ul>
<li>[<strong>Arguments Property of IExecAction</strong>](/windows/desktop/api/taskschd/nf-taskschd-iexecaction-get_arguments)</li>
<li>[<strong>WorkingDirectory Property of IExecAction</strong>](/windows/desktop/api/taskschd/nf-taskschd-iexecaction-get_workingdirectory)</li>
</ul>
<br/> Scripting:
<ul>
<li>[<strong>ExecAction.Arguments</strong>](execaction-arguments.md)</li>
<li>[<strong>ExecAction.WorkingDirectory</strong>](execaction-workingdirectory.md)</li>
</ul>
<br/></td>
</tr>
<tr class="even">
<td>Show Message Action</td>
<td>C++:
<ul>
<li>[<strong>Title Property of IShowMessageAction</strong>](/windows/desktop/api/taskschd/nf-taskschd-ishowmessageaction-get_title)</li>
<li>[<strong>MessageBody Property of IShowMessageAction</strong>](/windows/desktop/api/taskschd/nf-taskschd-ishowmessageaction-get_messagebody)</li>
</ul>
<br/> Scripting:
<ul>
<li>[<strong>ShowMessageAction.Title</strong>](showmessageaction-title.md)</li>
<li>[<strong>ShowMessageAction.MessageBody</strong>](showmessageaction-messagebody.md)</li>
</ul>
<br/></td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[About The Task Scheduler](about-the-task-scheduler.md)
</dt> </dl>

 

 





