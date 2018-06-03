---
title: Using Application Directory Partitions
description: Application data should be stored in one or more application directory partitions in AD LDS.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: f75a07fc-6371-4a6b-b901-1a675ba80948
ms.prod: windows-server-dev
ms.technology: active-directory-application-mode
ms.tgt_platform: multiple
keywords:
- Using Application Directory Partitions ADAM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using Application Directory Partitions

Application data should be stored in one or more application directory partitions in AD LDS. Although the installation process for the first AD LDS instance in a configuration set creates a schema directory partition and a configuration directory partition for the configuration set, creating the application directory partition at installation time is optional.

You can use the same process in AD LDS as you would in Active Directory to programmatically create and delete an application directory partition. For more information about how create an application directory partition, including example code, see [Application Directory Partitions](https://msdn.microsoft.com/library/ms675020).

 

 




