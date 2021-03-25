---
description: The DVDNotify event notifies an application of many different DVD events and disc instructions.
ms.assetid: 8e7d85fb-95c0-472d-ab17-a82da303b68f
title: DVDNotify (Segment.h)
ms.topic: reference
ms.date: 05/31/2018
---

# DVDNotify

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `DVDNotify` event notifies an application of many different DVD events and disc instructions.

``` syntax
DVDNotify(EventCode, Param1, Param2)
```

## Parameters

<dl> <dt>

<span id="EventCode"></span><span id="eventcode"></span><span id="EVENTCODE"></span>*EventCode*
</dt> <dd>

Specifies the DVD event notification code.

</dd> <dt>

<span id="Param1"></span><span id="param1"></span><span id="PARAM1"></span>*Param1*
</dt> <dd>

Can contain additional information related to the event.

</dd> <dt>

<span id="Param2"></span><span id="param2"></span><span id="PARAM2"></span>*Param2*
</dt> <dd>

Can contain additional information related to the event.

</dd> </dl>

## Remarks

[DVD Event Notification Codes](dvd-notification-codes.md) gives a full explanation of all DVD event notification codes and their parameters.

## Requirements



| Requirement | Value |
|-------------------|--------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Segment.h</dt> </dl> |



 

 




