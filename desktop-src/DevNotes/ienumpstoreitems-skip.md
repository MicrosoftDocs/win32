---
Description: Skips over the next specified number of items in the given enumeration sequence.
ms.assetid: 1459c18a-ccff-451f-8904-32858cc72b78
title: IEnumPStoreItems::Skip method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IEnumPStoreItems.Skip
api_type: 
- COM
api_location: 
- Pstorec.dll
---

# IEnumPStoreItems::Skip method

\[Protected Storage (Pstore) is available for use in Windows Server 2003 and Windows XP. It is only available for read-only operations in Windows Server 2008 and Windows Vista, but may be unavailable in subsequent versions. Pstore uses an older implementation of data protection. Developers are strongly encouraged to take advantage of the stronger data protection provided by the [**CryptProtectData**](https://msdn.microsoft.com/en-us/library/Aa380261(v=VS.85).aspx) and [**CryptUnprotectData**](https://msdn.microsoft.com/en-us/library/Aa380882(v=VS.85).aspx) functions.\]

Skips over the next specified number of items in the given enumeration sequence.

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

The number of data items to be skipped.

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

 

 




