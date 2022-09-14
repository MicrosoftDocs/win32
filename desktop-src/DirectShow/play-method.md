---
description: The Play method plays the current DVD title.
ms.assetid: fe9dc266-5b12-479d-85cb-50cc6bb9d580
title: Play Method (DirectShow)
ms.topic: reference
ms.date: 05/31/2018
---

# Play Method (DirectShow)

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `Play` method plays the current DVD title.

``` syntax
MSWebDVD.Play()
```

## Return Value

No return value.

## Remarks

If playback is paused or stopped and [**EnableResetOnStop**](enableresetonstop-property.md) is true, then calling **Play** will resume playback at normal speed at the current location. If playback is stopped and **EnableResetOnStop** is false, then calling **Play** will cause the disc to start playing at the beginning of the first title.

## See also

<dl> <dt>

[**Resume**](resume-method.md)
</dt> </dl>

 

 



