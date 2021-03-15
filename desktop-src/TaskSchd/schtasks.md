---
title: Schtasks.exe
description: Enables an administrator to create, delete, query, change, run, and end scheduled tasks on a local or remote computer.
ms.assetid: 3cf973de-14c4-4ca9-86a7-7f97181bd9e0
keywords:
- Schtasks.exe Task Scheduler
topic_type:
- apiref
api_name:
- Schtasks.exe
api_type:
- NA
ms.topic: reference
ms.custom: snippet-project
ms.date: 05/31/2018
---

# Schtasks.exe

Enables an administrator to create, delete, query, change, run, and end scheduled tasks on a local or remote computer. Running Schtasks.exe without arguments displays the status and next run time for each registered task. 

For more information on Task Scheduler, see this introduction: [Task Scheduler for developers](task-scheduler-start-page.md).

## Creating a Task

The following syntax is used to create a task on the local or remote computer.

``` syntax
schtasks /Create 
[/S system [/U username [/P [password]]]]
[/RU username [/RP [password]] /SC schedule [/MO modifier] [/D day]
[/M months] [/I idletime] /TN taskname /TR taskrun [/ST starttime]
[/RI interval] [ {/ET endtime | /DU duration} [/K] 
[/XML xmlfile] [/V1]] [/SD startdate] [/ED enddate] [/IT] [/Z] [/F]
```

## Parameters

<dl> <dt>

<span id="_S_system"></span><span id="_s_system"></span><span id="_S_SYSTEM"></span>**/S** **system**
</dt> <dd>

A value that specifies the remote computer to connect to. If omitted, the system parameter defaults to the local computer.

</dd> <dt>

<span id="_U_username"></span><span id="_u_username"></span><span id="_U_USERNAME"></span>**/U** **username**
</dt> <dd>

A value that specifies the user context under which Schtasks.exe should run.

</dd> <dt>

<span id="_P__password_"></span><span id="_p__password_"></span><span id="_P__PASSWORD_"></span>**/P** **\[password\]**
</dt> <dd>

A value that specifies the password for a given user context. If omitted, Schtasks.exe prompts the user for input.

</dd> <dt>

<span id="_RU_username"></span><span id="_ru_username"></span><span id="_RU_USERNAME"></span>**/RU** **username**
</dt> <dd>

A value that specifies the user context under which the task runs. For the system account, valid values are "", "NT AUTHORITY\\SYSTEM", or "SYSTEM". For Task Scheduler 2.0 tasks, "NT AUTHORITY\\LOCALSERVICE", and "NT AUTHORITY\\NETWORKSERVICE" are also valid values.

</dd> <dt>

<span id="_RP__password_"></span><span id="_rp__password_"></span><span id="_RP__PASSWORD_"></span>**/RP** **\[password\]**
</dt> <dd>

A value that specifies the password for the user specified with the /RU parameter. To prompt for the password, the value must be either "\*" or no value. This password is ignored for the system account. This parameter must be combined with either /RU or the /XML switch.

</dd> <dt>

<span id="_SC_schedule"></span><span id="_sc_schedule"></span><span id="_SC_SCHEDULE"></span>**/SC** **schedule**
</dt> <dd>

A value that specifies the schedule frequency. Valid values are: MINUTE, HOURLY, DAILY, WEEKLY, MONTHLY, ONCE, ONLOGON, ONIDLE, and ONEVENT.

</dd> <dt>

<span id="_MO_modifier"></span><span id="_mo_modifier"></span><span id="_MO_MODIFIER"></span>**/MO** **modifier**
</dt> <dd>

A value that refines the schedule type to allow for finer control over the schedule recurrence. Valid values are:

-   MINUTE: 1 - 1439 minutes.
-   HOURLY: 1 - 23 hours.
-   DAILY: 1 - 365 days.
-   WEEKLY: weeks 1 - 52.
-   ONCE: No modifiers.
-   ONSTART: No modifiers.
-   ONLOGON: No modifiers.
-   ONIDLE: No modifiers.
-   MONTHLY: 1 - 12, or FIRST, SECOND, THIRD, FOURTH, LAST, and LASTDAY.
-   ONEVENT: XPath event query string.

</dd> <dt>

<span id="_D_days"></span><span id="_d_days"></span><span id="_D_DAYS"></span>**/D** **days**
</dt> <dd>

A value that specifies the day of the week to run the task. Valid values are: MON, TUE, WED, THU, FRI, SAT, SUN and for MONTHLY schedules 1 - 31 (days of the month). The wildcard character (\*) specifies all days.

</dd> <dt>

<span id="_M_months"></span><span id="_m_months"></span><span id="_M_MONTHS"></span>**/M** **months**
</dt> <dd>

A value that specifies months of the year. Defaults to the first day of the month. Valid values are: JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, and DEC. The wildcard character (\*) specifies all months.

</dd> <dt>

<span id="_I_idletime"></span><span id="_i_idletime"></span><span id="_I_IDLETIME"></span>**/I** **idletime**
</dt> <dd>

A value that specifies the amount of idle time to wait before running a scheduled ONIDLE task. The valid range is 1 - 999 minutes.

</dd> <dt>

<span id="_TN_taskname"></span><span id="_tn_taskname"></span><span id="_TN_TASKNAME"></span>**/TN** **taskname**
</dt> <dd>

A value that specifies a name which uniquely identifies the scheduled task.

</dd> <dt>

<span id="_TR_taskrun"></span><span id="_tr_taskrun"></span><span id="_TR_TASKRUN"></span>**/TR** **taskrun**
</dt> <dd>

A value that specifies the path and file name of the task to be run at the scheduled time. For example: C:\\Windows\\System32\\calc.exe.

</dd> <dt>

<span id="_ST_starttime"></span><span id="_st_starttime"></span><span id="_ST_STARTTIME"></span>**/ST** **starttime**
</dt> <dd>

A value that specifies the start time to run the task. The time format is HH:mm (24-hour time). For example, 14:30 specifies 2:30PM. The default is the current time is /ST is not specified. This option is required wit the /SC ONCE argument.

</dd> <dt>

<span id="_RI_interval"></span><span id="_ri_interval"></span><span id="_RI_INTERVAL"></span>**/RI** **interval**
</dt> <dd>

A value that specifies the repetition interval in minutes. This is not applicable for the following schedule types: MINUTE, HOURLY, ONSTART, ONLOGON, ONIDLE, and ONEVENT. The valid range is 1 - 599940 minutes. If either the /ET or /DU parameters are specified, the default is 10 minutes.

**Windows XP and Windows Server 2003:** This option is not available.

</dd> <dt>

<span id="_ET_endtime"></span><span id="_et_endtime"></span><span id="_ET_ENDTIME"></span>**/ET** **endtime**
</dt> <dd>

A value that specifies the end time to run the task. The time format is HH:mm (24-hour time). For example, 14:50 specifies 2:50PM. This is not applicable for the following schedule types: ONSTART, ONLOGON, ONIDLE, and ONEVENT.

**Windows XP and Windows Server 2003:** This option is not available.

</dd> <dt>

<span id="_DU_duration"></span><span id="_du_duration"></span><span id="_DU_DURATION"></span>**/DU** **duration**
</dt> <dd>

A value that specifies the duration to run the task. The time format is HH:mm (24-hour time). For example, 14:50 specifies 2:50PM. This is not applicable with /ET and for the following schedule types: ONSTART, ONLOGON, ONIDLE, and ONEVENT. For /V1 tasks (Task Scheduler 1.0 tasks), if /RI is specified, then the duration default is one hour.

**Windows XP:** This option is not available.

</dd> <dt>

<span id="_K_"></span><span id="_k_"></span>**/K** 
</dt> <dd>

A value that terminates the task at the end time or duration time. This is not applicable for the following schedule types: ONSTART, ONLOGON, ONIDLE, and ONEVENT. Either /ET or /DU must be specified.

**Windows XP and Windows Server 2003:** This option is not available.

</dd> <dt>

<span id="_SD_startdate"></span><span id="_sd_startdate"></span><span id="_SD_STARTDATE"></span>**/SD** **startdate**
</dt> <dd>

A value that specifies the first date on which to run the task. The format is mm/dd/yyyy. This value defaults to the current date. This is not applicable for the following schedule types: ONCE, ONSTART, ONLOGON, ONIDLE, and ONEVENT.

</dd> <dt>

<span id="_ED_enddate"></span><span id="_ed_enddate"></span><span id="_ED_ENDDATE"></span>**/ED** **enddate**
</dt> <dd>

A value that specifies the last date that the task will run. The format is mm/dd/yyyy. This is not applicable for the following schedule types: ONCE, ONSTART, ONLOGON, ONIDLE, and ONEVENT.

</dd> <dt>

<span id="_EC_ChannelName"></span><span id="_ec_channelname"></span><span id="_EC_CHANNELNAME"></span>**/EC** **ChannelName**
</dt> <dd>

A value that specifies the event channel for ONEVENT triggers.

**Windows XP and Windows Server 2003:** This option is not available.

</dd> <dt>

<span id="_IT_"></span><span id="_it_"></span>**/IT** 
</dt> <dd>

A value that enables the task to run interactively only if the /RU user is currently logged on at the time the task runs. The task runs only if the user is logged on.

**Windows XP and Windows Server 2003:** This option is not available.

</dd> <dt>

<span id="_NP_"></span><span id="_np_"></span>**/NP** 
</dt> <dd>

A value that indicates that no password is stored. The task does not run interactively as the given user. Only local resources are available.

**Windows XP and Windows Server 2003:** This option is not available.

</dd> <dt>

<span id="_Z_"></span><span id="_z_"></span>**/Z** 
</dt> <dd>

A value that marks the task to be deleted after its final run.

**Windows XP and Windows Server 2003:** This option is not available.

</dd> <dt>

<span id="_XML_xmlfile"></span><span id="_xml_xmlfile"></span><span id="_XML_XMLFILE"></span>**/XML** **xmlfile**
</dt> <dd>

A value that creates a task from an XML file. This parameter can be combined with /RU and /RP switches, or with the /RP switch alone when the task XML already contains the principal.

**Windows XP and Windows Server 2003:** This option is not available.

</dd> <dt>

<span id="_V1_"></span><span id="_v1_"></span>**/V1** 
</dt> <dd>

A value that creates a task visible to Windows 2000, Windows Server 2003, and Windows XP platforms.

**Windows XP and Windows Server 2003:** This option is not available.

</dd> <dt>

<span id="_F_"></span><span id="_f_"></span>**/F** 
</dt> <dd>

A value that forcefully creates the task and suppresses warnings if the specified task already exists.

**Windows XP and Windows Server 2003:** This option is not available.

</dd> <dt>

<span id="_RL_level"></span><span id="_rl_level"></span><span id="_RL_LEVEL"></span>**/RL** **level**
</dt> <dd>

A value that sets the run level for the task. Valid values are LIMITED and HIGHEST. The default is LIMITED.

**Windows XP and Windows Server 2003:** This option is not available.

</dd> <dt>

<span id="_DELAY_delaytime"></span><span id="_delay_delaytime"></span><span id="_DELAY_DELAYTIME"></span>**/DELAY** **delaytime**
</dt> <dd>

A value that specifies the wait time to delay the task after the trigger is fired. The time format is mmmm:ss. This option is only valid for schedule types ONSTART, ONLOGON, and ONEVENT.

**Windows XP and Windows Server 2003:** This option is not available.

</dd> <dt>

<span id="___"></span>**/?** 
</dt> <dd>

A value that displays the help message for Schtasks.exe.

</dd> </dl>

## Remarks

When creating a task on a remote computer running on the Windows XP, Windows Server 2003, or Windows 2000 operating system, use the /V1 switch.

You cannot create a non-interactive remote Task Scheduler 1.0 task (create a task by not using the /IT switch and using the /V1 switch) if the remote computer has the File and Printer Sharing firewall exception enabled and the Remote Scheduled Tasks Management firewall exception disabled.

## Deleting a Task

The following syntax is used to delete one or more scheduled tasks.

``` syntax
schtasks /Delete 
[/S system [/U username [/P [password]]]]
[/TN taskname] [/F]
```

## Parameters

<dl> <dt>

<span id="_S_system"></span><span id="_s_system"></span><span id="_S_SYSTEM"></span>**/S** **system**
</dt> <dd>

A value that specifies the remote computer to connect to. If omitted, the system parameter defaults to the local computer.

</dd> <dt>

<span id="_U_username"></span><span id="_u_username"></span><span id="_U_USERNAME"></span>**/U** **username**
</dt> <dd>

A value that specifies the user context under which Schtasks.exe should run.

</dd> <dt>

<span id="_P__password_"></span><span id="_p__password_"></span><span id="_P__PASSWORD_"></span>**/P** **\[password\]**
</dt> <dd>

A value that specifies the password for the given user context. If omitted, Schtasks.exe prompts the user for input.

</dd> <dt>

<span id="_TN_taskname"></span><span id="_tn_taskname"></span><span id="_TN_TASKNAME"></span>**/TN** **taskname**
</dt> <dd>

A value that specifies the name of the scheduled task to delete. The wildcard character (\*) can be used to delete all tasks.

</dd> <dt>

<span id="_F_"></span><span id="_f_"></span>**/F** 
</dt> <dd>

A value that forcefully deletes the task and suppresses warnings if the specified task is running.

</dd> <dt>

<span id="__"></span>**/?**
</dt> <dd>

A value that displays Help for Schtasks.exe.

</dd> </dl>

## Running a Task

The following syntax is used to immediately run a scheduled task.

``` syntax
schtasks /Run 
[/S system [/U username [/P [password]]]]
/TN taskname
```

## Parameters

<dl> <dt>

<span id="_S_system"></span><span id="_s_system"></span><span id="_S_SYSTEM"></span>**/S** **system**
</dt> <dd>

A value that specifies the remote computer to connect to. If omitted, the system parameter defaults to the local computer.

</dd> <dt>

<span id="_U_username"></span><span id="_u_username"></span><span id="_U_USERNAME"></span>**/U** **username**
</dt> <dd>

A value that specifies the user context under which Schtasks.exe should run.

</dd> <dt>

<span id="_P__password_"></span><span id="_p__password_"></span><span id="_P__PASSWORD_"></span>**/P** **\[password\]**
</dt> <dd>

A value that specifies the password for the given user context. If omitted, Schtasks.exe prompts the user for input.

</dd> <dt>

<span id="_TN_taskname"></span><span id="_tn_taskname"></span><span id="_TN_TASKNAME"></span>**/TN** **taskname**
</dt> <dd>

A value that specifies the name of the scheduled task to run.

</dd> <dt>

<span id="__"></span>**/?**
</dt> <dd>

A value that displays Help for Schtasks.exe.

</dd> </dl>

## Ending a Running Task

The following syntax is used to stop a running scheduled task.

> [!Note]  
> To stop a remote task from running, ensure that the remote computer has the File and Printer Sharing and Remote Scheduled Tasks Management firewall exceptions enabled.

 

``` syntax
schtasks /End 
[/S system [/U username [/P [password]]]]
/TN taskname
```

## Parameters

<dl> <dt>

<span id="_S_system"></span><span id="_s_system"></span><span id="_S_SYSTEM"></span>**/S** **system**
</dt> <dd>

A value that specifies the remote computer to connect to. If omitted, the system parameter defaults to the local computer.

</dd> <dt>

<span id="_U_username"></span><span id="_u_username"></span><span id="_U_USERNAME"></span>**/U** **username**
</dt> <dd>

A value that specifies the user context under which Schtasks.exe should run.

</dd> <dt>

<span id="_P__password_"></span><span id="_p__password_"></span><span id="_P__PASSWORD_"></span>**/P** **\[password\]**
</dt> <dd>

A value that specifies the password for the given user context. If omitted, Schtasks.exe prompts the user for input.

</dd> <dt>

<span id="_TN_taskname"></span><span id="_tn_taskname"></span><span id="_TN_TASKNAME"></span>**/TN** **taskname**
</dt> <dd>

A value that specifies the name of the scheduled task to stop.

</dd> <dt>

<span id="__"></span>**/?**
</dt> <dd>

A value that displays Help for Schtasks.exe.

</dd> </dl>

## Querying for Task Information

The following syntax is used to display the scheduled tasks from the local or remote computer.

``` syntax
schtasks /Query 
[/S system [/U username [/P [password]]]]
[/FO format | /XML] [/NH] [/V] [/TN taskname] [/?]
```

## Parameters

<dl> <dt>

<span id="_S_system"></span><span id="_s_system"></span><span id="_S_SYSTEM"></span>**/S** **system**
</dt> <dd>

A value that specifies the remote computer to connect to. If omitted, the system parameter defaults to the local computer.

</dd> <dt>

<span id="_U_username"></span><span id="_u_username"></span><span id="_U_USERNAME"></span>**/U** **username**
</dt> <dd>

A value that specifies the user context under which Schtasks.exe should run.

</dd> <dt>

<span id="_P__password_"></span><span id="_p__password_"></span><span id="_P__PASSWORD_"></span>**/P** **\[password\]**
</dt> <dd>

A value that specifies the password for the given user context. If omitted, Schtasks.exe prompts the user for input.

</dd> <dt>

<span id="_FO_format"></span><span id="_fo_format"></span><span id="_FO_FORMAT"></span>**/FO** **format**
</dt> <dd>

A value that specifies the output format. The valid values are TABLE, LIST, and CSV.

</dd> <dt>

<span id="_NH_"></span><span id="_nh_"></span>**/NH** 
</dt> <dd>

A value that specifies that the column header should not be displayed in the output. This is valid only for TABLE and CSV formats.

</dd> <dt>

<span id="_V_"></span><span id="_v_"></span>**/V** 
</dt> <dd>

A value that displays verbose task output.

> [!Note]  
> If a task was scheduled to run only one time, then the displayed schedule information is "Scheduling data is not available in this format."

 

</dd> <dt>

<span id="_TN_taskname"></span><span id="_tn_taskname"></span><span id="_TN_TASKNAME"></span>**/TN** **taskname**
</dt> <dd>

A value that specifies the task name for which to retrieve the information. If no task name is specified, then information for all the tasks will be displayed.

**Windows XP and Windows Server 2003:** This option is not available.

</dd> <dt>

<span id="_XML_"></span><span id="_xml_"></span>**/XML** 
</dt> <dd>

A value that is used to display the task definitions in XML format.

**Windows XP and Windows Server 2003:** This option is not available.

</dd> <dt>

<span id="__"></span>**/?**
</dt> <dd>

A value that is used to display the Help for Schtasks.exe.

</dd> </dl>

## Changing a Task

The following syntax is used to change how the program runs, or change the user account and password used by a scheduled task.

``` syntax
schtasks /Change 
[/S system [/U username [/P [password]]]] /TN taskname
{ [/RU runasuser] [/RP runaspassword] [/TR taskrun] [/ST starttime] 
[/RI interval] [ {/ET endtime | /DU duration} [/K] ]
[/SD startdate] [/ED enddate] [/ENABLE | /DISABLE] [/IT] [/Z] }
```

## Parameters

<dl> <dt>

<span id="_S_system"></span><span id="_s_system"></span><span id="_S_SYSTEM"></span>**/S** **system**
</dt> <dd>

A value that specifies the remote computer to connect to. If omitted, the system parameter defaults to the local computer.

</dd> <dt>

<span id="_U_username"></span><span id="_u_username"></span><span id="_U_USERNAME"></span>**/U** **username**
</dt> <dd>

A value that specifies the user context under which Schtasks.exe should run.

</dd> <dt>

<span id="_P__password_"></span><span id="_p__password_"></span><span id="_P__PASSWORD_"></span>**/P** **\[password\]**
</dt> <dd>

A value that specifies the password for the given user context. If omitted, Schtasks.exe prompts the user for input.

</dd> <dt>

<span id="_TN_taskname"></span><span id="_tn_taskname"></span><span id="_TN_TASKNAME"></span>**/TN** **taskname**
</dt> <dd>

A value that specifies which scheduled task to change.

</dd> <dt>

<span id="_RU_runasuser"></span><span id="_ru_runasuser"></span><span id="_RU_RUNASUSER"></span>**/RU** **runasuser**
</dt> <dd>

A value that changes the user name (user context) under which the scheduled task will run. For the system account, valid values are "", "NT AUTHORITY\\SYSTEM", or "SYSTEM". For Task Scheduler 2.0 tasks, "NT AUTHORITY\\LOCALSERVICE" and "NT AUTHORITY\\NETWORKSERVICE" are also valid values.

</dd> <dt>

<span id="_RP_runaspassword"></span><span id="_rp_runaspassword"></span><span id="_RP_RUNASPASSWORD"></span>**/RP** **runaspassword**
</dt> <dd>

A value that specifies a new password for the existing user context or the password for a new user account. This password is ignored for the system account.

</dd> <dt>

<span id="_TR_taskrun"></span><span id="_tr_taskrun"></span><span id="_TR_TASKRUN"></span>**/TR** **taskrun**
</dt> <dd>

A value that specifies a new program that the task will run.

</dd> <dt>

<span id="_ST_starttime"></span><span id="_st_starttime"></span><span id="_ST_STARTTIME"></span>**/ST** **starttime**
</dt> <dd>

A value that specifies the start time to run the task. The time format is HH:mm (24-hour time). For example, 14:30 specifies 2:30PM.

**Windows XP and Windows Server 2003:** This option is not available.

</dd> <dt>

<span id="_RI_interval"></span><span id="_ri_interval"></span><span id="_RI_INTERVAL"></span>**/RI** **interval**
</dt> <dd>

A value that specifies the repetition interval, in minutes. The valid range is 1 - 599940 minutes.

**Windows XP and Windows Server 2003:** This option is not available.

</dd> <dt>

<span id="_ET_endtime"></span><span id="_et_endtime"></span><span id="_ET_ENDTIME"></span>**/ET** **endtime**
</dt> <dd>

A value that specifies the end time for the task. The time format is HH:mm (24-hour time). For example, 14:50 specifies 2:50PM.

**Windows XP and Windows Server 2003:** This option is not available.

</dd> <dt>

<span id="_DU_duration"></span><span id="_du_duration"></span><span id="_DU_DURATION"></span>**/DU** **duration**
</dt> <dd>

A value that specifies the duration to run the task. The time format is HH:mm (24-hour time). For example, 14:50 specifies 2:50PM. This is not applicable with the /ET parameter.

**Windows XP and Windows Server 2003:** This option is not available.

</dd> <dt>

<span id="_K_"></span><span id="_k_"></span>**/K** 
</dt> <dd>

A value that terminates the task at the end time or duration time.

**Windows XP and Windows Server 2003:** This option is not available.

</dd> <dt>

<span id="_SD_startdate"></span><span id="_sd_startdate"></span><span id="_SD_STARTDATE"></span>**/SD** **startdate**
</dt> <dd>

A value that specifies the first date on which to run the task. The format is mm/dd/yyyy.

**Windows XP and Windows Server 2003:** This option is not available.

</dd> <dt>

<span id="_ED_enddate"></span><span id="_ed_enddate"></span><span id="_ED_ENDDATE"></span>**/ED** **enddate**
</dt> <dd>

A value that specifies the last date that the task will run. The format is mm/dd/yyyy.

**Windows XP and Windows Server 2003:** This option is not available.

</dd> <dt>

<span id="_IT_"></span><span id="_it_"></span>**/IT** 
</dt> <dd>

A value that enables the task to run interactively only if the /RU user is currently logged on at the time the task runs. The task runs only if the user is logged on.

**Windows XP and Windows Server 2003:** This option is not available.

</dd> <dt>

<span id="_RL_level"></span><span id="_rl_level"></span><span id="_RL_LEVEL"></span>**/RL** **level**
</dt> <dd>

A value that sets the run level for the task. Valid values are LIMITED and HIGHEST.

**Windows XP and Windows Server 2003:** This option is not available.

</dd> <dt>

<span id="_ENABLE_"></span><span id="_enable_"></span>**/ENABLE** 
</dt> <dd>

A value that enables the scheduled task. An enabled task can run, and a disabled task cannot run.

**Windows XP and Windows Server 2003:** This option is not available.

</dd> <dt>

<span id="_DISABLE_"></span><span id="_disable_"></span>**/DISABLE** 
</dt> <dd>

A value that disables the scheduled task from running.

> [!Note]  
> If a remote Task Scheduler 1.0 task is disabled by Schtasks.exe and the remote computer has the File and Printer Sharing firewall exception enabled and the Remote Scheduled Tasks Management firewall exception disabled, then the task will not be disabled when read from a Task Scheduler 2.0 API.

 

**Windows XP and Windows Server 2003:** This option is not available.

</dd> <dt>

<span id="_Z_"></span><span id="_z_"></span>**/Z** 
</dt> <dd>

A value that marks the task to be deleted after its final run.

**Windows XP and Windows Server 2003:** This option is not available.

</dd> <dt>

<span id="_DELAY_delaytime"></span><span id="_delay_delaytime"></span><span id="_DELAY_DELAYTIME"></span>**/DELAY** **delaytime**
</dt> <dd>

A value that specifies the wait time to delay the running of the task after the trigger is fired. The time format is mmmm:ss. This option is only valid for tasks with the schedule types ONSTART, ONLOGON, and ONEVENT.

**Windows XP and Windows Server 2003:** This option is not available.

</dd> <dt>

<span id="___"></span>**/?** 
</dt> <dd>

A value that displays the Help message for Schtasks.exe.

</dd> </dl>

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |



 

 





