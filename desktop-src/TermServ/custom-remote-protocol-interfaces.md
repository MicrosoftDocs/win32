---
title: Remote Desktop Protocol Provider Interfaces
description: Interfaces that are supported by the Remote Desktop Protocol Provider API.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '180c29d4-a305-45ac-8989-6226dccb75d5'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
---

# Remote Desktop Protocol Provider Interfaces

The following interfaces are supported by the Remote Desktop Protocol Provider API.

## In this section

<dl> <dt>

[**IWRdsProtocolConnection**](iwrdsprotocolconnection.md)
</dt> <dd>

Exposes methods called by the Remote Desktop Services service to configure a client connection.

</dd> <dt>

[**IWRdsProtocolConnectionCallback**](iwrdsprotocolconnectioncallback.md)
</dt> <dd>

Exposes methods that provide information about the status of a client connection and that perform actions for the client. This interface is implemented by the Remote Desktop Services service and called by the protocol.

</dd> <dt>

[**IWRdsProtocolLicenseConnection**](iwrdsprotocollicenseconnection.md)
</dt> <dd>

Exposes methods used by the Remote Desktop Services service to perform the licensing handshake during a connection sequence.

</dd> <dt>

[**IWRdsProtocolListener**](iwrdsprotocollistener.md)
</dt> <dd>

Exposes methods that request that the protocol start and stop listening for client connection requests.

</dd> <dt>

[**IWRdsProtocolListenerCallback**](iwrdsprotocollistenercallback.md)
</dt> <dd>

Exposes methods that notify the Remote Desktop Services service that a client has connected.

</dd> <dt>

[**IWRdsProtocolLogonErrorRedirector**](iwrdsprotocollogonerrorredirector.md)
</dt> <dd>

Exposes methods called by the Remote Desktop Services service to update logon status and determine how to direct logon error messages.

</dd> <dt>

[**IWRdsProtocolManager**](iwrdsprotocolmanager.md)
</dt> <dd>

Exposes methods that the Remote Desktop Services service uses to communicate with the protocol provider.

</dd> <dt>

[**IWRdsProtocolSettings**](iwrdsprotocolsettings.md)
</dt> <dd>

Exposes methods for retrieving and adding policy-related settings.

</dd> <dt>

[**IWRdsProtocolShadowCallback**](iwrdsprotocolshadowcallback.md)
</dt> <dd>

Exposes methods called by the protocol to notify the Remote Desktop Services service to start or stop the target side of a shadow.

</dd> <dt>

[**IWRdsProtocolShadowConnection**](iwrdsprotocolshadowconnection.md)
</dt> <dd>

Exposes methods that notify the protocol provider about the status of session shadowing.

</dd> <dt>

[**IWRdsRemoteFXGraphicsConnection**](iwrdsremotefxgraphicsconnection.md)
</dt> <dd>

Exposes methods relating to the manipulation and understanding of graphics on the client connection.

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

 

 




