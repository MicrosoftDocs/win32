---
title: BITS Response Packets
description: BITS Response Packets
ms.assetid: 30755476-daa9-42ea-8fb3-5b505fc9dd75
ms.topic: article
ms.date: 05/31/2018
---

# BITS Response Packets

The following table lists the response packets sent to the BITS client for upload and upload-reply jobs. The table lists the packets in the typical sequence they are sent to the client.



| Response packet                                      | Purpose                                                                                                                                                                                     |
|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Ack for Ping](ack-for-ping.md)                     | Acknowledges the [Ping](ping.md) request.                                                                                                                                                  |
| [Ack for Create-Session](ack-for-create-session.md) | Acknowledges the [Create-Session](create-session.md) request and returns a session identifier that the BITS client uses on all subsequent requests to identify this file transfer session. |
| [Ack for Fragment](ack-for-fragment.md)             | Acknowledges the [Fragment](fragment.md) request and writes the fragment to the upload file on the server.                                                                                 |
| [Ack for Close-Session](ack-for-close-session.md)   | Acknowledges the [Close-Session](close-session.md) request and releases all resources associated with the session.                                                                         |
| [Ack for Cancel-Session](ack-for-cancel-session.md) | Acknowledges the [Cancel-Session](cancel-session.md) request and releases all resources associated with the session.                                                                       |



 

 

 




