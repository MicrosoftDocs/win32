---
description: Sets or retrieves the private key associated with the certificate.
ms.assetid: 976d81b4-5cbe-4824-9087-9a908b0e60e5
title: Certificate.PrivateKey property
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Certificate.PrivateKey
api_type:
- COM
api_location:
- Capicom.dll
---

# Certificate.PrivateKey property

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509Certificate2 Class**](/previous-versions/windows/embedded/hh424017(v=msdn.10)) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor) namespace.\]

The **PrivateKey** property sets or retrieves the private key associated with the certificate. This property was introduced in CAPICOM 2.0.

This property is read/write.

## Syntax


```VB
Certificate.PrivateKey As PrivateKey
```



## Property value

A [**PrivateKey**](privatekey.md) object that represents the private key that is associated with the certificate.

## Remarks

Setting the **PrivateKey** property to Nothing removes the association between the private key and the certificate, but it does not delete the private key. To delete the private key, call the [**PrivateKey.Delete**](privatekey-delete.md) method, and then set this property to Nothing.

This property raises CAPICOM\_E\_NOT\_ALLOWED when it is set from a web-based application.

## Requirements



| Requirement | Value |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Certificate**](certificate.md)
</dt> </dl>

 

 
