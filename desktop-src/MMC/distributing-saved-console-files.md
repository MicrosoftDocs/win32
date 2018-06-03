---
title: Distributing Saved Console Files
description: Provides a mechanism for distributing saved console files.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 45291ec4-f2a1-4d45-9598-3ea0d3d29390
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Distributing Saved Console Files

If you are running only on Windows operating systems with an Active Directory directory service enabled, the Windows Installer information in the previous section allows you to distribute only the saved console files that you are interested in. The snap-ins referenced in those saved console files are downloaded automatically. This also allows you to wrap your saved console files in a Windows Installer package and assign them to users. Alternatively, you can leave your saved console files on a shared network drive and have all users gain access to them from there; this might make updates to the saved console files easier.

If you must support a mixed environment where Windows Server application deployment is not available, then you should include the saved console files in the Windows Installer package that includes your snap-ins. In this case, ensure that all snap-ins referenced in the saved console file are locally installed before the user opens the file.

 

 




