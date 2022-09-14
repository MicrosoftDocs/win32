---
description: The DVDAdm.DisableScreenSaver property turns the system screen saver on or off.
ms.assetid: 78a0512f-456a-45b6-8717-13593461a765
title: DisableScreenSaver Property
ms.topic: reference
ms.date: 05/31/2018
---

# DisableScreenSaver Property

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `DVDAdm.DisableScreenSaver` property turns the system screen saver on or off.

``` syntax
[ bDisabled = ] DVD.DVDAdm.DisableScreenSaver
```

## Return Value

Returns a Boolean value indicating whether the system's screen saver settings are disabled for the DVD player application; true means the settings are disabled.

## Remarks

This property is read/write with a default value of true. When viewing a DVD-Video disc, a user typically does not use the mouse or keyboard for extended periods of time. The MSWebDVD ActiveX® control therefore disables the system screen saver by default. Object

## See also

<dl> <dt>

[**RestoreScreenSaver**](restorescreensaver-method.md)
</dt> <dt>

[MSDVDAdm Object](msdvdadm-object.md)
</dt> </dl>

 

 



