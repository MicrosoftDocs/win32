---
title: Create-Session
description: Use the Create-Session packet to request an upload session with the BITS server.
ms.assetid: eeb8ff83-2a7f-4fef-9df7-8c12febfcf36
keywords:
- Create-Session BITS
topic_type:
- apiref
api_name:
- Create-Session
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Create-Session

Use the **Create-Session** packet to request an upload session with the BITS server.

``` syntax
BITS_POST remote-URL HTTP/1.1
BITS-Packet-Type: Create-Session
BITS-Supported-Protocols: {guid1} ... {guidN}
```

## Headers

<dl> <dt>

<span id="BITS_POST"></span><span id="bits_post"></span>BITS\_POST
</dt> <dd>

BITS-specific verb that identifies this packet to the BITS server.

Replace remote-URL with the absolute or relative URI. Typically, replace remote-URL with the remote file name of the job. For network load balancing considerations, see the BITS-Host-Id header.

</dd> <dt>

<span id="BITS-Packet-Type"></span><span id="bits-packet-type"></span><span id="BITS-PACKET-TYPE"></span>BITS-Packet-Type
</dt> <dd>

Identifies this request packet as a Create-Session packet.

</dd> <dt>

<span id="BITS-Supported-Protocols"></span><span id="bits-supported-protocols"></span><span id="BITS-SUPPORTED-PROTOCOLS"></span>BITS-Supported-Protocols
</dt> <dd>

Space-delimited list of the protocols that the client supports. Use string GUIDs to identify the protocols. Specify the list in order of preference from most to least preferred. The following table lists the protocol that the BITS client supports. Replace {guid1} ... {guidN} with one or more string GUIDs from the list.



| Protocol                                          | Description                         |
|---------------------------------------------------|-------------------------------------|
| {7df0354d-249b-430f-820d-3d2a9bef4931}<br/> | BITS 1.5 Upload Protocol<br/> |



 

</dd> </dl>

## Remarks

You should send a [**Ping**](ping.md) packet to establish an HTTP connection before sending the Create-Session packet. The Create-Session packet can also establish the connection; however, the Create-Session packet is less efficient.

The server selects the protocol it wants to use from the list the client provides in the BITS-Supported-Protocols header. The server returns the selected protocol in the BITS-Protocol header of the [**Ack for Create-Session**](ack-for-create-session.md) response packet.

The client expects the server to return an [**Ack for Create-Session**](ack-for-create-session.md) response packet. If the server was able to establish a session, the client uses the [**Fragment**](fragment.md) request packet to send ranges of the file to the server.

## See also

<dl> <dt>

[**Ack for Create-Session**](ack-for-create-session.md)
</dt> <dt>

[**Fragment**](fragment.md)
</dt> <dt>

[**Ping**](ping.md)
</dt> </dl>

 

 





