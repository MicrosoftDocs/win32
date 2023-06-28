---
description: The GPRMARRAY data type contains an array of DVD general parameter register (GPRM) values.
ms.assetid: f0ab0a9d-00fa-4c61-9f5a-727cf69ffa1c
title: GPRMARRAY (Strmif.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# GPRMARRAY

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **GPRMARRAY** data type contains an array of DVD general parameter register (GPRM) values.


```C++
typedef DVD_REGISTER GPRMARRAY [16];
```



## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Strmif.h (include Dshow.h)</dt> </dl> |



## See also

<dl> <dt>

[DirectShow Data Types](directshow-data-types.md)
</dt> <dt>

[**DVD\_REGISTER**](dvd-register.md)
</dt> <dt>

[**IDvdInfo2::GetAllGPRMs**](/windows/desktop/api/Strmif/nf-strmif-idvdinfo2-getallgprms)
</dt> </dl>

 

 




