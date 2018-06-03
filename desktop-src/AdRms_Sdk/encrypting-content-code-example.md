---
Description: The example discussed in the following topics encrypts an item of content and writes it and the signed issuance license to a custom binary file.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 3bf7eca8-d817-4b35-b963-1fcfefd692f5
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Encrypting Content Code Example
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Encrypting Content Code Example

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The example discussed in the following topics encrypts an item of content and writes it and the signed issuance license to a custom binary file. The content is decrypted in the [Decrypting Content Code Example](decrypting-content-code-example.md). The file has the following format. The custom file is used only for illustration and is not suited for a production environment. For a more realistic file container format, see [Publishing Content](publishing-content.md).

-   A variable that specifies the length of the encrypted content (4 byte UINT value).
-   A variable that specifies the length of the issuance license (4 byte UINT value).
-   An array of bytes that contains the encrypted content (variable length).
-   An array of bytes that contains the issuance license (variable length).

The example requires that you enter the email address of the user and the path of the application manifest. For a more complete listing, see the Consumption sample included with the Microsoft Windows Software Development Kit (SDK). The following topics discuss the encrypting example source code.

-   [Encryption\_Main.cpp](encryption-main-cpp.md)
-   [Encryption\_EncryptContent.cpp](encryption-encryptcontent-cpp.md)
-   [Encryption\_GetCertificate.cpp](encryption-getcertificate-cpp.md)
-   [Encryption\_GetSecureEnvironment.cpp](encryption-getsecureenvironment-cpp.md)
-   [Encryption\_GetManifest.cpp](encryption-getmanifest-cpp.md)
-   [Encryption\_GetOfflineSignedIL.cpp](encryption-getofflinesignedil-cpp.md)
-   [Encryption\_Callback.cpp](encryption-callback-cpp.md)
-   [EncryptingContent.h](encryptingcontent-h.md)

## Related topics

<dl> <dt>

[Decrypting Content](decrypting-content.md)
</dt> <dt>

[Encrypting Content](encrypting-content.md)
</dt> </dl>

 

 



