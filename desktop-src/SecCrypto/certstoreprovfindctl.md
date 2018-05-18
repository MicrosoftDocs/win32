---
Description: 'Enumerates or finds the first or next CTL in an external store that matches specified criteria.'
ms.assetid: '0b465e6e-fb5c-4621-a968-c2cdcab0ea15'
title: CertStoreProvFindCTL callback function
---

# CertStoreProvFindCTL callback function

The **CertStoreProvFindCTL** callback function enumerates or finds the first or next [*CTL*](security.c_gly#-security-certificate-trust-list-gly) in an [*external store*](security.e_gly#-security-external-store-gly) that matches specified criteria.

## Syntax


```C++
BOOL WINAPI CertStoreProvFindCTL(
  _In_    HCERTSTOREPROV              hStoreProv,
  _In_    PCCERT_STORE_PROV_FIND_INFO pFindInfo,
  _In_    PCCTL_CONTEXT               pPrevCtlContext,
  _In_    DWORD                       dwFlags,
  _Inout_ void                        **ppvStoreProvFindInfo,
  _Out_   PCCTL_CONTEXT               *ppProvCtlContext
);
```



## Parameters

<dl> <dt>

*hStoreProv* \[in\]
</dt> <dd>

**HCERTSTOREPROV** handle to a [*certificate store*](security.c_gly#-security-certificate-store-gly).

</dd> <dt>

*pFindInfo* \[in\]
</dt> <dd>

A pointer to a [**CERT\_STORE\_PROV\_FIND\_INFO**](cert-store-prov-find-info.md) structure containing all the parameters passed to the [**CertFindCTLInStore**](certfindctlinstore.md). function.

</dd> <dt>

*pPrevCtlContext* \[in\]
</dt> <dd>

A pointer to a [**CTL\_CONTEXT**](ctl-context.md) structure of the last CTL found. On first call to the function, this parameter should be set to **NULL**. On subsequent calls, it should be set to the pointer returned in the *ppProvCTLContext* parameter on the last call. A non-**NULL** pointer passed in this parameter is freed by the callback function.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Any needed flag values.

</dd> <dt>

*ppvStoreProvFindInfo* \[in, out\]
</dt> <dd>

A pointer to a pointer to buffer to return the store provider information. Optionally, the callback can return a pointer to internal find information in this parameter. After the first call, this parameter is set to the pointer returned by the previous call to the function.

</dd> <dt>

*ppProvCtlContext* \[out\]
</dt> <dd>

On a successful find, a pointer to the CTL found is returned in this parameter.

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

[**CERT\_STORE\_PROV\_FIND\_INFO**](cert-store-prov-find-info.md)
</dt> <dt>

[**CertFindCTLInStore**](certfindctlinstore.md)
</dt> <dt>

[**CTL\_CONTEXT**](ctl-context.md)
</dt> </dl>

 

 




