---
Description: The example discussed in the following topics requires that you enter the email address of the user for whom the issuance license is being signed and the path of the application manifest.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: a156994b-e6a8-42dc-8a49-cae20ea2e9da
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Offline Signing Code Example
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Offline Signing Code Example

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The example discussed in the following topics requires that you enter the email address of the user for whom the issuance license is being signed and the path of the application manifest. The issuance license is signed by using the client licensor certificate from the certificate store. No service discovery is necessary (unless the client licensor certificate has not been downloaded yet). For a more complete listing, see the OfflinePublishing sample included with the Microsoft Windows Software Development Kit (SDK).

-   [OfflineSigning\_Main.cpp](offlinesigning-main-cpp.md)
-   [OfflineSigning\_GetSignedIL.cpp](offlinesigning-getsignedil-cpp.md)
-   [OfflineSigning\_GetServiceURL.cpp](offlinesigning-getserviceurl-cpp.md)
-   [OfflineSigning\_GetCertificate.cpp](offlinesigning-getcertificate-cpp.md)
-   [OfflineSigning\_GetCLC.cpp](offlinesigning-getclc-cpp.md)
-   [OfflineSigning\_GetManifest.cpp](offlinesigning-getmanifest-cpp.md)
-   [OfflineSigning\_Callback.cpp](offlinesigning-callback-cpp.md)
-   [OfflineILSigning.h](offlineilsigning-h.md)

## Related topics

<dl> <dt>

[Creating and Using Issuance Licenses](creating-and-using-issuance-licenses.md)
</dt> <dt>

[Offline Signing XML Example](offline-signing-xml-example.md)
</dt> <dt>

[Online Signing Code Example](online-signing-code-example.md)
</dt> </dl>

 

 



