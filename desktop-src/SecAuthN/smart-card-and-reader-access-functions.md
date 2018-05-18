---
Description: 'Connect to and communicate with a specific smart card.'
ms.assetid: '37d92491-174b-471e-b36e-46d9285dd404'
title: Smart Card and Reader Access Functions
---

# Smart Card and Reader Access Functions

The following functions connect to and communicate with a specific [*smart card*](security.s_gly#-security-smart-card-gly). I/O operations to the card use a buffer for sending or receiving data and a structure that contains protocol control information. The protocol control information structure always begins with an [**SCARD\_IO\_REQUEST**](scard-io-request.md) structure.



| Topic                                                  | Description                                                                                                                                                                                                                                |
|--------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SCardConnect**](scardconnect.md)                   | Connect to a card.                                                                                                                                                                                                                         |
| [**SCardReconnect**](scardreconnect.md)               | Reestablish a connection.                                                                                                                                                                                                                  |
| [**SCardDisconnect**](scarddisconnect.md)             | Terminate a connection.                                                                                                                                                                                                                    |
| [**SCardBeginTransaction**](scardbegintransaction.md) | Start a [*transaction*](security.t_gly#-security-transaction-gly), blocking other applications from accessing a card.                                                                                            |
| [**SCardEndTransaction**](scardendtransaction.md)     | End a transaction, allowing other applications to access a card.                                                                                                                                                                           |
| [**SCardStatus**](scardstatus.md)                     | Provide the current status of the reader.                                                                                                                                                                                                  |
| [**SCardTransmit**](scardtransmit.md)                 | Requests service and receives data back from a card using [*T=0*](security.t_gly#-security-t-0-protocol-gly), [*T=1*](security.t_gly#-security-t-1-protocol-gly), and raw protocols. |



 

 

 



