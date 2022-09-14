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


| Action | Properties | 
|--------|------------|
| COM Handler Action | C++:<ul><li><a href="/windows/desktop/api/taskschd/nf-taskschd-icomhandleraction-get_classid"><strong>ClassId Property of IComHandlerAction</strong></a></li><li><a href="/windows/desktop/api/taskschd/nf-taskschd-icomhandleraction-get_data"><strong>Data Property of IComHandlerAction</strong></a></li></ul><br /> Scripting:<ul><li><a href="comhandleraction-classid.md"><strong>ComHandlerAction.ClassId</strong></a></li><li><a href="comhandleraction-data.md"><strong>ComHandlerAction.Data</strong></a></li></ul><br /> | 
| Email Action | C++:<ul><li><a href="/windows/desktop/api/taskschd/nf-taskschd-iemailaction-get_body"><strong>Body Property of IEmailAction</strong></a></li><li><a href="/windows/desktop/api/taskschd/nf-taskschd-iemailaction-get_server"><strong>Server Property of IEmailAction</strong></a></li><li><a href="/windows/desktop/api/taskschd/nf-taskschd-iemailaction-get_subject"><strong>Subject Property of IEmailAction</strong></a></li><li><a href="/windows/desktop/api/taskschd/nf-taskschd-iemailaction-get_to"><strong>To Property of IEmailAction</strong></a></li><li><a href="/windows/desktop/api/taskschd/nf-taskschd-iemailaction-get_cc"><strong>Cc Property of IEmailAction</strong></a></li><li><a href="/windows/desktop/api/taskschd/nf-taskschd-iemailaction-get_bcc"><strong>Bcc Property of IEmailAction</strong></a></li><li><a href="/windows/desktop/api/taskschd/nf-taskschd-iemailaction-get_replyto"><strong>ReplyTo Property of IEmailAction</strong></a></li><li><a href="/windows/desktop/api/taskschd/nf-taskschd-iemailaction-get_from"><strong>From Property of IEmailAction</strong></a></li></ul><br /> Scripting:<ul><li><a href="emailaction-body.md"><strong>EmailAction.Body</strong></a></li><li><a href="emailaction-server.md"><strong>EmailAction.Server</strong></a></li><li><a href="emailaction-subject.md"><strong>EmailAction.Subject</strong></a></li><li><a href="emailaction-to.md"><strong>EmailAction.To</strong></a></li><li><a href="emailaction-cc.md"><strong>EmailAction.Cc</strong></a></li><li><a href="emailaction-bcc.md"><strong>EmailAction.Bcc</strong></a></li><li><a href="emailaction-replyto.md"><strong>EmailAction.ReplyTo</strong></a></li><li><a href="emailaction-from.md"><strong>EmailAction.From</strong></a></li></ul><br /> | 
| Exec Action | C++:<ul><li><a href="/windows/desktop/api/taskschd/nf-taskschd-iexecaction-get_arguments"><strong>Arguments Property of IExecAction</strong></a></li><li><a href="/windows/desktop/api/taskschd/nf-taskschd-iexecaction-get_workingdirectory"><strong>WorkingDirectory Property of IExecAction</strong></a></li></ul><br /> Scripting:<ul><li><a href="execaction-arguments.md"><strong>ExecAction.Arguments</strong></a></li><li><a href="execaction-workingdirectory.md"><strong>ExecAction.WorkingDirectory</strong></a></li></ul><br /> | 
| Show Message Action | C++:<ul><li><a href="/windows/desktop/api/taskschd/nf-taskschd-ishowmessageaction-get_title"><strong>Title Property of IShowMessageAction</strong></a></li><li><a href="/windows/desktop/api/taskschd/nf-taskschd-ishowmessageaction-get_messagebody"><strong>MessageBody Property of IShowMessageAction</strong></a></li></ul><br /> Scripting:<ul><li><a href="showmessageaction-title.md"><strong>ShowMessageAction.Title</strong></a></li><li><a href="showmessageaction-messagebody.md"><strong>ShowMessageAction.MessageBody</strong></a></li></ul><br /> | 




 

## Related topics

<dl> <dt>

[About The Task Scheduler](about-the-task-scheduler.md)
</dt> </dl>

 

 





