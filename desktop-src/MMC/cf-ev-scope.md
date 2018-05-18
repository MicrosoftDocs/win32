---
title: CF\_EV\_SCOPE clipboard format
description: The CF\_EV\_SCOPE clipboard format returns settings information, such as which event log is being viewed. This clipboard format applies only to the Scope node type.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'ac1737f9-773e-4132-918e-c2fbfdd2953d'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["CF_EV_SCOPE clipboard format MMC"]
topic_type:
- apiref
api_name:
- CF_EV_SCOPE
api_type:
- NA
---

# CF\_EV\_SCOPE clipboard format

The **CF\_EV\_SCOPE** clipboard format returns settings information, such as which event log is being viewed. This clipboard format applies only to the Scope node type.

## Data Format

The following example shows the display of the data provided by this clipboard format.


```C++
ULONG   flViewFlags,
ULONG   ulType,
USHORT  cchServerName,
WCHAR   wszServerName[],
USHORT  cchLogName,
WCHAR   wszLogName[],
USHORT  cchFileName,
WCHAR   wszFileName[],
USHORT  cchDisplayName,
WCHAR   wszDisplayName[]
```



## Members

<dl> <dt>

<span id="flViewFlags"></span><span id="flviewflags"></span><span id="FLVIEWFLAGS"></span>**flViewFlags**
</dt> <dd>

Describes the view. This value is a bitwise OR of zero or more of the following flags.



| Flag                        | Value  | Description                                                                                                                                                                               |
|-----------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **VIEWINFO\_BACKUP**        | 0x0001 | The view is for an archived .evt file. The Event Log service is not actively using this file, and the Event Viewer snap-in will not offer commands for configuring or clearing this file. |
| **VIEWINFO\_FILTERED**      | 0x0002 | The view is filtered. Use the **CF\_EV\_SCOPE\_FILTER** clipboard format to retrieve the filter settings.                                                                                 |
| **VIEWINFO\_LOW\_SPEED**    | 0x0004 | The event log is being accessed over a low-speed connection.                                                                                                                              |
| **VIEWINFO\_USER\_CREATED** | 0x0008 | The view was created by the user using the **New View** command. If this flag is not set, then the event log was discovered by enumeration of the log keys in the registry.               |
| **VIEWINFO\_ALLOW\_DELETE** | 0x0100 | The user can delete the view.                                                                                                                                                             |
| **VIEWINFO\_DISABLED**      | 0x0200 | The event log is disabled due to an error while attempting to access the log. If the user selects the **Refresh** command, this flag is cleared.                                          |
| **VIEWINFO\_READ\_ONLY**    | 0x0400 | The console process has read-only access to the event log.                                                                                                                                |
| **VIEWINFO\_DONT\_PERSIST** | 0x0800 | The view is not saved to the console file.                                                                                                                                                |



 

</dd> <dt>

<span id="ulType"></span><span id="ultype"></span><span id="ULTYPE"></span>**ulType**
</dt> <dd>

A value that specifies the event log type. This member can be one of the following values.



| Event log type       | Value | Description                                                      |
|----------------------|-------|------------------------------------------------------------------|
| **ELT\_APPLICATION** | 103   | Application log.                                                 |
| **ELT\_CUSTOM**      | 104   | All other logs besides the Application, Security or System logs. |
| **ELT\_SECURITY**    | 102   | Security log.                                                    |
| **ELT\_SYSTEM**      | 101   | System log.                                                      |



 

</dd> <dt>

<span id="cchServerName"></span><span id="cchservername"></span><span id="CCHSERVERNAME"></span>**cchServerName**
</dt> <dd>

Number of characters, including the terminating null character, in **wszServerName**.

</dd> <dt>

<span id="wszServerName"></span><span id="wszservername"></span><span id="WSZSERVERNAME"></span>**wszServerName**
</dt> <dd>

Null-terminated Unicode string specifying the computer name. If the selected node is for the local computer, then **wszServername** will be an empty string, L"", and **cchServerName** will be 1.

</dd> <dt>

<span id="cchLogName"></span><span id="cchlogname"></span><span id="CCHLOGNAME"></span>**cchLogName**
</dt> <dd>

Number of characters, including the terminating null character, in **wszLogName**.

</dd> <dt>

<span id="wszLogName"></span><span id="wszlogname"></span><span id="WSZLOGNAME"></span>**wszLogName**
</dt> <dd>

Null-terminated Unicode string specifying the event log name.

</dd> <dt>

<span id="cchFileName"></span><span id="cchfilename"></span><span id="CCHFILENAME"></span>**cchFileName**
</dt> <dd>

Number of characters, including the terminating null character, in **wszFileName**.

</dd> <dt>

<span id="wszFileName"></span><span id="wszfilename"></span><span id="WSZFILENAME"></span>**wszFileName**
</dt> <dd>

Null-terminated Unicode string specifying the event log file name. If the selected node is for a remote computer, then **wszFileName** is a Universal Naming Convention (UNC) path to the event log file. The path contains an administrative share, for example, "\\\\myserver\\C$\\windows\\system32\\config\\application.evt". Be aware that the console process may not have access permission to the event log file. If the selected node is for the local computer, the path is based on the local drive, for example, "c:\\windows\\system32\\config\\application.evt".

</dd> <dt>

<span id="cchDisplayName"></span><span id="cchdisplayname"></span><span id="CCHDISPLAYNAME"></span>**cchDisplayName**
</dt> <dd>

Number of characters, including the terminating null character, in **wszDisplayName**.

</dd> <dt>

<span id="wszDisplayName"></span><span id="wszdisplayname"></span><span id="WSZDISPLAYNAME"></span>**wszDisplayName**
</dt> <dd>

Null-terminated Unicode string specifying the event log display name. This member is the name of the view's scope item.

</dd> </dl>

## Note

On 64-bit platforms, padding may be used by the **CF\_EV\_SCOPE** clipboard format so that the data is naturally aligned. For example, padding could occur at the end of a string if the string contains an odd number of wide characters.

 

 




