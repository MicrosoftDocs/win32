---
title: Trigger Types
description: The time-based and event-based triggers that are described below allow you to start tasks in a variety of ways.
ms.assetid: 2f577103-3892-49ce-9a3b-7a4839da8a83
keywords:
- triggers Task Scheduler , types
- boot trigger Task Scheduler
- boot trigger Task Scheduler , described
- registration trigger Task Scheduler
- registration trigger Task Scheduler , described
- calendar trigger Task Scheduler
- calendar trigger Task Scheduler , described
- daily trigger Task Scheduler
- daily trigger Task Scheduler , described
- weekly trigger Task Scheduler
- weekly trigger Task Scheduler , described
- monthly trigger Task Scheduler
- monthly trigger Task Scheduler , described
- monthlyDOW trigger Task Scheduler
- monthlyDOW trigger Task Scheduler , described
- event trigger Task Scheduler
- event trigger Task Scheduler , described
- logon trigger Task Scheduler
- logon trigger Task Scheduler , described
- idle trigger Task Scheduler
- idle trigger Task Scheduler , described
- day-of-week trigger Task Scheduler
ms.topic: article
ms.date: 05/31/2018
---

# Trigger Types

The time-based and event-based triggers that are described below allow you to start tasks in a variety of ways.

## Task Scheduler 2.0 Triggers

The following trigger types are defined by the [**TASK\_TRIGGER\_TYPE2**](/windows/desktop/api/taskschd/ne-taskschd-task_trigger_type2) enumeration.

| Trigger                                                                                                                                                                                                                                                                                                                                                                                                                | Description                                                                                                                                                                                  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event trigger (event based trigger) For scripting development, see [**EventTrigger**](eventtrigger.md).<br/> For C++ development, see [**IEventTrigger**](/windows/desktop/api/taskschd/nn-taskschd-ieventtrigger).<br/> For XML development, see [**EventTrigger Element**](taskschedulerschema-eventtrigger-triggergroup-element.md).<br/>                                                                                             | Starts the task when a specific system event occurs.                                                                                                                                         |
| Time trigger (time-based trigger)For scripting development, see [**TimeTrigger**](timetrigger.md).<br/> For C++ development, see [**ITimeTrigger**](/windows/desktop/api/taskschd/nn-taskschd-itimetrigger).<br/> For XML development, see [**TimeTrigger Element**](taskschedulerschema-timetrigger-triggergroup-element.md).<br/>                                                                                                      | Starts the task at a specific date and time.                                                                                                                                                 |
| Daily trigger (time-based calendar trigger)For scripting development, see [**DailyTrigger**](dailytrigger.md).<br/> For C++ development, see [**IDailyTrigger**](/windows/desktop/api/taskschd/nn-taskschd-idailytrigger).<br/> For XML development, see [**CalendarTrigger Element**](taskschedulerschema-calendartrigger-triggergroup-element.md).<br/>                                                                                | Starts the task at a specific time on a daily schedule. For example, the task starts at 8:00 AM every day or every other day.                                                                |
| Weekly trigger (time-based calendar trigger)For scripting development, see [**WeeklyTrigger**](weeklytrigger.md).<br/> For C++ development, see [**IWeeklyTrigger**](/windows/desktop/api/taskschd/nn-taskschd-iweeklytrigger).<br/> For XML development, see [**CalendarTrigger Element**](taskschedulerschema-calendartrigger-triggergroup-element.md).<br/>                                                                           | Starts the task at a specific time on a weekly schedule. For example, the task starts at 8:00 AM on a specific day of the week every week or on a specific day of the week every other week. |
| Monthly trigger (time-based calendar trigger)For scripting development, see [**MonthlyTrigger**](monthlytrigger.md).<br/> For C++ development, see [**IMonthlyTrigger**](/windows/desktop/api/taskschd/nn-taskschd-imonthlytrigger).<br/> For XML development, see [**CalendarTrigger Element**](taskschedulerschema-calendartrigger-triggergroup-element.md).<br/>                                                                      | Starts the task at a specific time on a monthly schedule. For example, the task starts at 8:00 AM on specific days of the month on specific months.                                          |
| Monthly day-of-week (DOW) trigger (time-based calendar trigger)For scripting development, see [**MonthlyDOWTrigger**](monthlydowtrigger.md).<br/> For C++ development, see [**IMonthlyDOWTrigger**](/windows/desktop/api/taskschd/nn-taskschd-imonthlydowtrigger).<br/> For XML development, see [**CalendarTrigger Element**](taskschedulerschema-calendartrigger-triggergroup-element.md).<br/>                                        | Starts the task at a specific time on a monthly day-of-week schedule. For example, the task starts at 8:00 AM on specific days of the week, weeks of the month, and months of the year.      |
| Idle trigger (event-based trigger)For scripting development, see [**IdleTrigger**](idletrigger.md).<br/> For C++ development, see [**IIdleTrigger**](/windows/win32/api/taskschd/nn-taskschd-iidletrigger).<br/> For XML development, see [**IdleTrigger Element**](taskschedulerschema-idletrigger-triggergroup-element.md).<br/>                                                                                                     | Starts the task when the computer enters an idle state.                                                                                                                                      |
| Registration trigger (event-based trigger)For scripting development, see [**RegistrationTrigger**](registrationtrigger.md).<br/> For C++ development, see [**IRegistrationTrigger**](/windows/desktop/api/taskschd/nn-taskschd-iregistrationtrigger).<br/> For XML development, see [**RegistrationTrigger Element**](taskschedulerschema-registrationtrigger-triggergroup-element.md).<br/>                                             | Starts the task when the task is registered or updated.                                                                                                                                      |
| Boot trigger (event-based trigger)For scripting development, see [**BootTrigger**](boottrigger.md).<br/> For C++ development, see [**IBootTrigger**](/windows/desktop/api/taskschd/nn-taskschd-iboottrigger).<br/> For XML development, see [**BootTrigger Element**](taskschedulerschema-boottrigger-triggergroup-element.md).<br/>                                                                                                     | Starts the task when the system is booted.                                                                                                                                                   |
| Logon trigger (event-based trigger)For scripting development, see [**LogonTrigger**](logontrigger.md).<br/> For C++ development, see [**ILogonTrigger**](/windows/desktop/api/taskschd/nn-taskschd-ilogontrigger).<br/> For XML development, see [**LogonTrigger Element**](taskschedulerschema-logontrigger-triggergroup-element.md).<br/>                                                                                              | Starts the task when a user logs on.                                                                                                                                                         |
| Session state change trigger (event-based trigger)For scripting development, see [**SessionStateChangeTrigger**](sessionstatechangetrigger.md).<br/> For C++ development, see [**ISessionStateChangeTrigger**](/windows/desktop/api/taskschd/nn-taskschd-isessionstatechangetrigger).<br/> For XML development, see [**SessionStateChangeTrigger Element**](taskschedulerschema-sessionstatechangetrigger-triggergroup-element.md).<br/> | Starts the task when a Terminal Server session changes state.                                                                                                                                |



 

## Task Scheduler 1.0 Triggers

The following trigger types are defined by the [**TASK\_TRIGGER\_TYPE**](/windows/desktop/api/Mstask/ne-mstask-task_trigger_type) enumeration. To implement any of the following triggers, see the [**TASK\_TRIGGER**](/windows/desktop/api/Mstask/ns-mstask-task_trigger) structure.

-   Once trigger: Starts the task a single time.
-   Daily trigger: Starts the task on a daily interval.
-   Weekly trigger: Starts the task on a weekly schedule.
-   Monthly trigger: Starts the task on a monthly schedule.
-   Monthly DOW trigger: Starts the task on a monthly day-of-week schedule.
-   On Idle trigger: Starts the task when the computer is in an idle state.
-   System Start trigger: Starts the task when the computer is booted.
-   Logon trigger: Starts the task when a specific user logs on.

## Related topics

<dl> <dt>

[Task Triggers](task-triggers.md)
</dt> <dt>

[Trigger Interfaces](trigger-interfaces.md)
</dt> <dt>

[Trigger Structures](trigger-structures.md)
</dt> </dl>

 

