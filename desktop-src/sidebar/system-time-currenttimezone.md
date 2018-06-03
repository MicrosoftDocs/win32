---
title: System.Time.currentTimeZone property
description: Gets a System.Time.timeZone object that represents the system time zone.
ms.assetid: 530b9cad-e215-4237-baca-ea0a785fb6d4
keywords:
- currentTimeZone property Windows Sidebar
- currentTimeZone property Windows Sidebar , System.Time object
- System.Time object Windows Sidebar , currentTimeZone property
topic_type:
- apiref
api_name:
- System.Time.currentTimeZone
api_location:
- Sidebar.Exe
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# System.Time.currentTimeZone property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets a [**System.Time.timeZone**](system-time-timezone.md) object that represents the system time zone.

This property is read-only.

## Syntax


```JScript
objcurrentTimeZone = System.Time.currentTimeZone
```



## Property value

An **Object** that receives a [**System.Time.timeZone**](system-time-timezone.md) instance.

## Remarks

Each [**System.Time.timeZone**](system-time-timezone.md) in the [**timeZones**](system-time-timezones.md) collection corresponds to the system time zones itemized in the **Time Zone Settings** dialog.

The following image shows the Time Zone Settings dialog.

![time zone settings dialog](images/reference/timezonesettings.png)

## Examples

The following example demonstrates how to use **currentTimeZone** to get the details for the system time zone.


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
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**System.Time.timeZone**](system-time-timezone.md)
</dt> <dt>

[**timeZones**](system-time-timezones.md)
</dt> <dt>

[**System.Time**](system-time.md)
</dt> <dt>

[**getLocalTime**](system-time-getlocaltime.md)
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

 

 





