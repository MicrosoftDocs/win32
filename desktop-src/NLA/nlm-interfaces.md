---
title: NLM interfaces
description: NLM interfaces
ms.assetid: 57cc2a07-4551-428c-a303-9b1a4510f225
ms.topic: article
ms.date: 05/31/2018
---

# NLM interfaces

The following are the NLM interfaces.

| Interface | Description |
|-|-|
| [**IEnumNetworkConnections**](/windows/win32/api/netlistmgr/nn-netlistmgr-ienumnetworkconnections) | Provides a standard enumerator for network connections. It enumerates active, disconnected, or all network connections within a network. This interface can be obtained from the [**INetwork**](/windows/win32/api/netlistmgr/nn-netlistmgr-inetwork) interface. |
| [**IEnumNetworks**](/windows/win32/api/netlistmgr/nn-netlistmgr-ienumnetworks) | Enumerates all networks available on the server. This interface can be obtained from the [**INetwork**](/windows/win32/api/netlistmgr/nn-netlistmgr-inetwork) interface. |
| [**INetwork**](/windows/win32/api/netlistmgr/nn-netlistmgr-inetwork) | Represents a network on the server. It can also represent a collection of network connections with a similar network signature. |
| [**INetwork2**](/windows/win32/api/netlistmgr/nn-netlistmgr-inetwork2) | Represents a network on the server. It can also represent a collection of network connections with a similar network signature. |
| [**INetworkConnection**](/windows/win32/api/netlistmgr/nn-netlistmgr-inetworkconnection) | Represents a single network connection. |
| [**INetworkConnection2**](/windows/win32/api/netlistmgr/nn-netlistmgr-inetworkconnection2) | Represents a single network connection. |
| [**INetworkConnectionCost**](/windows/win32/api/netlistmgr/nn-netlistmgr-inetworkconnectioncost) | Used to query current network cost and data plan status associated with a connection. |
| [**INetworkConnectionCostEvents**](/windows/win32/api/netlistmgr/nn-netlistmgr-inetworkconnectioncostevents) | Used to notify an application of cost and data plan status change events for a connection. |
| [**INetworkConnectionEvents**](/windows/win32/api/netlistmgr/nn-netlistmgr-inetworkconnectionevents) | A sink interface that a client implements to receive events related to network connections. Applications that are interested on lower granular level events like authentication changes, implement this interface. |
| [**INetworkCostManager**](/windows/win32/api/netlistmgr/nn-netlistmgr-inetworkcostmanager) | Used to query machine-wide cost and data plan status information associated with either a connection used for machine-wide Internet connectivity, or the first-hop of routing to a specific destination on a connection. |
| [**INetworkCostManagerEvents**](/windows/win32/api/netlistmgr/nn-netlistmgr-inetworkcostmanagerevents) | Used to notify an application of machine-wide cost and data plan related events. |
| [**INetworkEvents**](/windows/win32/api/netlistmgr/nn-netlistmgr-inetworkevents) | A sink interface that a client implements to receive network related events. These APIs are all callback functions that are called automatically when the respective events are raised. |
| [**INetworkListManager**](/windows/win32/api/netlistmgr/nn-netlistmgr-inetworklistmanager) | Provides a set of methods to perform network list management functions. |
| [**INetworkListManagerEvents**](/windows/win32/api/netlistmgr/nn-netlistmgr-inetworklistmanagerevents) | A sink interface that a client implements to receive events related to the Network List Manager. Applications that are interested on higher granular level events like internet connectivity, implement the interface. |

