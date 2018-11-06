---
title: Security Principals
description: In Windows 2000, a security principal is a user, group, or computer \ 8212; an entity that the security system recognizes.
ms.assetid: 213ee563-35cd-43d2-abb2-f66652df5be1
ms.tgt_platform: multiple
keywords:
- security principals AD
ms.topic: article
ms.date: 05/31/2018
---

# Security Principals

In Windows 2000, a security principal is a user, group, or computer — an entity that the security system recognizes. This includes human users as well as autonomous processes. Strictly speaking, the security system cannot tell the difference between users who are logged in and processes running on the computer. It sees both as security principals with security principal names.

Users, groups, and computers are created and stored as objects in Active Directory Domain Services. There are also well-known security principals that represent special identities defined by the Windows 2000 security system, such as Everyone, Local System, Principal Self, Authenticated User, Creator Owner, and so on. Objects representing the well-known security principals, such as Anonymous Logon, are stored in the WellKnown Security Principals container beneath the Configuration container.

 

 




