---
Description: 'HPC uses HPC sessions to support the service-oriented architecture (SOA) programming model based on Windows Communication Foundation (WCF).'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '02acd324-6a7c-427d-84d6-b157144f8f2c'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'Using HPC Sessions to Run SOA-based Applications in Windows HPC Server 2008'
---

# Using HPC Sessions to Run SOA-based Applications in Windows HPC Server 2008

HPC uses HPC sessions to support the service-oriented architecture (SOA) programming model based on [Windows Communication Foundation](http://go.microsoft.com/fwlink/p/?linkid=122573) (WCF). The SOA programming model is ideal for writing interactive, embarrassingly parallel applications that provide near real-time calculation of complex algorithms, such as Monte Carlo simulations and BLAST searches.

The parts of an HPC session are the SOA client, the HPC session, and the SOA service. The following describes the basic flow of an HPC session:

-   The client application creates an HPC session that it uses to communicate with the service.
-   The scheduler creates a broker and service job for the session and assigns an endpoint reference (EPR) for the broker.
-   The client binds to the EPR.
-   The client posts requests.
-   The broker sends requests to instances of the service job and receives responses from the instances.
-   The broker returns the responses to the client.

The broker job runs on a broker node in the cluster and is responsible for routing requests from the client application to the service (which is why the client binds to the EPR for the broker, not the service). The client sends all requests to the broker, which in turn load balances and sends the requests to the service instances.

The broker creates and manages a pool of instances of the service job that process the requests from the client. The service instances run on one or more compute nodes in the cluster; the number of nodes can grow and shrink based on the level of incoming requests from the client application. When a service request completes, the broker returns the response back to the client application.

Typically, you need to access the broker and service jobs only if you are trying to diagnose a problem. However, you may need to access the broker job if you want to share an existing session (see [Using a Shared HPC Session](using-a-shared-hpc-session.md)).

Building an application based on SOA consists of the following steps:

1.  [Creating a SOA Service](creating-a-soa-service.md)
2.  [Deploying a SOA Service](deploying-a-soa-service.md)
3.  [Creating a SOA Client](creating-a-soa-client.md)

 

 



