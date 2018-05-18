---
title: System Registry Provider
description: The System Registry provider enables management applications to retrieve and modify data in the system registry, and receive notifications when changes occur.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '39323619-82db-45d3-b20e-4ba1d4c11388'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["providers Windows Management Instrumentation , System Registry", "System Registry provider Windows Management Instrumentation"]
---

# System Registry Provider

The System Registry provider enables management applications to retrieve and modify data in the system registry, and receive notifications when changes occur. The registry can be located on a local or remote computer. The [**\_Win32Provider**](https://msdn.microsoft.com/library/aa394688) instance name is "RegProv"; the property provider name is "RegPropProv"; and the event provider name is "RegistryEventProvider". For more information, see [Modifying the System Registry](https://msdn.microsoft.com/library/aa392388).

The provider has the following [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688) instances:

-   "RegProv"
-   "RegistryEventProvider"
-   "RegPropProv"

Two versions of the System Registry provider are available on 64-bit platforms. For more information, see [Getting and Providing Data on a 64-bit Computer](https://msdn.microsoft.com/library/aa390789).

## System Registry Provider

The System Registry providers allows you to subscribe to registry events, including changes in a subtree, key, or value. For more information, see topics under [Registering for System Registry Events](https://msdn.microsoft.com/library/aa393035) and [Receiving a WMI Event](https://msdn.microsoft.com/library/aa393013).The System Registry provider supports the following classes located in the **Root\\Default** namespace:



| Event class                                                  | Description                                                             |
|--------------------------------------------------------------|-------------------------------------------------------------------------|
| [**RegistryEvent**](registryevent.md)                       | Abstract class from which the other registry event classes are derived. |
| [**RegistryKeyChangeEvent**](registrykeychangeevent.md)     | Represents changes to a specific registry key.                          |
| [**RegistryTreeChangeEvent**](registrytreechangeevent.md)   | Represents changes to a specific key or its subkeys.                    |
| [**RegistryValueChangeEvent**](registryvaluechangeevent.md) | Represents changes to a single value of a specific key.                 |
| [**StdRegProv**](stdregprov.md)                             | Contains methods that manipulate system registry keys and values.       |



 

As an instance, property, and event provider, the System Registry provider supports the standard [**IWbemProviderInit**](https://msdn.microsoft.com/library/aa391853) interface, and the following [**IWbemServices**](https://msdn.microsoft.com/library/aa392093) methods:

-   [**CreateInstanceEnumAsync**](https://msdn.microsoft.com/library/aa392098)
-   [**ExecMethodAsync**](https://msdn.microsoft.com/library/aa392104)
-   [**ExecNotificationQueryAsync**](https://msdn.microsoft.com/library/aa392106)
-   [**ExecQueryAsync**](https://msdn.microsoft.com/library/aa392108)
-   [**GetObjectAsync**](https://msdn.microsoft.com/library/aa392110)
-   [**PutInstanceAsync**](https://msdn.microsoft.com/library/aa392116)

## StdRegProvider Class

The [**StdRegProv**](stdregprov.md) class is placed in the **Root\\Default** namespace by WMI. You can compile the Managed Object Format (MOF) file that defines the provider into another namespace for use by your applications. RegEvent.mof is the .mof file name.

[**StdRegProv**](stdregprov.md) contains only methods. You cannot create or get an instance of **StdRegProv**. The [**Win32\_Registry**](https://msdn.microsoft.com/library/aa394394) class contains configuration data about the registry. The only registry configuration you can change through WMI is the **ProposedSize** property.

## Related topics

<dl> <dt>

[WMI Providers](https://msdn.microsoft.com/library/aa394570)
</dt> </dl>

 

 




