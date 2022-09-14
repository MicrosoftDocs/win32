---
description: The three types of namespaces in the Windows Sockets (Winsock) SPI include dynamic, static, and persistent namespaces.
ms.assetid: 2968ac98-bd40-4d37-9dd7-7870c4decd40
title: Types of Namespaces in the SPI
ms.topic: article
ms.date: 05/31/2018
---

# Types of Namespaces in the SPI

There are three different types of namespaces in which a service could be registered:

-   Dynamic
-   Static
-   Persistent

Dynamic namespaces allow services to register with the namespace on the fly, and for clients to discover the available services at run time. Dynamic namespaces frequently rely on broadcasts to indicate the continued availability of a network service. Examples of dynamic namespaces include the SAP namespace used within a NetWare environment and the NBP namespace used by AppleTalk.

Static namespaces require all of the services to be registered ahead of time, that is, when the namespace is created. The DNS is an example of a static namespace. Although there is a programmatic way to resolve names, there is no programmatic way to register names.

Persistent namespaces allow services to register with the namespace on the fly. Unlike dynamic namespaces however, persistent namespaces retain the registration information in nonvolatile storage where it remains until such time as the service requests that it be removed. Persistent namespaces are typified by directory services such as X.500 and the NDS (NetWare Directory Service). These environments allow the adding, deleting, and modification of service properties. In addition, the service object representing the service within the directory service could have a variety of attributes associated with the service. The most important attribute for client applications is the service's addressing information.

 

 



