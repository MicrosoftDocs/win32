---
description: Displays or hides the auto complete list.
ms.assetid: 756ffa3d-03ee-4753-a826-3bc22ab16f5f
title: ITipAutocompleteProvider::Show method (TipAutoComplete.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ITipAutocompleteProvider.Show
api_type: 
- COM
api_location: 
- tiptsf.dll
---

# ITipAutocompleteProvider::Show method

Displays or hides the auto complete list.

## Syntax


```C++
HRESULT Show(
  [in] BOOL fShow
);
```



## Parameters

<dl> <dt>

*fShow* \[in\]
</dt> <dd>

**TRUE** to show the auto complete user interface, **FALSE** to hide the auto complete list user interface.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                            | Description                               |
|----------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | Success.<br/>                       |
| <dl> <dt>**E\_FAIL**</dt> </dl> | An unspecified error occurred.<br/> |



 

## Remarks

This method is called by the client to show or hide the auto complete list. If the auto complete list is not displayed and *fShow* is **FALSE**, this method does nothing. If the auto complete list is displayed and *fShow* is **TRUE**, this method does nothing.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                                   |
| Minimum supported server<br/> | None supported<br/>                                                                                                       |
| Header<br/>                   | <dl> <dt>TipAutoComplete.h (also requires Peninputpanel\_i.c)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Tiptsf.dll</dt> </dl>                                           |



## See also

<dl> <dt>

[**ITipAutocompleteProvider Interface**](itipautocompleteprovider.md)
</dt> <dt>

[Text Input Panel Reference](text-input-panel-reference.md)
</dt> </dl>

 

 




