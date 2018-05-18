---
Description: 'The following list provides concise descriptions of each Winsock ATM structure. For additional information on any structure, click the structure name.'
ms.assetid: 'ce80ef1f-9a76-4a6f-a7ce-f166bc46ca08'
title: Winsock ATM Structures
---

# Winsock ATM Structures

The following list provides concise descriptions of each Winsock ATM structure. For additional information on any structure, click the structure name.



| ATM Structure                           | Description                                                |
|-----------------------------------------|------------------------------------------------------------|
| [**ATM\_ADDRESS**](atm-address-2.md)   | Stores ATM address data for ATM-based sockets.             |
| [**ATM\_BHLI**](atm-bhli-2.md)         | Identifies B-HLI information for an associated ATM socket. |
| [**ATM\_BLLI**](atm-blli-2.md)         | Identifies B-LLI information for an associated ATM socket. |
| [**sockaddr\_atm**](sockaddr-atm-2.md) | Stores socket address information for ATM sockets.         |



 

For native ATM services, use AF\_ATM for address family and the [**sockaddr\_atm**](sockaddr-atm-2.md) socket address structure. To open a native ATM socket, pass AF\_ATM, SOCK\_RAW, and ATMPROTO\_AAL5 or ATMPROTO\_AALUSER into the [**socket**](socket-2.md) function, respectively.

 

 



