---
title: Ping
description: Use the Ping packet to establish a connection and negotiate security with the server.
ms.assetid: '10b01fe8-d1a3-4a3b-ac35-e3557d3ef4ee'
keywords:
- Ping BITS
topic_type:
- apiref
api_name:
- Ping
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Ping

Use the **Ping** packet to establish a connection and negotiate security with the server.

``` syntax
BITS_POST remote-URL HTTP/1.1
BITS-Packet-Type: Ping
```

## Headers

<dl> <dt>

<span id="BITS_POST"></span><span id="bits_post"></span>BITS\_POST
</dt> <dd>

BITS-specific verb that identifies this packet to the BITS server.

Replace remote-URL with the absolute or relative URI. Typically, replace remote-URL with the remote file name of the job.

</dd> <dt>

<span id="BITS-Packet-Type"></span><span id="bits-packet-type"></span><span id="BITS-PACKET-TYPE"></span>BITS-Packet-Type
</dt> <dd>

Identifies this request packet as a Ping packet.

</dd> </dl>

## Remarks

The **Ping** packet is optional. Instead of sending a **Ping** packet, you can use the [**Create-Session**](create-session.md) packet to establish a connection and negotiate security. However, it is more efficient to use the **Ping** packet for this purpose.

## See also

<dl> <dt>

[**Ack for Ping**](ack-for-ping.md)
</dt> <dt>

[**Create-Session**](create-session.md)
</dt> </dl>

 

 




