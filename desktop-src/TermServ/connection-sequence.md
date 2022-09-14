---
title: Connection Sequence
description: An illustration that shows the method calls made between the Remote Desktop Services service and your protocol during the client connection sequence.
ms.assetid: 60e56093-c457-43bc-b152-15c5acbfb016
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Connection Sequence

The following illustration shows the method calls made between the Remote Desktop Services service and your protocol during the client connection sequence. The actions shown here follow the [Start Sequence](start-sequence.md). The interaction between the service and the [**IWRdsProtocolLicenseConnection**](/windows/desktop/api/wtsprotocol/nn-wtsprotocol-iwrdsprotocollicenseconnection) object represents the licensing handshake for the client.

![client connection sequence](images/protocol-connectionsequence.png)

## Related topics

<dl> <dt>

[Method Call Sequence](method-call-sequence.md)
</dt> <dt>

[Reconnect Sequence](reconnect-sequence.md)
</dt> <dt>

[Start Sequence](start-sequence.md)
</dt> </dl>

 

 




