---
description: The WideStringFromResource function loads a wide-character string from a resource file with the given resource identifier.
ms.assetid: c5fac767-20c4-4342-9d4d-e1b916854b95
title: WideStringFromResource function (Wxutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WideStringFromResource
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# WideStringFromResource function

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `WideStringFromResource` function loads a wide-character string from a resource file with the given resource identifier.

## Syntax


```C++
WCHAR* WINAPI WideStringFromResource(
   pBuffer *pBuffer,
   int     iResourceID
);
```



## Parameters

<dl> <dt>

*pBuffer* 
</dt> <dd>

Pointer to the string corresponding to *iResourceID*.

</dd> <dt>

*iResourceID* 
</dt> <dd>

Resource identifier of the string to retrieve.

</dd> </dl>

## Return value

Returns the same string as *pBuffer*. If the function is not successful, returns a null string.

## Remarks

Property pages are typically called through their COM interfaces, which use wide-character strings regardless of how the binary is built. This function allows you to convert a resource string to a wide-character string. The function converts the resource to a wide-character string (if it is not already one) after loading it.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Property Page Helper Functions](property-page-helper-functions.md)
</dt> </dl>

 

 




