---
description: The PlayBackwards method starts backward playback from the current location at the specified speed.
ms.assetid: 7f8421e7-f835-4a10-a9c9-0e43de159e4f
title: PlayBackwards Method
ms.topic: reference
ms.date: 05/31/2018
---

# PlayBackwards Method

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `PlayBackwards` method starts backward playback from the current location at the specified speed.

``` syntax
MSWebDVD.PlayBackwards(nSpeed)
```

## Parameters

<dl> <dt>

<span id="nSpeed"></span><span id="nspeed"></span><span id="NSPEED"></span>*nSpeed*
</dt> <dd>

Specifies the speed at which to play as a number. This number is a multiplier—1.0 is normal playback speed; 2.0 is double speed, 0.5 is half speed, and so on. When**nSpeed**does not equal 1.0, audio is muted and the subpicture is turned off.

</dd> </dl>

## Return Value

No return value.

## See also

<dl> <dt>

[**PlayForwards**](playforwards-method.md)
</dt> </dl>

 

 



