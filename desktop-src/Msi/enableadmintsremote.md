---
description: Beginning with Windows Server 2008 and Windows Vista, this policy no longer has any effect.
ms.assetid: 27a4192e-0574-414d-993e-6c715577f0ba
title: EnableAdminTSRemote
ms.topic: article
ms.date: 05/31/2018
---

# EnableAdminTSRemote

Beginning with Windows Server 2008 and Windows Vista, this policy no longer has any effect. An administrator can perform an installation from the console session of a terminal server. An administrator can also perform an installation from a client session of the terminal server.

For more information, see [Terminal Services](/windows/desktop/TermServ/terminal-services-portal) in the Microsoft Windows Software Development Kit (SDK).

**Operating systems earlier than Windows Server 2008 and Windows Vista:  **

Setting this per-machine [system policy](system-policy.md) enables administrators to perform installations from a client session of the terminal server. If this policy is not set, administrators can only perform installations from the console session. Nonadministrative users can never perform installations from a client session. The default value for this policy allows only administrators to perform installations from the console session. Administrators can always do [Administrative installations](administrative-installation.md) from a client session of the terminal server, or from the console session, regardless of whether this policy is set.

## Registry Key

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Policies**\\**Microsoft**\\**Windows**\\**Installer**

## Data Type

**REG\_DWORD**

## Remarks

For more information see also, [Using Windows Installer with a Terminal Server](using-windows-installer-with-a-terminal-server.md).

 

 
