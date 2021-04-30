---
description: The Move method positions and resizes the dialog box. This method implements the IPropertyPage::Move method.
ms.assetid: b6cabb5c-196d-489b-9dd4-194d26f4de83
title: CBasePropertyPage.Move method (Cprop.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePropertyPage.Move
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBasePropertyPage.Move method

The `Move` method positions and resizes the dialog box. This method implements the **IPropertyPage::Move** method.

## Syntax


```C++
HRESULT Move(
   LPCRECT prect
);
```



## Parameters

<dl> <dt>

*prect* 
</dt> <dd>

Pointer to a **RECT** structure containing the positioning information.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include the following.



| Return code                                                                                  | Description                           |
|----------------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Success.<br/>                   |
| <dl> <dt>**E\_POINTER**</dt> </dl>    | **NULL** pointer argument.<br/> |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl> | Unexpected failure.<br/>        |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Cprop.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePropertyPage Class**](cbasepropertypage.md)
</dt> </dl>

 

 




