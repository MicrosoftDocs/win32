---
title: NLM Interfaces
description: NLM Interfaces
ms.assetid: '57cc2a07-4551-428c-a303-9b1a4510f225'
---

# NLM Interfaces

The following are the NLM interfaces.

| Interface                                                            | Description                                                                                                                                                                                                              |
|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IEnumNetworkConnections**](ienumnetworkconnections.md)           | Provides a standard enumerator for network connections. It enumerates active, disconnected, or all network connections within a network. This interface can be obtained from the [**INetwork**](inetwork.md) interface. |
| [**IEnumNetworks**](ienumnetworks.md)                               | Enumerates all networks available on the server. This interface can be obtained from the [**INetwork**](inetwork.md) interface.                                                                                         |
| [**INetwork**](inetwork.md)                                         | Represents a network on the server. It can also represent a collection of network connections with a similar network signature.                                                                                          |
| [**INetworkConnection**](inetworkconnection.md)                     | Represents a single network connection.                                                                                                                                                                                  |
| [**INetworkConnectionCost**](inetworkconnectcost.md)                | Used to query current network cost and data plan status associated with a connection.                                                                                                                                    |
| [**INetworkConnectionCostEvents**](inetworkconnectioncostevents.md) | Used to notify an application of cost and data plan status change events for a connection.                                                                                                                               |
| [**INetworkConnectionEvents**](inetworkconnectionevents.md)         | A sink interface that a client implements to receive events related to network connections. Applications that are interested on lower granular level events like authentication changes, implement this interface.       |
| [**INetworkCostManager**](inetworkcostmanager.md)                   | Used to query machine-wide cost and data plan status information associated with either a connection used for machine-wide Internet connectivity, or the first-hop of routing to a specific destination on a connection. |
| [**INetworkCostManagerEvents**](inetworkcostmanagerevents.md)       | Used to notify an application of machine-wide cost and data plan related events.                                                                                                                                         |
| [**INetworkEvents**](inetworkevents.md)                             | A sink interface that a client implements to receive network related events. These APIs are all callback functions that are called automatically when the respective events are raised.                                  |
| [**INetworkListManager**](inetworklistmanager.md)                   | Provides a set of methods to perform network list management functions.                                                                                                                                                  |
| [**INetworkListManagerEvents**](inetworklistmanagerevents.md)       | A sink interface that a client implements to receive events related to the Network List Manager. Applications that are interested on higher granular level events like internet connectivity, implement the interface.   |



 

 

 




