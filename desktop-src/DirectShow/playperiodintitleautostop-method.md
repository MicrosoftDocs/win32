---
description: The PlayPeriodInTitleAutoStop method starts playback at the specified time in the specified title until the specified stop time.
ms.assetid: 0c4df76d-3991-4a6c-a8e5-5fd713eeffc2
title: PlayPeriodInTitleAutoStop Method
ms.topic: reference
ms.date: 05/31/2018
---

# PlayPeriodInTitleAutoStop Method

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `PlayPeriodInTitleAutoStop` method starts playback at the specified time in the specified title until the specified stop time.

``` syntax
MSWebDVD.PlayPeriodInTitleAutoStop(iTitle, sStartTime, sEndTime)
```

## Parameters

<dl> <dt>

<span id="iTitle"></span><span id="ititle"></span><span id="ITITLE"></span>*iTitle*
</dt> <dd>

Specifies the title as an Integer.

</dd> <dt>

<span id="sStartTime"></span><span id="sstarttime"></span><span id="SSTARTTIME"></span>*sStartTime*
</dt> <dd>

Specifies the start time as a string in "hh:mm:ss:ff" format (specifying hours, minutes, seconds, frames).

</dd> <dt>

<span id="sEndTime"></span><span id="sendtime"></span><span id="SENDTIME"></span>*sEndTime*
</dt> <dd>

Specifies the end time as a String in "hh:mm:ss:ff" format.

</dd> </dl>

## Return Value

No return value.

## See also

<dl> <dt>

[**PlayChaptersAutoStop**](playchaptersautostop-method.md)
</dt> </dl>

 

 



