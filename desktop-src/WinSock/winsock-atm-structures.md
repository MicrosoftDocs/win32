---
Description: The following list provides concise descriptions of each Winsock ATM structure. For additional information on any structure, click the structure name.
ms.assetid: ce80ef1f-9a76-4a6f-a7ce-f166bc46ca08
title: Winsock ATM Structures
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Winsock ATM Structures

The following list provides concise descriptions of each Winsock ATM structure. For additional information on any structure, click the structure name.



| ATM Structure                           | Description                                                |
|-----------------------------------------|------------------------------------------------------------|
| [**ATM\_ADDRESS**](/windows/win32/Ws2atm/ns-ws2atm-atm_address?branch=master)   | Stores ATM address data for ATM-based sockets.             |
| [**ATM\_BHLI**](/windows/win32/Ws2atm/ns-ws2atm-atm_bhli?branch=master)         | Identifies B-HLI information for an associated ATM socket. |
| [**ATM\_BLLI**](/windows/win32/Ws2atm/ns-ws2atm-atm_blli?branch=master)         | Identifies B-LLI information for an associated ATM socket. |
| [**sockaddr\_atm**](/windows/win32/Ws2atm/ns-ws2atm-sockaddr_atm?branch=master) | Stores socket address information for ATM sockets.         |



 

For native ATM services, use AF\_ATM for address family and the [**sockaddr\_atm**](/windows/win32/Ws2atm/ns-ws2atm-sockaddr_atm?branch=master) socket address structure. To open a native ATM socket, pass AF\_ATM, SOCK\_RAW, and ATMPROTO\_AAL5 or ATMPROTO\_AALUSER into the [**socket**](/windows/win32/Winsock2/nf-winsock2-socket?branch=master) function, respectively.

 

 



