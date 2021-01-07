---
description: The network DDE agent starts network DDE if it detects local network DDE activity.
ms.assetid: bc1e6a06-be07-4ae8-94da-9603a885b3a5
title: Network DDE Agent
ms.topic: article
ms.date: 05/31/2018
---

# Network DDE Agent

\[Network DDE is no longer supported. Nddeapi.dll is present on Windows Vista, but all function calls return NDDE\_NOT\_IMPLEMENTED.\]

The network DDE agent starts network DDE if it detects local network DDE activity. It does not detect a remote client trying to connect. Therefore, before any client can successfully connect, network DDE must be started on the server computer. Note that network DDE is not started by default. To start network DDE, run NETDDE.EXE. This file is located in your Windows directory.

The network DDE agent also starts the applications necessary for network DDE. After network DDE is started, DDE conversations are controlled through a network DDE window associated with one of the network DDE applications. This application acts as a proxy. It communicates with all local and remote DDE applications.

 

 



