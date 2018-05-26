---
Description: The Active Directory Rights Management Services (AD RMS) SDK uses the Advanced Encryption Standard (AES) algorithm and the electronic code book (ECB) cipher mode to encrypt content.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 30959fa0-54e0-43c7-9b76-8551ac06076f
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Encrypting Content
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Encrypting Content

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The Active Directory Rights Management Services (AD RMS) SDK uses the Advanced Encryption Standard (AES) algorithm and the electronic code book (ECB) cipher mode to encrypt content. The key size is 128 bits, and data is encrypted in 16-byte blocks. To encrypt content, the computer and user must be activated, and you must acquire a signed issuance license. The code example discussed later in this documentation encrypts an item of plaintext and writes the encrypted content and the signed issuance license to a custom file. The [Decrypting Content Code Example](decrypting-content-code-example.md) reads the encrypted content from the file and decrypts it. For more information about encryption, see the following topics.

| Topic                                                                  | Description                                                                                         |
|------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| [Owner License](owner-license.md)                                     | Discusses the typical structure of an owner (end-user) license that can be used to encrypt content. |
| [Owner License Store](owner-license-store.md)                         | Identifies the local certificate store where AD RMS copies the owner license.                       |
| [Owner License XML Example](owner-license-xml-example.md)             | Contains an XrML owner license example.                                                             |
| [Encrypting Content Code Example](encrypting-content-code-example.md) | Presents a detailed code example that encrypts an item of content.                                  |



 

> \[!Important\]  
> In Windows 7, you can perform AES cipher-block chaining (CBC) encryption. One of the key features of CBC is the use of a chaining mechanism that ensures that blocks containing identical plain-text values will not produce identical cipher-text values. See the *wszSymKeyType* parameter of [**DRMGetSignedIssuanceLicense**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetsignedissuancelicense?branch=master) or [**DRMEncrypt**](/windows/previous-versions/Msdrm/nf-msdrm-drmencrypt?branch=master) to see how to perform CBC encryption on AD RMS protected content.

 

## Related topics

<dl> <dt>

[Activating a Computer](activating-a-computer.md)
</dt> <dt>

[Activating a User](activating-a-user.md)
</dt> <dt>

[Decrypting Content](decrypting-content.md)
</dt> <dt>

[Using the AD RMS SDK](using-the-ad-rms-sdk.md)
</dt> </dl>

 

 



