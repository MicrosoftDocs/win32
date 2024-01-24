---
description: Submits a job to an operating system for execution at a specified time and date in the future.
ms.assetid: 9d582fbb-24cb-401d-8b77-af7671a24e6d
ms.tgt_platform: multiple
title: Create method of the Win32_ScheduledJob class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_ScheduledJob.Create
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# Create method of the Win32\_ScheduledJob class

The **Create** [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) method submits a job to an operating system for execution at a specified time and date in the future. This method requires that the schedule service be started on the computer to which the job is submitted.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 Create(
  [in]           string   Command,
  [in]           datetime StartTime,
  [in, optional] boolean  RunRepeatedly,
  [in, optional] uint32   DaysOfWeek,
  [in, optional] uint32   DaysOfMonth,
  [in, optional] boolean  InteractWithDesktop,
  [out]          uint32   JobId
);
```



## Parameters

<dl> <dt>

*Command* \[in\]
</dt> <dd>

Name of the command, batch program, or binary file and command-line parameters that the schedule service uses to invoke the job.

Example: "defrag /q /f".

</dd> <dt>

*StartTime* \[in\]
</dt> <dd>

Coordinated Universal Time (UTC) time to run a job. The form must be: "YYYYMMDDHHMMSS.MMMMMM(+-)OOO", where "YYYYMMDD" must be replaced by "\*\*\*\*\*\*\*\*". For example: "\*\*\*\*\*\*\*\*143000.000000-420" specifies 14.30 (2:30 P.M.) PST with daylight savings time in effect.

The "(+-)OOO" section of the StartTime property value is the current bias for local time translation. The bias is the difference between the UTC time and the local time. To calculate the bias for your time zone, multiply the number of hours that your time zone is ahead or behind Greenwich Mean Time (GMT) by 60 (use a positive number for the number of hours if your time zone is ahead of GMT and a negative number if your time zone is behind GMT). Add an additional 60 to your calculation if your time zone is using daylight savings time. For example, the Pacific Standard Time zone is eight hours behind GMT, therefore the bias is equals to -420 (-8 \* 60 + 60) when daylight savings time is in use and -480 (-8 \* 60) when daylight savings time is not in use. You can also determine the value of the bias by querying the bias property of the [**Win32\_TimeZone**](win32-timezone.md) class.

</dd> <dt>

*RunRepeatedly* \[in, optional\]
</dt> <dd>

If **True**, a scheduled job runs repeatedly on specific days. The default is **False**.

</dd> <dt>

*DaysOfWeek* \[in, optional\]
</dt> <dd>

Days of the week when a job is scheduled to run; used only when the *RunRepeatedly* parameter is **True**. To schedule a job for more than one day of the week, join the appropriate values in a logical OR. For example, to schedule a job for Tuesdays and Fridays, the value of *DaysOfWeek* are 2 OR 16.

<dt>

<span id="Monday"></span><span id="monday"></span><span id="MONDAY"></span>

**Monday** (1)


</dt> <dd></dd> <dt>

<span id="Tuesday"></span><span id="tuesday"></span><span id="TUESDAY"></span>

**Tuesday** (2)


</dt> <dd></dd> <dt>

<span id="Wednesday"></span><span id="wednesday"></span><span id="WEDNESDAY"></span>

**Wednesday** (4)


</dt> <dd></dd> <dt>

<span id="Thursday"></span><span id="thursday"></span><span id="THURSDAY"></span>

**Thursday** (8)


</dt> <dd></dd> <dt>

<span id="Friday"></span><span id="friday"></span><span id="FRIDAY"></span>

**Friday** (16)


</dt> <dd></dd> <dt>

<span id="Saturday"></span><span id="saturday"></span><span id="SATURDAY"></span>

**Saturday** (32)


</dt> <dd></dd> <dt>

<span id="Sunday"></span><span id="sunday"></span><span id="SUNDAY"></span>

**Sunday** (64)


</dt> <dd></dd> </dl> </dd> <dt>

*DaysOfMonth* \[in, optional\]
</dt> <dd>

Days of the month when a job is scheduled to run; used only when the *RunRepeatedly* parameter is **True**.

<dt>

<span id="1"></span>

<span id="1"></span>**1** (1)


</dt> <dd>

Day 1 of a month

</dd> <dt>

<span id="2"></span>

<span id="2"></span>**2** (2)


</dt> <dd>

Day 2 of a month

</dd> <dt>

<span id="3"></span>

<span id="3"></span>**3** (4)


</dt> <dd>

Day 3 of a month

</dd> <dt>

<span id="4"></span>

<span id="4"></span>**4** (8)


</dt> <dd>

Day 4 of a month

</dd> <dt>

<span id="5"></span>

<span id="5"></span>**5** (16)


</dt> <dd>

Day 5 of a month

</dd> <dt>

<span id="6"></span>

<span id="6"></span>**6** (32)


</dt> <dd>

Day 6 of a month

</dd> <dt>

<span id="7"></span>

<span id="7"></span>**7** (64)


</dt> <dd>

Day 7 of a month

</dd> <dt>

<span id="8"></span>

<span id="8"></span>**8** (128)


</dt> <dd>

Day 8 of a month

</dd> <dt>

<span id="9"></span>

<span id="9"></span>**9** (256)


</dt> <dd>

Day 9 of a month

</dd> <dt>

<span id="10"></span>

<span id="10"></span>**10** (512)


</dt> <dd>

Day 10 of a month

</dd> <dt>

<span id="11"></span>

<span id="11"></span>**11** (1024)


</dt> <dd>

Day 11 of a month

</dd> <dt>

<span id="12"></span>

<span id="12"></span>**12** (2048)


</dt> <dd>

Day 12 of a month

</dd> <dt>

<span id="13"></span>

<span id="13"></span>**13** (4096)


</dt> <dd>

Day 13 of a month

</dd> <dt>

<span id="14"></span>

<span id="14"></span>**14** (8192)


</dt> <dd>

Day 14 of a month

</dd> <dt>

<span id="15"></span>

<span id="15"></span>**15** (16384)


</dt> <dd>

Day 15 of a month

</dd> <dt>

<span id="16"></span>

<span id="16"></span>**16** (32768)


</dt> <dd>

Day 16 of a month

</dd> <dt>

<span id="17"></span>

<span id="17"></span>**17** (65536)


</dt> <dd>

Day 17 of a month

</dd> <dt>

<span id="18"></span>

<span id="18"></span>**18** (131072)


</dt> <dd>

Day 18 of a month

</dd> <dt>

<span id="19"></span>

<span id="19"></span>**19** (262144)


</dt> <dd>

Day 19 of a month

</dd> <dt>

<span id="20"></span>

<span id="20"></span>**20** (524288)


</dt> <dd>

Day 20 of a month

</dd> <dt>

<span id="21"></span>

<span id="21"></span>**21** (1048576)


</dt> <dd>

Day 21 of a month

</dd> <dt>

<span id="22"></span>

<span id="22"></span>**22** (2097152)


</dt> <dd>

Day 22 of a month

</dd> <dt>

<span id="23"></span>

<span id="23"></span>**23** (4194304)


</dt> <dd>

Day 23 of a month

</dd> <dt>

<span id="24"></span>

<span id="24"></span>**24** (8388608)


</dt> <dd>

Day 24 of a month

</dd> <dt>

<span id="25"></span>

<span id="25"></span>**25** (16777216)


</dt> <dd>

Day 25 of a month

</dd> <dt>

<span id="26"></span>

<span id="26"></span>**26** (33554432)


</dt> <dd>

Day 26 of a month

</dd> <dt>

<span id="27"></span>

<span id="27"></span>**27** (67108864)


</dt> <dd>

Day 27 of a month

</dd> <dt>

<span id="28"></span>

<span id="28"></span>**28** (134217728)


</dt> <dd>

Day 28 of a month

</dd> <dt>

<span id="29"></span>

<span id="29"></span>**29** (268435456)


</dt> <dd>

Day 29 of a month

</dd> <dt>

<span id="30"></span>

<span id="30"></span>**30** (536870912)


</dt> <dd>

Day 30 of a month

</dd> <dt>

<span id="31"></span>

<span id="31"></span>**31** (1073741824)


</dt> <dd>

Day 31 of a month

</dd> </dl> </dd> <dt>

*InteractWithDesktop* \[in, optional\]
</dt> <dd>

If **True**, the specified job should be interactive, which means that a user can give input to a scheduled job while the job is executing. The default is **False**.

</dd> <dt>

*JobId* \[out\]
</dt> <dd>

Identifier number of a job. This parameter is a handle to a job being scheduled on a computer.

</dd> </dl>

## Return value

Returns a value of 0 (zero) when successful, and a different number to indicate an error. For additional error codes, see [**WMI Error Constants**](/windows/desktop/WmiSdk/wmi-error-constants) or [**WbemErrorEnum**](/windows/desktop/api/wbemdisp/ne-wbemdisp-wbemerrorenum). For general **HRESULT** values, see [System Error Codes](/windows/desktop/Debug/system-error-codes).

<dl> <dt>

**Successful completion**
</dt> <dd>

0

The request is accepted.

</dd> <dt>

**Not supported**
</dt> <dd>

1

The request is not supported.

</dd> <dt>

**Access denied**
</dt> <dd>

2

The user does not have the necessary access.

</dd> <dt>

**Unknown failure**
</dt> <dd>

8

Interactive process.

</dd> <dt>

**Path not found**
</dt> <dd>

9

The directory path to the service executable file cannot be found.

</dd> <dt>

**Invalid parameter**
</dt> <dd>

21

Invalid parameters have been passed to the service.

</dd> <dt>

**Service not started**
</dt> <dd>

22

The account that this service runs under is invalid or lacks the permissions to run the service.

</dd> <dt>

**Other**
</dt> <dd>

23 4294967295

</dd> </dl>

## Remarks

If your scheduled job starts an interactive program such as Notepad, then the **InteractWithDeskto** property must be set to **True** or the program's screen is not visible. The process still appears in the **Task Manager** even if it does not appear on the screen.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[Operating System Classes](/previous-versions//aa392727(v=vs.85))
</dt> <dt>

[**Win32\_ScheduledJob**](win32-scheduledjob.md)
</dt> </dl>

 

