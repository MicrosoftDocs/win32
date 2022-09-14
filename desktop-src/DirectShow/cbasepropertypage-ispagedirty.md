---
description: The IsPageDirty method indicates whether the property page has changed since it was activated or since the most recent call to IPropertyPage::Apply. This method implements the IPropertyPage::IsPageDirty method.
ms.assetid: 95eeec26-7dbb-4add-a827-6505b40afe48
title: CBasePropertyPage.IsPageDirty method (Cprop.h)
ms.topic: reference
ms.date: 05/31/2018
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
---

# CBasePropertyPage.IsPageDirty method

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

 

 




