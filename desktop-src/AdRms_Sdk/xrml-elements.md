---
Description: Active Directory Rights Management Services (AD RMS) uses the eXtensible rights Markup Language (XrML) in licenses, certificates, and templates to identify digital content and the rights and conditions that govern use of that content.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 15988182-690a-49fc-82ef-41289f04f0bd
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: XrML Elements
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# XrML Elements

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Active Directory Rights Management Services (AD RMS) uses the eXtensible rights Markup Language (XrML) in licenses, certificates, and templates to identify digital content and the rights and conditions that govern use of that content. Three version of the language currently exist - 1.0, 1.2, and 2.0. AD RMS uses XrML 1.2. You can visit the official website for the language, www.xrml.org, to download specifications, schemas, examples, and white papers. AD RMS uses XrML 1.2 in the following documents.

| Document                    | Description                                                                                                                                                                                                            |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Machine certificate         | Identifies a computer in the AD RMS certificate hierarchy. For an XrML 1.2 example, see [Machine Certificate XML Example](machine-certificate-xml-example.md).                                                        |
| Rights account certificate  | Identifies an Active Directory user account in the AD RMS certificate hierarchy. For an XrML 1.2 example, see [Rights Account Certificate XML Example](rights-account-certificate-xml-example.md).                    |
| Issuance license            | Identifies the users who can consume protected content and the rights that can be made available to them. For an XrML 1.2 example, see [Issuance License XML Examples](issuance-license-xml-examples.md).             |
| End-user license            | Identifies the right(s) granted to a specific user to consume protected content. For an XrML 1.2 example, see [End User License XML Example](end-user-license-xml-example.md).                                        |
| Client licensor certificate | Used to sign an issuance license offline.                                                                                                                                                                              |
| Server licensor certificate | Identifies an AD RMS server in the AD RMS certificate hierarchy.                                                                                                                                                       |
| Application manifest        | Identifies your application by signing it with the Pre-production or Production certificate provided by Microsoft. For more information, see [Creating an Application Manifest](creating-an-application-manifest.md). |
| Pre-Production certificate  | Provided by Microsoft to sign a custom application into the Pre-production AD RMS certificate hierarchy. This certificate is used during application development.                                                      |
| Production certificate      | Provided by Microsoft to sign a custom application into the Production AD RMS certificate hierarchy. This certificate is used by released applications that have been licensed by Microsoft.                           |
| Rights policy template      | Contains a set of predefined rights that can be used when protecting a document in place of manually defining usage policy.                                                                                            |



 

The **XrML** element is the root of an XrML license or certificate. It contains a **BODY** element that encapsulates the license or certificate information and an optional **SIGNATURE** element that contains an encrypted hash of the body. Attributes are used to identify the XrML version number (currently 1.2), namespace, and document purpose.

``` syntax
<!ELEMENT XrML (BODY, SIGNATURE?)>
<!ATTLIST XrML
  version  CDATA #REQUIRED
  xmlns    %URI; #IMPLIED
  purpose  CDATA #IMPLIED>
```

For more information, see the following topics:

-   [BODY](body.md)
-   [SIGNATURE](signature.md)

## Related topics

<dl> <dt>

[AD RMS SDK Reference](ad-rms-sdk-reference.md)
</dt> </dl>

 

 



