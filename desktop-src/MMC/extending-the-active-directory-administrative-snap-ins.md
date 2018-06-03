---
title: Extending the Active Directory Administrative Snap-ins
description: Microsoft Management Console (MMC) snap-in customization can extend the following Active Directory extension snap-ins (provided as part of Windows Server)
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7fe80c33-bc73-4f84-9fe9-43cd922c130d
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Microsoft Management Console MMC ,extending the Active Directory administrative snap-ins
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Extending the Active Directory Administrative Snap-ins

Microsoft Management Console (MMC) snap-in customization can extend the following Active Directory extension snap-ins (provided as part of Windows Server):

-   Active Directory Users and Computers
-   Active Directory Sites and Services
-   Active Directory Domains and Trusts

The Active Directory Schema Manager snap-in cannot be extended by snap-ins.

Extension snap-ins to the Active Directory administration snap-ins can extend the following user interface features available in MMC:

-   Scope pane tree view
-   Context menus
-   Property sheets
-   Taskpads
-   Toolbars
-   Menu buttons

Be aware that the Active Directory administrative snap-ins also provide some user interface elements that can be extended by an extension mechanism other than the MMC extension mechanism. For more information, see [About the User Interfaces of Active Directory Domain Services](https://msdn.microsoft.com/library/aa772143).

For detailed information about extending the Active Directory Users and Computers snap-in, see [Extending the Active Directory Users and Computers Snap-in](extending-the-active-directory-users-and-computers-snap-in.md).

The following topics provide information related to Active Directory MMC snap-in development.

-   [Extendable Node Types](extendable-node-types.md)
-   [**CFSTR\_DSOBJECTNAMES Clipboard Format**](cfstr-dsobjectnames-clipboard-format.md)

 

 




