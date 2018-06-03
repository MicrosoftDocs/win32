---
title: System.Time object
description: Defines the properties and methods for determining system time information as well as the properties for the timeZones collection.
ms.assetid: 09defa9c-0ba5-40e8-9ab9-35c2201c5005
keywords:
- System.Time object Windows Sidebar
- System.Time object Windows Sidebar , described
topic_type:
- apiref
api_name:
- System.Time
api_location:
- Sidebar.Exe
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# System.Time object

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Defines the properties and methods for determining system time information as well as the properties for the [**timeZones**](system-time-timezones.md) collection.

> [!Note]  
> Objects of type [**System.Time.timeZone**](system-time-timezone.md) can only be accessed through the [**timeZones**](system-time-timezones.md) collection. This collection is a member of **System.Time**.

 

## Members

The **System.Time** object has these types of members:

-   [Collections](#events)
-   [Methods](#methods)
-   [Properties](#properties)

### Collections

The **System.Time** object has these collections.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Collection</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;">[<strong>timeZones</strong>](system-time-timezones.md)</td>
<td style="text-align: left;">A collection of [<strong>System.Time.timeZone</strong>](system-time-timezone.md) objects. <br/>
<blockquote>
[!Note]<br />
Objects of type [<strong>System.Time.timeZone</strong>](system-time-timezone.md) can only be accessed through the [<strong>timeZones</strong>](system-time-timezones.md) collection. This collection is a member of <strong>System.Time</strong>.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

### Methods

The **System.Time** object has these methods.



| Method                                           | Description                                                |
|:-------------------------------------------------|:-----------------------------------------------------------|
| [**getLocalTime**](system-time-getlocaltime.md) | Gets the system time for a specific time zone. <br/> |



 

### Properties

The **System.Time** object has these properties.



| Property                                                          | Access type          | Description                                                                                                          |
|:------------------------------------------------------------------|:---------------------|:---------------------------------------------------------------------------------------------------------------------|
| [**currentTimeZone**](system-time-currenttimezone.md)<br/> | Read-only<br/> | Gets a [**System.Time.timeZone**](system-time-timezone.md) object that represents the system time zone. <br/> |



 

## Remarks

Each [**System.Time.timeZone**](system-time-timezone.md) in the [**timeZones**](system-time-timezones.md) collection corresponds to the time zones itemized in the **Time Zone Settings** dialog.

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



 

 





