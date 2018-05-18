---
Description: 'Skips over the next specified number of items in the enumeration sequence.'
ms.assetid: 'bf9ea700-3f44-48a7-8ea0-ee66dea61836'
title: 'IEnumPStoreProviders::Skip method'
---

# IEnumPStoreProviders::Skip method

\[Protected Storage (Pstore) is available for use in Windows Server 2003 and Windows XP. It is only available for read-only operations in Windows Server 2008 and Windows Vista, but may be unavailable in subsequent versions. Pstore uses an older implementation of data protection. Developers are strongly encouraged to take advantage of the stronger data protection provided by the [**CryptProtectData**](security.cryptprotectdata) and [**CryptUnprotectData**](security.cryptunprotectdata) functions.\]

Skips over the next specified number of items in the enumeration sequence.

## Syntax


```C++
HRESULT Skip(
  [in] DWORD celt
);
```



## Parameters

<dl> <dt>

*celt* \[in\]
</dt> <dd>

The number of provider types to be skipped.

</dd> </dl>

## Return value

The return value is an **HRESULT** value.

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Pstore.h</dt> </dl>    |
| DLL<br/>    | <dl> <dt>Pstorec.dll</dt> </dl> |



## See also

<dl> <dt>

[**IEnumPStoreProviders**](ienumpstoreproviders.md)
</dt> </dl>

 

 




