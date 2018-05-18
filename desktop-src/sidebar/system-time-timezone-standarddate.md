---
title: System.Time.timeZone.standardDate property
description: Gets the system date and local time when the transition from daylight saving time to standard time occurs on this operating system.
ms.assetid: '85c17936-3108-4831-957c-cd855cf79f2e'
keywords: ["standardDate property Windows Sidebar", "standardDate property Windows Sidebar , System.Time.timeZone object", "System.Time.timeZone object Windows Sidebar , standardDate property"]
topic_type:
- apiref
api_name:
- System.Time.timeZone.standardDate
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Time.timeZone.standardDate property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the system date and local time when the transition from daylight saving time to standard time occurs on this operating system.

This property is read-only.

## Syntax


```JScript
strstandardDate = System.Time.timeZone.standardDate
```



## Property value

A **String** that receives the date and local time.

> [!Note]  
> The year returned should be ignored.

 

## Examples

The following example demonstrates how to get system time details based on selected time zone.


```JScript
var oSelectedTimeZone = System.Time.currentTimeZone;

// Set the time zone details.
var sTimeZoneDetails = function() 
{
    var sDetails = "";
    sDetails += "Bias: " + oSelectedTimeZone.bias + "<hr />";
    sDetails += "Display Name: " + oSelectedTimeZone.displayName + "<hr />";
    sDetails += "DST Bias: " + oSelectedTimeZone.DSTBias + "<hr />";
    sDetails += "DST Date: " + oSelectedTimeZone.DSTDate + "<hr />";
    sDetails += "DST Display Name: " + oSelectedTimeZone.DSTDisplayName + "<hr />";
    sDetails += "Name: " + oSelectedTimeZone.name + "<hr />";
    sDetails += "Standard Bias: " + oSelectedTimeZone.standardBias + "<hr />";
    sDetails += "Standard Date: " + oSelectedTimeZone.standardDate + "<hr />";
    sDetails += "Standard Display Name: " + oSelectedTimeZone.standardDisplayName;
    return sDetails;
}
```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**System.Time.timeZone**](system-time-timezone.md)
</dt> <dt>

[**System.Time**](system-time.md)
</dt> <dt>

[**timeZones**](system-time-timezones.md)
</dt> <dt>

[**displayName**](system-time-timezone-displayname.md)
</dt> <dt>

[**DSTBias**](system-time-timezone-dstbias.md)
</dt> <dt>

[**DSTDate**](system-time-timezone-dstdate.md)
</dt> <dt>

[**DSTDisplayName**](system-time-timezone-dstdisplayname.md)
</dt> <dt>

[**name**](system-time-timezone-name.md)
</dt> <dt>

[**standardBias**](system-time-timezone-standardbias.md)
</dt> <dt>

[**standardDisplayName**](system-time-timezone-standarddisplayname.md)
</dt> <dt>

[**currentTimeZone**](system-time-currenttimezone.md)
</dt> <dt>

[**getLocalTime**](system-time-getlocaltime.md)
</dt> </dl>

 

 





