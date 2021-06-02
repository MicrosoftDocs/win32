---
description: Call center controls extend the TAPI 3 object model to support the requirements of Automatic Call Distribution (ACD) systems.
ms.assetid: cb7a4231-6249-4ab9-9de7-243768a18775
title: Using Call Center Controls
ms.topic: article
ms.date: 05/31/2018
---

# Using Call Center Controls

Call center controls extend the TAPI 3 object model to support the requirements of Automatic Call Distribution (ACD) systems. A call center is a location with agents or operators at banks of telephones either making outgoing telephone calls or fielding incoming ones. For example, a bank or credit card company will use a call center to process account inquiries.

Call center applications are divided into three basic types:

-   [ACD Proxy](acd-proxy.md): Handles incoming or outgoing sessions at the server, which can be anything from a proprietary telephone switch to an Internet gateway.
-   [ACD Agent Client](acd-agent-client.md): Services an individual agent who is receiving or making calls.
-   ACD Supervisor Client: Provides an overall view of agent and ACD operations.

> [!Note]  
> For Windows 2000, proxy functionality is available using TAPI 2.2, and supervisor functions are not implemented.

 

The samples section of the Windows SDK contains ACD code samples under Netds\\Tapi\\Tapi2\\Acd and Netds\\Tapi\\Tapi3\\Acd.

 

 



