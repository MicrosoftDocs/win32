---
description: Allows the client to suggest where to position the auto complete list to avoid overlapping the Input Panel.
ms.assetid: c82ffecb-f3e6-4c50-80bb-8393b39d3b2a
title: ITipAutocompleteClient::PreferredRects method (TipAutoComplete.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ITipAutocompleteClient.PreferredRects
api_type: 
- COM
api_location: 
- tiptsf.dll
---

# ITipAutocompleteClient::PreferredRects method

Allows the client to suggest where to position the auto complete list to avoid overlapping the Input Panel.

## Syntax


```C++
HRESULT PreferredRects(
  [in]      RECT *prcACList,
  [in]      RECT *prcField,
  [out]     RECT *prcModified,
  [in, out] BOOL *pfShownAboveTip
);
```



## Parameters

<dl> <dt>

*prcACList* \[in\]
</dt> <dd>

A rectangle, in screen coordinates, indicating the provider's preferred location and the size of the auto complete list user interface.

</dd> <dt>

*prcField* \[in\]
</dt> <dd>

A rectangle, in screen coordinates, indicating the location and the size of the focused field.

</dd> <dt>

*prcModified* \[out\]
</dt> <dd>

A rectangle based on the current state of the TIP and the preferred auto complete list location and size specified by *prcACList*.

</dd> <dt>

*pfShownAboveTip* \[in, out\]
</dt> <dd>

**TRUE** if the modified rectangle is to be shown above the Text Input Panel's target area; otherwise, **FALSE**. This value must be initialized to the provider's preferred orientation before the method is called.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                  | Description                                                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Success.<br/>                                                                                                                                                                                                                                                            |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Call the [**ITipAutocompleteClient::RequestShowUI Method**](itipautocompleteclient-requestshowui.md) to set the popup auto complete list window before calling the [**ITipAutocompleteClient::PreferredRects Method**](itipautocompleteclient-preferredrects.md).<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>       | An unspecified error occurred.<br/>                                                                                                                                                                                                                                      |



 

## Remarks

This is the method that the auto complete provider calls when it is about to show the auto complete user interface. The client modifies the provider's preferred rectangle specified by *prcACList* through *prcModified* argument.

Call the [**ITipAutocompleteClient::RequestShowUI Method**](itipautocompleteclient-requestshowui.md) to set the popup auto complete list window handle before you call **PreferredRects**. Failure to do so will cause an **E\_INVALIDARG** error when calling **PreferredRects**.

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

[**ITipAutocompleteClient::RequestShowUI Method**](itipautocompleteclient-requestshowui.md)
</dt> <dt>

[Text Input Panel Reference](text-input-panel-reference.md)
</dt> </dl>

 

 




