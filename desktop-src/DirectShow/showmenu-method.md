---
description: The ShowMenu method displays the specified menu on the screen.
ms.assetid: 971c5bc3-a327-4840-8f3c-9a6573204ffb
title: ShowMenu Method
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# ShowMenu Method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `ShowMenu` method displays the specified menu on the screen.

``` syntax
MSWebDVD.ShowMenu(iMenuID)
```

## Parameters

<dl> <dt>

<span id="iMenuID"></span><span id="imenuid"></span><span id="IMENUID"></span>*iMenuID*
</dt> <dd>

Specifies the menu ID as an Integer.



| Value | Description |
|-------|-------------|
| 2     | Title (Top) |
| 3     | Root        |
| 4     | Subpicture  |
| 5     | Audio       |
| 6     | Angle       |
| 7     | Chapter     |



 

</dd> </dl>

## Return Value

No return value.

## Remarks

DVD menu names can be somewhat confusing. The title menu is another name for the Video Manager Menu, the main menu for the entire disc; it generally lists all the video title sets available on the disc. The root menu is the menu for one video title set, which can contain one title or a group of titles. All the titles in a title set share the same Subpicture, Audio, and Angle menus.

 

 



