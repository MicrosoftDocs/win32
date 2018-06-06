---
Description: The ListReaders method retrieves the names of the smart card readers registered in the smart card database.
ms.assetid: e1ca85a1-9206-4c09-ba0f-10b60e472dfb
title: ISCardDatabase::ListReaders method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ISCardDatabase::ListReaders method

\[The **ListReaders** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](https://msdn.microsoft.com/a33e4e23-5f0d-4d03-ae3b-8727cdf57ab7) provide similar functionality.\]

The **ListReaders** method retrieves the names of the smart card [*readers*](security.r_gly#-security-reader-gly) registered in the [*smart card database*](security.s_gly#-security-smart-card-database-gly).

## Syntax


```C++
HRESULT ListReaders(
  [in]  LONG        localeId,
  [out] LPSAFEARRAY *ppReaders
);
```



## Parameters

<dl> <dt>

*localeId* \[in\]
</dt> <dd>

Language localization ID.

</dd> <dt>

*ppReaders* \[out\]
</dt> <dd>

Pointer to a SAFEARRAY of BSTRs that contains the names of the smart card readers if successful; **NULL** if the operation failed.

</dd> </dl>

## Return value

The method returns one of the following possible values.



| Return code                                                                                   | Description                                         |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Operation completed successfully.<br/>        |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Invalid parameter.<br/>                       |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | A bad pointer was passed in *ppReaders*.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Out of memory.<br/>                           |



 

## Remarks

To retrieve all known [*smart cards*](security.s_gly#-security-smart-card-gly) or [*reader groups*](security.r_gly#-security-reader-group-gly), call [**ListCards**](iscarddatabase-listcards.md) or [**ListReaderGroups**](iscarddatabase-listreadergroups.md) respectively.

To retrieve the [*primary service provider*](security.p_gly#-security-primary-service-provider-gly) or the interfaces of a specific card [**GetProviderCardId**](iscarddatabase-getprovidercardid.md) or [**ListCardInterfaces**](iscarddatabase-listcardinterfaces.md) respectively.

For a list of all the methods provided by this interface, see [**ISCardDatabase**](iscarddatabase.md).

In addition to the COM error codes listed above, this interface may return a smart card error code if a smart card function was called to complete the request. For more information, see [Smart Card Return Values](authentication-return-values.md#smart-card-return-values).

## Examples

The following example shows retrieving the names of the smart card readers registered in the smart card database.


```C++
LPSAFEARRAY pReaders = NULL;
HRESULT     hr;

// Determine the reader groups.
hr = pISCDataBase->ListReaders(0x0409,  // English (US)
                               &amp;pReaders);
if (FAILED(hr))
{
   printf("Failed ListReaders\n");
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

[**ListReaderGroups**](iscarddatabase-listreadergroups.md)
</dt> </dl>

 

 




