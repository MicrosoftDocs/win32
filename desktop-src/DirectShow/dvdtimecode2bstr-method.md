---
description: The DVDTimeCode2bstr method retrieves a string indicating the current time on the disc.
ms.assetid: 0a477274-ac56-4f46-8461-53411362b33e
title: DVDTimeCode2bstr Method
ms.topic: reference
ms.date: 05/31/2018
---

# DVDTimeCode2bstr Method

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `DVDTimeCode2bstr` method retrieves a string indicating the current time on the disc.

``` syntax
[ sTimeCode = ] MSWebDVD.DVDTimeCode2bstr(nTimeCode)
```

## Parameters

<dl> <dt>

<span id="sTimeCode"></span><span id="stimecode"></span><span id="STIMECODE"></span>*sTimeCode*
</dt> <dd>

Specifies the current time on the disc relative to the start of the title as a Number obtained through the [**EC\_DVD\_CURRENT\_HMSF\_TIME**](ec-dvd-current-hmsf-time.md) event.

</dd> </dl>

## Return Value

Returns an 11-character String in the format "hh:mm:ss:ff" representing the hours, minutes, seconds and frames that define the current time.

## Remarks

This method is read only.

## See also

<dl> <dt>

[Handling DVD Event Notifications](handling-dvd-event-notifications.md)
</dt> </dl>

 

 



