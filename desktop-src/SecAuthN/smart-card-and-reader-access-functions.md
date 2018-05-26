---
Description: Connect to and communicate with a specific smart card.
ms.assetid: 37d92491-174b-471e-b36e-46d9285dd404
title: Smart Card and Reader Access Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Smart Card and Reader Access Functions

The following functions connect to and communicate with a specific [*smart card*](security.s_gly#-security-smart-card-gly). I/O operations to the card use a buffer for sending or receiving data and a structure that contains protocol control information. The protocol control information structure always begins with an [**SCARD\_IO\_REQUEST**](scard-io-request.md) structure.



| Topic                                                  | Description                                                                                                                                                                                                                                |
|--------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SCardConnect**](/windows/win32/Winscard/nf-winscard-scardconnecta?branch=master)                   | Connect to a card.                                                                                                                                                                                                                         |
| [**SCardReconnect**](/windows/win32/Winscard/nf-winscard-scardreconnect?branch=master)               | Reestablish a connection.                                                                                                                                                                                                                  |
| [**SCardDisconnect**](/windows/win32/Winscard/nf-winscard-scarddisconnect?branch=master)             | Terminate a connection.                                                                                                                                                                                                                    |
| [**SCardBeginTransaction**](/windows/win32/Winscard/nf-winscard-scardbegintransaction?branch=master) | Start a [*transaction*](security.t_gly#-security-transaction-gly), blocking other applications from accessing a card.                                                                                            |
| [**SCardEndTransaction**](/windows/win32/Winscard/nf-winscard-scardendtransaction?branch=master)     | End a transaction, allowing other applications to access a card.                                                                                                                                                                           |
| [**SCardStatus**](/windows/win32/Winscard/nf-winscard-scardstatusa?branch=master)                     | Provide the current status of the reader.                                                                                                                                                                                                  |
| [**SCardTransmit**](/windows/win32/Winscard/nf-winscard-scardtransmit?branch=master)                 | Requests service and receives data back from a card using [*T=0*](security.t_gly#-security-t-0-protocol-gly), [*T=1*](security.t_gly#-security-t-1-protocol-gly), and raw protocols. |



 

 

 



