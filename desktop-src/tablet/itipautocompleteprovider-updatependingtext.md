---
description: Used by the auto complete client to notify the application of the text a user has inked into Input Panel.
ms.assetid: 68413836-321a-4e75-8538-c5a8fc577c0f
title: ITipAutocompleteProvider::UpdatePendingText method (TipAutoComplete.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ITipAutocompleteProvider.UpdatePendingText
api_type: 
- COM
api_location: 
- tiptsf.dll
---

# ITipAutocompleteProvider::UpdatePendingText method

Used by the auto complete client to notify the application of the text a user has inked into Input Panel.

## Syntax


```C++
HRESULT UpdatePendingText(
  [in] BSTR bstrPendingText
);
```



## Parameters

<dl> <dt>

*bstrPendingText* \[in\]
</dt> <dd>

Source text to be used to generate the auto complete list.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                            | Description                               |
|----------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | Success.<br/>                       |
| <dl> <dt>**E\_FAIL**</dt> </dl> | An unspecified error occurred.<br/> |



 

## Remarks

This text will not contain the text already inserted in the focused field. The auto complete provider is responsible for taking into account the current field text and the selection to generate the auto complete list. When *bstrPendingText* is **NULL**, the auto complete list is generated with the current text to the left of the selection in the field.

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

 

 




