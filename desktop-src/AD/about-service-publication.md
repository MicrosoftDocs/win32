---
title: About Service Publication
description: A service is an application that makes data or operations available to network clients. Often, a service is implemented as a formal Microsoft Win32-based service, but this is not required.
ms.assetid: 500f37ff-2551-44a0-91d8-56f0df5afa69
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# About Service Publication

A service is an application that makes data or operations available to network clients. Often, a service is implemented as a formal Microsoft Win32-based service, but this is not required.

Service publication is the act of creating and maintaining data about one or more instances of a given service so that network clients can find and use the service. Publishing a service in Active Directory Domain Services enables clients and administrators to move from a computer-centric view of the distributed system to a service-centric view.

**Microsoft Windows NT 3.51 and later operating systems:** A distributed system was a group of computers running various services. To access a service, an application required data about which computers offered the service.

**Windows 2000 Server, Windows 2000 Advanced Server and Windows 2000 Datacenter Server:** Services publish their existence using Active Directory Domain Services objects. The objects contain binding information that client applications use to connect to instances of the service. To access a service, a client does not need to know about specific computers: the objects in an Active Directory server include this information. A client queries the Active Directory server for an object representing a service (called a connection point object) and uses the binding data from the object to connect to the service.

The following table shows examples of bindings.



| Service      | Binding                                                                                                                                                                                                                     |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| File Service | UNC Name for a share. For example "\\\\MyServer\\MyshareName".                                                                                                                                                              |
| Web Service  | URL. For example "https://www.fabrikam.com".                                                                                                                                                                                 |
| RPC Service  | Remote procedure call (RPC) binding: special encoded information used to connect to the RPC server. RPC bindings can be converted to and from strings with the RPC APIs. For example: "ncacn\_ip\_tcp:server.fabrikam.com". |



 

In a distributed system, the computers are engines, and the interesting entities are the services that are available. From the user perspective, the identity of the computer that provides a particular service is not important. What is important is accessing the service itself.

This is also the case with service management. The administrator of a given DNS zone is not interested in the computers running the DNS service; the administrator wants to administer DNS. There will likely be multiple instances of the DNS service, one of which is authoritative. The computers that support DNS service are not important to the DNS administrator. What is important is how to manage the service as a single distributed resource—not as individual processes running on different computers.

 

 




