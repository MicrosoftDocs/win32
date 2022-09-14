---
title: Displaying Task Names and States (Scripting)
description: This scripting example shows how to enumerate tasks in a task folder and display property values from each task.
ms.assetid: 2a84a752-fbf3-4041-8b0a-304f89a49354
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Displaying Task Names and States (Scripting)

This scripting example shows how to enumerate tasks in a task folder and display property values from each task.

The following procedure describes how to display task names and states for all the tasks in a task folder.

**To display task names and state for all the tasks in a task folder**

1.  Create the [**TaskService**](taskservice.md) object.

    This object allows you to connect to the Task Scheduler service and access a specific task folder.

2.  Get a task folder that holds the tasks you want information about.

    Use the [**TaskService.GetFolder**](taskservice-getfolder.md) method to get the folder.

3.  Get the collection of tasks from the folder.

    Use the [**TaskFolder.GetTasks**](taskfolder-gettasks.md) method to get the collection of tasks ([**RegisteredTaskCollection**](registeredtaskcollection.md)).

4.  Get the number of tasks in the collection and enumerate through each task in the collection.

    Use the [**RegisteredTaskCollection**](registeredtaskcollection.md) collection of objects to get a [**RegisteredTask**](registeredtask.md) object instance. Each instance will contain a task in the collection. You can then display the information (property values) from each registered task.

The following VBScript example shows how to enumerate through a collection of registered tasks in the root task folder and display the name and state for each task.


```VB
'---------------------------------------------------------
' This sample enumerates through the tasks on the local computer and
' displays their name and state.
'---------------------------------------------------------


' Create the TaskService object.
Set service = CreateObject("Schedule.Service")
call service.Connect()

' Get the task folder that contains the tasks. 
Dim rootFolder
Set rootFolder = service.GetFolder("\")
 
Dim taskCollection
Set taskCollection = rootFolder.GetTasks(0)

Dim numberOfTasks
numberOfTasks = taskCollection.Count

If numberOfTasks = 0 Then 
    Wscript.Echo "No tasks are registered."
Else
    WScript.Echo "Number of tasks registered: " & numberOfTasks
    
    Dim registeredTask
    For Each registeredTask In taskCollection
        WScript.Echo "Task Name: " & registeredTask.Name
    
        Dim taskState 
        Select Case registeredTask.State 
            Case "0"
                taskState = "Unknown"
            Case "1"
                taskState = "Disabled"
            Case "2"
                taskState = "Queued"
            Case "3"
                taskState = "Ready"
            Case "4"
                taskState = "Running"
        End Select

        WScript.Echo "    Task State: " & taskState
    Next
End If

```



## Related topics

<dl> <dt>

[Using the Task Scheduler](using-the-task-scheduler.md)
</dt> </dl>

 

 




