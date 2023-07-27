---
description: The AnglesAvailable property retrieves the number of angles currently available.
ms.assetid: 1e2635d4-63f1-4c3d-a034-437489289bd7
title: AnglesAvailable Property
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AnglesAvailable Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `AnglesAvailable` property retrieves the number of angles currently available.

``` syntax
[ iAngles = ] MSWebDVD.AnglesAvailable
```

## Return Value

Returns an integer value from 1 through 9 representing the number of angles currently available. If


```
iAngles
```



= 1, there is no angle block at the current location.

## Remarks

This property is read-only with no default value. An *angle block* is a video segment that was shot from more than one camera angle. There can be up to nine angles in an angle block, numbered from 1 through 9. When the DVD Navigator first enters an angle block, it sends your application an EC\_DVD\_ANGLES\_AVAILABLE event notification with the number of angles in *lParam1*. A disc can be authored to automatically show a menu for available angles when it enters an angle block, but generally an application must determine the number of angles available and offer the user a way to select one.

## See also

<dl> <dt>

[**CurrentAngle**](currentangle-property.md)
</dt> </dl>

 

 



