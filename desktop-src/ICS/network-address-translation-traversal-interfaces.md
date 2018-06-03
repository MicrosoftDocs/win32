---
title: Network Address Translation Traversal Interfaces
description: The following interfaces make it possible to manage Network Address Translation (NAT) through UPnP™.
ms.assetid: bf14d633-4b91-4570-b4c9-fd524923914a
keywords:
- Network Address Translation Traversal Interfaces ICS/ICF
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Network Address Translation Traversal Interfaces

The following interfaces make it possible to manage Network Address Translation (NAT) through UPnP™.



| Interface                                                            | Purpose                                                               |
|----------------------------------------------------------------------|-----------------------------------------------------------------------|
| [**IUPnPNAT**](/previous-versions/windows/desktop/api/Natupnp/nn-natupnp-iupnpnat)                                         | Primary interface for UPnP management of NAT.                         |
| [**INATEventManager**](/previous-versions/windows/desktop/api/Natupnp/nn-natupnp-inateventmanager)                         | Provides methods to register application-defined callback interfaces. |
| **IDynamicPortMappingCollection**                                    | This interface is not currently supported.                            |
| **IDynamicPortMapping**                                              | This interface is not currently supported.                            |
| [**IStaticPortMappingCollection**](/previous-versions/windows/desktop/api/Natupnp/nn-natupnp-istaticportmappingcollection) | Collection interface for static port mappings.                        |
| [**IStaticPortMapping**](/previous-versions/windows/desktop/api/Natupnp/nn-natupnp-istaticportmapping)                     | Provides methods for managing a specific port mapping.                |



 

The following interfaces are implemented by the client application. The NAT calls the methods in these interfaces in order to inform the client of changes in the NAT configuration.



| Interface                                                              | Purpose                                                                           |
|------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| [**INATExternalIPAddressCallback**](/previous-versions/windows/desktop/api/Natupnp/nn-natupnp-inatexternalipaddresscallback) | Provides a method that the system calls if the NAT's external IP address changes. |
| [**INATNumberOfEntriesCallback**](/previous-versions/windows/desktop/api/Natupnp/nn-natupnp-inatnumberofentriescallback)     | Provides a method that the system calls if the number of port mappings changes.   |



 

 

 




