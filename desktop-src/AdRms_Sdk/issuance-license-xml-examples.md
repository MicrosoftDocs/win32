---
Description: You can sign an issuance license online, by using the certification service on an Active Directory Rights Management Services (AD RMS) server, or you can sign the license offline by using the client licensor certificate in the license store.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 94c6193b-8575-4878-a507-860b8fb83f95
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Issuance License XML Examples
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Issuance License XML Examples

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

You can sign an issuance license online, by using the certification service on an Active Directory Rights Management Services (AD RMS) server, or you can sign the license offline by using the client licensor certificate in the license store. Because the client licensor certificate is typically downloaded only once, offline signing reduces server connections. The following two XML examples show the license structure:

-   [Offline Signing XML Example](offline-signing-xml-example.md)
-   [Online Signing XML Example](online-signing-xml-example.md)

## Related topics

<dl> <dt>

[Creating and Using Issuance Licenses](creating-and-using-issuance-licenses.md)
</dt> <dt>

[Offline Signing Code Example](offline-signing-code-example.md)
</dt> <dt>

[Online Signing Code Example](online-signing-code-example.md)
</dt> </dl>

 

 



