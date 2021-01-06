---
description: The DVDAdm.RestoreScreenSaver method restores the system screen saver settings.
ms.assetid: 606ab850-95bf-4c60-b7cf-e3a94ceee7a7
title: RestoreScreenSaver Method
ms.topic: reference
ms.date: 05/31/2018
---

# RestoreScreenSaver Method

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `DVDAdm.RestoreScreenSaver` method restores the system screen saver settings.

``` syntax
DVD.DVDAdm.RestoreScreenSaver()
```

## Return Value

No return value.

## Remarks

Generally, a DVD application will disable the system's screen saver on startup by setting the [**DisableScreenSaver**](disablescreensaver-property.md) property to true, and then re-enable the screen saver again when the DVD application is closed by calling `RestoreScreenSaver`. If an application does not use the system's screen saver settings, it does not have to call this method or set the **DisableScreenSaver** property.

## See also

<dl> <dt>

[MSDVDAdm Object](msdvdadm-object.md)
</dt> </dl>

 

 



