---
title: NLM Interfaces
description: NLM Interfaces
ms.assetid: 57cc2a07-4551-428c-a303-9b1a4510f225
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# NLM Interfaces

The following are the NLM interfaces.

| Interface                                                            | Description                                                                                                                                                                                                              |
|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IEnumNetworkConnections**](/windows/desktop/api/Netlistmgr/nn-netlistmgr-ienumnetworkconnections)           | Provides a standard enumerator for network connections. It enumerates active, disconnected, or all network connections within a network. This interface can be obtained from the [**INetwork**](/windows/desktop/api/Netlistmgr/nn-netlistmgr-inetwork) interface. |
| [**IEnumNetworks**](/windows/desktop/api/Netlistmgr/nn-netlistmgr-ienumnetworks)                               | Enumerates all networks available on the server. This interface can be obtained from the [**INetwork**](/windows/desktop/api/Netlistmgr/nn-netlistmgr-inetwork) interface.                                                                                         |
| [**INetwork**](/windows/desktop/api/Netlistmgr/nn-netlistmgr-inetwork)                                         | Represents a network on the server. It can also represent a collection of network connections with a similar network signature.                                                                                          |
| [**INetworkConnection**](/windows/desktop/api/Netlistmgr/nn-netlistmgr-inetworkconnection)                     | Represents a single network connection.                                                                                                                                                                                  |
| [**INetworkConnectionCost**](/windows/desktop/api/Netlistmgr/nn-netlistmgr-inetworkconnectioncost)                | Used to query current network cost and data plan status associated with a connection.                                                                                                                                    |
| [**INetworkConnectionCostEvents**](/windows/desktop/api/Netlistmgr/nn-netlistmgr-inetworkconnectioncostevents) | Used to notify an application of cost and data plan status change events for a connection.                                                                                                                               |
| [**INetworkConnectionEvents**](/windows/desktop/api/Netlistmgr/nn-netlistmgr-inetworkconnectionevents)         | A sink interface that a client implements to receive events related to network connections. Applications that are interested on lower granular level events like authentication changes, implement this interface.       |
| [**INetworkCostManager**](/windows/desktop/api/Netlistmgr/nn-netlistmgr-inetworkcostmanager)                   | Used to query machine-wide cost and data plan status information associated with either a connection used for machine-wide Internet connectivity, or the first-hop of routing to a specific destination on a connection. |
| [**INetworkCostManagerEvents**](/windows/desktop/api/Netlistmgr/nn-netlistmgr-inetworkcostmanagerevents)       | Used to notify an application of machine-wide cost and data plan related events.                                                                                                                                         |
| [**INetworkEvents**](/windows/desktop/api/Netlistmgr/nn-netlistmgr-inetworkevents)                             | A sink interface that a client implements to receive network related events. These APIs are all callback functions that are called automatically when the respective events are raised.                                  |
| [**INetworkListManager**](/windows/desktop/api/Netlistmgr/nn-netlistmgr-inetworklistmanager)                   | Provides a set of methods to perform network list management functions.                                                                                                                                                  |
| [**INetworkListManagerEvents**](/windows/desktop/api/Netlistmgr/nn-netlistmgr-inetworklistmanagerevents)       | A sink interface that a client implements to receive events related to the Network List Manager. Applications that are interested on higher granular level events like internet connectivity, implement the interface.   |



 

 

 




