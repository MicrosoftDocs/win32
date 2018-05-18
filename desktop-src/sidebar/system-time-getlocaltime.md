---
title: System.Time.getLocalTime method
description: Gets the system time for a specific time zone.
ms.assetid: '55083fd2-c215-4836-9679-a5699990d824'
keywords: ["getLocalTime method Windows Sidebar", "getLocalTime method Windows Sidebar , System.Time object", "System.Time object Windows Sidebar , getLocalTime method"]
topic_type:
- apiref
api_name:
- System.Time.getLocalTime
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Time.getLocalTime method

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the system time for a specific time zone.

## Syntax


```JScript
strRetVal = System.Time.getLocalTime(
  oTimeZone
)
```



## Parameters

<dl> <dt>

*oTimeZone* \[in\]
</dt> <dd>

[**System.Time.timeZone**](system-time-timezone.md) that specifies the desired time zone offset.

</dd> </dl>

## Return value

The system time, adjusted for time zone offset, as a **String**.

## Remarks

Each [**System.Time.timeZone**](system-time-timezone.md) in the [**timeZones**](system-time-timezones.md) collection corresponds to the system time zones itemized in the **Time Zone Settings** dialog.

The following image shows the Time Zone Settings dialog.

![time zone settings dialog](images/reference/timezonesettings.png)

## Examples

The following example demonstrates how to get the local time based on a selected time zone.


```JScript
var oSelectedTimeZone = System.Time.currentTimeZone;
    
// --------------------------------------------------------------------
// Display the system time based on selected time zone.
// --------------------------------------------------------------------
function DisplayTime()
{
    // Retrieve the local time.
    var sTimeInfo = System.Time.getLocalTime(oSelectedTimeZone);
    if (sTimeInfo != "")
    {
        System.Sound.beep();
        var dDateInfo = new Date(Date.parse(sTimeInfo));   
        tHours = dDateInfo.getHours();
        tMinutes = dDateInfo.getMinutes();
        tMinutes = ((tMinutes < 10) ? ":0" : ":") + tMinutes
        tSeconds = dDateInfo.getSeconds();
        tSeconds = ((tSeconds < 10) ? ":0" : ":") + tSeconds;
        return tHours + tMinutes + tSeconds;
    }
    else
    {
        // Display default text.
    }
}
```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Sysinfoapi.h</dt> </dl>                        |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**System.Time**](system-time.md)
</dt> <dt>

[**currentTimeZone**](system-time-currenttimezone.md)
</dt> <dt>

[**timeZones**](system-time-timezones.md)
</dt> <dt>

[**System.Time.timeZone**](system-time-timezone.md)
</dt> <dt>

[**bias**](system-time-timezone-bias.md)
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

[**standardDate**](system-time-timezone-standarddate.md)
</dt> <dt>

[**standardDisplayName**](system-time-timezone-standarddisplayname.md)
</dt> </dl>

 

 





