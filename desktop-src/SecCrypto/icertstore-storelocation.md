---
description: Sets or retrieves the CAPICOM\_STORE\_LOCATION of a certificate store.
ms.assetid: 2bb76f51-f092-4dbe-93e9-1fdc185c7c50
title: ICertStore::StoreLocation property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ICertStore.StoreLocation
- ICertStore.get_StoreLocation
- ICertStore.put_StoreLocation
- CertStore.StoreLocation
api_type: 
- COM
api_location: 
- Capicom.dll
---

# ICertStore::StoreLocation property

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP.\]

The **StoreLocation** property sets or retrieves the [**CAPICOM\_STORE\_LOCATION**](capicom-store-location.md) of a certificate store.

This property is read/write.

## Syntax


```VB
CertStore.StoreLocation As CAPICOM_STORE_LOCATION
```



## Property value

The location of the certificate store.

## Error codes

If the property access methods **put\_StoreLocation** and **get\_StoreLocation** succeed, they return S\_OK.

Any other **HRESULT** value indicates that the call failed.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**ICertStore**](icertstore.md)
</dt> </dl>

 

 




