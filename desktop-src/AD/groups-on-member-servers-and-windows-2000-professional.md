---
title: Groups on Member Servers and Windows 2000 Professional
description: On member servers and computers running on Windows 2000 Professional, there is a local security database.
ms.assetid: 17a651e2-3650-4e12-b17e-badd3d479515
ms.tgt_platform: multiple
keywords:
- Groups on Member Servers and Windows 2000 Professional AD
- groups AD , groups on member servers and Windows 2000 Professional
ms.topic: article
ms.date: 05/31/2018
---

# Groups on Member Servers and Windows 2000 Professional

On member servers and computers running on Windows 2000 Professional, there is a local security database. This local security database can contain its own local user and local groups whose scope is only the particular computer where they are created. When managing these types of users and groups on member servers and computers running on Windows NT Workstation or Windows 2000 Professional, use the WinNT provider.

When a member server or a computer running on Windows 2000 Professional or Windows 2000 Professional is a member of a Windows 2000 domain, the groups or users in the domain can be used in the local security database to grant rights to that group on that particular computer.

When managing groups on a Windows 2000 domain using ADSI, use the LDAP provider. When managing groups on member servers and computers running on Windows NT Workstation or Windows 2000 Professional, use the WinNT provider.

You must bind, at least one instance, to each provider: 1) Bind to the LDAP provider to retrieve the ADsPath to the group or user you want to add to a group in the local database and 2) Bind to the WinNT provider to add that user or group to a local group.

 

 




