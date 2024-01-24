---
description: Called when the certificate returned by the CertStoreProvFindCTL callback was not used, and thus released, in a subsequent call to CertStoreProvFindCTL.
ms.assetid: 04e62a4e-4542-4225-8750-fabbda5adf0d
title: CertStoreProvFreeFindCTL callback function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CertStoreProvFreeFindCTL
api_type: 
- UserDefined
api_location: 
---

# CertStoreProvFreeFindCTL callback function

The **CertStoreProvFreeFindCTL** callback function is called when the certificate returned by the [**CertStoreProvFindCTL**](certstoreprovfindctl.md) callback was not used, and thus released, in a subsequent call to **CertStoreProvFindCTL**. Before the CLOSE callback is called, all certificates returned by the [**CertStoreProvFindCTL**](certstoreprovfindctl.md) callback must be released by the provider using **CertStoreProvFindCTL** or **CertStoreProvFreeFindCTL**.

## Syntax


```C++
BOOL CertStoreProvFreeFindCTL(
  _In_ HCERTSTOREPROV hStoreProv,
  _In_ PCCTL_CONTEXT  pCtlContext,
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

*pCtlContext* \[in\]
</dt> <dd>

A pointer to a [**CTL\_CONTEXT**](/windows/desktop/api/Wincrypt/ns-wincrypt-cert_context) structure.

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

[**CertStoreProvFindCTL**](certstoreprovfindctl.md)
</dt> <dt>

[**CTL\_CONTEXT**](/windows/desktop/api/Wincrypt/ns-wincrypt-cert_context)
</dt> </dl>

 

 
