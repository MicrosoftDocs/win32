---
Description: To publish digital content that has been protected by using the Active Directory Rights Management Services (AD RMS) SDK, you typically combine the encrypted content and the related issuance license in one package.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 6c6f9151-5d44-48ab-9f3f-2e45217e76d0
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Publishing Content
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Publishing Content

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

To publish digital content that has been protected by using the Active Directory Rights Management Services (AD RMS) SDK, you typically combine the encrypted content and the related issuance license in one package. This enables the intended consumer to more easily open the package, extract the issuance license, use the issuance license to acquire an end-user license, and employ the end-user license to decrypt the content. You may also want to add the end-user license to the package so that the consumer does not have to retrieve one from the AD RMS server.

The AD RMS SDK includes functions, structures, and other data types that enable your application to acquire the licenses and certificates needed to protect and consume content, but the SDK cannot be directly leveraged to create a publishing infrastructure, and AD RMS does not provide such a service.

Microsoft does, however, provide the Active Directory Rights Management Add-on for Internet Explorer that can process and display AD RMS-protected documents. You can use this, or you can also publish protected content by using a custom file format. The [Encrypting Content](encrypting-content.md) and [Decrypting Content](decrypting-content.md) examples included with this documentation use a custom binary file, but this particular format is not suitable for a production environment.

The Active Directory Rights Management Add-on for Internet Explorer uses the compound file binary format (CFBF), an open container format, that can store encrypted content, an issuance license, and end-user licenses at known locations within the container. This is discussed in the following sections:

-   [Understanding Compound Files](understanding-compound-files.md)
-   [Creating a Compound File and Adding Protected Content](creating-a-compound-file-and-adding-protected-content.md)
-   [Adding an Issuance License to the Compound File](adding-an-issuance-license-to-the-compound-file.md)
-   [Adding a Use License to the Compound File](adding-a-use-license-to-the-compound-file.md)
-   [Updating an Issuance License in a Compound File](updating-an-issuance-license-in-a-compound-file.md)

## Related topics

<dl> <dt>

[Using the AD RMS SDK](using-the-ad-rms-sdk.md)
</dt> <dt>

[Creating and Using Issuance Licenses](creating-and-using-issuance-licenses.md)
</dt> <dt>

[Decrypting Content](decrypting-content.md)
</dt> <dt>

[Encrypting Content](encrypting-content.md)
</dt> </dl>

 

 



