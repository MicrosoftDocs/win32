---
description: FOURCC Codes
ms.assetid: 7627b580-4119-48e2-88b7-51b714b5d5b2
title: FOURCC Codes
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# FOURCC Codes

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Many digital media formats have FOURCC codes assigned to them. A FOURCC code is a 32-bit unsigned integer that is created by concatenating four ASCII characters. For example, the FOURCC code for YUY2 video is 'YUY2'. For compressed video formats and non-RGB video formats (such as YUV), the **biCompression** member of the [**BITMAPINFOHEADER**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfoheader) structure should be set to the FOURCC code.

There are various C/C++ macros that make it easier to declare FOURCC values in source code. For example, the **MAKEFOURCC** macro is declared in Mmsystem.h, and the **FCC** macro is declared in Aviriff.h. Use them as follows:


```C++
DWORD fccYUY2 = MAKEFOURCC('Y','U','Y','2');
DWORD fccYUY2 = FCC('YUY2');
```



You can also declare a FOURCC code directly as a string literal simply by reversing the order of the characters. For example:


```C++
DWORD fccYUY2 = '2YUY';  // Declares the FOURCC 'YUY2'.
```



Reversing the order is necessary because the Microsoft Windows operating system uses a little-endian architecture. 'Y' = 0x59, 'U' = 0x55, and '2' = 0x32, so '2YUY' is 0x32595559.

### Converting FOURCC Codes to Subtype GUIDs

A range of 2\*32 GUIDs is reserved for representing FOURCCs. These GUIDs are all of the form `XXXXXXXX-0000-0010-8000-00AA00389B71` where `XXXXXXXX` is the FOURCC code. Thus, the subtype GUID for YUY2 is `32595559-0000-0010-8000-00AA00389B71`.

Many of these GUIDs are defined already in the header file Uuids.h. For example, the YUY2 subtype is defined as MEDIASUBTYPE\_YUY2. The DirectShow base class library also provides a helper class, [**FOURCCMap**](fourccmap.md), which can be used to convert FOURCC codes into GUID values. The **FOURCCMap** constructor takes a FOURCC code as an input parameter. You can then cast the **FOURCCMap** object to the corresponding GUID:


```C++
FOURCCMap fccMap(FCC('YUY2'));
GUID g1 = (GUID)fccMap;

// Equivalent:
GUID g2 = (GUID)FOURCCMap(FCC('YUY2'));
```



## Related topics

<dl> <dt>

[**Audio Subtypes**](audio-subtypes.md)
</dt> <dt>

[Video Subtypes](video-subtypes.md)
</dt> <dt>

[Working with Codecs](working-with-codecs.md)
</dt> </dl>

 

 



