---
title: Logon Trigger Example (XML)
description: The XML in this example defines a task that starts Notepad when a user logs on.
ms.assetid: c1cce95f-7558-489e-b092-c82d55b42165
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Logon Trigger Example (XML)

The XML in this example defines a task that starts Notepad when a user logs on.

To register a task that is defined in XML, you can use either the [**ITaskFolder::RegisterTask**](/windows/desktop/api/taskschd/nf-taskschd-itaskfolder-registertask) function ([**TaskFolder.RegisterTask**](taskfolder-registertask.md) for scripting) or the Schtasks.exe command-line tool. If you use the Schtasks.exe tool (located in the C:\\Windows\\System32 directory), then you can use the following command to register the task: **schtasks /create /XML** *\<path to the XML file containing the task definition\>* **/tn** *\<task name\>*.

## To define a task to start Notepad on system boot

The following XML example shows how to define a task with a single execution action (starting Notepad), a single logon trigger that starts the task when a user logs on, and several other task settings that affect how the task is handled by Task Scheduler.

> [!Note]  
> Set the value of the **UserId** element to a user name on the computer on which the task is registered.

 


```XML
<?xml version="1.0" ?>
<!--
This sample schedules a task to start notepad.exe when a user logs on.
-->
<Task xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
    <RegistrationInfo>
        <Date>2005-10-11T13:21:17-08:00</Date>
        <Author>AuthorName</Author>
        <Version>1.0.0</Version>
        <Description>Starts Notepad when a specified user logs on.</Description>
    </RegistrationInfo>
    <Triggers>
        <LogonTrigger>
            <StartBoundary>2005-10-11T13:21:17-08:00</StartBoundary>
            <EndBoundary>2006-01-01T00:00:00-08:00</EndBoundary>
            <Enabled>true</Enabled>
            <UserId>DOMAIN_NAME\UserName</UserId>
        </LogonTrigger>
    </Triggers>
    <Principals>
        <Principal>
            <GroupId>Builtin\Administrators</GroupId>
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

The following are some important elements to keep in mind when using this example:

-   [**RegistrationInfo**](taskschedulerschema-registrationinfo-tasktype-element.md): Contains registration information about the task.
-   [**Triggers**](taskschedulerschema-triggers-tasktype-element.md): Defines the trigger that starts the task.
-   [**LogonTrigger**](taskschedulerschema-logontrigger-triggergroup-element.md): Defines the logon trigger. In this case, three child elements are used: the start and end boundaries that specify when the trigger is activated and deactivated, and the [**UserId**](taskschedulerschema-userid-logontriggertype-element.md) element that identifier of the user. The task is started when this user logs on to the computer..
-   [**Principal**](taskschedulerschema-principal-principaltype-element.md): Defines the security context that a task runs under.
-   [**Settings**](taskschedulerschema-settings-tasktype-element.md): Defines the task settings that the Task Scheduler uses to perform the task.
-   [**Actions**](taskschedulerschema-actions-tasktype-element.md): Defines the actions the task performs. In this case, running Notepad.

## Related topics

<dl> <dt>

[Using the Task Scheduler](using-the-task-scheduler.md)
</dt> </dl>

 

 




