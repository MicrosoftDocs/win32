---
Description: The example discussed in the following topics requires that you enter the email address of the user for whom the issuance license is being created and signed.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 93b509a5-4997-46cd-823f-5529ec966ac6
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Online Signing Code Example
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Online Signing Code Example

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The example discussed in the following topics requires that you enter the email address of the user for whom the issuance license is being created and signed. Service discovery is used to find the URL of the AD RMS certification service. For a more complete listing, see the OnlinePublishing sample included with the Microsoft Windows Software Development Kit (SDK).

-   [OnlineSigning\_Main.cpp](onlinesigning-main-cpp.md)
-   [OnlineSigning\_GetServiceURL.cpp](onlinesigning-getserviceurl-cpp.md)
-   [OnlineSigning\_GetUnsignedIL.cpp](onlinesigning-getunsignedil-cpp.md)
-   [OnlineSigning\_Callback.cpp](onlinesigning-callback-cpp.md)
-   [OnlineILSigning.h](onlineilsigning-h.md)

## Related topics

<dl> <dt>

[Creating and Using Issuance Licenses](creating-and-using-issuance-licenses.md)
</dt> <dt>

[Online Signing XML Example](online-signing-xml-example.md)
</dt> <dt>

[Offline Signing Code Example](offline-signing-code-example.md)
</dt> </dl>

 

 



