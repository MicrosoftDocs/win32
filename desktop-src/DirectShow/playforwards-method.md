---
description: The PlayForwards method starts forward playback from the current location at the specified speed.
ms.assetid: 4f1a3e74-b343-413d-8df7-6c4bea39c62d
title: PlayForwards Method
ms.topic: reference
ms.date: 05/31/2018
---

# PlayForwards Method

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `PlayForwards` method starts forward playback from the current location at the specified speed.

``` syntax
MSWebDVD.PlayForwards(nSpeed)
```

## Parameters

<dl> <dt>

<span id="nSpeed"></span><span id="nspeed"></span><span id="NSPEED"></span>*nSpeed*
</dt> <dd>

Specifies the speed at which to play as an Integer value. This value is a multiplier—1.0 is normal playback speed; 2.0 is double speed, 0.5 is half speed, and so on. When**nSpeed**does not equal 1.0, audio is muted and the subpicture is turned off.

</dd> </dl>

## Return Value

No return value.

## See also

<dl> <dt>

[**PlayBackwards**](playbackwards-method.md)
</dt> </dl>

 

 



