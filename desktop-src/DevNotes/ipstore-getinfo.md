---
description: Returns information on the storage provider.
ms.assetid: bdacb5bb-a37a-4970-add7-57625bec1ce0
title: IPStore::GetInfo method (Pstore.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPStore.GetInfo
api_type: 
- COM
api_location: 
- Pstorec.dll
---

# IPStore::GetInfo method

\[Protected Storage (Pstore) is available for use in Windows Server 2003 and Windows XP. It is only available for read-only operations in Windows Server 2008 and Windows Vista, but may be unavailable in subsequent versions. Pstore uses an older implementation of data protection. Developers are strongly encouraged to take advantage of the stronger data protection provided by the [**CryptProtectData**](/windows/win32/api/dpapi/nf-dpapi-cryptprotectdata) and [**CryptUnprotectData**](/windows/win32/api/dpapi/nf-dpapi-cryptunprotectdata) functions.\]

Returns information on the storage provider.

## Syntax


```C++
HRESULT GetInfo(
  [out] PPST_PROVIDERINFO *ppProperties
);
```



## Parameters

<dl> <dt>

*ppProperties* \[out\]
</dt> <dd>

A pointer to a **PPST\_PROVIDERINFO** structure that contains information about the storage provider.

</dd> </dl>

## Return value

The return value is an **HRESULT** value. A value of **PST\_E\_OK** indicates the function was successful.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Pstore.h</dt> </dl>    |
| DLL<br/>    | <dl> <dt>Pstorec.dll</dt> </dl> |



## See also

<dl> <dt>

[**IPStore**](ipstore.md)
</dt> </dl>

 

 
