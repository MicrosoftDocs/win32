---
title: EAPHost Peer Method Run-Time Functions
description: EAPHost Peer Method Run-Time Functions
ms.assetid: 'fdfa595d-acf7-4489-88a8-113093567fe5'
---

# EAPHost Peer Method Run-Time Functions

The EAP Peer Method API run-time functions are as follows.



| Function                                                                   | Description                                                                                                                                                                                                                 |
|----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**EapPeerBeginSession**](eappeerbeginsession.md)                         | Starts a new authentication session on the peer EAPHost.                                                                                                                                                                    |
| [**EapPeerEndSession**](eappeerendsession.md)                             | Terminates a current EAP authentication session between EAPHost and the peer.                                                                                                                                               |
| [**EapPeerGetConfigBlobAndUserBlob**](eappeergetconfigblobanduserblob.md) | Allows EAP method developers to provide the various connection properties and user properties supported by the method. EAPHost invokes this function to create the connection property and user property of the EAP method. |
| [**EapPeerGetIdentity**](eappeergetidentity.md)                           | Obtains the identity for the EAP method that is calling.                                                                                                                                                                    |
| [**EapPeerGetInfo**](eappeergetinfo.md)                                   | Obtains a set of function pointers for an implementation of the loaded EAP peer method.                                                                                                                                     |
| [**EapPeerGetResponseAttributes**](eappeergetresponseattributes.md)       | Obtains an array of EAP attributes from the EAP method.                                                                                                                                                                     |
| [**EapPeerGetResponsePacket**](eappeergetresponsepacket.md)               | Obtains a response packet from the EAP method.                                                                                                                                                                              |
| [**EapPeerGetResult**](eappeergetresult.md)                               | Obtains the result of an authentication session from the EAP method.                                                                                                                                                        |
| [**EapPeerGetUIContext**](eappeergetuicontext.md)                         | Obtains the user interface context from the EAP method.                                                                                                                                                                     |
| [**EapPeerInitialize**](eappeerinitialize.md)                             | Initializes EAPHost for the peer method.                                                                                                                                                                                    |
| [**EapPeerProcessRequestPacket**](eappeerprocessrequestpacket.md)         | Processes a packet received by EAPHost from a supplicant.                                                                                                                                                                   |
| [**EapPeerSetCredentials**](eappeersetcredentials.md)                     | Supplies new or updated user credentials to the EAP method.                                                                                                                                                                 |
| [**EapPeerSetResponseAttributes**](eappeersetresponseattributes.md)       | Provides an updated array of EAP attributes to the EAP method.                                                                                                                                                              |
| [**EapPeerSetUIContext**](eappeersetuicontext.md)                         | Provides a user interface context to the EAP method.                                                                                                                                                                        |
| [**EapPeerShutdown**](eappeershutdown.md)                                 | Shuts down the EAP method and prepares to unload its corresponding DLL.                                                                                                                                                     |



 

## Related topics

<dl> <dt>

[EAPHost Peer Method Configuration Functions](eaphost-peer-method-run-time-functions.md)
</dt> </dl>

 

 




