---
Description: Gets the next specified number of providers in the enumeration sequence.
ms.assetid: 9ef8d330-6f78-4063-825c-9cf5b4f283cf
title: IEnumPStoreProviders::Next method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IEnumPStoreProviders::Next method

\[Protected Storage (Pstore) is available for use in Windows Server 2003 and Windows XP. It is only available for read-only operations in Windows Server 2008 and Windows Vista, but may be unavailable in subsequent versions. Pstore uses an older implementation of data protection. Developers are strongly encouraged to take advantage of the stronger data protection provided by the [**CryptProtectData**](https://msdn.microsoft.com/765a68fd-f105-49fc-a738-4a8129eb0770) and [**CryptUnprotectData**](https://msdn.microsoft.com/54eab3b0-d341-47c6-9c32-79328d7a7155) functions.\]

Gets the next specified number of providers in the enumeration sequence.

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

A pointer to the number of provider types that was actually supplied.

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

 

 




