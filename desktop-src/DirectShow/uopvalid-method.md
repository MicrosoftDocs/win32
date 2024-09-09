---
description: The UOPValid method retrieves a value that indicates whether the specified user operation (UOP) is currently valid.
ms.assetid: 0d2c4693-95eb-4cc8-a8f6-61fd0b6d57be
title: UOPValid Method (Segment.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# UOPValid Method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `UOPValid` method retrieves a value that indicates whether the specified user operation (UOP) is currently valid.

``` syntax
[ bIsValid = ] MSWebDVD.UOPValid(iUOP)
```

## Parameters

<dl> <dt>

<span id="iUOP"></span><span id="iuop"></span><span id="IUOP"></span>*iUOP*
</dt> <dd>

Specifies the user operation (UOP) as an Integer.



| Value | Description                                                                                                                                                                                                              |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0     | [**PlayTitle**](playtitle-method.md), [**PlayAtTime**](playattime-method.md)[**PlayAtTimeInTitle**](playattimeintitle-method.md)                                                                                      |
| 1     | [**PlayChapter**](playchapter-method.md)                                                                                                                                                                                |
| 2     | [**PlayTitle**](playtitle-method.md)                                                                                                                                                                                    |
| 3     | [**Stop**](stop-method.md)                                                                                                                                                                                              |
| 4     | [**ReturnFromSubmenu**](returnfromsubmenu-method.md)                                                                                                                                                                    |
| 5     | [**PlayChapter**](playchapter-method.md)                                                                                                                                                                                |
| 6     | [**PlayPrevChapter**](playprevchapter-method.md), [**ReplayChapter**](replaychapter-method.md)                                                                                                                         |
| 7     | [**PlayNextChapter**](playnextchapter-method.md)                                                                                                                                                                        |
| 8     | [**PlayForwards**](playforwards-method.md)                                                                                                                                                                              |
| 9     | [**PlayBackwards**](playbackwards-method.md)                                                                                                                                                                            |
| 10    | [**ShowMenu**](showmenu-method.md) with a parameter value of 2 (DVD\_MENU\_Title)                                                                                                                                       |
| 11    | [**ShowMenu**](showmenu-method.md) with a parameter value of 3 (DVD\_MENU\_Root)                                                                                                                                        |
| 12    | [**ShowMenu**](showmenu-method.md) with a parameter value of 4 (DVD\_MENU\_Subpicture)                                                                                                                                  |
| 13    | [**ShowMenu**](showmenu-method.md) with a parameter value of 5 (DVD\_MENU\_Audio)                                                                                                                                       |
| 14    | [**ShowMenu**](showmenu-method.md) with a parameter value of 6 (DVD\_MENU\_Angle)                                                                                                                                       |
| 15    | [**ShowMenu**](showmenu-method.md) with a parameter value of 7 (DVD\_MENU\_Chapter)                                                                                                                                     |
| 16    | [**Resume**](resume-method.md)                                                                                                                                                                                          |
| 17    | [**SelectLeftButton**](selectleftbutton-method.md), [**SelectRightButton**](selectrightbutton-method.md), [**SelectUpperButton**](selectupperbutton-method.md), [**SelectLowerButton**](selectlowerbutton-method.md) |
| 18    | [**StillOff**](stilloff-method.md)                                                                                                                                                                                      |
| 19    | [**Pause**](pause-method.md)                                                                                                                                                                                            |
| 20    | [**CurrentAudioStream**](currentaudiostream-property.md)                                                                                                                                                                |
| 21    | [**CurrentSubpictureStream**](currentsubpicturestream-property.md)                                                                                                                                                      |
| 22    | [**CurrentAngle**](currentangle-property.md), [**SelectParentalLevel**](selectparentallevel-method.md)                                                                                                                 |
| 23    | [**KaraokeAudioPresentationMode**](karaokeaudiopresentationmode-property.md)                                                                                                                                            |
| 24    | Select video mode preference.                                                                                                                                                                                            |



 

</dd> </dl>

## Return Value

Returns a Boolean value indicating whether the specified operation is permitted by UOP control.

## Requirements



| Requirement | Value |
|-------------------|--------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Segment.h</dt> </dl> |



 

 




