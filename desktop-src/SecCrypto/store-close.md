---
Description: Closes an open certificate store.
ms.assetid: 14db819a-b220-47d4-9030-72157e0e5019
title: Store.Close method
ms.topic: article
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Store.Close
api_type:
- COM
api_location:
- Capicom.dll
---

# Store.Close method

\[The **Close** method is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509Store Class**](https://msdn.microsoft.com/library/Hh424027(v=MSDN.10).aspx) in the [**System.Security.Cryptography.X509Certificates**](https://msdn.microsoft.com/library/73091bzx(v=VS.71).aspx) namespace.\]

The **Close** method closes an open [*certificate store*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx).

## Syntax


```VB
Store.Close()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

After the **Close** method is called, the [**Store**](store.md) object is destroyed.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.1 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Store**](store.md)
</dt> <dt>

[**Cryptography Objects**](cryptography-objects.md)
</dt> <dt>

[**Open**](store-open.md)
</dt> </dl>

 

 




