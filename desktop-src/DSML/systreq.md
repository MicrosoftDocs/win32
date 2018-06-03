---
title: System Requirements
description: The system requirements include a client computer running DSML V2, an Internet Information Services (IIS) server with DSML Services for Windows, and Active Directory or Active Directory Application Mode (ADAM).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 389e9408-f8eb-48ca-b276-33b954a75ef8
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- System Requirements DSML
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# System Requirements

DSML Services for Windows uses a three-tiered architecture. The system requirements include a client computer running DSML V2, an Internet Information Services (IIS) server with DSML Services for Windows, and Active Directory or Active Directory Application Mode (ADAM).

The detailed system requirements for the three tier components are:

-   Client computers running applications that use DSML V2

    These clients must be able to send HTTP requests and accept HTTP responses.

-   DSML Services for Windows, running on Microsoft Internet Information Services (IIS) 5.0 or later

    MSXML 4.0 Service Pack 1 or later must be installed on the IIS server.

-   Active Directory or Active Directory Application Mode (ADAM)

    Both DSML Services for Windows and Active Directory must be in the same Active Directory forest.

    If using DSML Services for Windows with ADAM instead of Active Directory, DSML Services for Windows and ADAM do not have to be in the same forest, or even be joined to a domain. However, if they are not in the same forest, then both DSML Services for Windows and ADAM should be run on the same computer, because IIS will use local accounts for authentication and would not be able to authenticate to ADAM using those local accounts if ADAM were on a separate computer.

All of these components can be installed on a single computer if the computer satisfies the system requirements for each of the components.

 

 




