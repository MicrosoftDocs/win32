---
Description: An Active Directory Rights Management Services (AD RMS) signs issuance licenses and issues end-user licenses to the AD RMS client.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 376dcfad-ca65-4540-80a8-7eea3a0e3ad5
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Official Template XrML
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Official Template XrML

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

An Active Directory Rights Management Services (AD RMS) signs issuance licenses and issues end-user licenses to the AD RMS client. The server provides a user interface that allows an administrator to create standardized issuance license templates quickly and easily. The interface allows a template designer to choose rights to apply to a document from a list. The new template can be distributed throughout the organization to provide company-wide standards that specify how documents should be handled.

The interface provides user-friendly terms for the underlying XrML tags that are entered into the template. These terms apply to a range of document types, including email and print documents. The user-friendly terms and corresponding XrML tags are shown in the following table.



| Display name     | XrML tag                    |
|------------------|-----------------------------|
| Full Control     | OWNER                       |
| View Rights      | VIEWRIGHTSDATA              |
| Export (Save As) | DOCEDIT, EDIT, VIEW, EXPORT |
| Save             | DOCEDIT, EDIT, VIEW         |
| View             | VIEW                        |
| Print            | PRINT                       |
| Extract          | EXTRACT                     |
| Edit             | DOCEDIT, EDIT, VIEW         |
| Allow Macros     | OBJMODEL                    |
| Forward          | FORWARD                     |
| Reply            | REPLY                       |
| Reply All        | REPLYALL                    |



 

Applications are not limited to these tags, but Microsoft Office uses and interprets these tags consistently. For information about how these tags should be interpreted by an application that uses Office documents, see the Microsoft Office Developer's Kit. Applications using tags in addition to these should be consistent in their use. For more information about implementing XrML rights, see [Understanding XrML Rights](understanding-xrml-rights.md).

## Related topics

<dl> <dt>

[Working with Licenses and Templates](working-with-licenses-and-templates.md)
</dt> </dl>

 

 



