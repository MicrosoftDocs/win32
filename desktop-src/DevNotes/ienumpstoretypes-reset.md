---
Description: Resets to the beginning of the enumeration sequence.
ms.assetid: 35f14aa5-92cb-4ad8-b80c-2550dedb7a7f
title: IEnumPStoreTypesReset method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IEnumPStoreTypes::Reset method

\[Protected Storage (Pstore) is available for use in Windows Server 2003 and Windows XP. It is only available for read-only operations in Windows Server 2008 and Windows Vista, but may be unavailable in subsequent versions. Pstore uses an older implementation of data protection. Developers are strongly encouraged to take advantage of the stronger data protection provided by the [**CryptProtectData**](security.cryptprotectdata) and [**CryptUnprotectData**](security.cryptunprotectdata) functions.\]

Resets to the beginning of the enumeration sequence.

## Syntax


```C++
HRESULT Reset();
```



## Parameters

This method has no parameters.

## Return value

The return value is an **HRESULT** value.

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Pstore.h</dt> </dl>    |
| DLL<br/>    | <dl> <dt>Pstorec.dll</dt> </dl> |



## See also

<dl> <dt>

[**IEnumPStoreTypes**](ienumpstoretypes.md)
</dt> </dl>

 

 




