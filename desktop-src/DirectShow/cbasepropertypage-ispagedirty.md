---
description: The IsPageDirty method indicates whether the property page has changed since it was activated or since the most recent call to IPropertyPage::Apply. This method implements the IPropertyPage::IsPageDirty method.
ms.assetid: 95eeec26-7dbb-4add-a827-6505b40afe48
title: CBasePropertyPage.IsPageDirty method (Cprop.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePropertyPage.IsPageDirty
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBasePropertyPage.IsPageDirty method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `IsPageDirty` method indicates whether the property page has changed since it was activated or since the most recent call to **IPropertyPage::Apply**. This method implements the **IPropertyPage::IsPageDirty** method.

## Syntax


```C++
HRESULT IsPageDirty();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK if [**CBasePropertyPage::m\_bDirty**](cbasepropertypage-m-bdirty.md) is **TRUE**, or S\_FALSE otherwise.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Cprop.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePropertyPage Class**](cbasepropertypage.md)
</dt> </dl>

 

 




