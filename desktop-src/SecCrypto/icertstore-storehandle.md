---
description: Sets or retrieves the HCERTSTORE handle of a certificate store.
ms.assetid: 3ff8b4c7-4a9a-4cc1-b0ea-da442ebce157
title: ICertStore::StoreHandle property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ICertStore.StoreHandle
- ICertStore.get_StoreHandle
- ICertStore.put_StoreHandle
- CertStore.StoreHandle
api_type: 
- COM
api_location: 
- Capicom.dll
---

# ICertStore::StoreHandle property

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP.\]

The **StoreHandle** property sets or retrieves the HCERTSTORE handle of a certificate store.

This property is read/write.

## Syntax


```VB
CertStore.StoreHandle As Long
```



## Property value

The HCERTSTORE handle of the certificate store.

## Error codes

If the property access methods **put\_StoreHandle** and **get\_StoreHandle** succeed, they return S\_OK.

Any other **HRESULT** value indicates that the call failed.

## Remarks

You must call either the [**CloseHandle**](icertstore-closehandle.md) method or the [**CertCloseStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certclosestore) function to free the context.

If you set the **StoreHandle** property, the state of the entire [**Store**](store.md) object is reset.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**ICertStore**](icertstore.md)
</dt> </dl>

 

 




