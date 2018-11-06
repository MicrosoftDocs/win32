---
Description: Enumerates or finds the first or next CRL in an external store that matches specified criteria.
ms.assetid: caf218f5-f379-4cb6-bb4b-4767b846d45c
title: CertStoreProvFindCRL callback function
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CertStoreProvFindCRL
api_type: 
- UserDefined
api_location: 
---

# CertStoreProvFindCRL callback function

The **CertStoreProvFindCRL** callback function enumerates or finds the first or next [*CRL*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx) in an external [*store*](https://msdn.microsoft.com/en-us/library/ms721575(v=VS.85).aspx) that matches specified criteria.

## Syntax


```C++
BOOL WINAPI CertStoreProvFindCRL(
  _In_    HCERTSTOREPROV              hStoreProv,
  _In_    PCCERT_STORE_PROV_FIND_INFO pFindInfo,
  _In_    PCCRL_CONTEXT               pPrevCrlContext,
  _In_    DWORD                       dwFlags,
  _Inout_ void                        **ppvStoreProvFindInfo,
  _Out_   PCCRL_CONTEXT               *ppProvCrlContext
);
```



## Parameters

<dl> <dt>

*hStoreProv* \[in\]
</dt> <dd>

**HCERTSTOREPROV** handle to a [*certificate store*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx).

</dd> <dt>

*pFindInfo* \[in\]
</dt> <dd>

A pointer to a [**CERT\_STORE\_PROV\_FIND\_INFO**](/windows/desktop/api/Wincrypt/ns-wincrypt-_cert_store_prov_find_info) structure containing all the parameters passed to the [**CertFindCRLInStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certfindcrlinstore) function.

</dd> <dt>

*pPrevCrlContext* \[in\]
</dt> <dd>

A pointer to a [**CRL\_CONTEXT**](/windows/desktop/api/Wincrypt/ns-wincrypt-_crl_context) structure of the last CRL found. On first call to the function, this parameter should be set to **NULL**. On subsequent calls, it should be set to the pointer returned in the *ppProvCRLContext* parameter on the last call. A non-**NULL** pointer passed in this parameter is freed by the callback function.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Any needed flag values.

</dd> <dt>

*ppvStoreProvFindInfo* \[in, out\]
</dt> <dd>

A pointer to a pointer to a buffer to return the store provider information. Optionally, the callback can return a pointer to internal find information in this parameter. After the first call, this parameter is set to the pointer returned by the previous call to the function.

</dd> <dt>

*ppProvCrlContext* \[out\]
</dt> <dd>

On a successful find, a pointer to the CRL found is returned in this parameter.

</dd> </dl>

## Return value

Returns **TRUE** if the function succeeds or **FALSE** if it fails.

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**CERT\_STORE\_PROV\_FIND\_INFO**](/windows/desktop/api/Wincrypt/ns-wincrypt-_cert_store_prov_find_info)
</dt> <dt>

[**CertFindCRLInStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certfindcrlinstore)
</dt> <dt>

[**CRL\_CONTEXT**](/windows/desktop/api/Wincrypt/ns-wincrypt-_crl_context)
</dt> </dl>

 

 




