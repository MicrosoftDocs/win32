---
Description: Connect to and communicate with a specific smart card.
ms.assetid: 37d92491-174b-471e-b36e-46d9285dd404
title: Smart Card and Reader Access Functions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Smart Card and Reader Access Functions

The following functions connect to and communicate with a specific [*smart card*](security.s_gly#-security-smart-card-gly). I/O operations to the card use a buffer for sending or receiving data and a structure that contains protocol control information. The protocol control information structure always begins with an [**SCARD\_IO\_REQUEST**](scard-io-request.md) structure.



| Topic                                                  | Description                                                                                                                                                                                                                                |
|--------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SCardConnect**](/windows/desktop/api/Winscard/nf-winscard-scardconnecta)                   | Connect to a card.                                                                                                                                                                                                                         |
| [**SCardReconnect**](/windows/desktop/api/Winscard/nf-winscard-scardreconnect)               | Reestablish a connection.                                                                                                                                                                                                                  |
| [**SCardDisconnect**](/windows/desktop/api/Winscard/nf-winscard-scarddisconnect)             | Terminate a connection.                                                                                                                                                                                                                    |
| [**SCardBeginTransaction**](/windows/desktop/api/Winscard/nf-winscard-scardbegintransaction) | Start a [*transaction*](security.t_gly#-security-transaction-gly), blocking other applications from accessing a card.                                                                                            |
| [**SCardEndTransaction**](/windows/desktop/api/Winscard/nf-winscard-scardendtransaction)     | End a transaction, allowing other applications to access a card.                                                                                                                                                                           |
| [**SCardStatus**](/windows/desktop/api/Winscard/nf-winscard-scardstatusa)                     | Provide the current status of the reader.                                                                                                                                                                                                  |
| [**SCardTransmit**](/windows/desktop/api/Winscard/nf-winscard-scardtransmit)                 | Requests service and receives data back from a card using [*T=0*](security.t_gly#-security-t-0-protocol-gly), [*T=1*](security.t_gly#-security-t-1-protocol-gly), and raw protocols. |



 

 

 



