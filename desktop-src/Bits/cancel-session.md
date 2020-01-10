---
title: Cancel-Session
description: Use the Cancel-Session packet to terminate the upload session with the BITS server.
ms.assetid: 670d061e-ab73-4aa8-85ba-2c9693794235
keywords:
- Cancel-Session BITS
topic_type:
- apiref
api_name:
- Cancel-Session
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Cancel-Session

Use the **Cancel-Session** packet to terminate the upload session with the BITS server.

``` syntax
BITS_POST remote-URL HTTP/1.1
BITS-Packet-Type: Cancel-Session
BITS-Session-Id: {guid}
```

## Headers

<dl> <dt>

<span id="BITS_POST"></span><span id="bits_post"></span>BITS\_POST
</dt> <dd>

BITS-specific verb that identifies this packet to the BITS server.

Replace remote-URL with the absolute or relative URI. Typically, replace remote-URL with the remote file name of the job. For network load balancing considerations, see the BITS-Host-Id header in the [**Create-Session**](create-session.md) packet.

</dd> <dt>

<span id="BITS-Packet-Type"></span><span id="bits-packet-type"></span><span id="BITS-PACKET-TYPE"></span>BITS-Packet-Type
</dt> <dd>

Identifies this request packet as a Cancel-Session packet.

</dd> <dt>

<span id="BITS-Session-Id"></span><span id="bits-session-id"></span><span id="BITS-SESSION-ID"></span>BITS-Session-Id
</dt> <dd>

String GUID that identifies the session to the server. Replace {guid} with the session identifier that the server returns in the [**Ack for Create-Session**](ack-for-create-session.md) response packet.

</dd> </dl>

## Remarks

This packet cancels an upload job if it is sent before the last fragment is sent. Cancel-Session has no effect on a file whose last fragment has already been sent. When the BITS server receives the last fragment, it writes the file to its final destination and, in the case of an upload-reply, posts the file to the server application. In the upload-reply case, the Cancel-Session packet cancels the reply portion of an upload-reply job.

The BITS server releases all resources and deletes all temporary files when it receives this packet.

The BITS client sends this packet when the user cancels the job.

## See also

<dl> <dt>

[**Ack for Create-Session**](ack-for-create-session.md)
</dt> <dt>

[**Close-Session**](close-session.md)
</dt> </dl>

 

 




