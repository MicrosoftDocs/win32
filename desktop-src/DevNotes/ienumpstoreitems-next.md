---
description: Gets the next specified number of data item names in the enumeration sequence.
ms.assetid: 6f30bf64-bd63-43d7-ab7e-f64e372c723b
title: IEnumPStoreItems::Next method (Pstore.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IEnumPStoreItems.Next
api_type: 
- COM
api_location: 
- Pstorec.dll
---

# IEnumPStoreItems::Next method

\[Protected Storage (Pstore) is available for use in Windows Server 2003 and Windows XP. It is only available for read-only operations in Windows Server 2008 and Windows Vista, but may be unavailable in subsequent versions. Pstore uses an older implementation of data protection. Developers are strongly encouraged to take advantage of the stronger data protection provided by the [**CryptProtectData**](/windows/win32/api/dpapi/nf-dpapi-cryptprotectdata) and [**CryptUnprotectData**](/windows/win32/api/dpapi/nf-dpapi-cryptunprotectdata) functions.\]

Gets the next specified number of data item names in the enumeration sequence.

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

The number of data items requested.

</dd> <dt>

*rgelt* \[out\]
</dt> <dd>

A pointer to a string in which to return the data item name.

</dd> <dt>

*pceltFetched* \[in, out\]
</dt> <dd>

A pointer to the number of data item names actually supplied.

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

[**IEnumPStoreItems**](ienumpstoreitems.md)
</dt> </dl>

 

 
