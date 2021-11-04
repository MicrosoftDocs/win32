---
description: The SetPageSite method initializes the property page and provides a pointer to the property frame's IPropertyPageSite interface. This method implements the IPropertyPage::SetPageSite method.
ms.assetid: 16c4633f-2f91-4b1b-a47c-4ef945c3af00
title: CBasePropertyPage.SetPageSite method (Cprop.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePropertyPage.SetPageSite
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBasePropertyPage.SetPageSite method

The `SetPageSite` method initializes the property page and provides a pointer to the property frame's **IPropertyPageSite** interface. This method implements the **IPropertyPage::SetPageSite** method.

## Syntax


```C++
HRESULT SetPageSite(
   IPropertyPageSite *pPageSite
);
```



## Parameters

<dl> <dt>

*pPageSite* 
</dt> <dd>

Pointer to the **IPropertyPageSite** interface.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include the following.



| Return code                                                                                  | Description                    |
|----------------------------------------------------------------------------------------------|--------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Success.<br/>            |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl> | Unexpected failure.<br/> |



 

## Remarks

The method stores the *pPageSite* pointer in the [**CBasePropertyPage::m\_pPageSite**](cbasepropertypage-m-ppagesite.md) member variable.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Cprop.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePropertyPage Class**](cbasepropertypage.md)
</dt> </dl>

 

 




