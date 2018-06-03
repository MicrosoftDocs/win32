---
title: Modifying a Directory Entry
description: You can use the LDAP API to add and delete directory entries and to compare and modify values within existing entries.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: ad7be3a1-663c-489e-8eb3-1aea910ee366
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
keywords:
- Modifying a Directory Entry
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Modifying a Directory Entry

You can use the LDAP API to add and delete directory entries and to compare and modify values within existing entries. Any of these operations can be performed either [synchronously or asynchronously](synchronous-vs--asynchronous-calls.md). Effective with LDAP 3, extensions to the add, delete, and modify functions enable you to perform these operations using controls. For more information, see [Using Controls](using-controls.md).

**To make a change to a directory**

1.  Create an [**LDAPMod**](/previous-versions/windows/desktop/api/Winldap/ns-winldap-ldapmoda) structure, assigning the appropriate values to each member of the structure.

    For multiple changes, or to add an entry, create a separate **LDAPMod** structure for each attribute or change.

2.  Pass these structures as an array when you call the modification function.

## Ramifications of User Account Control

The introduction of User Account Control in Windows Server 2008 and Windows Vista has a very important consequence with regard to making modifications or additions in LDAP. When a user is logged on to a DC with a restricted UAC Administrator token and using **NULL** credentials, any modification or addition to the directory, or any schema change operation, will fail. This includes DirSync searches, retrieving the SACL from an object's [**ntSecurityDescriptor**](https://msdn.microsoft.com/library/ms679006) attribute when using SecurityDescriptorFlags, and many other operations. These will all fail with insufficient access rights. To work around this, either run the command from an elevated-credential command prompt or use explicit credentials.

 

 




