---
description: The DbgOutString function sends a string to the debug output location. Ignored in retail builds.
ms.assetid: 644bf4f7-ec2d-466e-85c6-690dd44da702
title: DbgOutString function (Wxdebug.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DbgOutString
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# DbgOutString function

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **DbgOutString** function sends a string to the debug output location. Ignored in retail builds.

## Syntax


```C++
void DbgOutString(
   LPCTSTR psz
);
```



## Parameters

<dl> <dt>

*psz* 
</dt> <dd>

String to output.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

In debug builds, this function always outputs the string, regardless of the current debug output levels. For finer control over the output, use the [**DbgLog**](dbglog.md) macro.

## Examples


```C++
DbgOutString("Creating the filter graph...\n"); 
```



## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxdebug.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Debug Output Functions](debug-output-functions.md)
</dt> </dl>

 

 




