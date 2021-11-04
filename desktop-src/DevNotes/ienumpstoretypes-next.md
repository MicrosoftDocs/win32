---
description: Gets the next specified number of provider types in the enumeration sequence.
ms.assetid: 9a1d0db0-1e9b-48f8-b373-2a82a48e4f63
title: IEnumPStoreTypes::Next method (Pstore.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IEnumPStoreTypes.Next
api_type: 
- COM
api_location: 
- Pstorec.dll
---

# IEnumPStoreTypes::Next method

\[Protected Storage (Pstore) is available for use in Windows Server 2003 and Windows XP. It is only available for read-only operations in Windows Server 2008 and Windows Vista, but may be unavailable in subsequent versions. Pstore uses an older implementation of data protection. Developers are strongly encouraged to take advantage of the stronger data protection provided by the [**CryptProtectData**](/windows/win32/api/dpapi/nf-dpapi-cryptprotectdata) and [**CryptUnprotectData**](/windows/win32/api/dpapi/nf-dpapi-cryptunprotectdata) functions.\]

Gets the next specified number of provider types in the enumeration sequence.

## Syntax


```C++
HRESULT Next(
  [in]      DWORD  celt,
  [out]     LPWSTR *rgelt,
  [in, out] DWORD  *pceltFetched
);
```



## Parameters

<dl> <dt>

*celt* \[in\]
</dt> <dd>

The number of provider types requested.

</dd> <dt>

*rgelt* \[out\]
</dt> <dd>

A pointer to a string in which to return the provider type name.

</dd> <dt>

*pceltFetched* \[in, out\]
</dt> <dd>

A pointer to the number of provider types actually supplied.

</dd> </dl>

## Return value

The return value is an **HRESULT** value.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Pstore.h</dt> </dl>    |
| DLL<br/>    | <dl> <dt>Pstorec.dll</dt> </dl> |



## See also

<dl> <dt>

[**IEnumPStoreTypes**](ienumpstoretypes.md)
</dt> </dl>

 

 
