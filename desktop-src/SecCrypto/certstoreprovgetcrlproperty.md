---
Description: 'Retrieves a specified property of a CRL.'
ms.assetid: 'b02f4f92-952a-4625-a7d4-6e78e542774e'
title: CertStoreProvGetCRLProperty callback function
---

# CertStoreProvGetCRLProperty callback function

The **CertStoreProvGetCRLProperty** callback function retrieves a specified property of a [*CRL*](security.c_gly#-security-certificate-revocation-list-gly).

## Syntax


```C++
BOOL WINAPI CertStoreProvGetCRLProperty(
  _In_    HCERTSTOREPROV hStoreProv,
  _In_    PCCRL_CONTEXT  pCrlContext,
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

**HCERTSTOREPROV** handle to a [*certificate store*](security.c_gly#-security-certificate-store-gly).

</dd> <dt>

*pCrlContext* \[in\]
</dt> <dd>

A pointer to a [**CRL\_CONTEXT**](crl-context.md) structure.

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

A pointer to a buffer to contain the pointer to a [**CRL\_CONTEXT**](crl-context.md) structure to be returned by the function. May be set to **NULL** on a first call to the function to get the value of *pcbData* before allocating memory for the buffer.

</dd> <dt>

*pcbData* \[in, out\]
</dt> <dd>

A pointer to a **DWORD** indicating the length of the *pvData* buffer.

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

[**CRL\_CONTEXT**](crl-context.md)
</dt> </dl>

 

 




