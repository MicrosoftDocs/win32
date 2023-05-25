---
description: Tests whether a pointer is aligned to a specified boundary. If not, this macro invokes the ASSERT macro. Ignored in retail builds.
ms.assetid: 4d9ec3a9-7107-45a3-a7aa-28d6e38fa92a
title: DbgAssertAligned macro (Wxdebug.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DbgAssertAligned
api_type: 
- HeaderDef
api_location: 
- Wxdebug.h
ms.custom: UpdateFrequency5
---

# DbgAssertAligned macro

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Tests whether a pointer is aligned to a specified boundary. If not, this macro invokes the [**ASSERT**](assert.md) macro. Ignored in retail builds.

## Syntax


```C++
void DbgAssertAligned(
    ptr,
    alignment
);
```



## Parameters

<dl> <dt>

*ptr* 
</dt> <dd>

Pointer variable.

</dd> <dt>

*alignment* 
</dt> <dd>

Required alignment.

</dd> </dl>

## Return value

This macro does not return a value.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wxdebug.h (include Streams.h)</dt> </dl> |



## See also

<dl> <dt>

[Assert and Breakpoint Macros](assert-and-breakpoint-macros.md)
</dt> </dl>

 

 




