---
Description: If your application does not correctly interpret and enforce the rights specified in the Active Directory Rights Management Services (AD RMS) issuance license, you may make content available in ways that the content owner did not intend.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 2e5a1fea-1317-4d3a-a3d4-53fdaf66a75e
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Rights Enforcement
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Rights Enforcement

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

If your application does not correctly interpret and enforce the rights specified in the Active Directory Rights Management Services (AD RMS) issuance license, you may make content available in ways that the content owner did not intend. For example, if the issuance license confers only the right to view content, you cannot allow a user to save the content. AD RMS classifies rights into the following groups:

-   EDIT   The EDIT right allows a user to create an AD RMS encrypting object and an AD RMS decrypting object to consume or publish content at will.
-   OWNER   The OWNER right allows a user to exercise all rights in the license, whether or not they are specifically granted. It also allows the creation of both an AD RMS encrypting object and an AD RMS decrypting object.
-   VIEWRIGHTSDATA   The VIEWRIGHTSDATA right allows data in an existing issuance license to be reused. For example, if this right is granted, you can create a new issuance license by using an existing license. It grants the right to make a decrypting object but should be used only for reusing the rights information from an existing license.
-   EDITRIGHTSDATA   The EDITRIGHTSDATA right allows the data and content key in an existing issuance license to be reused. For example, if this right is granted, you can create a new issuance license by using an existing license and content key. It grants the right to make a decrypting object but should be used only for reusing the rights information and content key from an existing license.
-   All other rights   Users granted rights other than EDIT, OWNER, and VIEWRIGHTSDATA can create an AD RMS decrypting object only if the granted rights are defined by the application and none of the rights allow the creation of an AD RMS encrypting object. Content use is limited to the functions explicitly allowed by the various rights.

Your application is responsible for managing and protecting decrypted content from unauthorized use. For example, if the issuance license grants only a PLAY right, the user interface for your application should not enable features that allow a user to save the content. Your test suite should verify that your application acts correctly on all the license rights that it recognizes.



| Standard level                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum standard<br/>     | The implementation of XrML v.1.2 rights should be consistent with the definitions of these rights, as described in the XrML specifications. Any rights specific to your application must be defined for all users.<br/> Your test suite and test process should verify that your application executes properly against the rights that the application supports and that it does not act upon unsupported rights.<br/> If you are building a publishing application, you must make available information that specifies which rights are supported by the application and how these rights should be interpreted. In addition, the user interface should make clear to the end user what the implications are of each right granted or denied for an individual item of content.<br/> Any rights that are abstracted by inclusion in new rights implemented by an application must be mapped to the new terminology. For example, a new right called MANAGER might include as abstracted rights the PRINT, COPY, and EDIT rights.<br/> |
| Recommended standard<br/> | None at this time.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Preferred standard<br/>   | None at this time.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |



 

## Related topics

<dl> <dt>

[Required Application Security Standards](required-application-security-standards.md)
</dt> </dl>

 

 




