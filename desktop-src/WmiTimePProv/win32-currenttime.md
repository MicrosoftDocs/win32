---
Description: The Win32\_CurrentTime abstract is a singleton WMI class that describes a point in time by using the component items, such as milliseconds, seconds, minutes, hours, days, days of the week, week in the month, months, quarters, and years.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: dbf9e183-e45d-41ba-b872-5435562cace1
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_CurrentTime class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_CurrentTime class

The **Win32\_CurrentTime** abstract is a singleton [WMI class](https://msdn.microsoft.com/library/aa393244) that describes a point in time by using the component items, such as milliseconds, seconds, minutes, hours, days, days of the week, week in the month, months, quarters, and years.

The following two important classes are derived from this class. [**Win32\_LocalTime**](win32-localtime.md) allows you to monitor time in local reference and [**Win32\_UTCTime**](win32-utctime.md) allows you to monitor time in coordinated universal time (UTC) reference.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, Singleton, AMENDMENT]
class Win32_CurrentTime
{
  uint32 Day;
  uint32 DayOfWeek;
  uint32 Hour;
  uint32 Milliseconds;
  uint32 Minute;
  uint32 Month;
  uint32 Quarter;
  uint32 Second;
  uint32 WeekInMonth;
  uint32 Year;
};
```

## Members

The **Win32\_CurrentTime** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_CurrentTime** class has these properties.

<dl> <dt>

**Day**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current day that matches the query (1 31).

</dd> <dt>

**DayOfWeek**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current day of the current week that match the query (0 6). By convention, the value 0 (zero) is always Sunday, regardless of the culture or the locale set on the machine.

</dd> <dt>

**Hour**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current hour of the current day (0 23).

</dd> <dt>

**Milliseconds**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Not used.

This property is not returned.

</dd> <dt>

**Minute**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current minute (0 59).

</dd> <dt>

**Month**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current month that matches the query (1 12).

</dd> <dt>

**Quarter**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current quarter of the current year (1 4).

</dd> <dt>

**Second**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current second of the current minute (0 59).

</dd> <dt>

**WeekInMonth**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current week (1 6) in the current month (1 12).

</dd> <dt>

**Year**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current year that matches the query (4 digits).

</dd> </dl>

## Remarks

You cannot subscribe to events with this class because it is abstract and cannot have instances. However, use either [**Win32\_LocalTime**](win32-localtime.md) or [**Win32\_UTCTime**](win32-utctime.md) to subscribe to events.

## Examples

The following PowerShell code sample displays both local and UTC time.


```PowerShell
# Get Local Time and UTC Time
$Localtime, $UTCTime = gwmi win32_currenttime

# Display local and UTC time
"Local Time:"
" Day           : {0}" -f $localtime.day
" Day Of Week   : {0}" -f $localtime.dayofweek
" Hour          : {0}" -f $localtime.hour
" Milliseconds  : {0}" -f $localtime.Milliseconds
" Minute        : {0}" -f $localtime.minute
" Month         : {0}" -f $localtime.month
" Quarter       : {0}" -f $localtime.quarter
" Second        : {0}" -f $localtime.second
" Week in Month : {0}" -f $localtime.weekinmonth
" Year          : {0}" -f $localtime.year
""

# Display UTC
"UTC Time:"
" Day           : {0}" -f $UTCTime.day
" Day Of Week   : {0}" -f $UTCTime.dayofweek
" Hour          : {0}" -f $UTCTime.hour
" Milliseconds  : {0}" -f $UTCTime.Milliseconds
" Minute        : {0}" -f $UTCTime.minute
" Month         : {0}" -f $UTCTime.month
" Quarter       : {0}" -f $UTCTime.quarter
" Second        : {0}" -f $UTCTime.second
" Week in Month : {0}" -f $UTCTime.weekinmonth
" Year          : {0}" -f $UTCTime.year
""
```



The previous code sample creates the following output:

``` syntax
Local Time:
 Day           : 23
 Day Of Week   : 6
 Hour          : 14
 Milliseconds  :
 Minute        : 28
 Month         : 6
 Quarter       : 2
 Second        : 16
 Week in Month : 4
 Year          : 2007

UTC Time:
 Day           : 23
 Day Of Week   : 6
 Hour          : 13
 Milliseconds  :
 Minute        : 28
 Month         : 6
 Quarter       : 2
 Second        : 16
 Week in Month : 4
 Year          : 2007
```

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Wmitimep.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wmitimep.dll</dt> </dl> |



## See also

<dl> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> <dt>

[**Win32\_LocalTime**](win32-localtime.md)
</dt> <dt>

[**Win32\_UTCTime**](win32-utctime.md)
</dt> <dt>

[Creating a Timer Event with Win32\_LocalTime or Win32\_UTCTime](https://msdn.microsoft.com/library/aa389758)
</dt> </dl>

 

 




