---
Description: Retrieves the location of the certificate store that this object represents.
ms.assetid: b0c64e54-7139-4945-9802-6e6c479481e2
title: Store.Location property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Store.Location property

\[The **Location** property is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509Store Class**](T:System.Security.Cryptography.X509Certificates.X509Store) in the [**System.Security.Cryptography.X509Certificates**](frlrfSystemSecurityCryptographyX509Certificates) namespace.\]

The **Location** property retrieves the location of the certificate store that this object represents.

## Syntax


```VB
Store.Location As CAPICOM_STORE_LOCATION
```



## Property value

The [**CAPICOM\_STORE\_LOCATION**](capicom-store-location.md) value that represents the location of the certificate store.

## Remarks

The value of the **Location** property is the same as the value supplied for the *StoreLocation* parameter of the [**Open**](store-open.md) method when the store was opened.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.1 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Store**](store.md)
</dt> </dl>

 

 




