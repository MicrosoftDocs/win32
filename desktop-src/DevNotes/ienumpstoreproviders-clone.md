---
Description: Creates another enumerator that contains the same enumeration state as the current one.
ms.assetid: c9a53005-4bb2-4a07-8f58-28d51f22c9e8
title: IEnumPStoreProviders::Clone method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IEnumPStoreProviders::Clone method

\[Protected Storage (Pstore) is available for use in Windows Server 2003 and Windows XP. It is only available for read-only operations in Windows Server 2008 and Windows Vista, but may be unavailable in subsequent versions. Pstore uses an older implementation of data protection. Developers are strongly encouraged to take advantage of the stronger data protection provided by the [**CryptProtectData**](https://msdn.microsoft.com/765a68fd-f105-49fc-a738-4a8129eb0770) and [**CryptUnprotectData**](https://msdn.microsoft.com/54eab3b0-d341-47c6-9c32-79328d7a7155) functions.\]

Creates another enumerator that contains the same enumeration state as the current one.

## Syntax


```C++
HRESULT Clone(
  [out] IEnumPStoreProviders **ppenum
);
```



## Parameters

<dl> <dt>

*ppenum* \[out\]
</dt> <dd>

A pointer to an [**IEnumPStoreProviders**](ienumpstoreproviders.md) pointer.

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

 

 




