---
description: The GetSPRM method retrieves the specified system parameter register.
ms.assetid: c6177f43-2809-4ef2-bc94-ac9a28f94621
title: GetSPRM Method
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# GetSPRM Method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `GetSPRM` method retrieves the specified system parameter register.

``` syntax
[ iSPRM = ] MSWebDVD.GetSPRM(iIndex)
```

## Parameters

<dl> <dt>

<span id="iIndex"></span><span id="iindex"></span><span id="IINDEX"></span>*iIndex*
</dt> <dd>

Specifies the register whose value you want to retrieve as an Integer. The Integer must range from 0 through 23.

</dd> </dl>

## Return Value

Returns an integer value representing the contents of the specified register.

## Remarks

The disc controls system parameter registers (SPRMs). A player application doesn't need to access these registers for any standard navigation functionality. SPRMs represent the status of the player. Each one has a meaning, set by user preferences, disc commands, and other occurrences that an application has no direct control over. An application can read these registers but cannot write to them. To use these registers effectively, you will probably need a more detailed knowledge of the DVD navigation commands than is provided in this documentation. The following table shows the contents of each register. For more detailed information on the register contents, see [**IDvdInfo2::GetAllSPRMs**](/windows/desktop/api/Strmif/nf-strmif-idvdinfo2-getallsprms)



| Register | Contents                        |
|----------|---------------------------------|
| 0        | Menu language code              |
| 1        | Audio stream number             |
| 2        | Subpicture stream number        |
| 3        | Current angle number            |
| 4        | Current title number            |
| 5        | Title number                    |
| 6        | PGC number                      |
| 7        | Current chapter number (PTT)    |
| 8        | Highlighted button number       |
| 9        | Navigation timer                |
| 10       | PGC jump for nav. timer         |
| 11       | Karaoke audio presentation mode |
| 12       | PML country/region code         |
| 13       | PML                             |
| 14       | Video setting                   |
| 15       | Audio capability                |
| 16       | Audio language                  |
| 17       | Audio language extension        |
| 18       | Subpicture language             |
| 19       | Subpicture language extension   |
| 20       | Player region code              |
| 21       | Reserved                        |
| 22       | Reserved                        |
| 23       | Reserved                        |



 

## See also

<dl> <dt>

[**GetGPRM**](getgprm-method.md)
</dt> <dt>

[**SetGPRM**](setgprm-method.md)
</dt> </dl>

 

 



