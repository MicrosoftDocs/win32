---
description: Manages the application's side of the Text Input Panel auto complete integration.
ms.assetid: 02601258-d867-4c01-b094-bf9ff96d2f6e
title: ITipAutocompleteProvider interface (TipAutoComplete.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ITipAutocompleteProvider
api_type: 
- COM
api_location: 
- tiptsf.dll
---

# ITipAutocompleteProvider interface

Manages the application's side of the Text Input Panel auto complete integration.

## Members

The **ITipAutocompleteProvider** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **ITipAutocompleteProvider** also has these types of members:

-   [Methods](#methods)

### Methods

The **ITipAutocompleteProvider** interface has these methods.



| Method                                                                  | Description                                                                                                          |
|:------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------|
| [**Show**](itipautocompleteprovider-show.md)                           | Displays or hides the auto complete list.<br/>                                                                 |
| [**UpdatePendingText**](itipautocompleteprovider-updatependingtext.md) | Used by the auto complete client to notify the application of the text a user has inked into Input Panel.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                                   |
| Minimum supported server<br/> | None supported<br/>                                                                                                       |
| Header<br/>                   | <dl> <dt>TipAutoComplete.h (also requires Peninputpanel\_i.c)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Tiptsf.dll</dt> </dl>                                           |



## See also

<dl> <dt>

[Text Input Panel Reference](text-input-panel-reference.md)
</dt> <dt>

[**ITipAutocompleteClient Interface**](itipautocompleteclient.md)
</dt> </dl>

 

