---
Description: The Active Directory Rights Management Services (AD RMS) SDK uses the Advanced Encryption Standard (AES) algorithm and the electronic code book (ECB) cipher mode to encrypt and decrypt content.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 768767a0-b76c-4a9a-a4b1-22dd1923c667
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Decrypting Content
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Decrypting Content

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The Active Directory Rights Management Services (AD RMS) SDK uses the Advanced Encryption Standard (AES) algorithm and the electronic code book (ECB) cipher mode to encrypt and decrypt content. The key size is 128 bits, and data is encrypted in 16-byte blocks. To decrypt content, the computer and user must be activated, and you must acquire a signed issuance license. The code example discussed later in this documentation decrypts an item of content that has been previously encrypted by using the [Encrypting Content Code Example](encrypting-content-code-example.md). That example writes the encrypted content and the signed issuance license to a custom file. The [Decrypting Content Code Example](decrypting-content-code-example.md) reads the encrypted content from the file and decrypts it. For more information about decryption, see the following topics.



| Topic                                                                  | Description                                                                                 |
|------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| [End-User License](end-user-license.md)                               | Discusses the typical structure of an end-user license that can be used to decrypt content. |
| [End-User License Store](end-user-license-store.md)                   | Identifies the local certificate store where AD RMS copies the end user license.            |
| [End User License XML Example](end-user-license-xml-example.md)       | Contains an XrML end-user license example.                                                  |
| [Decrypting Content Code Example](decrypting-content-code-example.md) | Presents a detailed code example that decrypts an item of content.                          |



 

## Related topics

<dl> <dt>

[Activating a Computer](activating-a-computer.md)
</dt> <dt>

[Activating a User](activating-a-user.md)
</dt> <dt>

[Encrypting Content](encrypting-content.md)
</dt> <dt>

[Using the AD RMS SDK](using-the-ad-rms-sdk.md)
</dt> </dl>

 

 



