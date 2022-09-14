---
description: The Apply method applies the current property page values to the object associated with the property page. This method implements the IPropertyPage::Apply method.
ms.assetid: 9fe759d1-2b46-4489-b7b8-b5a35330091d
title: CBasePropertyPage.Apply method (Cprop.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePropertyPage.Apply
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBasePropertyPage.Apply method

The `Apply` method applies the current property page values to the object associated with the property page. This method implements the **IPropertyPage::Apply** method.

## Syntax


```C++
HRESULT Apply();
```



## Parameters

This method has no parameters.

## Return value

Returns an **HRESULT** value. Possible values include the following.



| Return code                                                                                  | Description                    |
|----------------------------------------------------------------------------------------------|--------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Success.<br/>            |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl> | Unexpected failure.<br/> |



 

## Remarks

If the [**CBasePropertyPage::m\_bDirty**](cbasepropertypage-m-bdirty.md) flag is **TRUE**, this method calls the [**CBasePropertyPage::OnApplyChanges**](cbasepropertypage-onapplychanges.md) method. Override **OnApplyChanges** to apply the changes to the object.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Cprop.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePropertyPage Class**](cbasepropertypage.md)
</dt> </dl>

 

 




