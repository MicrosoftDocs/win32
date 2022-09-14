---
title: Users in Active Directory Domain Services
description: Active Directory Domain Services includes a directory service that stores domain, user, user group, and security data.
ms.assetid: 7630fde1-14c0-4518-bb77-813f6913503e
ms.tgt_platform: multiple
keywords:
- Users in Active Directory Domain Services Active Directory
- users, active directory domain services
- active directory domain services, users
ms.topic: article
ms.date: 05/31/2018
---

# Users in Active Directory Domain Services

Active Directory Domain Services includes a directory service that stores domain, user, user group, and security data.

On Windows NT 4.0 and earlier, you can use functions such as [**NetUserAdd**](/windows/desktop/api/lmaccess/nf-lmaccess-netuseradd), [**NetUserEnum**](/windows/desktop/api/lmaccess/nf-lmaccess-netuserenum), [**NetUserDel**](/windows/desktop/api/lmaccess/nf-lmaccess-netuserdel), and so on, to manage users, user groups, and other network items. On Windows 2000 and later versions of Windows, ADSI provides uniform and secure access to these items and their properties. Be aware that ADSI provides a Windows NT 4.0 provider that enables you to use ADSI to manage user, user groups, and computers on Windows NT 4.0 systems. There are also providers for Windows Server 2008 Enterprise (Server Core installation), Microsoft Exchange 5.5, Microsoft Internet Information Server (IIS), Novell NetWare Directory Services (NDS), and Novell NetWare 3. That is, a single set of standardized methods for managing users and user groups for Windows NT, NDS, and NetWare 3.

In addition, Windows 2000 is a multi-master directory. That is, changes to users, user groups, and other data stored in the directory can be made at any domain controller. On Windows 2000, you are not required to locate the primary domain controller (PDC) and make user and user group changes on the PDC.

Windows 2000 also introduces a new hierarchical namespace within a domain called an organizational unit (OU). An OU can contain computers, users, user groups, and other network objects. Usually, an OU is used for the purpose of grouping things for administrative purposes, such as delegating administrative rights and assigning policies to the group as a single unit.

Domains, OUs, users, user groups, computers, and other network items are stored as objects in Active Directory Domain Services. In Windows 2000 and later versions of Windows, you still add users, user groups, and computers to a domain. However, you now have the option of adding these objects to an OU container or any other type of container that the object you want to add defines in its **classSchema** object's **possSuperiors** attribute; this is an attribute on an object's **classSchema** object and this attribute restricts what types of objects can contain that object.

 

 