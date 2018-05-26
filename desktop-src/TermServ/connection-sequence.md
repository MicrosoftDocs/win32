---
title: Connection Sequence
description: An illustration that shows the method calls made between the Remote Desktop Services service and your protocol during the client connection sequence.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 60e56093-c457-43bc-b152-15c5acbfb016
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Connection Sequence

The following illustration shows the method calls made between the Remote Desktop Services service and your protocol during the client connection sequence. The actions shown here follow the [Start Sequence](start-sequence.md). The interaction between the service and the [**IWRdsProtocolLicenseConnection**](/windows/win32/wtsprotocol/nn-wtsprotocol-iwrdsprotocollicenseconnection?branch=master) object represents the licensing handshake for the client.

![client connection sequence](images/protocol-connectionsequence.png)

## Related topics

<dl> <dt>

[Method Call Sequence](method-call-sequence.md)
</dt> <dt>

[Reconnect Sequence](reconnect-sequence.md)
</dt> <dt>

[Start Sequence](start-sequence.md)
</dt> </dl>

 

 




