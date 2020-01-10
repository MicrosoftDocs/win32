---
Description: The EnvelopedData object provides properties and methods to envelop data for privacy by encryption.
ms.assetid: 7c5f3e3d-6a70-455d-8921-20495eec4b3e
title: EnvelopedData object
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- EnvelopedData
api_type:
- COM
api_location:
- Capicom.dll
---

# EnvelopedData object

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**EnvelopedCms Class**](https://msdn.microsoft.com/library/f73feezf(v=VS.90).aspx) in the [**System.Security.Cryptography.Pkcs**](https://msdn.microsoft.com/library/6see7k14(v=VS.100).aspx) namespace.\]

The **EnvelopedData** object provides properties and methods to envelop data for privacy by encryption. To envelop data, a session cryptographic key is generated. That [*session key*](https://msdn.microsoft.com/library/ms721625(v=VS.85).aspx) is then encrypted for each intended recipient using the [*public key*](https://msdn.microsoft.com/library/ms721603(v=VS.85).aspx) of that intended recipient from the recipient's certificate. The encrypted data and the set of encrypted session keys can be sent to all intended recipients. The message generated is in PKCS \#7 format.

## Members

The **EnvelopedData** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **EnvelopedData** object has these methods.



| Method                                   | Description                                                                                                 |
|:-----------------------------------------|:------------------------------------------------------------------------------------------------------------|
| [**Decrypt**](envelopeddata-decrypt.md) | Decrypts enveloped content.<br/>                                                                      |
| [**Encrypt**](envelopeddata-encrypt.md) | Encrypts the content, encrypts a session key for each recipient, and returns the encrypted BLOB.<br/> |



 

### Properties

The **EnvelopedData** object has these properties.



| Property                                                  | Access type           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|:----------------------------------------------------------|:----------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Algorithm**](envelopeddata-algorithm.md)<br/>   | Read/write<br/> | Encryption algorithm and [*key length*](https://msdn.microsoft.com/library/ms721590(v=VS.85).aspx).<br/>                                                                                                                                                                                                                                                                                                                              |
| [**Content**](envelopeddata-content.md)<br/>       | Read/write<br/> | The plaintext content of a message to be enveloped. Setting this property must be done before the [**Encrypt**](envelopeddata-encrypt.md) method is called.<br/> When the value of this property is reset, directly or indirectly, the whole [*state*](https://msdn.microsoft.com/library/ms721625(v=VS.85).aspx) of the object is reset, and any encrypted content in the object is lost.<br/> This is the default property.<br/> |
| [**Recipients**](envelopeddata-recipients.md)<br/> | Read-only<br/>  | Collection of [**Certificate**](certificate.md) objects to receive the enveloped message.<br/>                                                                                                                                                                                                                                                                                                                                              |



 

## Remarks

The **EnvelopedData** object can be created, and it is safe for scripting. The ProgID for the **EnvelopedData** object is CAPICOM.EnvelopedData.1.

## Requirements



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Cryptography Objects**](cryptography-objects.md)
</dt> </dl>

 

 




