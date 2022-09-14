---
description: Unregisters the associated provider.
ms.assetid: b5edc33d-dfd0-4350-b8cd-eaa30b726771
title: ITipAutocompleteClient::UnadviseProvider method (TipAutoComplete.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ITipAutocompleteClient.UnadviseProvider
api_type: 
- COM
api_location: 
- tiptsf.dll
---

# ITipAutocompleteClient::UnadviseProvider method

Unregisters the associated provider.

## Syntax


```C++
HRESULT UnadviseProvider(
  [in] HWND                   hWndField,
  [in] ITipAutocompleProvider *pIACProvider
);
```



## Parameters

<dl> <dt>

*hWndField* \[in\]
</dt> <dd>

Window handle of the field which provide the auto complete feature.

</dd> <dt>

*pIACProvider* \[in\]
</dt> <dd>

Interface pointer to the auto complete provider interface to be unregistered.

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

[Text Input Panel Reference](text-input-panel-reference.md)
</dt> </dl>

 

 




