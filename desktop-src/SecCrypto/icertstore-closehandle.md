---
description: Closes an HCERTSTORE handle acquired through the StoreHandle property.
ms.assetid: 1b0d3d9b-09e0-4035-88ac-2887b3ab60c9
title: ICertStore::CloseHandle method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ICertStore.CloseHandle
- CertStore.CloseHandle
api_type: 
- COM
api_location: 
- Capicom.dll
---

# ICertStore::CloseHandle method

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP.\]

The **CloseHandle** method closes an HCERTSTORE handle acquired through the [**StoreHandle**](icertstore-storehandle.md) property.

## Syntax


```VB
CertStore.CloseHandle( _
  ByVal hCertStore _
)
```



## Parameters

<dl> <dt>

*hCertStore* \[in\]
</dt> <dd>

The HCERTSTORE handle to be closed.

</dd> </dl>

## Return value

The return value is an **HRESULT**. A value of **S\_OK** indicates success. Any other value indicates that the operation failed.

## Remarks

This method does not release the HCERTSTORE handle contained within a [**Store**](store.md) object. It should be used only to release a HCERTSTORE handle acquired through the [**StoreHandle**](icertstore-storehandle.md) property.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**ICertStore**](icertstore.md)
</dt> </dl>

 

 




