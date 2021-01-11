---
description: Called when the certificate returned by the CertStoreProvFindCert callback was not used, and thus released, in a subsequent call to CertStoreProvFindCert.
ms.assetid: be882b56-027c-4540-9426-27d3c2b262e9
title: CertStoreProvFreeFindCert callback function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CertStoreProvFreeFindCert
api_type: 
- UserDefined
api_location: 
---

# CertStoreProvFreeFindCert callback function

The **CertStoreProvFreeFindCert** callback function is called when the certificate returned by the [**CertStoreProvFindCert**](certstoreprovfindcert.md) callback was not used, and thus released, in a subsequent call to **CertStoreProvFindCert**. Before the CLOSE callback is called, all certificates returned by the [**CertStoreProvFindCert**](certstoreprovfindcert.md) callback must be released by the provider using **CertStoreProvFindCert** or **CertStoreProvFreeFindCert**.

## Syntax


```C++
BOOL WINAPI CertStoreProvFreeFindCert(
  _In_ HCERTSTOREPROV hStoreProv,
  _In_ PCCERT_CONTEXT pCertContext,
  _In_ void           *pvStoreProvFindInfo,
  _In_ DWORD          dwFlags
);
```



## Parameters

<dl> <dt>

*hStoreProv* \[in\]
</dt> <dd>

**HCERTSTOREPROV** handle to a [*certificate store*](../secgloss/c-gly.md).

</dd> <dt>

*pCertContext* \[in\]
</dt> <dd>

A pointer to a [**CERT\_CONTEXT**](/windows/desktop/api/Wincrypt/ns-wincrypt-cert_context).

</dd> <dt>

*pvStoreProvFindInfo* \[in\]
</dt> <dd>

A pointer to a buffer containing find information.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Any needed flag values.

</dd> </dl>

## Return value

Returns **TRUE** if the function succeeds or **FALSE** if it fails.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**CERT\_CONTEXT**](/windows/desktop/api/Wincrypt/ns-wincrypt-cert_context)
</dt> <dt>

[**CertStoreProvFindCert**](certstoreprovfindcert.md)
</dt> </dl>

 

 
