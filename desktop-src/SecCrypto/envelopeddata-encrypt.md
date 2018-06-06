---
Description: Generates a session key and encrypts and envelopes data.
ms.assetid: 7ae0c908-207b-4a74-a195-d12e9e7dec76
title: EnvelopedData.Encrypt method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# EnvelopedData.Encrypt method

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**EnvelopedCms Class**](https://www.bing.com/search?q=**EnvelopedCms+Class**) in the [**System.Security.Cryptography.Pkcs**](https://www.bing.com/search?q=**System.Security.Cryptography.Pkcs**) namespace.\]

The **Encrypt** method generates a session key, uses that key to encrypt the contents, envelops the encrypted content for each recipient by encrypting the session key with each recipient's public key, and then returns the [*BLOB*](security.b_gly#-security-blob-gly) that contains the encrypted contents and the encrypted session keys as an encoded string.

## Syntax


```VB
EnvelopedData.Encrypt( _
  [ ByVal EncodingType ] _
)
```



## Parameters

<dl> <dt>

*EncodingType* \[in, optional\]
</dt> <dd>

A value of the [**CAPICOM\_ENCODING\_TYPE**](capicom-encoding-type.md) enumeration that indicates the encoding type used to encode the enveloped data. The default encoding value is CAPICOM\_ENCODE\_BASE64. This parameter can be one of the following values.



| Value                                                                                                                                                                                  | Meaning                                                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="CAPICOM_ENCODE_ANY"></span><span id="capicom_encode_any"></span><dl> <dt>**CAPICOM\_ENCODE\_ANY**</dt> </dl>          | This encoding type is used only when the input data has an unknown encoding type. If this value is used to specify the output's encoding type, CAPICOM\_ENCODE\_BASE64 will be used instead. Introduced in CAPICOM 2.0.<br/> |
| <span id="CAPICOM_ENCODE_BASE64"></span><span id="capicom_encode_base64"></span><dl> <dt>**CAPICOM\_ENCODE\_BASE64**</dt> </dl> | Data is saved as a base64-encoded string.<br/>                                                                                                                                                                               |
| <span id="CAPICOM_ENCODE_BINARY"></span><span id="capicom_encode_binary"></span><dl> <dt>**CAPICOM\_ENCODE\_BINARY**</dt> </dl> | Data is saved as a pure binary sequence.<br/>                                                                                                                                                                                |



 

</dd> </dl>

## Return value

This method returns a BLOB that contains the enveloped data in an encoded string.

## Remarks

The returned BLOB contains the encrypted content and an encrypted session key for each intended recipient. These session keys are encrypted using the public key of each recipient. The encrypted session keys can be decrypted only with a recipient's private key.

If the [**Recipients**](envelopeddata-recipients.md) property does not contain any information, this method searches the current user's AddressBook certificate store for potential recipients. If more than one potential recipient is found, the user is prompted to select a recipient from a selection dialog box.

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
</dt> <dt>

[**EnvelopedData**](envelopeddata.md)
</dt> </dl>

 

 




