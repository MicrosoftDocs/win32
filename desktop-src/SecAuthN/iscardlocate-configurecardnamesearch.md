---
description: The ConfigureCardNameSearch method specifies the card names to be used in the search for the smart card.
ms.assetid: fb406696-0cf0-4d67-8125-8888ee1b8213
title: ISCardLocate::ConfigureCardNameSearch method (Scardmgr.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardLocate.ConfigureCardNameSearch
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# ISCardLocate::ConfigureCardNameSearch method

\[The **ConfigureCardNameSearch** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **ConfigureCardNameSearch** method specifies the card names to be used in the search for the [*smart card*](../secgloss/s-gly.md).

## Syntax


```C++
HRESULT ConfigureCardNameSearch(
  [in] LPSAFEARRAY pCardNames,
  [in] LPSAFEARRAY pGroupNames,
  [in] BSTR        bstrTitle,
  [in] LONG        lFlags
);
```



## Parameters

<dl> <dt>

*pCardNames* \[in\]
</dt> <dd>

A pointer to an Automation safe array of card names in BSTR form.

</dd> <dt>

*pGroupNames* \[in\]
</dt> <dd>

A pointer to an Automation safe array of names of card/reader groups in BSTR form to add to the search.

</dd> <dt>

*bstrTitle* \[in\]
</dt> <dd>

Dialog box title for the search common control.

</dd> <dt>

*lFlags* \[in\]
</dt> <dd>

Specifies when [*user interface*](../secgloss/u-gly.md) is displayed.



| Value                                                                                                                                                                       | Meaning                                                                                                                                                                                                                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="SC_DLG_MINIMAL_UI"></span><span id="sc_dlg_minimal_ui"></span><dl> <dt>**SC\_DLG\_MINIMAL\_UI**</dt> </dl> | Displays the dialog box only if the card being searched for by the calling application is not located and available for use in a reader. This allows the card to be found, connected (either through an internal dialog box mechanism or by using the user callback functions), and returned to the calling application.<br/> |
| <span id="SC_DLG_NO_UI"></span><span id="sc_dlg_no_ui"></span><dl> <dt>**SC\_DLG\_NO\_UI**</dt> </dl>                | Causes no UI display, regardless of the search outcome.<br/>                                                                                                                                                                                                                                                                  |
| <span id="SC_DLG_FORCE_UI"></span><span id="sc_dlg_force_ui"></span><dl> <dt>**SC\_DLG\_FORCE\_UI**</dt> </dl>       | Causes UI display regardless of the search outcome.<br/>                                                                                                                                                                                                                                                                      |



 

</dd> </dl>

## Return value

The method returns one of the following possible values.



| Return code                                                                                   | Description                                                           |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Operation completed successfully.<br/>                          |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Invalid parameter.<br/>                                         |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | A bad pointer was passed in *pCardNames* or *pGroupNames*.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Out of memory.<br/>                                             |



 

## Remarks

To locate the [*smart card*](../secgloss/s-gly.md), call [**FindCard**](iscardlocate-findcard.md).

For a list of all the methods provided by this interface, see [**ISCardLocate**](iscardlocate.md).

In addition to the COM error codes listed above, this interface may return a smart card error code if a smart card function was called to complete the request. For more information, see [Smart Card Return Values](authentication-return-values.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| End of client support<br/>    | Windows XP<br/>                                                                   |
| End of server support<br/>    | Windows Server 2003<br/>                                                          |
| Header<br/>                   | <dl> <dt>Scardmgr.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Scardmgr.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Scardssp.dll</dt> </dl> |
| IID<br/>                      | IID\_ISCardLocate is defined as 1461AACD-6810-11D0-918F-00AA00C18068<br/>         |



## See also

<dl> <dt>

[**FindCard**](iscardlocate-findcard.md)
</dt> <dt>

[**ISCardLocate**](iscardlocate.md)
</dt> </dl>

 

 
