---
description: The Deactivate method destroys the dialog window. This method implements the IPropertyPage::Deactivate method.
ms.assetid: f2d2f15f-15f6-4902-bafc-f58a684ff193
title: CBasePropertyPage.Deactivate method (Cprop.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePropertyPage.Deactivate
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBasePropertyPage.Deactivate method

The `Deactivate` method destroys the dialog window. This method implements the **IPropertyPage::Deactivate** method.

## Syntax


```C++
HRESULT Deactivate();
```



## Parameters

This method has no parameters.

## Return value

Returns an **HRESULT** value. Possible values include the following.



| Return code                                                                                  | Description                    |
|----------------------------------------------------------------------------------------------|--------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Success.<br/>            |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl> | Unexpected failure.<br/> |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Cprop.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePropertyPage Class**](cbasepropertypage.md)
</dt> <dt>

[**CBasePropertyPage::OnDeactivate**](cbasepropertypage-ondeactivate.md)
</dt> </dl>

 

 




