---
description: AppSequence information contained in WS-Discovery announcement and response messages (Hello, ProbeMatches, and ResolveMatches).
ms.assetid: f54eaa09-7ce8-4948-a0c5-edf2d054f6d5
title: AppSequence Validation Rules
ms.topic: article
ms.date: 05/31/2018
---

# AppSequence Validation Rules

AppSequence information contained in WS-Discovery announcement and response messages ([Hello](hello-message.md), [ProbeMatches](probematches-message.md), and [ResolveMatches](resolvematches-message.md)). This information is processed and validated by WSDAPI before these messages are passed on to components above the stack (such as Network Explorer or an application calling into WSDAPI).

The following XML shows a sample AppSequence element. The wsd prefix refers to the namespace `https://schemas.xmlsoap.org/ws/2005/04/discovery`.

``` syntax
<wsd:AppSequence InstanceId="2"
    SequenceId="urn:uuid:369a7d7b-5f87-48a4-aa9a-189edf2a8772"
    MessageNumber="21">
</wsd:AppSequence>
```

WSDAPI ignores stale messages. For each device (uniquely identified by the Endpoint Address in the SOAP Body), WSDAPI ignores any messages with an AppSequence MessageNumber lower than the last message seen.

WSDAPI ignores stale XAddr announcements. If the AppSequence InstanceId is lower than the last InstanceId seen, WSDAPI ignores the XAddrs advertised in the SOAP body. Also, if the InstanceId is the same as previous but the MetadataVersion is lower than the last MetadataVersion, WSDAPI ignores the XAddrs.

WSDAPI ignores duplicate WS-Discovery messages. If two identical WS-Discovery messages are sent to WSDAPI, only the first received will be processed. This is typically only relevant for applications that call directly into the [**IWSDiscoveryPublisher**](/windows/desktop/api/WsdDisco/nn-wsddisco-iwsdiscoverypublisher) or [**IWSDiscoveryProvider**](/windows/desktop/api/WsdDisco/nn-wsddisco-iwsdiscoveryprovider) interfaces.

## Related topics

<dl> <dt>

[Discovery and Metadata Exchange Message Patterns](discovery-and-metadata-exchange-message-patterns.md)
</dt> </dl>

 

 



