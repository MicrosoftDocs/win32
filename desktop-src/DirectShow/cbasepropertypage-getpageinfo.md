---
description: The GetPageInfo method retrieves information about the property page. This method implements the IPropertyPage::GetPageInfo method.
ms.assetid: f2e04652-7c71-48b2-b964-4e07ac98d367
title: CBasePropertyPage.GetPageInfo method (Cprop.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePropertyPage.GetPageInfo
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBasePropertyPage.GetPageInfo method

The `GetPageInfo` method retrieves information about the property page. This method implements the **IPropertyPage::GetPageInfo** method.

## Syntax


```C++
HRESULT GetPageInfo(
   LPPROPPAGEINFO pPageInfo
);
```



## Parameters

<dl> <dt>

*pPageInfo* 
</dt> <dd>

Pointer to a caller-allocated **PROPPAGEINFO** structure.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include the following.



| Return code                                                                                   | Description                     |
|-----------------------------------------------------------------------------------------------|---------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Success.<br/>             |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory.<br/> |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Cprop.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePropertyPage Class**](cbasepropertypage.md)
</dt> </dl>

 

 




