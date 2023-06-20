---
description: The QueryFilterInfo method retrieves information about the filter. This method implements the IBaseFilter::QueryFilterInfo method.
ms.assetid: 0c25aa9e-933c-4c45-a1cc-ffc9253dd561
title: CBaseFilter.QueryFilterInfo method (Amfilter.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseFilter.QueryFilterInfo
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseFilter.QueryFilterInfo method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `QueryFilterInfo` method retrieves information about the filter. This method implements the [**IBaseFilter::QueryFilterInfo**](/windows/desktop/api/Strmif/nf-strmif-ibasefilter-queryfilterinfo) method.

## Syntax


```C++
HRESULT QueryFilterInfo(
   FILTER_INFO *pInfo
);
```



## Parameters

<dl> <dt>

*pInfo* 
</dt> <dd>

Pointer to a [**FILTER\_INFO**](/windows/win32/api/strmif/ns-strmif-filter_info) structure.

</dd> </dl>

## Return value

Returns S\_OK or E\_POINTER.

## Remarks

This method copies the filter's name from the [**CBaseFilter::m\_pName**](cbasefilter-m-pname.md) member variable into the **achName** member of the FILTER\_INFO structure. If **m\_pName** is **NULL**, the method sets **achName** to L'\\0'.

The method sets the **pGraph** member of the FILTER\_INFO structure equal to the [**CBaseFilter::m\_pGraph**](cbasefilter-m-pgraph.md) member variable, and increments the reference count. The caller must release the interface.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseFilter Class**](cbasefilter.md)
</dt> </dl>

 

 




