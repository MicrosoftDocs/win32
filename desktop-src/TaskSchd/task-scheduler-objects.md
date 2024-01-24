---
title: Task Scheduler Scripting Objects
description: The scripting objects that are described in the following topics provide programmatic access to the functionality that is available within the Task Scheduler for Visual Basic and Visual Basic script developers.
ms.assetid: 632bc9ae-b300-42ed-9d2c-f1d2d53d44fb
keywords:
- Task Scheduler Task Scheduler , reference, scripting objects
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Task Scheduler Scripting Objects

The scripting objects that are described in the following topics provide programmatic access to the functionality that is available within the Task Scheduler for Visual Basic and Visual Basic script developers.


The following objects are introduced in Task Scheduler 2.0.



| Object                                                         | Description                                                                                                                                                                                                                                           |
|----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Action**](action.md)                                       | Provides the common properties that are inherited by all action objects.                                                                                                                                                                              |
| [**ActionCollection**](actioncollection.md)                   | Contains the actions performed by the task.                                                                                                                                                                                                           |
| [**BootTrigger**](boottrigger.md)                             | Represents a trigger that starts a task when the system is booted.                                                                                                                                                                                    |
| [**ComHandlerAction**](comhandleraction.md)                   | Represents an action that fires a handler.                                                                                                                                                                                                            |
| [**DailyTrigger**](dailytrigger.md)                           | Represents a trigger that starts a task based on a daily schedule.                                                                                                                                                                                    |
| [**EmailAction**](emailaction.md)                             | Represents an action that sends an email message.                                                                                                                                                                                                     |
| [**EventTrigger**](eventtrigger.md)                           | Represents a trigger that starts a task when a system event occurs.                                                                                                                                                                                   |
| [**ExecAction**](execaction.md)                               | Represents an action that executes a command-line operation.                                                                                                                                                                                          |
| [**IdleSettings**](idlesettings.md)                           | Specifies how the Task Scheduler performs tasks when the computer is in an idle condition.                                                                                                                                                            |
| [**IdleTrigger**](idletrigger.md)                             | Represents a trigger that starts a task when an idle condition occurs.                                                                                                                                                                                |
| [**LogonTrigger**](logontrigger.md)                           | Represents a trigger that starts a task when a user logs on.                                                                                                                                                                                          |
| [**MonthlyDOWTrigger**](monthlydowtrigger.md)                 | Represents a trigger that starts a task on a monthly day-of-week schedule.                                                                                                                                                                            |
| [**MonthlyTrigger**](monthlytrigger.md)                       | Represents a trigger that starts a task based on a monthly schedule.                                                                                                                                                                                  |
| [**NetworkSettings**](networksettings.md)                     | Provides the settings that the Task Scheduler service uses to obtain a network profile.                                                                                                                                                               |
| [**Principal**](principal.md)                                 | Provides the security credentials for a principal.                                                                                                                                                                                                    |
| [**RegisteredTask**](registeredtask.md)                       | Provides the methods that are used to run the task immediately, get any running instances of the task, get or set the credentials that are used to register the task, and the properties that describe the task.                                      |
| [**RegisteredTaskCollection**](registeredtaskcollection.md)   | Contains all the tasks that are registered.                                                                                                                                                                                                           |
| [**RegistrationInfo**](registrationinfo.md)                   | Provides the administrative information that can be used to describe the task. This information includes details such as a description of the task, the author of the task, the date the task is registered, and the security descriptor of the task. |
| [**RegistrationTrigger**](registrationtrigger.md)             | Represents a trigger that starts a task when the task is registered.                                                                                                                                                                                  |
| [**RepetitionPattern**](repetitionpattern.md)                 | Defines how often the task is run and how long the repetition pattern is repeated after the task is started.                                                                                                                                          |
| [**RunningTask**](runningtask.md)                             | Provides the methods to get information from and control a running task.                                                                                                                                                                              |
| [**RunningTaskCollection**](runningtaskcollection.md)         | Used to retrieve a running task.                                                                                                                                                                                                                      |
| [**SessionStateChangeTrigger**](sessionstatechangetrigger.md) | Used to trigger tasks for console connect or disconnect, remote connect or disconnect, or workstation lock or unlock notifications.                                                                                                                   |
| [**ShowMessageAction**](showmessageaction.md)                 | Represents an action that shows a message box when a task is activated.                                                                                                                                                                               |
| [**TaskDefinition**](taskdefinition.md)                       | Defines all the components of a task, such as the task settings, triggers, actions, and registration information.                                                                                                                                     |
| [**TaskFolder**](taskfolder.md)                               | Provides the methods that are used to register (create) tasks in the folder, remove tasks from the folder, and create or remove subfolders from the folder.                                                                                           |
| [**TaskFolderCollection**](taskfoldercollection.md)           | Counts the number of folders in the collection and retrieve a specified folder from the collection.                                                                                                                                                   |
| [**TaskNamedValuePair**](tasknamedvaluepair.md)               | Creates a name-value pair in which the name is associated with the value.                                                                                                                                                                             |
| [**TaskNamedValueCollection**](tasknamedvaluecollection.md)   | Contains a collection of [**TaskNamedValuePair**](tasknamedvaluepair.md) object name-value pairs.                                                                                                                                                    |
| [**TaskService**](taskservice.md)                             | Provides access to the Task Scheduler service for managing registered tasks.                                                                                                                                                                          |
| [**TaskSettings**](tasksettings.md)                           | Provides the settings that the Task Scheduler services uses to perform the task.                                                                                                                                                                      |
| [**TaskVariables**](taskvariables.md)                         | Defines task variables that can be passed as parameters to task handlers and external executables that are launched by tasks.                                                                                                                         |
| [**TimeTrigger**](timetrigger.md)                             | Represents a trigger that starts a task when the trigger is activated.                                                                                                                                                                                |
| [**Trigger**](trigger.md)                                     | Provides the common properties that are inherited by all trigger objects.                                                                                                                                                                             |
| [**TriggerCollection**](triggercollection.md)                 | Used to add to, remove from, and retrieve the triggers of a task.                                                                                                                                                                                     |
| [**WeeklyTrigger**](weeklytrigger.md)                         | Represents a trigger that starts a task based on a weekly schedule.                                                                                                                                                                                   |



 

## Related topics

<dl> <dt>

[Task Scheduler Reference](task-scheduler-reference.md)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 




