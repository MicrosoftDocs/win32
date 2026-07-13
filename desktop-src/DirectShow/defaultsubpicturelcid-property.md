---
description: The DVDAdm.DefaultSubpictureLCID property sets or retrieves the registry setting for the user-specified default LCID for the subpicture stream.
ms.assetid: 12dd308e-483b-489d-8d81-8da399bfac4d
title: DefaultSubpictureLCID Property
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DefaultSubpictureLCID Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `DVDAdm.DefaultSubpictureLCID` property sets or retrieves the registry setting for the user-specified default LCID for the subpicture stream.

``` syntax
[ iSubpictureLCID = ] DVD.DVDAdm.DefaultSubpictureLCID
```

## Return Value

Returns an Integer value representing the user-specified default subpicture LCID as stored in the registry settings for the DVD application. This value is not necessarily the same as the default subpicture stream as authored on the DVD. For the range of valid LCIDs, see the Win32 documentation in the Platform SDK.

## Remarks

This property is read/write with no default value. If no default subpicture LCID is specified, the MSDVDAdm object will play the subpicture stream that is marked as the default stream on the disc.

## See also

<dl> <dt>

[MSDVDAdm Object](msdvdadm-object.md)
</dt> </dl>

 

 



