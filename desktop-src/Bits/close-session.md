---
title: Close-Session
description: Use the Close-Session packet to tell the BITS server that file upload is complete and to end the session.
ms.assetid: 9d4b658a-8b41-4678-b996-f2174784cdd6
keywords:
- Close-Session BITS
topic_type:
- apiref
api_name:
- Close-Session
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Close-Session

Use the **Close-Session** packet to tell the BITS server that file upload is complete and to end the session.

``` syntax
BITS_POST remote-URL HTTP/1.1
BITS-Packet-Type: Close-Session
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

Identifies this request packet as a Close-Session packet.

</dd> <dt>

<span id="BITS-Session-Id"></span><span id="bits-session-id"></span><span id="BITS-SESSION-ID"></span>BITS-Session-Id
</dt> <dd>

String GUID that identifies the session to the server. Replace {guid} with the session identifier that the server returns in the [**Ack for Create-Session**](ack-for-create-session.md) response packet.

</dd> </dl>

## Remarks

The BITS server releases all resources and deletes all temporary files when it receives this packet.

For upload-reply jobs, you must download the reply before sending **Close-Session**. Otherwise, the reply is lost.

If you send this packet before uploading all fragments, the upload file is deleted; you cannot upload a partial file.

## See also

<dl> <dt>

[**Ack for Close-Session**](ack-for-close-session.md)
</dt> <dt>

[**Cancel-Session**](cancel-session.md)
</dt> <dt>

[**Create-Session**](create-session.md)
</dt> </dl>

 

 




