---
description: The DVDAdm.DefaultAudioLCID property sets or retrieves the registry setting for the user-specified default LCID for the audio stream.
ms.assetid: ed347a5e-d4cc-42f1-8b75-0a0a2ca40476
title: DefaultAudioLCID Property
ms.topic: reference
ms.date: 05/31/2018
---

# DefaultAudioLCID Property

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `DVDAdm.DefaultAudioLCID` property sets or retrieves the registry setting for the user-specified default LCID for the audio stream.

``` syntax
[ iAudioLCID = ] DVD.DVDAdm.DefaultAudioLCID
```

## Return Value

Returns an Integer value representing the user-specified default audio LCID as stored in the registry settings for the DVD application. This value is not necessarily the same as the default audio stream as authored on the DVD.

## Remarks

This property is read/write with no default value. If no default audio LCID is specified, the MSDVDAdm object will play the audio stream that is marked as the default stream on the disc.

## See also

<dl> <dt>

[MSDVDAdm Object](msdvdadm-object.md)
</dt> </dl>

 

 



