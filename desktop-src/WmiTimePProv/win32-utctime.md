---
Description: The Win32\_UTCTimeWMI class describes a point in time that is returned as Win32\_UTCTime objects that result from a query.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0e28819a-56ea-45c6-b1bd-7043d03159cd
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_UTCTime class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Win32\_UTCTime class

The **Win32\_UTCTime**[WMI class](https://msdn.microsoft.com/library/aa393244) describes a point in time that is returned as **Win32\_UTCTime** objects that result from a query. These are returned as the value for the **TargetInstance** property in the [**\_\_InstanceModificationEvent**](https://msdn.microsoft.com/library/aa394651) system class. The **Hour** property is returned as the Coordinated Universal Time (UTC) time on a 24 hour clock.

> [!Note]  
> The smallest time segment supported is a second.

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[dynamic, provider("Win32ClockProvider"), AMENDMENT]
class Win32_UTCTime : Win32_CurrentTime
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

The **Win32\_UTCTime** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_UTCTime** class has these properties.

<dl> <dt>

**Day**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current day that matches the query (1 31).

This property is inherited from [**Win32\_CurrentTime**](win32-currenttime.md).

</dd> <dt>

**DayOfWeek**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current day of the current week that matches the query (0 6). By convention, the value 0 (zero) is always Sunday, regardless of the culture or the locale set on the machine.

This property is inherited from [**Win32\_CurrentTime**](win32-currenttime.md).

</dd> <dt>

**Hour**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current hour of the current day (0 23).

This property is inherited from [**Win32\_CurrentTime**](win32-currenttime.md).

</dd> <dt>

**Milliseconds**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Not implemented.

This property is inherited from [**Win32\_CurrentTime**](win32-currenttime.md).

</dd> <dt>

**Minute**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current minute (0 59).

This property is inherited from [**Win32\_CurrentTime**](win32-currenttime.md).

</dd> <dt>

**Month**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current month that matches the query (1 12).

This property is inherited from [**Win32\_CurrentTime**](win32-currenttime.md).

</dd> <dt>

**Quarter**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current quarter of the current year (1 4).

This property is inherited from [**Win32\_CurrentTime**](win32-currenttime.md).

</dd> <dt>

**Second**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current second of the current minute (0 59).

This property is inherited from [**Win32\_CurrentTime**](win32-currenttime.md).

</dd> <dt>

**WeekInMonth**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current week in the current month (1 6).

This property is inherited from [**Win32\_CurrentTime**](win32-currenttime.md).

</dd> <dt>

**Year**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current year matching the query (4 digits).

This property is inherited from [**Win32\_CurrentTime**](win32-currenttime.md).

</dd> </dl>

## Remarks

When you subscribe to events by using this class, you can create sophisticated schedules that can be implemented through events returned from WMI. For example, you can subscribe to an event for a specific day of the week in a specific quarter of a specific year. However, for schedules, the [**Win32\_LocalTime**](win32-localtime.md) class is more commonly used unless UTC time is required.

The following query example shows you how to generate an event every Friday morning at 8:00:00 (UTC time) during the entire year of 2001. However, if the line "AND TargetInstance.Second=0" is removed, then the query generates 60 notifications between 8:00:00 and 8:01:00, every Friday morning in 2001.


```VB
SELECT * FROM __InstanceModificationEvent
WHERE
    TargetInstance ISA "Win32_UTCTime" 
    AND TargetInstance.Year = 2001 
    AND TargetInstance.DayOfWeek=5 
    AND TargetInstance.Hour=8 
    AND TargetInstance.Minute=0 
    AND TargetInstance.Second=0
```



The following query example shows you how to generate events every second forever.


```VB
SELECT * FROM __InstanceModificationEvent
WHERE
    TargetInstance ISA "Win32_UTCTime"
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

[Creating a Timer Event with Win32\_LocalTime or Win32\_UTCTime](https://msdn.microsoft.com/library/aa389758)
</dt> <dt>

[**Win32\_LocalTime**](win32-localtime.md)
</dt> <dt>

[**Win32\_CurrentTime**](win32-currenttime.md)
</dt> </dl>

 

 




