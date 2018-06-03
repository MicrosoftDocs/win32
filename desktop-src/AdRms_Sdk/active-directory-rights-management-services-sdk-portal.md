---
Description: The Active Directory Rights Management Services (AD RMS) SDK can be used by applications to enforce terms of use for encrypted digital assets, regardless of their format or content.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 6156f045-202d-4a59-8dc0-1314ae989a3a
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Active Directory Rights Management Services SDK
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Active Directory Rights Management Services SDK

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

## Purpose

The Microsoft Windows Active Directory Rights Management Services (AD RMS) SDK can be used to create applications that enforce terms of use for digital assets, regardless of their format or content. The following are just a few of the many scenarios to which applications built on the AD RMS SDK can be applied:

## Where applicable

-   A law firm wants to prevent sensitive email messages from being printed or forwarded.
-   The developers of computer-aided design and manufacturing software want to limit drawing access to a small group of users within the research division without requiring the use of passwords.
-   The owners of a graphic design website want to use a single license that allows free viewing of low-resolution copies of their images but requires payment for access to the high-resolution versions.
-   The owners of an online document library want to enable rights to view, print, or edit documents based on the identity of the user.
-   A company wants to publish a website that contains dynamic information and allows the data to be viewed for only one week.
-   A corporation wants to publish sensitive employee information to an internal website that restricts viewing and editing privileges to certain users.

The AD RMS SDK enables you to encrypt and decrypt content, associate rights with content, discover AD RMS services, and publish and acquire content licenses.

## Developer audience

The AD RMS SDK is used to create custom applications that encrypt digital assets and enforce term of use for those assets. Knowledge of the C++ programming language is required.

## Run-time requirements

For information about the run-time requirements for a particular programming element, see the Requirements section of the reference topic for that element.

## In this section

<dl> <dt>

[What's New in the AD RMS SDK](what-s-new-in-the-ad-rms-sdk.md)
</dt> <dd>

Discusses new content for each release of the SDK.

</dd> <dt>

[Application Licensing and Best Practices](application-licensing-and-best-practices.md)
</dt> <dd>

Describes how to license your AD RMS applications during product development and release.

</dd> <dt>

[About the AD RMS SDK](about-the-ad-rms-sdk.md)
</dt> <dd>

Discusses the major portions of the SDK.

</dd> <dt>

[Using the AD RMS SDK](using-the-ad-rms-sdk.md)
</dt> <dd>

Explains common scenarios implemented by applications built using the SDK.

</dd> <dt>

[AD RMS SDK Reference](ad-rms-sdk-reference.md)
</dt> <dd>

Provides reference information for the functions, enumeration types, structures, and web methods published by the SDK.

</dd> <dt>

[AD RMS SDK Glossary](ad-rms-sdk-glossary.md)
</dt> <dd>

Provides a glossary of technical terms used in the SDK.

</dd> </dl>

 

 



