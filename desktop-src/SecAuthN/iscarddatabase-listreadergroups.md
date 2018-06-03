---
Description: The ListReaderGroups method retrieves the names of the reader groups registered in the smart card database.
ms.assetid: 81f6356a-92eb-4d27-abfe-e4a32de14d1c
title: ISCardDatabase::ListReaderGroups method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ISCardDatabase::ListReaderGroups method

\[The **ListReaderGroups** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](https://msdn.microsoft.com/windows/desktop/a33e4e23-5f0d-4d03-ae3b-8727cdf57ab7) provide similar functionality.\]

The **ListReaderGroups** method retrieves the names of the [*reader groups*](https://www.bing.com/search?q=*reader groups*) registered in the smart card database.

## Syntax


```C++
HRESULT ListReaderGroups(
  [in]  LONG        localeId,
  [out] LPSAFEARRAY *ppReaderGroups
);
```



## Parameters

<dl> <dt>

*localeId* \[in\]
</dt> <dd>

Language localization ID.

</dd> <dt>

*ppReaderGroups* \[out\]
</dt> <dd>

Pointer to a SAFEARRAY of BSTRs that contains the names of the smart card reader groups that satisfied the search parameters if successful; **NULL** if the operation failed.

</dd> </dl>

## Return value

The method returns one of the following possible values.



| Return code                                                                                   | Description                                              |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Operation completed successfully.<br/>             |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Invalid parameter.<br/>                            |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | A bad pointer was passed in *ppReaderGroups*.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Out of memory.<br/>                                |



 

## Remarks

To retrieve all known [*smart cards*](https://www.bing.com/search?q=*smart cards*) or [*readers*](https://www.bing.com/search?q=*readers*), call [**ListCards**](iscarddatabase-listcards.md) or [**ListReaders**](iscarddatabase-listreaders.md) respectively.

To retrieve the [*primary service provider*](https://www.bing.com/search?q=*primary service provider*) or the interfaces of a specific card [**GetProviderCardId**](iscarddatabase-getprovidercardid.md) or [**ListCardInterfaces**](iscarddatabase-listcardinterfaces.md) respectively.

For a list of all the methods provided by this interface, see [**ISCardDatabase**](iscarddatabase.md).

In addition to the COM error codes listed above, this interface may return a smart card error code if a smart card function was called to complete the request. For more information, see [Smart Card Return Values](https://www.bing.com/search?q=Smart Card Return Values).

## Examples

The following example shows retrieving the names of the reader groups registered in the smart card database.


```C++
LPSAFEARRAY pGroups = NULL;
HRESULT     hr;

// Determine the reader groups.
hr = pISCDataBase->ListReaderGroups(0x0409,  // English (US)
                                    &amp;pGroups);
if (FAILED(hr))
{
   printf("Failed ListReaderGroups\n");
   // Take other error handling action as needed.
}
else
{
   // Use the safe array as needed.
   // ...
}
```



## Requirements



|                                     |                                                                                         |
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

[**ListCardInterfaces**](iscarddatabase-listcardinterfaces.md)
</dt> <dt>

[**ListCards**](iscarddatabase-listcards.md)
</dt> <dt>

[**ListReaders**](iscarddatabase-listreaders.md)
</dt> </dl>

 

 




