---
description: The SPRMARRAY data type contains an array of DVD system parameter register (SPRM) values.
ms.assetid: 5c285f6e-2921-4684-bc42-762fc80a5e6b
title: SPRMARRAY (Strmif.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# SPRMARRAY

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **SPRMARRAY** data type contains an array of DVD system parameter register (SPRM) values.


```C++
typedef DVD_REGISTER SPRMARRAY [24];
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

[**IDvdInfo2::GetAllSPRMs**](/windows/desktop/api/Strmif/nf-strmif-idvdinfo2-getallsprms)
</dt> </dl>

 

 




