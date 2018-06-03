---
Description: 'The Active Directory Rights Management Services (AD RMS) system has four built-in rights: EDIT, OWNER, VIEWRIGHTSDATA, and EDITRIGHTSDATA.'
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 40e87b21-162c-408d-81ca-16443352ce16
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Understanding XrML Rights
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Understanding XrML Rights

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The Active Directory Rights Management Services (AD RMS) system has four built-in rights: EDIT, OWNER, VIEWRIGHTSDATA, and EDITRIGHTSDATA. An application can create additional rights, such as a PLAY right, a PRINT right, or a FORWARD right, but how these rights are defined is determined by the application. The purpose of the AD RMS system is to determine whether a particular right in a license applies to the current user; that is, whether the right is assigned to the current user, whether the validity time has not been exceeded, whether all environment requirements are satisfied, and so on. AD RMS performs the following actions, depending on the right.



| Right            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EDIT             | The AD RMS client allows a user granted the EDIT right to create a decrypting object and an encrypting object. This allows a user to decrypt content, and then re-encrypt it by using the same key. The application itself must determine which additional rights will be granted along with it, and must enable or disable UI buttons for the use of various functions.                                                                                                               |
| OWNER            | The AD RMS client allows a user granted the OWNER right to exercise all rights in the license, whether or not they are specifically granted to that user. It also allows the creation of both a decrypting object and an encrypting object. Zero, one, or more users can be granted this right in a license.                                                                                                                                                                           |
| VIEWRIGHTSDATA   | The AD RMS client allows a user that is granted the VIEWRIGHTSDATA right to allow the license information to be reused. It grants the right to make a decrypting object, but it should ideally only be used for reusing the rights information from a license. This cannot be done in a publishing application that does not use a lockbox.                                                                                                                                            |
| EDITRIGHTSDATA   | The AD RMS client allows a user that is granted the EDITRIGHTSDATA right to reuse the license information and content key from an existing issuance license. It grants the right to make a decrypting object, but it should ideally only be used for reusing the rights information and content key from a license. This cannot be done in a publishing application that does not use a lockbox.                                                                                       |
| All other rights | If granted, all other rights allow a user to create only a decrypting object associated with that right. This means that the user has access to the content; what the user is permitted to do with this content (print, forward, and so on) is strictly controlled by the application. The user cannot re-encrypt the content using the same content key unless the user is granted the EDIT or OWNER right. The result is that the content tied to the license is essentially static. |



 

The task of deciding how the user interface should change depending on the rights that are granted to the user is the job of your application. For example, you would typically enable the **Save** button if a user is granted the EDIT right, enable the **Print**, and so on.

## Related topics

<dl> <dt>

[Working with Licenses and Templates](working-with-licenses-and-templates.md)
</dt> </dl>

 

 



