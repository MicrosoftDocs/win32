---
description: The DVDUniqueID property retrieves a system-generated number that uniquely identifies the current disc.
ms.assetid: 8ea6dd4d-6998-4212-8874-9c6cd93a1db3
title: DVDUniqueID Property
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DVDUniqueID Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `DVDUniqueID` property retrieves a system-generated number that uniquely identifies the current disc.

``` syntax
[ iDiscID = ] MSWebDVD.DVDUniqueID
```

## Return Value

Returns an integer value that uniquely identifies the current disc.

## Remarks

This property is read-only with no default value. The identifier (ID) number is not absolutely unique, but it is unique for all practical purposes. The ID applies to all replicated copies of a disc. In other words, all copies of a specific movie have the same ID. The ID is based on file sizes, dates, and other information, and not the BCA value.

 

 



