---
description: The TAPI server (TAPISRV) is the central repository of telephony data on a user computer.
ms.assetid: 794d230c-abe8-429d-bbf5-91ba364b16ab
title: TAPI Server
ms.topic: article
ms.date: 05/31/2018
---

# TAPI Server

The TAPI server (TAPISRV) is the central repository of telephony data on a user computer. This service process tracks local and remote telephony resources, applications registered to handle Assisted Telephony requests, and pending asynchronous functions, and it also enables a consistent interface with telephony service providers (TSPs). For more information and a diagram that illustrates the relationship of the TAPI Server to other components and an overview of their roles, see [Microsoft Telephony Programming Model](microsoft-telephony-programming-model.md).

For computers running on Windows Server 2003 operating systems, Windows XP, and Windows 2000, TAPISRV runs within the context of Svchost.exe. For computers running on Windows NT, it runs as a separate service process. When an application loads a TAPI DLL into its process space and performs an initialization operation, the DLL establishes an RPC link to the TAPI Server. The TAPI Server loads telephone service providers (TSPs) into its process space. Regardless of how many applications access a given provider's devices, only one instance of a given TSP will exist.

 

 



