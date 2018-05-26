---
title: Remote Desktop Protocol Provider Interfaces
description: Interfaces that are supported by the Remote Desktop Protocol Provider API.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 180c29d4-a305-45ac-8989-6226dccb75d5
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Remote Desktop Protocol Provider Interfaces

The following interfaces are supported by the Remote Desktop Protocol Provider API.

## In this section

<dl> <dt>

[**IWRdsProtocolConnection**](/windows/win32/wtsprotocol/nn-wtsprotocol-iwrdsprotocolconnection?branch=master)
</dt> <dd>

Exposes methods called by the Remote Desktop Services service to configure a client connection.

</dd> <dt>

[**IWRdsProtocolConnectionCallback**](/windows/win32/wtsprotocol/nn-wtsprotocol-iwrdsprotocolconnectioncallback?branch=master)
</dt> <dd>

Exposes methods that provide information about the status of a client connection and that perform actions for the client. This interface is implemented by the Remote Desktop Services service and called by the protocol.

</dd> <dt>

[**IWRdsProtocolLicenseConnection**](/windows/win32/wtsprotocol/nn-wtsprotocol-iwrdsprotocollicenseconnection?branch=master)
</dt> <dd>

Exposes methods used by the Remote Desktop Services service to perform the licensing handshake during a connection sequence.

</dd> <dt>

[**IWRdsProtocolListener**](/windows/win32/wtsprotocol/nn-wtsprotocol-iwrdsprotocollistener?branch=master)
</dt> <dd>

Exposes methods that request that the protocol start and stop listening for client connection requests.

</dd> <dt>

[**IWRdsProtocolListenerCallback**](/windows/win32/wtsprotocol/nn-wtsprotocol-iwrdsprotocollistenercallback?branch=master)
</dt> <dd>

Exposes methods that notify the Remote Desktop Services service that a client has connected.

</dd> <dt>

[**IWRdsProtocolLogonErrorRedirector**](/windows/win32/wtsprotocol/nn-wtsprotocol-iwrdsprotocollogonerrorredirector?branch=master)
</dt> <dd>

Exposes methods called by the Remote Desktop Services service to update logon status and determine how to direct logon error messages.

</dd> <dt>

[**IWRdsProtocolManager**](/windows/win32/wtsprotocol/nn-wtsprotocol-iwrdsprotocolmanager?branch=master)
</dt> <dd>

Exposes methods that the Remote Desktop Services service uses to communicate with the protocol provider.

</dd> <dt>

[**IWRdsProtocolSettings**](/windows/win32/wtsprotocol/nn-wtsprotocol-iwrdsprotocolsettings?branch=master)
</dt> <dd>

Exposes methods for retrieving and adding policy-related settings.

</dd> <dt>

[**IWRdsProtocolShadowCallback**](/windows/win32/wtsprotocol/nn-wtsprotocol-iwrdsprotocolshadowcallback?branch=master)
</dt> <dd>

Exposes methods called by the protocol to notify the Remote Desktop Services service to start or stop the target side of a shadow.

</dd> <dt>

[**IWRdsProtocolShadowConnection**](/windows/win32/wtsprotocol/nn-wtsprotocol-iwrdsprotocolshadowconnection?branch=master)
</dt> <dd>

Exposes methods that notify the protocol provider about the status of session shadowing.

</dd> <dt>

[**IWRdsRemoteFXGraphicsConnection**](/windows/win32/wtsprotocol/nn-wtsprotocol-iwrdsremotefxgraphicsconnection?branch=master)
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

 

 




