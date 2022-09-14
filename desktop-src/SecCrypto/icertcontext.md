---
description: Provides access to the context of a CAPICOM X.509v3 Certificate object. This context allows the CAPICOM certificate to be used in other derivations of CryptoAPI.
ms.assetid: 084a3a7b-7523-419f-a504-6fd397030d78
title: ICertContext interface
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ICertContext
api_type: 
- COM
api_location: 
- Capicom.dll
---

# ICertContext interface

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP.\]

The **ICertContext** interface provides access to the context of a CAPICOM X.509v3 [**Certificate**](certificate.md) object. This context allows the CAPICOM certificate to be used in other derivations of CryptoAPI.

## When to use

Use this interface when you need to use a CAPICOM [**Certificate**](certificate.md) object in another derivation of CryptoAPI.

## Members

The **ICertContext** interface has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ICertContext** interface has these methods.



| Method                                          | Description                                                                                                          |
|:------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------|
| [**FreeContext**](icertcontext-freecontext.md) | Releases a PCCERT\_CONTEXT acquired through the [**CertContext**](icertcontext-certcontext.md) property.<br/> |



 

### Properties

The **ICertContext** interface has these properties.



| Property                                                   | Access type           | Description                                                        |
|:-----------------------------------------------------------|:----------------------|:-------------------------------------------------------------------|
| [**CertContext**](icertcontext-certcontext.md)<br/> | Read/write<br/> | Sets or retrieves the PCCERT\_CONTEXT of a certificate.<br/> |



 

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



 

 




