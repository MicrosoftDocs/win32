---
description: The system registry contains configuration data that the operating system, services, and applications use.
ms.assetid: e16a5d4c-46a0-4798-894d-0af4cfa18f22
ms.tgt_platform: multiple
title: Modifying the System Registry
ms.topic: article
ms.date: 05/31/2018
---

# Modifying the System Registry

The system registry contains configuration data that the operating system, services, and applications use. Windows Management Instrumentation (WMI) has a [System Registry Provider](/previous-versions/windows/desktop/regprov/system-registry-provider) and the [**StdRegProv**](/previous-versions/windows/desktop/regprov/stdregprov) class with methods that use to monitor or modify the registry on the local computer or remote computers. The [Win32 Provider](/windows/desktop/CIMWin32Prov/win32-provider) supports the [**Win32\_Registry**](/windows/desktop/CIMWin32Prov/win32-registry) class that contains static data about the size of a registry.

The System Registry Provider is an instance, property, and event provider that interfaces with the system registry. The System Registry Provider is a standard provider with the [**IWbemServices**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices) interface. You can use the System Registry Provider to access registry keys and information on local and remote systems. For more information, see [System Registry Provider](/previous-versions/windows/desktop/regprov/system-registry-provider).

WMI places the [**StdRegProv**](/previous-versions/windows/desktop/regprov/stdregprov) in the root\\default namespace. However, you can compile the Regevent.mof file into other namespaces for other applications to use.

The topics identified in the following table can show you how to use the [**StdRegProv**](/previous-versions/windows/desktop/regprov/stdregprov) class and the System Registry Provider.



| Topic                                                                                              | Description                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Obtaining Registry Data](obtaining-registry-data.md)                                             | You can obtain or modify registry data through methods of the [**StdRegProv**](/previous-versions/windows/desktop/regprov/stdregprov) class, which allows you to automate registry activities locally or remotely.                    |
| [Changing Registry Data](changing-registry-data.md)                                               | You can add or delete keys, and add or change registry entry values under keys.                                                                                                                    |
| [Programming with the System Registry Provider](programming-with-the-system-registry-provider.md) | You can define your own classes that the System Registry supplies with data.                                                                                                                       |
| [Registering for System Registry Events](registering-for-system-registry-events.md)               | The System Registry provider can send events to a consumer. To receive events, you must register your consumer, create a query, and then ensure that the provider is sending you events—correctly. |
| [Registering the System Registry Provider](registering-the-system-registry-provider.md)           | The System Registry provider is registered as part of the WMI installation process.                                                                                                                |



 

 

 
