---
title: Registration Trigger Example (XML)
description: The XML in this example defines a task that starts Notepad when the task is registered.
ms.assetid: 976b9767-635f-42a6-84f5-7e0203478594
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Registration Trigger Example (XML)

The XML in this example defines a task that starts Notepad when the task is registered.

To register a task that is defined in XML, you can use either the [**ITaskFolder::RegisterTask**](/windows/desktop/api/taskschd/nf-taskschd-itaskfolder-registertask) function ([**TaskFolder.RegisterTask**](taskfolder-registertask.md) for scripting) or the Schtasks.exe command-line tool. If you use the Schtasks.exe tool (located in the C:\\Windows\\System32 directory), then you can use the following command to register the task: **schtasks /create /XML** *\<path to the XML file containing the task definition>* **/tn** *\<task name>*.

> [!Note]  
> When a task with a registration trigger is updated, the task will execute after the update occurs.

 

## To define a task to start Notepad on registration

The following XML example shows how to define a task with a single execution action (starting Notepad), a single registration trigger that starts the task when it is registered, and several other task settings that affect how the task is handled by the Task Scheduler.

> [!Note]  
> When a task with a registration trigger is updated, the task will execute after the update occurs.

 


```XML
<?xml version="1.0" ?>
<!--
This sample schedules a task to start notepad.exe when
the task is registered.
-->
<Task xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
    <RegistrationInfo>
        <Date>2005-10-11T13:21:17-08:00</Date>
        <Author>AuthorName</Author>
        <Version>1.0.0</Version>
        <Description>Task starts after registration.</Description>
    </RegistrationInfo>
    <Triggers>
        <RegistrationTrigger>
        </RegistrationTrigger>
    </Triggers>
    <Principals>
        <Principal>
            <UserId>Administrator</UserId>
            <LogonType>InteractiveToken</LogonType>
        </Principal>
    </Principals>
    <Settings>
        <Enabled>true</Enabled>
        <AllowStartOnDemand>true</AllowStartOnDemand>
        <AllowHardTerminate>true</AllowHardTerminate>
    </Settings>
    <Actions>
        <Exec>
            <Command>notepad.exe</Command>
        </Exec>
    </Actions>
</Task>
```



## TaskScheduler Schema Elements

Here are some important elements to keep in mind when using this example.

-   [**RegistrationInfo**](taskschedulerschema-registrationinfo-tasktype-element.md): Contains registration information about the task.
-   [**Triggers**](taskschedulerschema-triggers-tasktype-element.md): Defines the trigger that starts the task.
-   [**RegistrationTrigger**](taskschedulerschema-registrationtrigger-triggergroup-element.md): Defines the registration trigger. In this case, only two child elements are used: the start and end boundaries that specify when the trigger is activated and deactivated.
-   [**Principal**](taskschedulerschema-principal-principaltype-element.md): Defines the security context that a task runs under.
-   [**Settings**](taskschedulerschema-settings-tasktype-element.md): Defines the task settings that the Task Scheduler uses to perform the task.
-   [**Actions**](taskschedulerschema-actions-tasktype-element.md): Defines the actions the task performs. In this case, running Notepad.

## Related topics

<dl> <dt>

[Using the Task Scheduler](using-the-task-scheduler.md)
</dt> </dl>

 

 




