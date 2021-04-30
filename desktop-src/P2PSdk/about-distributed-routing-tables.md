---
description: A Distributed Routing Table (DRT) exists as a mesh of cooperating nodes, where each node is an instance of an application using the DRT API.
ms.assetid: 257ad7ea-636b-45f2-b514-4a213939d107
title: About Distributed Routing Tables
ms.topic: article
ms.date: 05/31/2018
---

# About Distributed Routing Tables

A Distributed Routing Table (DRT) exists as a mesh of cooperating nodes, where each node is an instance of an application using the DRT API. Nodes that publish keys are responsible for assisting other nodes publish and resolve keys. Nodes can also participate in a "resolve only" fashion, which does not require them to assist peers. The DRT protocol executes over a UDP/IPv6 transport.

A node that publishes a key builds and maintains a local routing table of other nodes in the mesh. This routing table is optimized so that the node can quickly locate a specific key in the mesh by finding the key directly in the local routing table, or by asking other nodes publishing keys numerically close to the target. This action is repeated until the required key is found or the node determines that no such key exists.

DRT keys are 256-bit unsigned integers. Closeness between keys is defined by the numerical difference between them. The DRT keyspace is considered circular. For example, the first possible key value, and the last possible key value are considered neighbors.

In a secure DRT, nodes are required to authenticate the keys they publish. The mechanism by which nodes authenticate keys must be set using the DRT API when the DRT is initialized. This is done by choosing a security provider for the DRT. A security provider is a module that can produce tokens used to authenticate keys, and verify tokens produced by other nodes. It must implement the security provider interface that is defined in this documentation. The Windows 7 DRT ships with two fully implemented security providers that can be used to build Windows applications.

During initialization, an application must also supply the DRT with a bootstrap provider. The bootstrap provider is a module that can retrieve the network endpoints of nodes already present in the DRT mesh, and is called upon by the DRT when a new node is established. Like the security provider module, the bootstrap provider must implement a well defined interface. The Windows 7 DRT ships with two fully implemented bootstrap providers.

The DRT considers the immediate neighbors of a key special. The five closest keys numerically smaller and the five closest keys numerically larger than a published key form what is called a leaf set. The DRT reports changes to the leaf set of a key through the DRT API.

## DRT Life Cycle and State Transitions

An application can initialize a local DRT instance using the [**DrtOpen**](/windows/desktop/api/drt/nf-drt-drtopen) function. This function triggers the bootstrapping process, where the DRT API calls upon the bootstrap provider to learn the keys and network endpoints of other nodes already participating in the DRT. If the bootstrap provider successfully locates at least one other node, the DRT enters the DRT\_ACTIVE state. In this state, the application can search for keys published by other nodes, and can publish keys that can be resolved. If the bootstrap provider cannot successfully locate other nodes, the DRT enters the DRT\_ALONE state. The DRT will stay in the DRT\_ALONE state and will attempt to bootstrap periodically in order to locate peers and move to the DRT\_ACTIVE state.

A node can transition to these states from DRT\_ACTIVE.

| Life Cycle State | Conditions                                                                                                                                                                                                                                                                                                                                                                                                                 |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DRT\_ALONE       | The local node has not discovered other nodes in the DRT. While in this state, the node continues to listen for other nodes within the DRT.<br/> If another node joins the DRT, the local node will transition to the DRT\_ACTIVE state. If the network is down, it will transition to DRT\_NO\_NETWORK. In the event of a serious error with the DRT the node will transition to the DRT\_FAULTED state.<br/> |
| DRT\_NO\_NETWORK | When a node loses network connectivity, it transitions to the DRT\_NO\_NETWORK state. At this point the application can wait for network connectivity to be restored, and can close the DRT.<br/>                                                                                                                                                                                                                    |
| DRT\_FAULTED     | A serious error has occurred within the local node. For example, if the local machine runs out of physical memory.<br/> While a node enters this state, the application must call the [**DrtClose**](/windows/desktop/api/drt/nf-drt-drtclose) API, correct the problem, and re-initialize the DRT with [**DrtOpen**](/windows/desktop/api/drt/nf-drt-drtopen).<br/>                                                                                                   |



 

## Related topics

<dl> <dt>

[Using the Distributed Routing Table API](using-the-distributed-routing-table-api.md)
</dt> <dt>

[Distributed Routing Table API Reference](distributed-routing-table-api-reference.md)
</dt> </dl>

 

 




