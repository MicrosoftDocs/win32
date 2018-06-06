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

The following functions connect to and communicate with a specific [*smart card*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50). I/O operations to the card use a buffer for sending or receiving data and a structure that contains protocol control information. The protocol control information structure always begins with an [**SCARD\_IO\_REQUEST**](scard-io-request.md) structure.



| Topic                                                  | Description                                                                                                                                                                                                                                |
|--------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SCardConnect**](/windows/desktop/api/Winscard/nf-winscard-scardconnecta)                   | Connect to a card.                                                                                                                                                                                                                         |
| [**SCardReconnect**](/windows/desktop/api/Winscard/nf-winscard-scardreconnect)               | Reestablish a connection.                                                                                                                                                                                                                  |
| [**SCardDisconnect**](/windows/desktop/api/Winscard/nf-winscard-scarddisconnect)             | Terminate a connection.                                                                                                                                                                                                                    |
| [**SCardBeginTransaction**](/windows/desktop/api/Winscard/nf-winscard-scardbegintransaction) | Start a [*transaction*](https://msdn.microsoft.com/11f2e098-1d1e-473b-90ff-7b86eb923e9f), blocking other applications from accessing a card.                                                                                            |
| [**SCardEndTransaction**](/windows/desktop/api/Winscard/nf-winscard-scardendtransaction)     | End a transaction, allowing other applications to access a card.                                                                                                                                                                           |
| [**SCardStatus**](/windows/desktop/api/Winscard/nf-winscard-scardstatusa)                     | Provide the current status of the reader.                                                                                                                                                                                                  |
| [**SCardTransmit**](/windows/desktop/api/Winscard/nf-winscard-scardtransmit)                 | Requests service and receives data back from a card using [*T=0*](https://msdn.microsoft.com/11f2e098-1d1e-473b-90ff-7b86eb923e9f), [*T=1*](https://msdn.microsoft.com/11f2e098-1d1e-473b-90ff-7b86eb923e9f), and raw protocols. |



 

 

 



