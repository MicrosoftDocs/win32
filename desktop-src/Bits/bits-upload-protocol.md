---
title: BITS Upload Protocol
description: This section describes the network protocol for BITS upload and upload-reply job types.
ms.assetid: d0706ab1-1bf4-4b17-9321-ec3e00dd25e2
ms.topic: article
ms.date: 05/31/2018
---

# BITS Upload Protocol

This section describes the network protocol for BITS upload and upload-reply job types. The BITS upload protocol is layered on top of HTTP 1.1 and uses many of the existing HTTP headers and defines new headers. The BITS upload protocol supports a single upload file per session.

BITS uses packets to describe client requests and server responses. The BITS-Packet-Type header specifies the type of packet being sent. Each packet contains specific headers. BITS uses the BITS\_POST verb to identify BITS upload packets. Response packets always use the Ack packet type which stands for acknowledge. The Ack packet is sent in the context of the previous request; there can be only one outstanding request at one time.

For upload-reply jobs, BITS uses this protocol to upload the file but does not use this protocol to send the reply to the client. Instead, the BITS server sends the location of the reply file to the client and the client creates a BITS download job to download the reply file.

Use the upload protocol to replace the BITS client or server software with your own implementation. For a list of request packets sent by the BITS client, see [BITS Request Packets](bits-request-packets.md). For a list of response packets sent by the BITS server, see [BITS Response Packets](bits-response-packets.md).

The client determines how it responds to errors or unexpected packets from the BITS server. If the server receives a packet that it does not expect, the server should send an Ack packet with a 400 (Bad Request) return code.

 

 




