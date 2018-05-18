---
title: Network Address Translation Traversal Interfaces
description: The following interfaces make it possible to manage Network Address Translation (NAT) through UPnP™.
ms.assetid: 'bf14d633-4b91-4570-b4c9-fd524923914a'
keywords: ["Network Address Translation Traversal Interfaces ICS/ICF"]
---

# Network Address Translation Traversal Interfaces

The following interfaces make it possible to manage Network Address Translation (NAT) through UPnP™.



| Interface                                                            | Purpose                                                               |
|----------------------------------------------------------------------|-----------------------------------------------------------------------|
| [**IUPnPNAT**](iupnpnat.md)                                         | Primary interface for UPnP management of NAT.                         |
| [**INATEventManager**](inateventmanager.md)                         | Provides methods to register application-defined callback interfaces. |
| **IDynamicPortMappingCollection**                                    | This interface is not currently supported.                            |
| **IDynamicPortMapping**                                              | This interface is not currently supported.                            |
| [**IStaticPortMappingCollection**](istaticportmappingcollection.md) | Collection interface for static port mappings.                        |
| [**IStaticPortMapping**](istaticportmapping.md)                     | Provides methods for managing a specific port mapping.                |



 

The following interfaces are implemented by the client application. The NAT calls the methods in these interfaces in order to inform the client of changes in the NAT configuration.



| Interface                                                              | Purpose                                                                           |
|------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| [**INATExternalIPAddressCallback**](inatexternalipaddresscallback.md) | Provides a method that the system calls if the NAT's external IP address changes. |
| [**INATNumberOfEntriesCallback**](inatnumberofentriescallback.md)     | Provides a method that the system calls if the number of port mappings changes.   |



 

 

 




