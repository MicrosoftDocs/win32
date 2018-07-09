---
Description: Decrypts enveloped content.
ms.assetid: 717d0595-e8bb-4725-bd53-fc1281cbc8ee
title: EnvelopedData.Decrypt method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EnvelopedData.Decrypt
api_type: 
- COM
api_location: 
- Capicom.dll
---

# EnvelopedData.Decrypt method

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**EnvelopedCms Class**](https://www.bing.com/search?q=**EnvelopedCms+Class**) in the [**System.Security.Cryptography.Pkcs**](https://www.bing.com/search?q=**System.Security.Cryptography.Pkcs**) namespace.\]

The **Decrypt** method decrypts enveloped content. Decryption is done if the recipient of the message has access to the [*private key*](https://msdn.microsoft.com/en-us/library/ms721603(v=VS.85).aspx) paired with one of the [*public keys*](https://msdn.microsoft.com/en-us/library/ms721603(v=VS.85).aspx) used to envelop the message. Calling the **Decrypt** method resets the [*state*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx) of the object. If the **Decrypt** method succeeds, the [**Content**](envelopeddata-content.md) property of the [**EnvelopedData**](envelopeddata.md) object is set to the plaintext message.

## Syntax


```VB
EnvelopedData.Decrypt( _
  ByVal EnvelopedMessage _
)
```



## Parameters

<dl> <dt>

*EnvelopedMessage* \[in\]
</dt> <dd>

String that contains the enveloped data to be decrypted.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The decrypted data becomes the [**Content**](envelopeddata-content.md) property value for the [**EnvelopedData**](envelopeddata.md) object.

If the user of this method does not have access to a private key that matches one of the public keys used to envelop the message, the method fails. This method will fail if the certificate for the associated private key is not in either the local computer MY store or the current user MY store.

> \[!Important\]  
> When this method is called from a web script, the script needs to use your [*private key*](https://msdn.microsoft.com/en-us/library/ms721603(v=VS.85).aspx) to decrypt the data. Allowing untrusted websites to use your private key is a security risk. A dialog box that asks whether the website can use your private key appears when this method is first called. If you allow the script to use your private key and select "Do not ask me this again," the dialog box will no longer appear for any script that uses your private key to decrypt data within that domain. However, scripts outside that domain that attempt to use your private key to decrypt data will still cause this dialog box to appear. If you do not allow the script to use your private key and select "Do not ask me this again," scripts within that domain will automatically be refused the ability to use your private key to decrypt data.

 

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

 

 




