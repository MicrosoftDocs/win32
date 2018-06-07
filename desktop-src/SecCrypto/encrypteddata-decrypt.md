---
Description: Decrypts an encrypted and encoded data string.
ms.assetid: 7601083d-0adb-48e1-98a7-804a49f71206
title: EncryptedData.Decrypt method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# EncryptedData.Decrypt method

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use Platform Invocation Services (PInvoke) to call the Win32 API functions [**CryptEncryptMessage**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptencryptmessage) and [**CryptDecryptMessage**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptdecryptmessage) to encrypt and decrypt messages. For information about PInvoke, see [Platform Invoke Tutorial](http://go.microsoft.com/fwlink/p/?linkid=119531). The [.NET and CryptoAPI via P/Invoke: Part 1](http://go.microsoft.com/fwlink/p/?linkid=119533) and [.NET and CryptoAPI via P/Invoke: Part 2](http://go.microsoft.com/fwlink/p/?linkid=119534) subsections of [Extending .NET Cryptography with CAPICOM and P/Invoke](http://go.microsoft.com/fwlink/p/?linkid=119532) may also be helpful.\]

The **Decrypt** method decrypts an encrypted and encoded data string. The resulting plaintext data becomes the [**Content**](encrypteddata-content.md) property of the [**EncryptedData**](encrypteddata.md) object. Decryption of the content fails unless the secret, set by the [**SetSecret**](encrypteddata-setsecret.md) method, is exactly the same as the secret used to derive the key used to encrypt the content.

## Syntax


```VB
EncryptedData.Decrypt( _
  ByVal EncryptedMessage _
)
```



## Parameters

<dl> <dt>

*EncryptedMessage* \[in\]
</dt> <dd>

String that contains the encoded, encrypted data to be decrypted.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The session key derived from the current secret is used for the decryption. This method will not produce the correct plaintext unless the current secret exactly matches the secret used to encrypt the message.

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

[**EncryptedData**](encrypteddata.md)
</dt> </dl>

 

 




