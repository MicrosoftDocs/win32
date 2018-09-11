---
Description: Retrieves the location of the certificate store that this object represents.
ms.assetid: '756ee7cb-5f9f-4fb2-bf10-79b543895189'
title: Store.Location property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Store.Location
api_type:
- COM
api_location:
- Capicom.dll
---

# Store.Location property

\[The **Location** property is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509Store Class**](https://msdn.microsoft.com/library/d228271e(v=VS.100).aspx) in the [**System.Security.Cryptography.X509Certificates**](https://msdn.microsoft.com/library/73091bzx(v=VS.71).aspx) namespace.\]

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

 

 




