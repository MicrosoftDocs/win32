---
description: Sets or retrieves a string that contains an EKU OID string value as defined in Wincrypt.h.
ms.assetid: 2fdaeddc-5ed6-46a6-a4f7-827a605e890a
title: IEKU::OID property
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- IEKU.OID
- IEKU.get_OID
- IEKU.put_OID
- EKU.OID
api_type:
- COM
api_location:
- Capicom.dll
---

# IEKU::OID property

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509EnhancedKeyUsageExtension Class**](/dotnet/api/system.security.cryptography.x509certificates.x509enhancedkeyusageextension?view=netcore-3.1) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor?view=netcore-3.1) namespace.\]

The **OID** property sets or retrieves a string that contains an EKU OID string value as defined in Wincrypt.h.

This property is read/write.

## Syntax


```VB
EKU.OID As String
```



## Property value

String that contains the EKU OID string value as defined in Wincrypt.h.

## Remarks

This property does not use the [**OID**](oid.md) object introduced in CAPICOM 2.0.

## Requirements



| Requirement | Value |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



 

 
