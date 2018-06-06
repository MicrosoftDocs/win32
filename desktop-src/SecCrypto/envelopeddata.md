---
Description: The EnvelopedData object provides properties and methods to envelop data for privacy by encryption.
ms.assetid: 7c5f3e3d-6a70-455d-8921-20495eec4b3e
title: EnvelopedData object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# EnvelopedData object

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**EnvelopedCms Class**](https://www.bing.com/search?q=**EnvelopedCms+Class**) in the [**System.Security.Cryptography.Pkcs**](https://www.bing.com/search?q=**System.Security.Cryptography.Pkcs**) namespace.\]

The **EnvelopedData** object provides properties and methods to envelop data for privacy by encryption. To envelop data, a session cryptographic key is generated. That [*session key*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50) is then encrypted for each intended recipient using the [*public key*](https://msdn.microsoft.com/2fe6cfd3-8a2e-4dbe-9fb8-332633daa97a) of that intended recipient from the recipient's certificate. The encrypted data and the set of encrypted session keys can be sent to all intended recipients. The message generated is in PKCS \#7 format.

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
| [**Algorithm**](envelopeddata-algorithm.md)<br/>   | Read/write<br/> | Encryption algorithm and [*key length*](https://msdn.microsoft.com/f17042c3-ba1a-408f-af55-5f171b0dee33).<br/>                                                                                                                                                                                                                                                                                                                              |
| [**Content**](envelopeddata-content.md)<br/>       | Read/write<br/> | The plaintext content of a message to be enveloped. Setting this property must be done before the [**Encrypt**](envelopeddata-encrypt.md) method is called.<br/> When the value of this property is reset, directly or indirectly, the whole [*state*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50) of the object is reset, and any encrypted content in the object is lost.<br/> This is the default property.<br/> |
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

 

 




