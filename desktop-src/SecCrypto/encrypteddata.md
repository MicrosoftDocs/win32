---
description: Provides properties and methods to encrypt and decrypt data using a session key derived from a secret.
ms.assetid: 3b9bd0a2-6e15-4d58-a682-588a93895799
title: EncryptedData object
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EncryptedData
api_type: 
- COM
api_location: 
- Capicom.dll
---

# EncryptedData object

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use Platform Invocation Services (PInvoke) to call the Win32 API functions [**CryptEncryptMessage**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptencryptmessage) and [**CryptDecryptMessage**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptdecryptmessage) to encrypt and decrypt messages. For information about PInvoke, see [Platform Invoke Tutorial](https://msdn.microsoft.com/library/aa288468.aspx). The [.NET and CryptoAPI via P/Invoke: Part 1](/previous-versions/ms867087(v=msdn.10)#netcryptoapi_topic5) and [.NET and CryptoAPI via P/Invoke: Part 2](/previous-versions/ms867087(v=msdn.10)#netcryptoapi_topic6) subsections of [Extending .NET Cryptography with CAPICOM and P/Invoke](/previous-versions/ms867087(v=msdn.10)) may also be helpful.\]

The **EncryptedData** object provides properties and methods to encrypt and decrypt data using a [*session key*](../secgloss/s-gly.md) derived from a secret.

> [!Note]  
> CAPICOM does not support the PKCS \#7 EncryptedData content type but uses a nonstandard ASN structure for **EncryptedData**. Therefore, only CAPICOM can decrypt a CAPICOM **EncryptedData** object.

 

## Members

The **EncryptedData** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **EncryptedData** object has these methods.



| Method                                       | Description                                                                             |
|:---------------------------------------------|:----------------------------------------------------------------------------------------|
| [**Decrypt**](encrypteddata-decrypt.md)     | Decrypts encrypted content using the secret.<br/>                                 |
| [**Encrypt**](encrypteddata-encrypt.md)     | Encrypts the content using the current secret and encryption algorithm.<br/>      |
| [**SetSecret**](encrypteddata-setsecret.md) | Sets the secret from which the encryption/decryption session key is derived.<br/> |



 

### Properties

The **EncryptedData** object has these properties.



| Property                                                | Access type           | Description                                                                                                                                                                                                                                                                                                                                                                                                                               |
|:--------------------------------------------------------|:----------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Algorithm**](encrypteddata-algorithm.md)<br/> | Read-only<br/>  | Algorithm used for encryption/decryption.<br/>                                                                                                                                                                                                                                                                                                                                                                                      |
| [**Content**](encrypteddata-content.md)<br/>     | Read/write<br/> | The content to be encrypted or decrypted. Setting this property must be done before the [**Encrypt**](encrypteddata-encrypt.md) method is called. <br/> When the value of this property is reset, directly or indirectly, the whole [*state*](../secgloss/s-gly.md) of the object is reset, and any encrypted content in the object is lost.<br/> This is the default property.<br/> |



 

## Remarks

The **EncryptedData** object can be created, and it is safe for scripting. The ProgID for the **EncryptedData** object is CAPICOM.EncryptedData.1.

## Requirements



| Requirement | Value |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Cryptography Objects**](cryptography-objects.md)
</dt> </dl>

 

 
