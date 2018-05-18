---
title: Overview
description: Rights Management Services (RMS) is an information protection technology that helps safeguard digital information from unauthorized use.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'B546B6C1-ADC1-4EBD-95E2-B4A74E4E980B'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
---

# Overview

Rights Management Services (RMS) is an information protection technology that helps safeguard digital information from unauthorized use. Through your rights-enabled application, content owners will be able to define who can open, modify, print, forward, or take other actions with the content.

## Overview

RMS consists of both [server](ad-rms-server.md) and [client](ad-rms-client.md) components. The server, running on Azure or Windows Server, consists of multiple web services.

The [client](ad-rms-client.md) component can be run on either a client or server operating system and contains functions that enable an application to encrypt and decrypt content, retrieve templates and revocation lists, acquire licenses and certificates from a server, and other related rights management tasks.

For more information, see [Application types](application-types.md).

The following are just a few of the scenarios to which applications built on the Rights Management Services SDK 2.1 can be applied.

-   A law firm wants to prevent sensitive email messages from being printed or forwarded.
-   The developers of computer-aided design and manufacturing software want to limit drawing access to a small group of users within the research division without requiring the use of passwords.
-   The owners of a graphic design website want to use a single license that allows free viewing of low-resolution copies of their images but requires payment for access to the high-resolution versions.
-   The owners of an online document library want to enable rights to view, print, or edit documents based on the identity of the user.
-   A corporation wants to publish sensitive employee information to an internal website that restricts viewing and editing privileges to certain users.

For more information on Azure RMS, RMS server, RMS client and their functionality, see [IT Pro documentation for AD RMS](https://TechNet.Microsoft.Com/library/cc771234.aspx).

The remaining topics in this section cover the RMS Architecture and its implementations.

## In this section



| Topic                                  | Description                                                                                                |
|----------------------------------------|------------------------------------------------------------------------------------------------------------|
| [Client](ad-rms-client.md)<br/> | This topic describes the purpose and function of the Rights Management Service Client 2.1<br/>       |
| [Server](ad-rms-server.md)<br/> | This topic describes the purpose and functions of the RMS Server; for Azure and Windows Server.<br/> |



 

## Related topics

<dl> <dt>

[RMS Concepts](application-types.md)
</dt> <dt>

[Get started](getting-started-with-ad-rms-2-0.md)
</dt> <dt>

[IT Pro documentation for AD RMS](https://TechNet.Microsoft.Com/library/cc771234.aspx)
</dt> </dl>

 

 





