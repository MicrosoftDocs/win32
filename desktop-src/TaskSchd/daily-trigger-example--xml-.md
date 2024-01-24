---
title: Daily Trigger Example (XML)
description: The XML in this example defines a task that starts Notepad at 8 00 AM every day.
ms.assetid: b7818071-12b6-41df-85b9-282c08cf6e31
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Daily Trigger Example (XML)

The XML in this example defines a task that starts Notepad at 8:00 AM every day. The example also shows how to set a repetition pattern for the trigger to repeat the task.

To register a task that is defined in XML, you can use either the [**ITaskFolder::RegisterTask**](/windows/desktop/api/taskschd/nf-taskschd-itaskfolder-registertask) function ([**TaskFolder.RegisterTask**](taskfolder-registertask.md) for scripting) or the Schtasks.exe command-line tool. If you use the Schtasks.exe tool (located in the C:\\Windows\\System32 directory), then you can use the following command to register the task: **schtasks /create /XML** *\<path to the XML file containing the task definition\>* **/tn** *\<task name\>*.

## To define a task to start Notepad every day at 8:00 AM

The following XML example shows how to define a task with a single execution action (starting Notepad), a single calendar trigger (starts the task every day at 8:00 AM), and several other task settings that affect how the task is handled by Task Scheduler.


```XML
<?xml version="1.0" ?>
<!--
This sample schedules a task to start on a daily basis.
-->
<Task xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
    <RegistrationInfo>
        <Date>2005-10-11T13:21:17-08:00</Date>
        <Author>AuthorName</Author>
        <Version>1.0.0</Version>
        <Description>Notepad starts every day.</Description>
    </RegistrationInfo>
    <Triggers>
        <CalendarTrigger>
            <StartBoundary>2005-10-11T13:21:17-08:00</StartBoundary>
            <EndBoundary>2006-01-01T00:00:00-08:00</EndBoundary>
            <Repetition>
                <Interval>PT1M</Interval>
                <Duration>PT4M</Duration>
            </Repetition>
            <ScheduleByDay>
                <DaysInterval>1</DaysInterval>
            </ScheduleByDay>
        </CalendarTrigger>
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

-   [**RegistrationInfo**](taskschedulerschema-registrationinfo-tasktype-element.md)

    Contains registration information about the task.

-   [**Triggers**](taskschedulerschema-triggers-tasktype-element.md)

    Defines the trigger that starts the task.

-   [**CalendarTrigger**](taskschedulerschema-calendartrigger-triggergroup-element.md)

    Defines the daily calendar trigger. In this case, four child elements are used: the start and end boundaries that specify when the trigger is activated and deactivated, the daily schedule, and the repetition pattern for the task. The [**StartBoundary**](taskschedulerschema-startboundary-triggerbasetype-element.md) element is a required element for calendar triggers.

-   [**ScheduleByDay**](taskschedulerschema-schedulebyday-calendartriggertype-element.md)

    Defines the daily schedule. In this case, the interval is set to perform the task every day.

-   [**Principal**](taskschedulerschema-principal-principaltype-element.md): Defines the security context that a task runs under.
-   [**Settings**](taskschedulerschema-settings-tasktype-element.md)

    Defines the task settings that Task Scheduler uses to perform the task.

-   [**Actions**](taskschedulerschema-actions-tasktype-element.md)

    Defines the actions the task performs (in this case, running Notepad).

## Related topics

<dl> <dt>

[Using the Task Scheduler](using-the-task-scheduler.md)
</dt> </dl>

 

 




