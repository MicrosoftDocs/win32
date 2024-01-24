---
description: These functions register a filter.
ms.assetid: c9c4976f-d4c5-465e-8ad7-4294c05d0e0a
title: DLL Setup Functions (Dllsetup.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DLL
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# DLL Setup Functions

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

These functions register a filter.



| Function                                                         | Description                                        |
|------------------------------------------------------------------|----------------------------------------------------|
| [**AMovieDllRegisterServer**](amoviedllregisterserver.md)       | Obsolete.                                          |
| [**AMovieDllRegisterServer2**](amoviedllregisterserver2.md)     | Registers and unregisters filters.                 |
| [**AMovieDllUnregisterServer**](amoviedllunregisterserver.md)   | Obsolete.                                          |
| [**AMovieSetupRegisterFilter**](amoviesetupregisterfilter.md)   | Obsolete.                                          |
| [**AMovieSetupRegisterFilter2**](amoviesetupregisterfilter2.md) | Registers a filter's merit, pins, and media types. |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Dllsetup.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




