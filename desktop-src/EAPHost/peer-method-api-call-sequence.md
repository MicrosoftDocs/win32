---
title: Peer Method API Call Sequence
description: Provides the specific call sequence for the peer method API.
ms.assetid: aac69e89-249d-4bc8-baef-1f0681f9f7ae
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Peer Method API Call Sequence

This topic provides the specific call sequence for the peer method API. During a typical EAP authentication session EAPHost makes a number of calls on EAP methods to implement the EAPHost peer method API.

The following list demonstrates the sequence of calls made by EAPHost on an EAP peer method.

-   Loads the EAP peer method DLL used for the authentication.
-   Calls [**EapPeerGetInfo**](/windows/previous-versions/eapmethodpeerapis/nf-eapmethodpeerapis-eappeergetinfo?branch=master) on the method to obtain a list of pointers to functions implemented on the DLL. Subsequent function calls by the EAPHost peer (client) are assumed to be implemented on the DLL.
-   Calls [**EapPeerInitialize**](/windows/previous-versions/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerinitialize?branch=master) to instruct the EAP Method Library to prepare for at least one authentication session using this peer method.
-   Calls [**EapPeerBeginSession**](/windows/previous-versions/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerbeginsession?branch=master) to establish a unique authentication session.
-   Calls [**EapPeerGetIdentity**](/windows/previous-versions/eapmethodpeerapis/nf-eapmethodpeerapis-eappeergetidentity?branch=master) to obtain the identity to use for authentication. If the identity is not available, or if the user must provide additional information, EAPHost calls [**EapPeerGetUIContext.**](/windows/previous-versions/eapmethodpeerapis/nf-eapmethodpeerapis-eappeergetuicontext?branch=master) This function obtains the context information for the user interface dialog box that will be raised on the supplicant. After the user has submitted the identity information, the user identity is set with a call to [**EapPeerSetUIContext**](/windows/previous-versions/eapmethodpeerapis/nf-eapmethodpeerapis-eappeersetuicontext?branch=master), and obtained by a call to **EapPeerGetIdentity**.
-   Repeats the following steps until [**EapPeerProcessRequestPacket**](/windows/previous-versions/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerprocessrequestpacket?branch=master) indicates that an authentication result is available.
    -   Calls [**EapPeerProcessRequestPacket**](/windows/previous-versions/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerprocessrequestpacket?branch=master) with the pointer of a request packet to pass to the supplicant.
    -   Calls **EapPeerGetResponsePacket** to retrieve the response packet to send to the authenticator.
    -   Optionally, if EAP attributes need to be retrieved or sent during the authentication session, EAPHost calls [**EapPeerGetResponseAttributes**](/windows/previous-versions/eapmethodpeerapis/nf-eapmethodpeerapis-eappeergetresponseattributes?branch=master) and [**EapPeerSetResponseAttributes**](/windows/previous-versions/eapmethodpeerapis/nf-eapmethodpeerapis-eappeersetresponseattributes?branch=master) respectively.
-   When the authenticator sends an action code that indicates authentication is complete, EAPHost calls [**EapPeerGetResult**](/windows/previous-versions/eapmethodpeerapis/nf-eapmethodpeerapis-eappeergetresult?branch=master) and obtains the results of the authentication.
-   Calls [**EapPeerEndSession**](/windows/previous-versions/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerendsession?branch=master) to end the authentication session.
-   Calls [**EapPeerShutdown**](/windows/previous-versions/eapmethodpeerapis/nf-eapmethodpeerapis-eappeershutdown?branch=master) to unload the peer method DLL.
-   Unloads the EAP Method Library.

## Related topics

<dl> <dt>

[Supplicant API Call Sequence](supplicant-api-call-sequence.md)
</dt> <dt>

[Authenticator Method API Call Sequence](authenticator-method-api-call-sequence.md)
</dt> <dt>

[EAPHost Call Sequences](about-eaphost-call-sequences.md)
</dt> </dl>

 

 




