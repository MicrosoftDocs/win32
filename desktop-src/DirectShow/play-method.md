---
description: The Play method plays the current DVD title.
ms.assetid: fe9dc266-5b12-479d-85cb-50cc6bb9d580
title: Play Method (DirectShow)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Play Method (DirectShow)

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 



