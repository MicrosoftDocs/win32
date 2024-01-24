---
description: Provides access to the context of a CAPICOM Store object. This context allows the CAPICOM certificate store to be used in other derivations of CryptoAPI.
ms.assetid: dc108e2d-d6ec-4972-9c8e-e6e738c25756
title: ICertStore interface
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ICertStore
api_type: 
- COM
api_location: 
- Capicom.dll
---

# ICertStore interface

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP.\]

The **ICertStore** interface provides access to the context of a CAPICOM [**Store**](store.md) object. This context allows the CAPICOM certificate store to be used in other derivations of CryptoAPI.

## When to use

Use this interface when you need to use a CAPICOM [**Store**](store.md) object in another derivation of CryptoAPI.

## Members

The **ICertStore** interface has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ICertStore** interface has these methods.



| Method                                        | Description                                                                                                         |
|:----------------------------------------------|:--------------------------------------------------------------------------------------------------------------------|
| [**CloseHandle**](icertstore-closehandle.md) | Closes an HCERTSTORE handle acquired through the [**StoreHandle**](icertstore-storehandle.md) property.<br/> |



 

### Properties

The **ICertStore** interface has these properties.



| Property                                                     | Access type           | Description                                                                                                         |
|:-------------------------------------------------------------|:----------------------|:--------------------------------------------------------------------------------------------------------------------|
| [**StoreHandle**](icertstore-storehandle.md)<br/>     | Read/write<br/> | Sets or retrieves the HCERTSTORE handle of a certificate store.<br/>                                          |
| [**StoreLocation**](icertstore-storelocation.md)<br/> | Read/write<br/> | Sets or retrieves the [**CAPICOM\_STORE\_LOCATION**](capicom-store-location.md) of a certificate store.<br/> |



 

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



 

 




