---
title: CF\_EV\_SCOPE\_FILTER clipboard format
description: The CF\_EV\_SCOPE\_FILTER clipboard format returns the filter settings.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '8ec50ded-331e-4dbe-9397-ee6d650da995'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["CF_EV_SCOPE_FILTER clipboard format MMC"]
topic_type:
- apiref
api_name:
- CF_EV_SCOPE_FILTER
api_type:
- NA
---

# CF\_EV\_SCOPE\_FILTER clipboard format

The **CF\_EV\_SCOPE\_FILTER** clipboard format returns the filter settings. This clipboard format applies only to the Scope node type. Additionally, filter settings are not in effect unless the **VIEWINFO\_FILTERED** flag is set. The **VIEWINFO\_FILTERED** flag applies to the **flViewFlags** member of the **CF\_EV\_SCOPE** clipboard format.

## Data Format

The data provided by this clipboard format is structured as follows.


```C++
ULONG   flRecType,
USHORT  usCategory,
BOOL    fEventID,
ULONG   ulEventID,
USHORT  cchSource,
WCHAR   wszSource[],
USHORT  cchUser,
WCHAR   wszUser[],
USHORT  cchComputer,
WCHAR   wszComputer[],
ULONG   ulFrom,
ULONG   ulTo
```



## Member

<dl> <dt>

<span id="flRecType"></span><span id="flrectype"></span><span id="FLRECTYPE"></span>**flRecType**
</dt> <dd>

A value that specifies which event types are included in the view. This value is a bitwise OR of zero or more of the following flags. These flags are defined in WinNT.h. For more information, see [Event Types](https://msdn.microsoft.com/library/windows/desktop/aa363662).



| Flag                            | Description         |
|---------------------------------|---------------------|
| **EVENTLOG\_AUDIT\_FAILURE**    | Failure audit event |
| **EVENTLOG\_AUDIT\_SUCCESS**    | Success audit event |
| **EVENTLOG\_ERROR\_TYPE**       | Error event         |
| **EVENTLOG\_INFORMATION\_TYPE** | Information event   |
| **EVENTLOG\_WARNING\_TYPE**     | Warning event       |



 

</dd> <dt>

<span id="usCategory"></span><span id="uscategory"></span><span id="USCATEGORY"></span>**usCategory**
</dt> <dd>

If this value is zero, then a category is not used in the filter. If this value is nonzero, then **usCategory** specifies a category for the filter. Categories are defined by the event source.

</dd> <dt>

<span id="fEventID"></span><span id="feventid"></span><span id="FEVENTID"></span>**fEventID**
</dt> <dd>

A value that specifies whether the view is filtered by an event ID. If **fEventID** is **TRUE**, then the view is restricted to the events matching the **ulEventID** value.

</dd> <dt>

<span id="ulEventID"></span><span id="uleventid"></span><span id="ULEVENTID"></span>**ulEventID**
</dt> <dd>

Event ID. This value should be ignored unless **fEventID** is **TRUE**.

</dd> <dt>

<span id="cchSource"></span><span id="cchsource"></span><span id="CCHSOURCE"></span>**cchSource**
</dt> <dd>

Number of characters, including the terminating null character, in **wszSource**.

</dd> <dt>

<span id="wszSource"></span><span id="wszsource"></span><span id="WSZSOURCE"></span>**wszSource**
</dt> <dd>

Null-terminated Unicode string specifying the name of the source (for example, application, service, driver, or subsystem) that generated the event.

</dd> <dt>

<span id="cchUser"></span><span id="cchuser"></span><span id="CCHUSER"></span>**cchUser**
</dt> <dd>

Number of characters, including the terminating null character, in **wszUser**.

</dd> <dt>

<span id="wszUser"></span><span id="wszuser"></span><span id="WSZUSER"></span>**wszUser**
</dt> <dd>

Null-terminated Unicode string specifying the name of the user when the event was logged. Be aware that some events are not attributed to a specific user.

</dd> <dt>

<span id="cchComputer"></span><span id="cchcomputer"></span><span id="CCHCOMPUTER"></span>**cchComputer**
</dt> <dd>

Number of characters, including the terminating null character, in **wszComputer**.

</dd> <dt>

<span id="wszComputer"></span><span id="wszcomputer"></span><span id="WSZCOMPUTER"></span>**wszComputer**
</dt> <dd>

Null-terminated Unicode string specifying the name of the computer that generated this event.

</dd> <dt>

<span id="ulFrom"></span><span id="ulfrom"></span><span id="ULFROM"></span>**ulFrom**
</dt> <dd>

A value that specifies the beginning of the interval of events being filtered. If this value is zero, then there is no minimum timestamp on the filtered event records. If this value is nonzero, then **ulFrom** is the number of elapsed seconds since 00:00:00 January 1, 1970, Universal Coordinated Time. The **ulFrom** member serves as the minimum timestamp for the filtered event. That is, the **ulFrom** value is compared to the event log record time value, as specified by the **TimeGenerated** member of the [**EVENTLOGRECORD**](https://msdn.microsoft.com/library/windows/desktop/aa363646) structure.

</dd> <dt>

<span id="ulTo"></span><span id="ulto"></span><span id="ULTO"></span>**ulTo**
</dt> <dd>

A value that specifies the end of the interval of events being filtered. If this value is zero, then there is no maximum timestamp on the filtered event records. If this value is nonzero, then **ulTo** is the number of elapsed seconds since 00:00:00 January 1, 1970, Universal Coordinated Time. The **ulTo** member serves as the maximum timestamp for the filtered event. That is, the **ulTo** value is compared to the event log record time value, as specified by the **TimeGenerated** member of the [**EVENTLOGRECORD**](https://msdn.microsoft.com/library/windows/desktop/aa363646) structure.

</dd> </dl>

## Note

On 64-bit platforms, padding may be used by the **CF\_EV\_SCOPE\_FILTER** clipboard format so that the data is naturally aligned. For example, padding could occur at the end of a string if the string contains an odd number of wide characters.

 

 




