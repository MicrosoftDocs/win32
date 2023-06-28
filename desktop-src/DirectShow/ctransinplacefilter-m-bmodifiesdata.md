---
description: The m\_bModifiesData member variable indicates whether the filter modifies the sample data that is receives. The value is set in the CTransInPlaceFilter constructor, but defaults to TRUE.
ms.assetid: 8ccdba46-315f-4519-b363-6870d1217f98
title: CTransInPlaceFilter::m_bModifiesData member (Transip.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- m_bModifiesData
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CTransInPlaceFilter::m\_bModifiesData member

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `m_bModifiesData` member variable indicates whether the filter modifies the sample data that is receives. The value is set in the **CTransInPlaceFilter** constructor, but defaults to **TRUE**.

## Syntax


```C++
bool m_bModifiesData;
```



## Remarks

This variable affects how the filter negotiates the allocator. If the value is **TRUE**, the filter cannot use a read-only allocator for both pin connections.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transip.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransInPlaceFilter Class**](ctransinplacefilter.md)
</dt> </dl>

 

 




