---
description: The NotifyParentalLevelChange method enables or disables the event handling for temporary parental management level commands.
ms.assetid: c8252cc6-a83f-4cce-ba3e-7db669eeb465
title: NotifyParentalLevelChange Method (Segment.h)
ms.topic: reference
ms.date: 05/31/2018
---

# NotifyParentalLevelChange Method

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `NotifyParentalLevelChange` method enables or disables the event handling for temporary parental management level commands.

``` syntax
MSWebDVD.NotifyParentalLevelChange(bNotify)
```

## Parameters

<dl> <dt>

<span id="bNotify"></span><span id="bnotify"></span><span id="BNOTIFY"></span>*bNotify*
</dt> <dd>

Specifies a Boolean value indicating whether or not the application is notified when the MSWebDVD object encounters video segments with a rating more restrictive than the overall rating for the disc.

</dd> </dl>

## Return Value

No return value.

## Remarks

Parental management notifications are disabled by default. This means that temporary parental commands from the disc are allowed but ignored and disc will play without interruption. Call this method during initialization of your application if you need to handle temporary parental management level commands from the disc. To disable parental management after it is enabled, call this method with an argument of false. For more details on parental management, see [**AcceptParentalLevelChange**](acceptparentallevelchange-method.md).

## Requirements



| Requirement | Value |
|-------------------|--------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Segment.h</dt> </dl> |



## See also

<dl> <dt>

[**SelectParentalLevel**](selectparentallevel-method.md)
</dt> <dt>

[**GetTitleParentalLevels**](gettitleparentallevels-method.md)
</dt> <dt>

[**GetPlayerParentalCountry**](getplayerparentalcountry-method.md)
</dt> <dt>

[**GetPlayerParentalLevel**](getplayerparentallevel-method.md)
</dt> <dt>

[**SelectParentalCountry**](selectparentalcountry-method.md)
</dt> </dl>

 

 




