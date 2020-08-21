---
title: Remote Desktop Services WMI provider
description: The Remote Desktop Services WMI provider provides programmatic access to the information and settings that are exposed by the Remote Desktop Services Configuration/Connections Microsoft Management Console (MMC) snap-in.
ms.assetid: d205a3da-3f9a-4ee1-9c99-a39e9cce0a11
ms.tgt_platform: multiple
keywords:
- Remote Desktop Services Remote Desktop Services , WMI provider
ms.topic: article
ms.date: 05/31/2018
---

# Remote Desktop Services WMI provider

The Remote Desktop Services WMI provider provides programmatic access to the information and settings that are exposed by the Remote Desktop Services Configuration/Connections Microsoft Management Console (MMC) snap-in.

The provider DLL is loaded by the Windows Management process (Winmgmt.exe) when a client makes a request to the server. Administration is possible by using the provider methods. The provider is registered as both an instance and a method provider.

The Remote Desktop Services WMI provider has been implemented as a dynamic provider derived from the [**Win32\_Service**](/windows/desktop/CIMWin32Prov/win32-service) base class, inheriting all of its properties and methods, and an in-process dynamic link library.

For more information, see the [Remote Desktop Services WMI Provider reference](terminal-services-wmi-provider-reference.md).

## Related topics

<dl> <dt>

[Remote Desktop Services WMI Provider Reference](terminal-services-wmi-provider-reference.md)
</dt> </dl>

 

 