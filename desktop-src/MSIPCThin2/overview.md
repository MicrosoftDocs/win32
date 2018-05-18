---
title: Overview
description: Microsoft Rights Management Services (AD RMS and Azure RMS) is an information protection technology that helps safeguard digital information from unauthorized use.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '8A13494E-C1D7-407D-BCD1-A406915EA578'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
---

# Overview

Microsoft Rights Management Services (AD RMS and Azure RMS) is an information protection technology that helps safeguard digital information from unauthorized use. Through your rights-enabled applications, content owners will be able to define who can open, modify, print, forward, or take other actions with their content.

Rights Management SDK 4.2 is available for several platforms and is a software developer kit (SDK) or framework, which is designed for client computers and devices to help protect access to and usage of information flowing through applications that are “rights-enabled”. The SDKs for these platforms provide a simple API for an application developer to protect or consume digital content, retrieve templates and acquire policies from a server, and other related rights management tasks.

For more information on the currently supported platforms, see our developer documentation portal for [Microsoft Rights Management SDK](active-directory-rights-management-services-multi-platform-thin-client-sdk-portal.md).

The following are just a few of the scenarios possible:

-   A law firm wants to prevent sensitive email messages from being printed or forwarded on a mobile device.
-   The developers of computer-aided design and manufacturing software want to limit drawing access to a small group of users within the research division without requiring the use of passwords.
-   The owners of a graphic design mobile app want to use a single license that allows free viewing of low-resolution copies of their images but requires payment for access to the high-resolution versions.
-   The owners of an online document library want to enable rights to view, print, or edit documents based on the identity of the user, when documents are downloaded to a mobile device.
-   A corporation wants to publish sensitive employee information to an internal website that restricts viewing and editing privileges to certain users.

RMS SDK 4.2 can be downloaded, with acknowledgment and acceptance of its license agreement, freely distributed with your third-party software to enable client access to content that has been rights-protected by use and deployment of AD RMS servers in your environment or Azure RMS services. For more information, see [Get started](get-started.md).

## SDK Highlights

RMS SDK 4.2 offers some new cool features that include the following:

-   **Re-designed API** – RMS SDK 4.2 API was re-designed for maximum simplicity, so developers can enjoy a simple and transparent encryption and decryption API, which provides consistent RMS behaviors with minimum efforts.
-   **Hybrid support for AD RMS and Azure RMS** – a single RMS enabled app can consume and protect content from both AD RMS server (using AD RMS’s mobile device extension) and Azure RMS service. RMS SDK 4.2 transparently discovers the relevant end-point that IT administrators can configure.
-   **Bring your own authentication library** – as an app developer you can choose which authentication library is used with RMS SDK 4.2. Whether it is [Azure AD Authentication Library](https://msdn.microsoft.com/library/jj573266.aspx) or your organization’s custom library, RMS SDK 4.2 segregates the auth stack so you can choose the library that most fits your needs.
-   **Bring your own user interface** - RMS SDK 4.2 now allows you to implement your customize user interface. From protecting content and choosing templates to showing and changing permissions while consuming protected content, RMS SDK 4.2 does not enforce any built-in UI on your apps. If you would like, however, you can use Microsoft RMS UI libraries for all platforms via our [GitHub account](https://github.com/AzureAD/).
-   **Access protected content offline** – RMS SDK 4.2 allows your app users to access protected content even when there is no internet connectivity. RMS SDK 4.2 securely caches the consumption policies of the protected content so your users can access RMS protected data offline.

Use the [Get started](get-started.md) guide to begin your protected information device app project.

## Related topics

<dl> <dt>

[Microsoft Rights Management SDK](active-directory-rights-management-services-multi-platform-thin-client-sdk-portal.md)
</dt> <dt>

[Get started](get-started.md)
</dt> <dt>

[Azure AD Authentication Library](https://msdn.microsoft.com/library/jj573266.aspx)
</dt> <dt>

[GitHub account](https://github.com/AzureAD/)
</dt> </dl>

 

 




