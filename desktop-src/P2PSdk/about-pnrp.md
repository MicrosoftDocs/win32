---
description: The Peer Name Resolution Protocol (PNRP) Namespace Provider (NSP) is a serverless name resolution technology that allows nodes to discover each other.
ms.assetid: e11d0f07-f3a0-4c0f-94ce-1d4944a34230
title: About PNRP
ms.topic: concept-article
ms.date: 05/31/2018
---

# About PNRP

The Peer Name Resolution Protocol (PNRP) Namespace Provider (NSP) is a serverless name resolution technology that allows nodes to discover each other. PNRP uses the Winsock 2 Namespace Provider API.

IPv6 support is required by PNRP and is the only Internet Protocol native to the API. However, PNRP can resolve IPv4 addresses via the 6to4 or [Teredo](/windows/desktop/Teredo/portal) transition technologies. Windows XP with Service Pack 1 (SP1) users must use the Advanced Networking Pack to enable the IPv6 support required by PNRP.

> [!Note]  
> Applications using PNRP in an environment with a firewall require exception groups that cover the port specific to the application, as well as port '3540-UDP' for PNRP. These exception groups should be enabled whenever the application is running.

PNRP 2.0 is native to the Windows Vista and Windows Server 2008 platforms.

 

 
