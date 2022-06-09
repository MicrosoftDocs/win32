---
title: Remote Desktop Protocol Provider Interfaces
description: Interfaces that are supported by the Remote Desktop Protocol Provider API.
ms.assetid: 180c29d4-a305-45ac-8989-6226dccb75d5
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Remote Desktop Protocol Provider Interfaces

The following interfaces are supported by the Remote Desktop Protocol Provider API.

## In this section

<dl> <dt>

[**IWRdsProtocolConnection**](/windows/desktop/api/wtsprotocol/nn-wtsprotocol-iwrdsprotocolconnection)
</dt> <dd>

Exposes methods called by the Remote Desktop Services service to configure a client connection.

</dd> <dt>

[**IWRdsProtocolConnectionCallback**](/windows/desktop/api/wtsprotocol/nn-wtsprotocol-iwrdsprotocolconnectioncallback)
</dt> <dd>

Exposes methods that provide information about the status of a client connection and that perform actions for the client. This interface is implemented by the Remote Desktop Services service and called by the protocol.

</dd> <dt>

[**IWRdsProtocolLicenseConnection**](/windows/desktop/api/wtsprotocol/nn-wtsprotocol-iwrdsprotocollicenseconnection)
</dt> <dd>

Exposes methods used by the Remote Desktop Services service to perform the licensing handshake during a connection sequence.

</dd> <dt>

[**IWRdsProtocolListener**](/windows/desktop/api/wtsprotocol/nn-wtsprotocol-iwrdsprotocollistener)
</dt> <dd>

Exposes methods that request that the protocol start and stop listening for client connection requests.

</dd> <dt>

[**IWRdsProtocolListenerCallback**](/windows/desktop/api/wtsprotocol/nn-wtsprotocol-iwrdsprotocollistenercallback)
</dt> <dd>

Exposes methods that notify the Remote Desktop Services service that a client has connected.

</dd> <dt>

[**IWRdsProtocolLogonErrorRedirector**](/windows/desktop/api/wtsprotocol/nn-wtsprotocol-iwrdsprotocollogonerrorredirector)
</dt> <dd>

Exposes methods called by the Remote Desktop Services service to update logon status and determine how to direct logon error messages.

</dd> <dt>

[**IWRdsProtocolManager**](/windows/desktop/api/wtsprotocol/nn-wtsprotocol-iwrdsprotocolmanager)
</dt> <dd>

Exposes methods that the Remote Desktop Services service uses to communicate with the protocol provider.

</dd> <dt>

[**IWRdsProtocolSettings**](/windows/desktop/api/wtsprotocol/nn-wtsprotocol-iwrdsprotocolsettings)
</dt> <dd>

Exposes methods for retrieving and adding policy-related settings.

</dd> <dt>

[**IWRdsProtocolShadowCallback**](/windows/desktop/api/wtsprotocol/nn-wtsprotocol-iwrdsprotocolshadowcallback)
</dt> <dd>

Exposes methods called by the protocol to notify the Remote Desktop Services service to start or stop the target side of a shadow.

</dd> <dt>

[**IWRdsProtocolShadowConnection**](/windows/desktop/api/wtsprotocol/nn-wtsprotocol-iwrdsprotocolshadowconnection)
</dt> <dd>

Exposes methods that notify the protocol provider about the status of session shadowing.

</dd> <dt>

[Deprecated Desktop Protocol Provider Interfaces](deprecated-desktop-protocol-provider-interfaces.md)
</dt> <dd>

The following interfaces have been deprecated and should no longer be used. For new projects, use the Remote Desktop Protocol Provider Interfaces interfaces instead.

</dd> </dl>

## Related topics

<dl> <dt>

[Remote Desktop Protocol Provider Reference](custom-remote-protocol-reference.md)
</dt> <dt>

[Remote Desktop Protocol Provider Enumerations](custom-remote-protocol-enumerations.md)
</dt> <dt>

[Remote Desktop Protocol Provider Structures](custom-remote-protocol-structures.md)
</dt> <dt>

[Remote Desktop Protocol Provider Unions](custom-remote-protocol-unions.md)
</dt> </dl>

 

 




