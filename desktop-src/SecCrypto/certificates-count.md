---
Description: Retrieves the number of Certificate objects in the collection.
ms.assetid: 95931721-3b0c-4915-805f-039d1d5510fa
title: Certificates.Count property
ms.topic: article
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Certificates.Count
api_type:
- COM
api_location:
- Capicom.dll
---

# Certificates.Count property

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509Certificate2Collection Class**](https://msdn.microsoft.com/library/ms148470(v=VS.90).aspx) in the [**System.Security.Cryptography.X509Certificates**](https://msdn.microsoft.com/library/73091bzx(v=VS.71).aspx) namespace.\]

The **Count** property retrieves the number of [**Certificate**](certificate.md) objects in the collection.

## Syntax


```VB
Certificates.Count As Long
```



## Property value

The number of [**Certificate**](certificate.md) objects in the collection. Each **Certificate** object represents a single certificate in the collection.

## Remarks

CAPICOM only supports a single certificate for the [*smart card*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx) store. Even if the smart card store contains more than one certificate, this property will contain 1. For more information about the smart card store, see the **CAPICOM\_SMART\_CARD\_USER\_STORE** member of the [**CAPICOM\_STORE\_LOCATION**](capicom-store-location.md) enumeration.

## Requirements



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Certificates**](certificates.md)
</dt> </dl>

 

 




