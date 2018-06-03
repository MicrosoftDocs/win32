---
title: Registering a Snap-in for an Optional Service
description: A service is considered optional if it may or may not be installed on a target machine.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: eb5955b0-41c4-480c-925a-50e7f0a2f2e6
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Registering a Snap-in for an Optional Service

A service is considered optional if it may or may not be installed on a target machine. A design goal of the Computer Management snap-in is to list an optional service under the **Services and Applications** node only if the service is installed. In other words, the snap-in for an optional service should appear under the **Services and Applications** node in the Computer Management snap-in only if the service (not just the service's snap-in) is installed. To satisfy the intended Computer Management user experience, the snap-in for an optional service must extend the **Services and Applications** node. Be aware that only dynamic extensions should extend the **Services and Applications** node type, and only in the manner described here. When using a snap-in to manage an optional service, follow these Steps:

1.  During installation of your service, register your snap-in CLSID as a value under the following key:

    **HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Control\\Server Applications**

    The name of the value is **{***snapinCLSID***}**, where *snapinCLSID* is the class identifier for your extension. The value type should be REG\_SZ, and the value data should be a description of your snap-in.

    Be aware that you should add the registry value only when the service (not the service's snap-in) is installed.

2.  During installation of the service's snap-in, register the service's snap-in as an extension. For more information about registering your service's snap-in as an extension, see [Registration Requirements for Extension Snap-ins](registration-requirements-for-extension-snap-ins.md).

    Also, register your service's snap-in as a dynamic extension for the **Services and Applications** node type, by adding your snap-in CLSID as a value under the following key:

    **HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\MMC\\NodeTypes\\{476E6449-AAFF-11D0-B944-00C04FD8D5B0}\\Dynamic Extensions**

    The name of the value is **{***snapinCLSID***}**, where *snapinCLSID* is the class identifier of your extension (the same value used in Step 1 above). The value type should be REG\_SZ, and the value data should be a description of your snap-in.

## Note

When your extension is uninstalled, remove registry values added for the extension during installation.

To have your snap-in automatically installed, you can register your snap-in with the Class Store for every domain. The Class Store will download your snap-in to a target machine where it is not already installed. For more information, see [**Publishing COM+ Services**](https://msdn.microsoft.com/library/ms677635).

 

 




