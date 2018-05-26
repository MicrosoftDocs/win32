---
title: System.Time.timeZone object
description: Defines the properties and methods of each member of the System.Time.timeZone collection.
ms.assetid: 68dcf69b-4d0b-4c44-9470-9f0bd7f6e8be
keywords:
- System.Time.timeZone object Windows Sidebar
- System.Time.timeZone object Windows Sidebar , described
topic_type:
- apiref
api_name:
- System.Time.timeZone
api_location:
- Sidebar.Exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.Time.timeZone object

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Defines the properties and methods of each member of the **System.Time.timeZone** collection.

## Members

The **System.Time.timeZone** object has these types of members:

-   [Properties](#properties)

### Properties

The **System.Time.timeZone** object has these properties.



| Property                                                                           | Access type          | Description                                                                                                                                     |
|:-----------------------------------------------------------------------------------|:---------------------|:------------------------------------------------------------------------------------------------------------------------------------------------|
| [**bias**](system-time-timezone-bias.md)<br/>                               | Read-only<br/> | Gets the number of minutes that a time zone is offset from UTC. <br/>                                                                     |
| [**displayName**](system-time-timezone-displayname.md)<br/>                 | Read-only<br/> | Gets the display name for a time zone. <br/>                                                                                              |
| [**DSTBias**](system-time-timezone-dstbias.md)<br/>                         | Read-only<br/> | Gets the Daylight Savings Time (DST) offset in minutes. <br/>                                                                             |
| [**DSTDate**](system-time-timezone-dstdate.md)<br/>                         | Read-only<br/> | Gets the system date and local time when the transition from standard time to daylight saving time occurs on this operating system. <br/> |
| [**DSTDisplayName**](system-time-timezone-dstdisplayname.md)<br/>           | Read-only<br/> | Gets the system display name for a time zone during Daylight Savings Time (DST). <br/>                                                    |
| [**name**](system-time-timezone-name.md)<br/>                               | Read-only<br/> | Gets the name for a time zone. <br/>                                                                                                      |
| [**standardBias**](system-time-timezone-standardbias.md)<br/>               | Read-only<br/> | Gets the Standard Time offset in minutes. <br/>                                                                                           |
| [**standardDate**](system-time-timezone-standarddate.md)<br/>               | Read-only<br/> | Gets the system date and local time when the transition from daylight saving time to standard time occurs on this operating system. <br/> |
| [**standardDisplayName**](system-time-timezone-standarddisplayname.md)<br/> | Read-only<br/> | Gets the system display name for a time zone during non-Daylight Savings Time (DST). <br/>                                                |



 

## Remarks

Each **System.Time.timeZone** in the [**timeZones**](system-time-timezones.md) collection corresponds to the system time zones itemized in the **Time Zone Settings** dialog.

The following image shows the Time Zone Settings dialog.

![time zone settings dialog](images/reference/timezonesettings.png)

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 





