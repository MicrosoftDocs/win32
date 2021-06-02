---
description: Retrieves a specified property of a certificate trust list (CTL).
ms.assetid: 65309715-65b4-4608-960d-3404e68800a2
title: CertStoreProvGetCTLProperty callback function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CertStoreProvGetCTLProperty
api_type: 
- UserDefined
api_location: 
---

# CertStoreProvGetCTLProperty callback function

The **CertStoreProvGetCTLProperty** callback function retrieves a specified property of a [*certificate trust list*](../secgloss/c-gly.md) (CTL).

## Syntax


```C++
BOOL WINAPI CertStoreProvGetCTLProperty(
  _In_    HCERTSTOREPROV hStoreProv,
  _In_    PCCTL_CONTEXT  pCtlContext,
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

A **HCERTSTOREPROV** handle to a [*certificate store*](../secgloss/c-gly.md).

</dd> <dt>

*pCtlContext* \[in\]
</dt> <dd>

A pointer to a [**CTL\_CONTEXT**](/windows/desktop/api/Wincrypt/ns-wincrypt-ctl_context) structure.

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

A pointer to a buffer to contain the pointer to a [**CTL\_CONTEXT**](/windows/desktop/api/Wincrypt/ns-wincrypt-ctl_context) structure to be returned by the function. To get the value of *pcbData* before allocating memory for the buffer, this parameter can be set to **NULL** on a first call to the function.

</dd> <dt>

*pcbData* \[in, out\]
</dt> <dd>

A pointer to a **DWORD** that indicates the length of the *pvData* buffer.

</dd> </dl>

## Return value

If the function succeeds, the function returns nonzero.

If the function fails, it returns zero.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**CTL\_CONTEXT**](/windows/desktop/api/Wincrypt/ns-wincrypt-ctl_context)
</dt> </dl>

 

 
