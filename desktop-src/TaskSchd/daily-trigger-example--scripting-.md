---
title: Daily Trigger Example (Scripting)
description: This scripting example shows how to create a task that runs Notepad at 8 00 AM every day.
ms.assetid: a13bd54d-b45a-46e5-8281-d080f50f6bef
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Daily Trigger Example (Scripting)

This scripting example shows how to create a task that runs Notepad at 8:00 AM every day. The task contains a daily trigger that specifies a start boundary to activate the trigger and to specify the time of day that the task runs, a trigger interval to specify that the task runs every day, and an end boundary to deactivates the trigger. The example also shows how to set a repetition pattern for the trigger to repeat the task. The task also contains an executable action that runs Notepad.

The following procedure describes how to schedule a task to start an executable at 8:00 AM every day. (These steps correspond to the code comments included in the example code.)

**To schedule Notepad to start at 8:00 AM every day**

1.  Create a [**TaskService**](taskservice.md) object. This object allows you to create the task in a specified folder.
2.  Get a task folder and create a task. Use the [**TaskService.GetFolder**](taskservice-getfolder.md) method to get the folder where the task is stored and the [**TaskService.NewTask**](taskservice-newtask.md) method to create the [**TaskDefinition**](taskdefinition.md) object that represents the task.
3.  Define information about the task using the [**TaskDefinition**](taskdefinition.md) object. Use the [**TaskDefinition.Settings**](taskdefinition-settings.md) property to define the settings that determine how the Task Scheduler service performs the task and the [**TaskDefinition.RegistrationInfo**](taskdefinition-registrationinfo.md) property to define the information that describes the task.
4.  Create a daily trigger using the [**TaskDefinition.Triggers**](taskdefinition-triggers.md) property. This property provides access to the [**TriggerCollection**](triggercollection.md) object that is used to create the trigger. Use the [**TriggerCollection.Create**](triggercollection-create.md) method (specifying the type of trigger you want to create) to create a daily trigger. As you create the trigger, set the start boundary to activate the trigger and specify the time of day that the task runs, the interval between the days, and the end boundary to deactivate the trigger. The example below shows how to set a repetition pattern for the trigger to repeat the task.
5.  Create an action for the task to execute by using the [**TaskDefinition.Actions**](taskdefinition-actions.md) property. This property provides access to the [**ActionCollection**](actioncollection.md) object used to create the action. Use the [**ActionCollection.Create**](actioncollection-create.md) method to specify the type of action you want to create. This example uses an [**ExecAction**](execaction.md) object, which represents an action that executes a command-line operation.
6.  Register the task using the [**TaskFolder.RegisterTaskDefinition**](taskfolder-registertaskdefinition.md) method. For this example the task will start Notepad at 8:00 AM every day.

The following VBScript example shows how to schedule a task to execute Notepad every day at 8:00 AM.


```VB
'------------------------------------------------------------------
' This sample schedules a task to start on a daily basis.
'------------------------------------------------------------------

' A constant that specifies a daily trigger.
const TriggerTypeDaily = 2
' A constant that specifies an executable action.
const ActionTypeExec = 0

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
regInfo.Description = "Start notepad at 8:00AM daily"
regInfo.Author = "Administrator"

' Set the task setting info for the Task Scheduler by
' creating a TaskSettings object.
Dim settings
Set settings = taskDefinition.Settings
settings.Enabled = True
settings.StartWhenAvailable = True
settings.Hidden = False

'********************************************************
' Create a daily trigger. Note that the start boundary 
' specifies the time of day that the task starts and the 
' interval specifies what days the task is run.
Dim triggers
Set triggers = taskDefinition.Triggers

Dim trigger
Set trigger = triggers.Create(TriggerTypeDaily)

' Trigger variables that define when the trigger is active 
' and the time of day that the task is run. The format of 
' this time is YYYY-MM-DDTHH:MM:SS
Dim startTime, endTime

Dim time
startTime = "2006-05-02T08:00:00"  'Task runs at 8:00 AM
endTime = "2015-05-02T08:00:00"

WScript.Echo "startTime :" & startTime
WScript.Echo "endTime :" & endTime

trigger.StartBoundary = startTime
trigger.EndBoundary = endTime
trigger.DaysInterval = 1    'Task runs every day.
trigger.Id = "DailyTriggerId"
trigger.Enabled = True

' Set the task repetition pattern for the task.
' This will repeat the task 5 times.
Dim repetitionPattern
Set repetitionPattern = trigger.Repetition
repetitionPattern.Duration = "PT4M"
repetitionPattern.Interval = "PT1M"

'***********************************************************
' Create the action for the task to execute.

' Add an action to the task to run notepad.exe.
Dim Action
Set Action = taskDefinition.Actions.Create( ActionTypeExec )
Action.Path = "C:\Windows\System32\notepad.exe"

WScript.Echo "Task definition created. About to submit the task..."

'***********************************************************
' Register (create) the task.

call rootFolder.RegisterTaskDefinition( _
    "Test Daily Trigger", taskDefinition, 6, , , 3)

WScript.Echo "Task submitted."

```



## Related topics

<dl> <dt>

[Using the Task Scheduler](using-the-task-scheduler.md)
</dt> </dl>

 

 




