---
description: Transport addresses (XAddrs) included in ProbeMatches and ResolveMatches messages are subject to basic validation before WSDAPI sends an HTTP message, such as a metadata request.
ms.assetid: 6b5139b5-aa31-42bc-a281-8784006edfbe
title: XAddr Validation Rules
ms.topic: article
ms.date: 05/31/2018
---

# XAddr Validation Rules

Transport addresses (XAddrs) included in [ProbeMatches](probematches-message.md) and [ResolveMatches](resolvematches-message.md) messages are subject to basic validation before WSDAPI sends an HTTP message, such as a metadata request.

This is in order to ensure that the XAddrs are on the same subnet as the client.

The following XML shows a sample XAddrs element. The wsd prefix refers to the namespace `https://schemas.xmlsoap.org/ws/2005/04/discovery`.

``` syntax
<wsd:XAddrs>
    https://192.168.0.2:5357/37f86d35-e6ac-4241-964f-1d9ae46fb366
</wsd:XAddrs>
```

All of the following conditions must be met before the HTTP message will go out over the wire.

-   XAddrs must be HTTP or HTTPS addresses. XAddrs of other schemes are ignored.
-   If any HTTPS XAddrs are present, all XAddrs must be HTTPS. XAddr sections which include both HTTP and HTTPS addresses are completely ignored. Additionally, the device's endpoint address must match the HTTPS XAddrs exactly.
-   XAddrs must be IP addresses or hostnames resolvable through DNS. Usually, IP addresses are used.
-   At least one IP address included in the XAddrs (or IP address resolved from a hostname included in the XAddrs) must be on the same subnet as the adapter over which the [ProbeMatches](probematches-message.md) or [ResolveMatches](resolvematches-message.md) message was received.
-   The address and port specified in the first XAddr must be accessible. WSDAPI attempts to connect to this address when establishing an HTTP connection.

## Related topics

<dl> <dt>

[ProbeMatches](probematches-message.md)
</dt> <dt>

[ResolveMatches](resolvematches-message.md)
</dt> <dt>

[Discovery and Metadata Exchange Message Patterns](discovery-and-metadata-exchange-message-patterns.md)
</dt> </dl>

 

 



