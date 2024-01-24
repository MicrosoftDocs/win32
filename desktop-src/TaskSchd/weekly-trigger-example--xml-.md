---
title: Weekly Trigger Example (XML)
description: The XML in this example defines a task that starts Notepad on a bi-weekly basis.
ms.assetid: 1911e8b1-2583-440c-a6ed-d71080b60987
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Weekly Trigger Example (XML)

The XML in this example defines a task that starts Notepad on a bi-weekly basis.

To register a task that is defined in XML, you can use either the [**ITaskFolder::RegisterTask**](/windows/desktop/api/taskschd/nf-taskschd-itaskfolder-registertask) function ([**TaskFolder.RegisterTask**](taskfolder-registertask.md) for scripting) or the Schtasks.exe command-line tool. If you use the Schtasks.exe tool (located in the C:\\Windows\\System32 directory), then you can use the following command to register the task: **schtasks /create /XML** *\<path to the XML file containing the task definition\>* **/tn** *\<task name\>*.

## To define a task to start Notepad every other week on Monday at 8:00 AM

The following XML example shows how to define a task with a single execution action (starting Notepad), a single calendar trigger (starts the task every other week on Monday at 8:00 AM), and several other task settings that affect how the task is handled by Task Scheduler.


```XML
<?xml version="1.0" ?>
<!--
This sample schedules a task to start on a bi-weekly basis.
-->
<Task xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
    <RegistrationInfo>
        <Date>2005-05-01T09:00:00</Date>
        <Author>AuthorName</Author>
        <Version>1.0.0</Version>
        <Description>Notepad starts every other week on Monday at 8:00am.</Description>
    </RegistrationInfo>
    <Triggers>
        <CalendarTrigger>
            <StartBoundary>2005-05-02T08:00:00</StartBoundary>
            <EndBoundary>2006-01-01T00:00:00</EndBoundary>
            <ScheduleByWeek>
                <WeeksInterval>2</WeeksInterval>
                <DaysOfWeek>
                    <Monday/>
                </DaysOfWeek>
            </ScheduleByWeek>
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

    Defines the weekly calendar trigger. In this case, only four child elements are used: the start and end boundaries that specify when the trigger is activated and deactivated, the weekly schedule, and the days of the week that the task will run on. The [**StartBoundary**](taskschedulerschema-startboundary-triggerbasetype-element.md) element is a required element for calendar triggers.

-   [**ScheduleByWeek**](taskschedulerschema-schedulebyweek-calendartriggertype-element.md)

    Defines the weekly schedule. In this case, the interval is set to perform the task every other week on a Monday.

-   [**Principal**](taskschedulerschema-principal-principaltype-element.md)

    Defines the security context that a task runs under.

-   [**Settings**](taskschedulerschema-settings-tasktype-element.md)

    Defines the task settings that Task Scheduler uses to perform the task.

-   [**Actions**](taskschedulerschema-actions-tasktype-element.md)

    Defines the actions the task performs (in this case, running Notepad).

## Related topics

<dl> <dt>

[Using the Task Scheduler](using-the-task-scheduler.md)
</dt> </dl>

 

 




