---
description: The ListCardInterfaces method retrieves the identifiers (GUIDs) of all the interfaces supported for the specified smart card.
ms.assetid: c9dfd17e-f4a9-47d3-974e-66e78bc4b06a
title: ISCardDatabase::ListCardInterfaces method (Scardmgr.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardDatabase.ListCardInterfaces
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# ISCardDatabase::ListCardInterfaces method

\[The **ListCardInterfaces** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **ListCardInterfaces** method retrieves the identifiers (GUIDs) of all the interfaces supported for the specified [*smart card*](../secgloss/s-gly.md).

## Syntax


```C++
HRESULT ListCardInterfaces(
  [in]  BSTR        bstrCardName,
  [out] LPSAFEARRAY *ppInterfaceGuids
);
```



## Parameters

<dl> <dt>

*bstrCardName* \[in\]
</dt> <dd>

Name of the smart card.

</dd> <dt>

*ppInterfaceGuids* \[out\]
</dt> <dd>

Pointer to the interface GUIDs if successful; **NULL** if operation failed.

</dd> </dl>

## Return value

The method returns one of the following possible values.



| Return code                                                                                   | Description                                                |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Operation completed successfully.<br/>               |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Invalid parameter.<br/>                              |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | A bad pointer was passed in *ppInterfaceGuids*.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Out of memory.<br/>                                  |



 

## Remarks

To retrieve the [*primary service provider*](../secgloss/p-gly.md) of the smart card, call [**GetProviderCardId**](iscarddatabase-getprovidercardid.md).

To retrieve all known [*smart cards*](../secgloss/s-gly.md), [*readers*](../secgloss/r-gly.md), and [*reader groups*](../secgloss/r-gly.md) call [**ListCards**](iscarddatabase-listcards.md), [**ListReaders**](iscarddatabase-listreaders.md), and [**ListReaderGroups**](iscarddatabase-listreadergroups.md) respectively.

For a list of all the methods provided by this interface, see [**ISCardDatabase**](iscarddatabase.md).

In addition to the COM error codes listed above, this interface may return a smart card error code if a smart card function was called to complete the request. For more information, see [Smart Card Return Values](authentication-return-values.md).

## Examples

The following example shows retrieving the identifiers of the interfaces supported for the specified smart card.


```C++
BSTR         bstrCard = NULL;
LPSAFEARRAY  pGuids = NULL;
HRESULT      hr;

bstrCard = SysAllocString(L"GemSAFE");
// Call the function for the specified card.
hr = pISCDataBase->ListCardInterfaces(bstrCard,
                                      &pGuids);
if (FAILED(hr))
{
   printf("Failed ListCardInterfaces\n");
   // Take other error handling action as needed.
}
else
{
   // Use the safe array as needed.
   // ...
   // Free BSTR when done.
   if (bstrCard)
       SysFreeString(bstrCard);
}
```



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
| IID<br/>                      | IID\_ISCardDatabase is defined as 1461AAC8-6810-11D0-918F-00AA00C18068<br/>       |



## See also

<dl> <dt>

[**GetProviderCardId**](iscarddatabase-getprovidercardid.md)
</dt> <dt>

[**ISCardDatabase**](iscarddatabase.md)
</dt> <dt>

[**ListCards**](iscarddatabase-listcards.md)
</dt> <dt>

[**ListReaderGroups**](iscarddatabase-listreadergroups.md)
</dt> <dt>

[**ListReaders**](iscarddatabase-listreaders.md)
</dt> </dl>

 

 
