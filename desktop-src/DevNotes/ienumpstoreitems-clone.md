---
Description: Creates another enumerator that contains the same enumeration state as the current one.
ms.assetid: ab9eaf63-54e4-4322-9bb5-227982b15c73
title: IEnumPStoreItemsClone method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IEnumPStoreItems::Clone method

\[Protected Storage (Pstore) is available for use in Windows Server 2003 and Windows XP. It is only available for read-only operations in Windows Server 2008 and Windows Vista, but may be unavailable in subsequent versions. Pstore uses an older implementation of data protection. Developers are strongly encouraged to take advantage of the stronger data protection provided by the [**CryptProtectData**](security.cryptprotectdata) and [**CryptUnprotectData**](security.cryptunprotectdata) functions.\]

Creates another enumerator that contains the same enumeration state as the current one.

## Syntax


```C++
HRESULT Clone(
  [out] IEnumPStoreItems **ppenum
);
```



## Parameters

<dl> <dt>

*ppenum* \[out\]
</dt> <dd>

A pointer to an [**IEnumPStoreItems**](ienumpstoreitems.md) pointer.

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

[**IEnumPStoreItems**](ienumpstoreitems.md)
</dt> </dl>

 

 




