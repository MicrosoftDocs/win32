---
title: EAPHost Peer Method Run-Time Functions
description: EAPHost Peer Method Run-Time Functions
ms.assetid: fdfa595d-acf7-4489-88a8-113093567fe5
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# EAPHost Peer Method Run-Time Functions

The EAP Peer Method API run-time functions are as follows.



| Function                                                                   | Description                                                                                                                                                                                                                 |
|----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**EapPeerBeginSession**](/windows/previous-versions/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerbeginsession?branch=master)                         | Starts a new authentication session on the peer EAPHost.                                                                                                                                                                    |
| [**EapPeerEndSession**](/windows/previous-versions/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerendsession?branch=master)                             | Terminates a current EAP authentication session between EAPHost and the peer.                                                                                                                                               |
| [**EapPeerGetConfigBlobAndUserBlob**](/windows/previous-versions/eapmethodpeerapis/nf-eapmethodpeerapis-eappeergetconfigblobanduserblob?branch=master) | Allows EAP method developers to provide the various connection properties and user properties supported by the method. EAPHost invokes this function to create the connection property and user property of the EAP method. |
| [**EapPeerGetIdentity**](/windows/previous-versions/eapmethodpeerapis/nf-eapmethodpeerapis-eappeergetidentity?branch=master)                           | Obtains the identity for the EAP method that is calling.                                                                                                                                                                    |
| [**EapPeerGetInfo**](/windows/previous-versions/eapmethodpeerapis/nf-eapmethodpeerapis-eappeergetinfo?branch=master)                                   | Obtains a set of function pointers for an implementation of the loaded EAP peer method.                                                                                                                                     |
| [**EapPeerGetResponseAttributes**](/windows/previous-versions/eapmethodpeerapis/nf-eapmethodpeerapis-eappeergetresponseattributes?branch=master)       | Obtains an array of EAP attributes from the EAP method.                                                                                                                                                                     |
| [**EapPeerGetResponsePacket**](/windows/previous-versions/eapmethodpeerapis/nf-eapmethodpeerapis-eappeergetresponsepacket?branch=master)               | Obtains a response packet from the EAP method.                                                                                                                                                                              |
| [**EapPeerGetResult**](/windows/previous-versions/eapmethodpeerapis/nf-eapmethodpeerapis-eappeergetresult?branch=master)                               | Obtains the result of an authentication session from the EAP method.                                                                                                                                                        |
| [**EapPeerGetUIContext**](/windows/previous-versions/eapmethodpeerapis/nf-eapmethodpeerapis-eappeergetuicontext?branch=master)                         | Obtains the user interface context from the EAP method.                                                                                                                                                                     |
| [**EapPeerInitialize**](/windows/previous-versions/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerinitialize?branch=master)                             | Initializes EAPHost for the peer method.                                                                                                                                                                                    |
| [**EapPeerProcessRequestPacket**](/windows/previous-versions/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerprocessrequestpacket?branch=master)         | Processes a packet received by EAPHost from a supplicant.                                                                                                                                                                   |
| [**EapPeerSetCredentials**](/windows/previous-versions/eapmethodpeerapis/nf-eapmethodpeerapis-eappeersetcredentials?branch=master)                     | Supplies new or updated user credentials to the EAP method.                                                                                                                                                                 |
| [**EapPeerSetResponseAttributes**](/windows/previous-versions/eapmethodpeerapis/nf-eapmethodpeerapis-eappeersetresponseattributes?branch=master)       | Provides an updated array of EAP attributes to the EAP method.                                                                                                                                                              |
| [**EapPeerSetUIContext**](/windows/previous-versions/eapmethodpeerapis/nf-eapmethodpeerapis-eappeersetuicontext?branch=master)                         | Provides a user interface context to the EAP method.                                                                                                                                                                        |
| [**EapPeerShutdown**](/windows/previous-versions/eapmethodpeerapis/nf-eapmethodpeerapis-eappeershutdown?branch=master)                                 | Shuts down the EAP method and prepares to unload its corresponding DLL.                                                                                                                                                     |



 

## Related topics

<dl> <dt>

[EAPHost Peer Method Configuration Functions](eaphost-peer-method-run-time-functions.md)
</dt> </dl>

 

 




