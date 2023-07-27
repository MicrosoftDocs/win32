---
description: The DbgLog macro sends a string to the debug output location, if logging is enabled for the specified type and level. This macro is ignored in retail builds.
ms.assetid: 10e95d63-14f2-4fdb-a1b8-c5bf654f9819
title: DbgLog macro (Wxdebug.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DbgLog
api_type: 
- HeaderDef
api_location: 
- Wxdebug.h
ms.custom: UpdateFrequency5
---

# DbgLog macro

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **DbgLog** macro sends a string to the debug output location, if logging is enabled for the specified type and level. This macro is ignored in retail builds.

## Syntax


```C++
void DbgLog(
         DWORD Types,
         DWORD Level,
   const TCHAR *pFormat,
               ...
);
```



## Parameters

<dl> <dt>

*Types* 
</dt> <dd>

Bitwise combination of one or more message types.

</dd> <dt>

*Level* 
</dt> <dd>

Logging level for this message.

</dd> <dt>

*pFormat* 
</dt> <dd>

A **printf** -style format string.

</dd> <dt>

*...* 
</dt> <dd>

Additional arguments for the format string.

</dd> </dl>

## Return value

This macro does not return a value.

## Remarks

If debug logging for any of the message types is set to the specified level or higher, this macro sends the formatted string to the debug output location.

The macro automatically adds a newline character to the output string.

> [!Note]  
> An additional set of parentheses must enclose the macro parameters:

 


```C++
DbgLog((LOG_TRACE, 3, TEXT("Connected input pin %d"), nPinNumber));
```



## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wxdebug.h (include Streams.h)</dt> </dl> |



## See also

<dl> <dt>

[Debug Output Functions](debug-output-functions.md)
</dt> </dl>

 

 




