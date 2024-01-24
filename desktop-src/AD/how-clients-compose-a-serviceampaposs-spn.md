---
title: How Clients Compose a Service's SPN
description: To authenticate a service, a client application composes an SPN for the service instance to which it must connect.
ms.assetid: cf6c491a-d84d-4c9c-bd69-1f2264f395b6
ms.tgt_platform: multiple
keywords:
- How Clients Compose a Service's SPN AD
- service principal name AD , how clients compose a service's SPN
ms.topic: article
ms.date: 05/31/2018
---

# How Clients Compose a Service's SPN

To authenticate a service, a client application composes an SPN for the service instance to which it must connect. The client application can use the [**DsMakeSpn**](/windows/desktop/api/Dsparse/nf-dsparse-dsmakespna) function to compose an SPN. The client specifies the components of the SPN using known data or data retrieved from sources other than the service itself.

The form of an SPN is as shown in the following form:

```C++
<service class>/<host>:<port>/<service name>
```

In this form, "&lt;service class&gt;" and "&lt;host&gt;" are required. "&lt;port&gt;" and "&lt;service name&gt;" are optional.

Typically, the client recognizes the "&lt;service class&gt;" part of the name, and recognizes which of the optional components to include in the SPN. The client can retrieve components of the SPN from sources such as a service connection point (SCP) or user input. For example, the client can read the **serviceDNSName** attribute of a service's SCP to get the "&lt;host&gt;" component. The **serviceDNSName** attribute contains either the DNS name of the server on which the service instance is running or the DNS name of SRV records containing the host data for service replicas. The "&lt;service name&gt;" component, used only for replicable services, can be the distinguished name of the service's SCP, the DNS name of the domain served by the service, or the DNS name of SRV or MX records.

For more information and a code example used to compose an SPN for a service, see [How a Client Authenticates an SCP-based Windows Sockets Service](how-a-client-authenticates-an-scp-based-windows-sockets-service.md).

For more information and a description of the SPN components, see [Name Formats for Unique SPNs](name-formats-for-unique-spns.md).
