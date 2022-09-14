---
title: Service Connection Points for Replicated, Host-based, and Database Services
description: When you publish a service using a service connection point (SCP), consider how clients will locate the SCP for your service.
ms.assetid: 944e8ecd-f8ea-4506-992c-bbbfc82d11f3
ms.tgt_platform: multiple
keywords:
- Service Connection Points for Replicated, Host-based, and Database Services AD
ms.topic: article
ms.date: 05/31/2018
---

# Service Connection Points for Replicated, Host-based, and Database Services

When you publish a service using a service connection point (SCP), consider how clients will locate the SCP for your service. If multiple instances of the service exist, consider how clients will distinguish the service with the desired features from similar services with different features. If you publish a replicated service, consider how a client will choose a replica. This topic discusses these issues for various types of services.

## Replicable services

For a replicable service there can be one or many instances, or replicas, of the service, and clients do not care which replica they connect to because each provides the same service. Active Directory Domain Services are examples of replicated services: all domain controllers for a given domain hold identical data, subject to replication latency, and provide identical services.

Replicable services can store the SCPs and other service-specific objects for multiple replicas in a single container. The setup application for the first replica can create the container as a child of the local domain's System container. For more information, see [Publishing in a Domain System Container](publishing-in-a-domain-system-container.md). Ensure that the security descriptor for your container allows the setup programs for subsequent replicas to create their objects in the same container. Grant permissions for the installing administrator to specify the users or groups that can create or modify objects in the container.

One strategy for a replicable service is to create an SCP for each replica. When a client queries for the service's product GUID or other identifying keyword, it finds the SCP objects for all replicas and selects one at random or using some load-balancing algorithm. For example, an administrator could specify priority and load-balancing data for each replica, similar to the priority and weight fields of a DNS SRV record. The service's setup application can store this data in the **serviceBindingInformation** attribute of each replica's SCP. Clients retrieve the data from each SCP and use it to select a replica.

Another strategy is to create a single SCP for all replicas and set the SCP **serviceDNSName** attribute to the name of a DNS SRV record. Then the setup application for each replica registers a SRV record with that name. When a client identifies the service's lone SCP, the client retrieves the name of the SRV record and uses the [**DnsQuery**](/windows/desktop/api/windns/nf-windns-dnsquery_a) function to retrieve the array of SRV records for the replicas. Each SRV record contains the name of a host computer and additional data that the client can use to select a replica.

## Database services

Different instances of a database service may contain entirely different data, even though they are all the same kind of service, usually called service class. To publish this kind of service, the **keywords** attribute of the SCP can identify both the service class and the specific database. A general-purpose client that knows only the GUID of the service class can query for all databases published by that service class, and then present a user interface to allow the user to select one. For a client that is designed specifically for the target database, you can hard-code the database GUID into the client code.

## Host-based services

Host-based services are services that are closely tied to a single host computer. You can install instances of the service class on many computers and each instance provides services that are identified with its host computer.

Each instance of a host-based service should create its own SCP under the computer object of its host. Clients who use a product GUID to search for the SCP of a host-based service typically find many instances of the service class throughout the enterprise forest. Clients can then use the **serviceDNSName** attribute of the SCPs to find the SCP for the service instance on the desired host computer.

 

 