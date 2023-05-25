---
description: The DVDAdm.DisableScreenSaver property turns the system screen saver on or off.
ms.assetid: 78a0512f-456a-45b6-8717-13593461a765
title: DisableScreenSaver Property
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DisableScreenSaver Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 



