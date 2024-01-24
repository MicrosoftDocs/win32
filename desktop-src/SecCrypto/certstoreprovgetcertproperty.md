---
description: Retrieves a specified property of a certificate.
ms.assetid: 827e0331-1f87-4891-8cc1-de1bcbad2963
title: CertStoreProvGetCertProperty callback function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CertStoreProvGetCertProperty
api_type: 
- UserDefined
api_location: 
---

# CertStoreProvGetCertProperty callback function

The **CertStoreProvGetCertProperty** callback function retrieves a specified property of a certificate.

## Syntax


```C++
BOOL WINAPI CertStoreProvGetCertProperty(
  _In_    HCERTSTOREPROV hStoreProv,
  _In_    PCCERT_CONTEXT pCertContext,
  _In_    DWORD          dwPropId,
  _In_    DWORD          dwFlags,
  _Out_   void           *pvData,
  _Inout_ DWORD          *pcbData
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

A pointer to a [**CERT\_CONTEXT**](/windows/desktop/api/Wincrypt/ns-wincrypt-cert_context) structure.

</dd> <dt>

*dwPropId* \[in\]
</dt> <dd>

Indicates a property identifier.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Any needed flag values.

</dd> <dt>

*pvData* \[out\]
</dt> <dd>

A pointer to a buffer to contain the pointer to a [**CERT\_CONTEXT**](/windows/desktop/api/Wincrypt/ns-wincrypt-cert_context) structure to be returned by the function. May be set to **NULL** on a first call to the function to get the value of *pcbData* before allocating memory for the buffer.

</dd> <dt>

*pcbData* \[in, out\]
</dt> <dd>

A pointer to a **DWORD** indicating the length of the *pvData* buffer.

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
</dt> </dl>

 

 
