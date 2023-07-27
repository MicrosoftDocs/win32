---
description: Verifies that the calling process has read access to a wide-character string. If not, the macro calls the DbgBreak macro.
ms.assetid: 526e8027-31e5-428d-856d-9fc6698693c3
title: ValidateStringPtrW macro (Wxdebug.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ValidateStringPtrW
api_type: 
- HeaderDef
api_location: 
- Wxdebug.h
ms.custom: UpdateFrequency5
---

# ValidateStringPtrW macro

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Verifies that the calling process has read access to a wide-character string. If not, the macro calls the [**DbgBreak**](dbgbreak.md) macro.

> [!Note]  
> This macro is deprecated. In the Windows SDK for Windows Vista (and later) this macro does not do anything.

 

## Syntax


```C++
void ValidateStringPtrW(
   LPCWSTR p
);
```



## Parameters

<dl> <dt>

*p* 
</dt> <dd>

Pointer to a NULL-terminated wide-character string.

</dd> </dl>

## Return value

This macro does not return a value.

## Remarks

This macro is ignored unless DEBUG, \_DEBUG, or VFWROBUST is defined when the DirectShow base-class header file is included. This macro can have a significant performance cost.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wxdebug.h (include Streams.h)</dt> </dl> |



## See also

<dl> <dt>

[Pointer Validation Macros](pointer-validation-macros.md)
</dt> </dl>

 

 




