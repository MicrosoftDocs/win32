---
description: Closes an open certificate store.
ms.assetid: 14db819a-b220-47d4-9030-72157e0e5019
title: Store.Close method
ms.topic: reference
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

\[The **Close** method is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509Store Class**](/previous-versions/windows/embedded/hh424027(v=msdn.10)) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor?view=netcore-3.1&preserve-view=true) namespace.\]

The **Close** method closes an open [*certificate store*](../secgloss/c-gly.md).

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



| Requirement | Value |
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

 

 
