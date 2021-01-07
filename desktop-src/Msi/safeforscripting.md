---
description: If this per-machine system policy is set to &\#0034;1&\#0034;, the installer does not prompt users when scripts within a Web page use the installer's automation interface.
ms.assetid: 1365996d-30a2-43f9-8e1b-7704d46a11c9
title: SafeForScripting
ms.topic: article
ms.date: 05/31/2018
---

# SafeForScripting

If this per-machine [system policy](system-policy.md) is set to "1", the installer does not prompt users when scripts within a Web page use the installer's [automation interface](automation-interface.md).

Before setting this policy, you should consider whether foregoing the user prompt provides an appropriate level of security for your users. If this policy is not set, when a script hosted by an Internet browser tries to install an application, the system warns the user and asks them to accept or refuse the installation. Setting SafeForScripting suppresses this warning and may allow the installation of applications on the system without the user's knowledge. This policy may be useful for an enterprise that uses web-based tools to distribute programs.

For more information, see [Guidelines for Authoring Secure Installations](guidelines-for-authoring-secure-installations.md) and [Digital Signatures and Windows Installer](digital-signatures-and-windows-installer.md) and [Downloading an Installation from the Internet](downloading-an-installation-from-the-internet.md).

## Registry Key

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Policies**\\**Microsoft**\\**Windows**\\**Installer**

## Data Type

**REG\_DWORD**

 

 



