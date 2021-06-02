---
description: Notifies the Input Panel that the user has selected something in the auto complete list and to discard all remaining text that has not yet been inserted.
ms.assetid: 2e6fabe1-7984-4908-bf90-0603d0dad268
title: ITipAutocompleteClient::UserSelection method (TipAutoComplete.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ITipAutocompleteClient.UserSelection
api_type: 
- COM
api_location: 
- tiptsf.dll
---

# ITipAutocompleteClient::UserSelection method

Notifies the Input Panel that the user has selected something in the auto complete list and to discard all remaining text that has not yet been inserted.

## Syntax


```C++
HRESULT UserSelection();
```



## Parameters

This method has no parameters.

## Return value

This method can return one of these values.



| Return code                                                                            | Description                               |
|----------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | Success.<br/>                       |
| <dl> <dt>**E\_FAIL**</dt> </dl> | An unspecified error occurred.<br/> |



 

## Remarks

This method is called from the provider to notify the client that a selection has been made by the user.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                                   |
| Minimum supported server<br/> | None supported<br/>                                                                                                       |
| Header<br/>                   | <dl> <dt>TipAutoComplete.h (also requires Peninputpanel\_i.c)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Tiptsf.dll</dt> </dl>                                           |



## See also

<dl> <dt>

[**ITipAutocompleteClient Interface**](itipautocompleteclient.md)
</dt> <dt>

[Text Input Panel Reference](text-input-panel-reference.md)
</dt> </dl>

 

 




