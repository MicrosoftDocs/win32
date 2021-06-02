---
description: Starting with Windows Server 2008, the Server Feature Provider supplies information on what server features are installed on the server. This class allows administrators to inventory and manage their server roles and features.
ms.assetid: f7932eaa-6730-4301-9809-32de9c1a20de
ms.tgt_platform: multiple
title: Server Feature Provider
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Server Feature Provider

Starting with Windows Server 2008, the Server Feature Provider supplies information on what server features are installed on the server. This class allows administrators to inventory and manage their server roles and features.

A server role is defined as a group of components that provide functions for a specific area of functionality, such as printing, files, domain control, and so on. Typical server roles are File Server, Mail Server, DNS Server, Domain Controller, Application Server, and so on.

If an enterprise is not running management software that reports server roles, such as Microsoft Operations Manager with management packs installed, then you can obtain that information by querying the [**Win32\_ServerFeature**](win32-serverfeature.md) class. Server role and feature information from remote computers is available through normal WMI remote connections or by using the Windows Remote Management (WinRM) service. For more information about remote WMI DCOM connections, see [Connecting to WMI on a Remote Computer](connecting-to-wmi-on-a-remote-computer.md). For more information about connections using the [*WS-Management*](/windows/desktop/WinRM/windows-remote-management-glossary) protocol, see [Windows Remote Management](/windows/desktop/WinRM/portal).

The Server Feature Provider supports the following WMI classes:

-   [**Win32\_ServerFeature**](win32-serverfeature.md)

## Related topics

<dl> <dt>

[WMI Providers](wmi-providers.md)
</dt> </dl>

 

 
