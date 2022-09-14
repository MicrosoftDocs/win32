---
description: The Activate method creates the dialog box window. This method implements the IPropertyPage::Activate method.
ms.assetid: 8f030dc5-1d14-46b5-9d40-7f07a1177dbe
title: CBasePropertyPage.Activate method (Cprop.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePropertyPage.Activate
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBasePropertyPage.Activate method

The `Activate` method creates the dialog box window. This method implements the **IPropertyPage::Activate** method.

## Syntax


```C++
HRESULT Activate(
   HWND    hwndParent,
   LPCRECT prect,
   BOOL    fModal
);
```



## Parameters

<dl> <dt>

*hwndParent* 
</dt> <dd>

Handle to the parent window of the dialog box.

</dd> <dt>

*prect* 
</dt> <dd>

Pointer to a **RECT** structure that contains positioning information for the dialog box.

</dd> <dt>

*fModal* 
</dt> <dd>

Boolean value indicating whether the dialog box frame is modal (**TRUE**) or modeless (**FALSE**).

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include the following.



| Return code                                                                                   | Description                           |
|-----------------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Success.<br/>                   |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory.<br/>       |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | **NULL** pointer argument.<br/> |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl>  | Unexpected failure.<br/>        |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Cprop.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePropertyPage Class**](cbasepropertypage.md)
</dt> <dt>

[**CBasePropertyPage::OnActivate**](cbasepropertypage-onactivate.md)
</dt> </dl>

 

 




