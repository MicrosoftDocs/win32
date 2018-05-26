---
Description: The example discussed in the following topics reads encrypted content from a custom file created by the Encrypting Content Code Example and decrypts it into the original plaintext.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: f4e3da83-2b6b-4975-898c-ed3d5e6c45ff
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Decrypting Content Code Example
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Decrypting Content Code Example

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The example discussed in the following topics reads encrypted content from a custom file created by the [Encrypting Content Code Example](encrypting-content-code-example.md) and decrypts it into the original plaintext. The file has the following format. The custom file is used only for illustration and is not suited for a production environment. For a more realistic file container format, see [Publishing Content](publishing-content.md).

-   A variable that specifies the length of the encrypted content (4 byte UINT value).
-   A variable that specifies the length of the issuance license (4 byte UINT value).
-   An array of bytes that contains the encrypted content (variable length).
-   An array of bytes that contains the issuance license (variable length).

The example requires that you enter the name of the file that contains the encrypted content, the email address of the user, and the path of the application manifest. For a more complete listing, see the Consumption sample included with the Microsoft Windows Software Development Kit (SDK). The following topics discuss the source code for the decrypting example.

-   [Decryption\_Main.cpp](decryption-main-cpp.md)
-   [Decryption\_ReadEncryptedContent.cpp](decryption-readencryptedcontent-cpp.md)
-   [Decryption\_GetSecureEnvironment.cpp](decryption-getsecureenvironment-cpp.md)
-   [Decryption\_GetManifest.cpp](decryption-getmanifest-cpp.md)
-   [Decryption\_GetContentID.cpp](decryption-getcontentid-cpp.md)
-   [Decryption\_GetCertificate.cpp](decryption-getcertificate-cpp.md)
-   [Decryption\_GetBoundLicense.cpp](decryption-getboundlicense-cpp.md)
-   [Decryption\_DecryptContent.cpp](decryption-decryptcontent-cpp.md)
-   [Decryption\_Callback.cpp](decryption-callback-cpp.md)
-   [DecryptingContent.h](decryptingcontent-h.md)

## Related topics

<dl> <dt>

[Decrypting Content](decrypting-content.md)
</dt> <dt>

[Encrypting Content](encrypting-content.md)
</dt> </dl>

 

 



