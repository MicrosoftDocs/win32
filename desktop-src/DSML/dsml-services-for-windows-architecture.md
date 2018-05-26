---
title: DSML Services for Windows Architecture
description: DSML Services for Windows runs as a module on a server running Internet Information Services (IIS) version 5.0 or later.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 150d306a-6c9e-422f-9ed8-ce0acbbc47ac
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- DSML Services for Windows Architecture DSML
- DSML Services for Windows, architecture
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DSML Services for Windows Architecture

[*DSML Services for Windows*](glossary.md#dsml-services-for-windows) runs as a module on a server running Internet Information Services (IIS) version 5.0 or later. It uses [*SOAP*](glossary.md#simple-object-access-protocol) over HTTP to transmit and receive directory requests from client computers. DSML Services for Windows translates the client computer's [*DSML V2*](glossary.md#dsmlv2) requests from XML into LDAP commands. The LDAP commands are used to query the domain controllers in the Active Directory forest or on an Active Directory Application Mode (ADAM) server.

The following topics provide more detail on DSML Services for Windows architecture:

-   [DSML Services for Windows and LDAP](dsml-services-for-windows-and-ldap.md)
-   [DSML Services for Windows Standard Binding Methods](dsml-services-for-windows-standard-binding-methods.md)
-   [DSML Services for Windows Session Support](dsml-services-for-windows-session-support.md)

 

 




