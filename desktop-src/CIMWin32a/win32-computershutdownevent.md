---
title: Win32\_ComputerShutdownEvent class
description: The Win32\_ComputerShutdownEvent is a Windows Management Instrumentation (WMI) event class that represents events when a computer begins the process of shutting down.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3787b9f2-d753-4918-aabf-050bbb5f6bc4
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Win32_ComputerShutdownEvent class
- Win32_ComputerShutdownEvent class, described
topic_type:
- apiref
api_name:
- Win32_ComputerShutdownEvent
- Win32_ComputerShutdownEvent.MachineName
- Win32_ComputerShutdownEvent.SECURITY_DESCRIPTOR
- Win32_ComputerShutdownEvent.TIME_CREATED
- Win32_ComputerShutdownEvent.Type
api_location:
- WmiPciMa.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_ComputerShutdownEvent class

The **Win32\_ComputerShutdownEvent** is a Windows Management Instrumentation (WMI) event class that represents events when a computer begins the process of shutting down. It identifies the type of shutdown, which can be a user log off, complete shutdown, or restart.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[UUID("{A6B834B1-F974-4445-8F2E-FC996638B350}"), AMENDMENT]
class Win32_ComputerShutdownEvent : Win32_ComputerSystemEvent
{
  string MachineName;
  uint8  SECURITY_DESCRIPTOR[];
  uint64 TIME_CREATED;
  uint32 Type;
};
```

## Members

The **Win32\_ComputerShutdownEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_ComputerShutdownEvent** class has these properties.

<dl> <dt>

**MachineName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: 
</dt> </dl>

Name of the computer for which the event occurred.

This property is inherited from [**Win32\_ComputerSystemEvent**](win32-computersystemevent.md).

</dd> <dt>

**SECURITY\_DESCRIPTOR**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Descriptor that the event provider uses to determine which users can receive the event.

This property is inherited from [**Win32\_ComputerSystemEvent**](win32-computersystemevent.md).

</dd> <dt>

**TIME\_CREATED**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Unique value that indicates the time an event is generated. This is a 64-bit value that represents the number of 100-nanosecond intervals after January 1, 1601. The information is in the Coordinated Universal Time (UTC) format.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

This property is inherited from [**Win32\_ComputerSystemEvent**](win32-computersystemevent.md).

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The following list lists the values of the type of shutdown initiated.

<dt>

<span id="Log_Off"></span><span id="log_off"></span><span id="LOG_OFF"></span>

<span id="Log_Off"></span><span id="log_off"></span><span id="LOG_OFF"></span>**Log Off** (0)


</dt> <dd>

"Log off"

</dd> <dt>

<span id="Shutdown_or_Reboot"></span><span id="shutdown_or_reboot"></span><span id="SHUTDOWN_OR_REBOOT"></span>

<span id="Shutdown_or_Reboot"></span><span id="shutdown_or_reboot"></span><span id="SHUTDOWN_OR_REBOOT"></span>**Shutdown or Reboot** (1)


</dt> <dd>

"Shutdown or Reboot"

</dd> </dl>

</dd> </dl>

## Remarks

The **Win32\_ComputerShutdownEvent** class is derived from [**Win32\_ComputerSystemEvent**](win32-computersystemevent.md).

**Win32\_ComputerShutdownEvent** may not work properly on local systems, as the application that receives the event may be terminated before the event is delivered. However, the event does still work for remote system shutdowns.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>WmiPciMa.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WmiPciMa.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_ComputerSystemEvent**](win32-computersystemevent.md)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/dn792258)
</dt> </dl>

 

 





