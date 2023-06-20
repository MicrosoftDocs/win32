---
description: Causes a breakpoint exception, and logs the specified string using the DbgLog macro. Ignored in retail builds.
ms.assetid: 475810db-692b-4727-9ef1-ece74e9618d0
title: KDbgBreak macro (Wxdebug.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- KDbgBreak
api_type: 
- HeaderDef
api_location: 
- Wxdebug.h
ms.custom: UpdateFrequency5
---

# KDbgBreak macro

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Causes a breakpoint exception, and logs the specified string using the [**DbgLog**](dbglog.md) macro. Ignored in retail builds.

## Syntax


```C++
void KDbgBreak(
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

## Remarks

Unlike the [**DbgBreak**](dbgbreak.md) macro, this macro does not display a message box prompting the user. In debug builds, it automatically causes a breakpoint exception to occur.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wxdebug.h (include Streams.h)</dt> </dl> |



## See also

<dl> <dt>

[Assert and Breakpoint Macros](assert-and-breakpoint-macros.md)
</dt> </dl>

 

 




