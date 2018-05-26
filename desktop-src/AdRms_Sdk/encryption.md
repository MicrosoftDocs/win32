---
Description: Encryption is the process that Active Directory Rights Management Services (AD RMS) uses to protect content.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: d9fffa43-26fa-4195-bcb3-7a7879ec2a40
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Encryption
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Encryption

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Encryption is the process that Active Directory Rights Management Services (AD RMS) uses to protect content. Decryption reverses the protection so that the content can be consumed. Currently, AD RMS uses the Advanced Encryption Standard (AES) algorithm and the electronic codebook (ECB) block cipher, or cipher-block chaining (CBC), for encryption.

You can use the [**DRMEncrypt**](/windows/previous-versions/Msdrm/nf-msdrm-drmencrypt?branch=master) function to encrypt content and the [**DRMDecrypt**](/windows/previous-versions/Msdrm/nf-msdrm-drmdecrypt?branch=master) function to decrypt it. Encryption requires that the content owner create a signed [*issuance license*](i-gly.md#-rm-issuance-license-gly) that specifies who can consume content and acquire an [*end-user license*](e-gly.md#-rm-end-user-license-gly) that has either the OWNER or EDIT rights defined. Decryption requires and end-user license for which the EDIT right is defined. For more information, see [Encrypting Content](encrypting-content.md) and [Decrypting Content](decrypting-content.md).

## Related topics

<dl> <dt>

[AD RMS Concepts](ad-rms-concepts.md)
</dt> </dl>

 

 



