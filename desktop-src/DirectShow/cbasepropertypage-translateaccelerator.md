---
description: The TranslateAccelerator method instructs the property page to process a keystroke. This method implements the IPropertyPage::TranslateAccelerator method.
ms.assetid: 2da214c9-35dc-470c-9b7f-2f4ef6bcd40a
title: CBasePropertyPage.TranslateAccelerator method (Cprop.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePropertyPage.TranslateAccelerator
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBasePropertyPage.TranslateAccelerator method

The `TranslateAccelerator` method instructs the property page to process a keystroke. This method implements the **IPropertyPage::TranslateAccelerator** method.

## Syntax


```C++
HRESULT TranslateAccelerator(
   LPMSG lpMsg
);
```



## Parameters

<dl> <dt>

*lpMsg* 
</dt> <dd>

Pointer to a **MSG** structure describing the keystroke to process.

</dd> </dl>

## Return value

Returns E\_NOTIMPL.

## Remarks

Override this method if you want to provide keyboard accelerators for the property page.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Cprop.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePropertyPage Class**](cbasepropertypage.md)
</dt> </dl>

 

 




