---
title: Weekly Trigger Example (Scripting)
description: This scripting example shows how to create a task that runs Notepad at 8 00 AM on Monday of every week.
ms.assetid: 68ef73b0-3780-480e-90fe-940b6e8a5340
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Weekly Trigger Example (Scripting)

This scripting example shows how to create a task that runs Notepad at 8:00 AM on Monday of every week. The task contains a daily trigger that specifies when the task runs and an executable action that runs Notepad.

The following procedure describes how to schedule a task to start an executable at 8:00 AM on Monday of every week.

**To schedule Notepad to start at 8:00 AM on Monday of every week**

1.  Create a [**TaskService**](taskservice.md) object. This object allows you to create the task in a specified folder.
2.  Get a task folder and create a task. Use the [**TaskService.GetFolder**](taskservice-getfolder.md) method to get the folder where the task is stored and the [**TaskService.NewTask**](taskservice-newtask.md) method to create the [**TaskDefinition**](taskdefinition.md) object that represents the task.
3.  Define information about the task using the [**TaskDefinition**](taskdefinition.md) object. Use the [**TaskDefinition.Settings**](taskdefinition-settings.md) property to define the settings that determine how the Task Scheduler service performs the task and the [**TaskDefinition.RegistrationInfo**](taskdefinition-registrationinfo.md) property to define the information that describes the task.
4.  Create a weekly trigger using the [**TaskDefinition.Triggers**](taskdefinition-triggers.md) property. This property provides access to the [**TriggerCollection**](triggercollection.md) object that is used to create the trigger.

    Use the [**TriggerCollection.Create**](triggercollection-create.md) method (specifying the type of trigger you want to create) to create a weekly trigger.

    Set the [**WeeklyTrigger.StartBoundary**](trigger-startboundary.md) property to specify when the trigger is activated and the time of the day when the task is run. In this example the trigger is activated on January 1, 2005 and the task runs at 8:00 AM.

    Set the [**WeeklyTrigger.EndBoundary**](trigger-endboundary.md)property to specify when the trigger is deactivated. In this example the trigger is deactivated on January 1, 2015.

    Set the [**WeeklyTrigger.DaysOfWeek**](weeklytrigger-daysofweek.md) property to specify the days of the week on which the task runs. In this example the task is run on Monday.

    Set the [**WeeklyTrigger.WeeksInterval**](weeklytrigger-weeksinterval.md)property to specify the interval between the weeks in the schedule. In this example the task runs every week.

5.  Create an action for the task to execute by using the [**TaskDefinition.Actions**](taskdefinition-actions.md) property. This property provides access to the [**ActionCollection**](actioncollection.md) object used to create the action. Use the [**ActionCollection.Create**](actioncollection-create.md) method to specify the type of action you want to create. This example uses an [**ExecAction**](execaction.md) object, which represents an action that executes a command-line operation.
6.  Register the task using the [**TaskFolder.RegisterTaskDefinition**](taskfolder-registertaskdefinition.md) method. For this example the task will start Notepad at 8:00 AM on Monday of every week.

The following VBScript example shows how to schedule a task to execute Notepad every day at 8:00 AM.


```VB
'------------------------------------------------------------------
' This sample schedules a task to start on a weekly basis.
'------------------------------------------------------------------

' A constant that specifies a weekly trigger.
const TriggerTypeWeekly = 3
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
regInfo.Description = "Start Notepad weekly."
regInfo.Author = "Administrator"

' Set the task setting info for the Task Scheduler by
' creating a TaskSettings object.
Dim settings
Set settings = taskDefinition.Settings
settings.Enabled = True
settings.StartWhenAvailable = True
settings.Hidden = False

'********************************************************
' Create a weekly trigger. Note that the start boundary 
' specifies the time of day that the task starts, the 
' day-of-week specfies on what day of the week the task 
' runs, and the interval specifies what weeks the task runs.
Dim triggers
Set triggers = taskDefinition.Triggers

Dim trigger
Set trigger = triggers.Create(TriggerTypeWeekly)

' Trigger variables that define when the trigger is active 
' and the time of day that the task is run. The format of 
' this tims is YYYY-MM-DDTHH:MM:SS
Dim startTime, endTime

Dim time
startTime = "2006-05-02T08:00:00"  'Task runs at 8:00 AM
endTime = "2015-05-02T08:00:00"

WScript.Echo "startTime :" & startTime
WScript.Echo "endTime :" & endTime

trigger.StartBoundary = startTime
trigger.EndBoundary = endTime
trigger.DaysOfWeek = 1
trigger.WeeksInterval = 1    'Task runs every week.
trigger.Id = "WeeklyTriggerId"
trigger.Enabled = True

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
    "Test Weekly Trigger", taskDefinition, 6, , , 3)

WScript.Echo "Task submitted."

```



## Related topics

<dl> <dt>

[Using the Task Scheduler](using-the-task-scheduler.md)
</dt> </dl>

 

 




