---
title: Logon Trigger Example (Scripting)
description: This scripting example shows how to create a task that is scheduled to execute Notepad when a user logs on.
ms.assetid: f25e105f-9439-4646-bdfd-609ee99a5d55
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Logon Trigger Example (Scripting)

This scripting example shows how to create a task that is scheduled to execute Notepad when a user logs on. The task contains a logon trigger that specifies a start boundary for the task to start and a user identifier that specifies the user. The task is registered using the Administrators group as a security context to run the task.

The following procedure describes how to schedule an executable such as Notepad to start when a specified user logs on.

**To schedule Notepad to start when a user logs on**

1.  Create a [**TaskService**](taskservice.md) object. This object allows you to create the task in a specified folder.
2.  Get a task folder and create a task. Use the [**TaskService.GetFolder**](taskservice-getfolder.md) method to get the folder where the task is stored and the [**TaskService.NewTask**](taskservice-newtask.md) method to create the [**TaskDefinition**](taskdefinition.md) object that represents the task.
3.  Define information about the task using the [**TaskDefinition**](taskdefinition.md) object. Use the [**TaskDefinition.Settings**](taskdefinition-settings.md) property to define the settings that determine how the Task Scheduler service performs the task and the [**TaskDefinition.RegistrationInfo**](taskdefinition-registrationinfo.md) property to define the information that describes the task.
4.  Create a logon trigger using the [**TaskDefinition.Triggers**](taskdefinition-triggers.md) property. This property provides access to the [**TriggerCollection**](triggercollection.md) object. Use the [**TriggerCollection.Create**](triggercollection-create.md) method (specifying the type of trigger that you want to create) to create a logon trigger. As you create the trigger, set the start boundary and end boundary of the trigger to activate and deactivate the trigger. You must set the [**UserId**](/windows/desktop/api/taskschd/nf-taskschd-ilogontrigger-get_userid) property for the trigger so that the task's actions will be scheduled to execute when the specified user logs on after the start boundary.
5.  Create an action for the task to execute by using the [**TaskDefinition.Actions**](taskdefinition-actions.md) property. This property provides access to the [**ActionCollection**](actioncollection.md) object. Use the [**ActionCollection.Create**](actioncollection-create.md) method to specify the type of action that you want to create. This example uses an [**ExecAction**](execaction.md) object, which represents an action that starts an executable.
6.  Register the task using the [**TaskFolder.RegisterTaskDefinition**](taskfolder-registertaskdefinition.md) method. This example registers the task so that it uses the Administrators group as a security context to run the task.

The following VBScript example shows how to schedule a task to execute Notepad when a user logs on.


```VB
'---------------------------------------------------------
' This sample schedules a task to start notepad.exe when a user logs on.
'---------------------------------------------------------

' A constant that specifies a logon trigger.
const TriggerTypeLogon = 9
' A constant that specifies an executable action.
const ActionTypeExecutable = 0   

'********************************************************
' Create the TaskService object.
Set service = CreateObject("Schedule.Service")
call service.Connect()

'********************************************************
' Get a folder to create a task definition in. 
Dim rootFolder
Set rootFolder = service.GetFolder("\")

' The taskDefinition variable is the TaskDefinition object.
Dim taskDefinition
' The flags parameter is 0 because it is not supported.
Set taskDefinition = service.NewTask(0) 

'********************************************************
' Define information about the task.

' Set the registration info for the task by 
' creating the RegistrationInfo object.
Dim regInfo
Set regInfo = taskDefinition.RegistrationInfo
regInfo.Description = "Task will execute Notepad when a " & _
    "specified user logs on."
regInfo.Author = "Author Name"

' Set the task setting info for the Task Scheduler by
' creating a TaskSettings object.
Dim settings
Set settings = taskDefinition.Settings
settings.StartWhenAvailable = True

'********************************************************
' Create a logon trigger.
Dim triggers
Set triggers = taskDefinition.Triggers

Dim trigger
Set trigger = triggers.Create(TriggerTypeLogon)

' Trigger variables that define when the trigger is active.
Dim startTime, endTime
startTime = "2006-05-02T10:49:02"
endTime = "2006-05-02T10:52:02"

WScript.Echo "startTime :" & startTime
WScript.Echo "endTime :" & endTime

trigger.StartBoundary = startTime
trigger.EndBoundary = endTime
trigger.ExecutionTimeLimit = "PT5M"    ' Five minutes
trigger.Id = "LogonTriggerId"
trigger.UserId = "DOMAIN\UserName"   ' Must be a valid user account   

'***********************************************************
' Create the action for the task to execute.

' Add an action to the task. The action executes notepad.
Dim Action
Set Action = taskDefinition.Actions.Create( ActionTypeExecutable )
Action.Path = "C:\Windows\System32\notepad.exe"

WScript.Echo "Task definition created. About to submit the task..."

'***********************************************************
' Register (create) the task.
const createOrUpdateTask = 6
call rootFolder.RegisterTaskDefinition( _
    "Test Logon Trigger", taskDefinition, createOrUpdateTask, _
    "Builtin\Administrators", , 4)

WScript.Echo "Task submitted."
```



## Related topics

<dl> <dt>

[Using the Task Scheduler](using-the-task-scheduler.md)
</dt> </dl>

 

 




