---
description: The DVD\_REGISTER data type contains a value for a DVD general parameter register (GPRM) or system parameter register (SPRM).
ms.assetid: cd1aaeff-241c-4e54-9d05-da5cf61b58df
title: DVD_REGISTER (Strmif.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DVD\_REGISTER

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **DVD\_REGISTER** data type contains a value for a DVD general parameter register (GPRM) or system parameter register (SPRM).


```C++
typedef WORD DVD_REGISTER;
```



## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Strmif.h (include Dshow.h)</dt> </dl> |



## See also

<dl> <dt>

[DirectShow Data Types](directshow-data-types.md)
</dt> <dt>

[**GPRMARRAY**](gprmarray.md)
</dt> <dt>

[**SPRMARRAY**](sprmarray.md)
</dt> </dl>

 

 




