---
title: BITS Request Packets
description: BITS Request Packets
ms.assetid: 4d8fd5f3-7621-438f-926f-38ece7a52f52
ms.topic: article
ms.date: 05/31/2018
---

# BITS Request Packets

Request packets describe client requests. There can be only one outstanding request at any given time; you must receive an [Ack](bits-response-packets.md) for the current request from the server before sending another request.

The following table lists the request packets sent to the BITS server for upload and upload-reply jobs. The table lists the packets in the typical sequence they are sent to the server.



| Request packet                       | Purpose                                                                                                                                                        |
|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Ping](ping.md)                     | Establishes a connection and negotiates security with the server.                                                                                              |
| [Create-Session](create-session.md) | Requests an upload session with the BITS server.                                                                                                               |
| [Fragment](fragment.md)             | Sends a fragment of the file to the BITS server. The number of fragment requests sent depends on the fragment size you choose and the size of the upload file. |
| [Close-Session](close-session.md)   | Ends the file upload session with the BITS server.                                                                                                             |
| [Cancel-Session](cancel-session.md) | Ends the file upload session with the BITS server. Typically, you send the Cancel-Session packet if the user canceled the job.                                 |



 

The Ping packet is optional. Instead of sending a Ping packet, you can use the Create-Session packet to establish a connection and negotiate security. However, it is more efficient to use the Ping packet for this purpose.

 

 




