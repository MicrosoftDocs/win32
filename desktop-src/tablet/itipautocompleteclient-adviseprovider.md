---
description: Registers the provider with the client to enable the client to call the application's auto complete provider object.
ms.assetid: 7b761b30-66f7-454a-9e0d-f45c8099f19f
title: ITipAutocompleteClient::AdviseProvider method (TipAutoComplete.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ITipAutocompleteClient.AdviseProvider
api_type: 
- COM
api_location: 
- tiptsf.dll
---

# ITipAutocompleteClient::AdviseProvider method

Registers the provider with the client to enable the client to call the application's auto complete provider object.

## Syntax


```C++
HRESULT AdviseProvider(
  [in] HWND                     hWndField,
  [in] ITipAutocompleteProvider *pIACProvider
);
```



## Parameters

<dl> <dt>

*hWndField* \[in\]
</dt> <dd>

The window handle of the field which provide the auto complete feature.

</dd> <dt>

*pIACProvider* \[in\]
</dt> <dd>

The interface pointer to the auto complete provider interface.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                            | Description                               |
|----------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | Success.<br/>                       |
| <dl> <dt>**E\_FAIL**</dt> </dl> | An unspecified error occurred.<br/> |



 

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

[**ITipAutocompleteClient::UnadviseProvider Method**](itipautocompleteclient-unadviseprovider.md)
</dt> <dt>

[Text Input Panel Reference](text-input-panel-reference.md)
</dt> </dl>

 

 




