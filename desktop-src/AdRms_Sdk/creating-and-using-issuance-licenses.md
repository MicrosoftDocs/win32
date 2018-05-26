---
Description: An issuance license is a version 1.2 Extensible Rights Markup Language (XrML) document that identifies the rights that can be made available to users who want to consume content that has been protected by using Active Directory Rights Management Services (AD RMS). The issuance license is used to acquire an owner license that the content owner can use to encrypt content or an end-user license that a consumer can use to decrypt content.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 9948c2a4-cb42-42c1-bd22-33d39c039391
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Creating and Using Issuance Licenses
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Creating and Using Issuance Licenses

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

An issuance license is a version 1.2 Extensible Rights Markup Language (XrML) document that identifies the rights that can be made available to users who want to consume content that has been protected by using Active Directory Rights Management Services (AD RMS). The [*issuance license*](i-gly.md#-rm-issuance-license-gly) is used to acquire an owner license that the content owner can use to encrypt content or an [*end-user license*](e-gly.md#-rm-end-user-license-gly) that a consumer can use to decrypt content.

An application can create an issuance license from scratch, from a template, or from an existing license by using the [**DRMCreateIssuanceLicense**](/windows/previous-versions/Msdrm/nf-msdrm-drmcreateissuancelicense?branch=master) function. The function returns a license handle. After a license has been created, it must be signed before it can be used. Licenses can be signed online or offline by using the [**DRMGetSignedIssuanceLicense**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetsignedissuancelicense?branch=master) function. Additionally, online signing can be accomplished by using the [**AcquireIssuanceLicense**](-acquireissuancelicense.md) SOAP method. Online signing uses the AD RMS certification service. Offline signing uses a client licensor certificate issued previously by an AD RMS service. When signed online, only the issuance license is returned to the caller. When signed offline, the license chain includes the signed issuance license and the client licensor certificate.

Unsigned issuance licenses can be used to create issuance license templates or to update existing issuance licenses. For more information, see [**DRMGetIssuanceLicenseTemplate**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetissuancelicensetemplate?branch=master).

An issuance license can contain the following items.

-   The date and time that it was issued.
-   The validity period.
-   The content ID, name, and description.
-   The name and public key of the license issuer.
-   The silent license acquisition URL (signed issuance license only).
-   The nonsilent license acquisition URL and fallback URL (RMS client 1.0 signed issuance licenses only).
-   The users and groups that can be granted issuance licenses.
-   The rights available to the users and groups.
-   The conditions for using the issuance license.
-   The content key and rights information encrypted by using the server public key.
-   The digital signature of the license contents.

Issuance licenses are discussed in more detail in the following topics.

| Topic                                                              | Description                                                                                                                                  |
|--------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| [Issuance License XML Examples](issuance-license-xml-examples.md) | Contains XML examples for issuance licenses that have been signed online and offline.                                                        |
| [Creating an Issuance License](creating-an-issuance-license.md)   | Discusses multiple ways to create an issuance license.                                                                                       |
| [Online Signing Code Example](online-signing-code-example.md)     | Contains a C++ sample that creates an issuance license and signs it by using an AD RMS certification service in the enterprise.              |
| [Offline Signing Code Example](offline-signing-code-example.md)   | Contains a C++ sample that creates an issuance license and signs it by using a client licensor certificate from the local certificate store. |



 

## Related topics

<dl> <dt>

[Using the AD RMS SDK](using-the-ad-rms-sdk.md)
</dt> </dl>

 

 



