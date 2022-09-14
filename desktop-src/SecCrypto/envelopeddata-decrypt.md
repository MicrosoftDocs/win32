---
description: Decrypts enveloped content.
ms.assetid: 717d0595-e8bb-4725-bd53-fc1281cbc8ee
title: EnvelopedData.Decrypt method
ms.topic: reference
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

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**EnvelopedCms Class**](/dotnet/api/system.security.cryptography.pkcs.envelopedcms?view=dotnet-plat-ext-3.1&preserve-view=true) in the [**System.Security.Cryptography.Pkcs**](/dotnet/api/system.security.cryptography.pkcs?view=dotnet-plat-ext-3.1&preserve-view=true) namespace.\]

The **Decrypt** method decrypts enveloped content. Decryption is done if the recipient of the message has access to the [*private key*](../secgloss/p-gly.md) paired with one of the [*public keys*](../secgloss/p-gly.md) used to envelop the message. Calling the **Decrypt** method resets the [*state*](../secgloss/s-gly.md) of the object. If the **Decrypt** method succeeds, the [**Content**](envelopeddata-content.md) property of the [**EnvelopedData**](envelopeddata.md) object is set to the plaintext message.

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

> [!IMPORTANT]
> When this method is called from a web script, the script needs to use your [*private key*](../secgloss/p-gly.md) to decrypt the data. Allowing untrusted websites to use your private key is a security risk. A dialog box that asks whether the website can use your private key appears when this method is first called. If you allow the script to use your private key and select "Do not ask me this again," the dialog box will no longer appear for any script that uses your private key to decrypt data within that domain. However, scripts outside that domain that attempt to use your private key to decrypt data will still cause this dialog box to appear. If you do not allow the script to use your private key and select "Do not ask me this again," scripts within that domain will automatically be refused the ability to use your private key to decrypt data.

 

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
</dt> <dt>

[**EnvelopedData**](envelopeddata.md)
</dt> </dl>

 

 
