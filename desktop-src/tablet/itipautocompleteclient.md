---
description: Enables the client to call the application's Text Input Panel auto complete provider object.
ms.assetid: 448b8136-ebcb-4116-9a81-a77a37d69e24
title: ITipAutocompleteClient interface (TipAutoComplete.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ITipAutocompleteClient
api_type: 
- COM
api_location: 
- tiptsf.dll
---

# ITipAutocompleteClient interface

Enables the client to call the application's Text Input Panel auto complete provider object.

## Members

The **ITipAutocompleteClient** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **ITipAutocompleteClient** also has these types of members:

-   [Methods](#methods)

### Methods

The **ITipAutocompleteClient** interface has these methods.



| Method                                                              | Description                                                                                                                                                          |
|:--------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AdviseProvider**](itipautocompleteclient-adviseprovider.md)     | Registers the provider with the client to enable the client to call the application's auto complete provider object.<br/>                                      |
| [**PreferredRects**](itipautocompleteclient-preferredrects.md)     | Allows the client to suggest where to position the auto complete list to avoid overlapping the Input Panel.<br/>                                               |
| [**RequestShowUI**](itipautocompleteclient-requestshowui.md)       | Determines whether Input Panel is ready to have the auto complete list shown.<br/>                                                                             |
| [**UnadviseProvider**](itipautocompleteclient-unadviseprovider.md) | Unregisters the associated provider.<br/>                                                                                                                      |
| [**UserSelection**](itipautocompleteclient-userselection.md)       | Notifies the Input Panel that the user has selected something in the auto complete list and to discard all remaining text that has not yet been inserted.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                                   |
| Minimum supported server<br/> | None supported<br/>                                                                                                       |
| Header<br/>                   | <dl> <dt>TipAutoComplete.h (also requires Peninputpanel\_i.c)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Tiptsf.dll</dt> </dl>                                           |



 

