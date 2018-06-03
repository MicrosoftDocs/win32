---
title: Why Use Active Directory Lightweight Directory Services
description: Active Directory Lightweight Directory Services (AD LDS) has both functional benefits and operational benefits for developers who create or adapt directory-enabled applications.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 93169df7-cf07-4948-ab83-6c24fdf2ddb9
ms.prod: windows-server-dev
ms.technology: active-directory-application-mode
ms.tgt_platform: multiple
keywords:
- AD LDS ADAM , benefits of
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Why Use Active Directory Lightweight Directory Services?

Active Directory Lightweight Directory Services (AD LDS) has both functional benefits and operational benefits for developers who create or adapt directory-enabled applications.

## Functional Benefits of AD LDS

Developers using AD LDS have access to the following functional benefits:

-   AD LDS uses the same directory service technology as Active Directory. This means there is a common framework for both the network operating system (NOS) services of Active Directory and the application services of AD LDS.
-   Use of the same directory service technology increases reusability of design and code between Active Directory and AD LDS.
-   AD LDS increases the scalability of directory services by separating the NOS services from the application services.
-   Multiple instances of AD LDS, each designed for a specific application, can run on a single AD LDS installation.
-   Each AD LDS configuration set has a separate schema, independent of the Active Directory schema.
-   AD LDS can use X.500-style naming contexts, such as O=Fabrikam and C=US.
-   To increase application security, AD LDS can use Windows security principals for authentication and access control.
-   Development for AD LDS can occur on Professional, Business, Enterprise, and Ultimate SKUs as well as on the Windows Server operating systems.

## Operational Benefits of AD LDS

Developers using AD LDS have access to the following operational benefits:

-   AD LDS is easy to deploy. Installation and setup are simple.
-   AD LDS can be installed without affecting Active Directory.
-   AD LDS can be reinstalled or restarted without a restart.
-   AD LDS uses the same administrative model as Active Directory.
-   AD LDS increases reliability by separating application directory services from NOS directory services.

 

 




