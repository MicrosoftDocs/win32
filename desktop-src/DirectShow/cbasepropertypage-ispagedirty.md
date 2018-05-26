---
Description: The IsPageDirty method indicates whether the property page has changed since it was activated or since the most recent call to IPropertyPageApply. This method implements the IPropertyPageIsPageDirty method.
ms.assetid: 95eeec26-7dbb-4add-a827-6505b40afe48
title: CBasePropertyPage.IsPageDirty method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Cprop.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePropertyPage Class**](cbasepropertypage.md)
</dt> </dl>

 

 




