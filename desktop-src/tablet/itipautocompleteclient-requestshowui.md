---
description: Determines whether Input Panel is ready to have the auto complete list shown.
ms.assetid: 1e0d4bc6-e6a3-4123-a381-00a41ed9c848
title: ITipAutocompleteClient::RequestShowUI method (TipAutoComplete.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ITipAutocompleteClient.RequestShowUI
api_type: 
- COM
api_location: 
- tiptsf.dll
---

# ITipAutocompleteClient::RequestShowUI method

Determines whether Input Panel is ready to have the auto complete list shown.

## Syntax


```C++
HRESULT RequestShowUI(
  [in]  HWND hWndACList,
  [out] BOOL *pfAllowShowing
);
```



## Parameters

<dl> <dt>

*hWndACList* \[in\]
</dt> <dd>

Window handle of the auto complete list user interface.

</dd> <dt>

*pfAllowShowing* \[out\]
</dt> <dd>

**FALSE** if client recommends to not show the auto complete list user interface. **TRUE** if the auto complete provider can show the list user interface.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                            | Description                               |
|----------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | Success.<br/>                       |
| <dl> <dt>**E\_FAIL**</dt> </dl> | An unspecified error occurred.<br/> |



 

## Remarks

This method is called by the auto complete provider when it is about to show the auto complete user interface. If the client's internal state doesn't allow the provider to show the user interface, *pfAllowShowing* will be set to **FALSE**. For example, when the text gets sent to the field from the handwriting skin on the Tablet PC Input Panel and the user immediately starts inking, the client will recommend to not show the auto complete user interface, in order to avoid destructing the user's inking, by setting *pfAllowShowing* to **FALSE**.

Call **RequestShowUI** to set the popup auto complete list window handle before you call the [**ITipAutocompleteClient::PreferredRects Method**](itipautocompleteclient-preferredrects.md). Failure to do so will cause an **E\_INVALIDARG** error when calling **PreferredRects**.

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

[**ITipAutocompleteClient::PreferredRects Method**](itipautocompleteclient-preferredrects.md)
</dt> <dt>

[Text Input Panel Reference](text-input-panel-reference.md)
</dt> </dl>

 

 




