---
title: Differences between LDAP 2 and LDAP 3
description: LDAP 3 defines a number of improvements that allow a more efficient implementation of the Internet directory user agent access model.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 0103829a-a562-4196-93b8-615cd4043b69
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
keywords:
- Differences between LDAP 2 and LDAP 3 LDAP
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Differences between LDAP 2 and LDAP 3

LDAP 3 defines a number of improvements that allow a more efficient implementation of the Internet directory user agent access model. These changes include:

-   Use of UTF-8 for all text string attributes to support extended character sets.
-   Operational attributes that the directory maintains for its own use; for example, to log the date and time when another attribute has been modified.
-   Referrals allow a server to direct a client to another server that may have the data that the client requested.
-   Schema publishing with the directory, allowing a client to discover the object classes and attributes that a server supports.
-   Extended searching operations to allow paging and sorting of results, and client-defined searching and sorting controls.
-   Stronger security through an SASL-based authentication mechanism.
-   Extended operations, providing additional features without changing the protocol version.

LDAP 3 is compatible with LDAP 2. An LDAP 2 client can connect to an LDAP 3 server (this is a requirement of an LDAP 3 server). However, an LDAP 3 server can choose not to talk to an LDAP 2 client if LDAP 3 features are critical to its application.

 

 




