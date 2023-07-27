---
description: Displays a message box with the specified string, the name of the source file, and the line number. The user can ignore the message, enter the debugger, or quit the application. Ignored in retail builds.
ms.assetid: ac4da7da-f9d0-44ae-9ad1-9a5908b288fb
title: DbgBreak macro (Wxdebug.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DbgBreak
api_type: 
- HeaderDef
api_location: 
- Wxdebug.h
ms.custom: UpdateFrequency5
---

# DbgBreak macro

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Displays a message box with the specified string, the name of the source file, and the line number. The user can ignore the message, enter the debugger, or quit the application. Ignored in retail builds.

## Syntax


```C++
void DbgBreak(
    strLiteral
);
```



## Parameters

<dl> <dt>

*strLiteral* 
</dt> <dd>

Text string.

</dd> </dl>

## Return value

This macro does not return a value.

## Examples


```C++
DbgBreak("Unrecoverable error occurred.");
```



## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wxdebug.h (include Streams.h)</dt> </dl> |



## See also

<dl> <dt>

[Assert and Breakpoint Macros](assert-and-breakpoint-macros.md)
</dt> </dl>

 

 




