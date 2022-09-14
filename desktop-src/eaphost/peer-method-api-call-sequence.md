---
title: Peer Method API Call Sequence
description: Learn about the peer method API call sequence. See a list that demonstrates the sequence of calls made by an EAPHost on an EAP peer method.
ms.assetid: aac69e89-249d-4bc8-baef-1f0681f9f7ae
ms.topic: article
ms.date: 05/31/2018
---

# Peer Method API Call Sequence

This topic provides the specific call sequence for the peer method API. During a typical EAP authentication session EAPHost makes a number of calls on EAP methods to implement the EAPHost peer method API.

The following list demonstrates the sequence of calls made by EAPHost on an EAP peer method.

-   Loads the EAP peer method DLL used for the authentication.
-   Calls [**EapPeerGetInfo**](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeergetinfo) on the method to obtain a list of pointers to functions implemented on the DLL. Subsequent function calls by the EAPHost peer (client) are assumed to be implemented on the DLL.
-   Calls [**EapPeerInitialize**](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerinitialize) to instruct the EAP Method Library to prepare for at least one authentication session using this peer method.
-   Calls [**EapPeerBeginSession**](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerbeginsession) to establish a unique authentication session.
-   Calls [**EapPeerGetIdentity**](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeergetidentity) to obtain the identity to use for authentication. If the identity is not available, or if the user must provide additional information, EAPHost calls [**EapPeerGetUIContext.**](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeergetuicontext) This function obtains the context information for the user interface dialog box that will be raised on the supplicant. After the user has submitted the identity information, the user identity is set with a call to [**EapPeerSetUIContext**](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeersetuicontext), and obtained by a call to **EapPeerGetIdentity**.
-   Repeats the following steps until [**EapPeerProcessRequestPacket**](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerprocessrequestpacket) indicates that an authentication result is available.
    -   Calls [**EapPeerProcessRequestPacket**](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerprocessrequestpacket) with the pointer of a request packet to pass to the supplicant.
    -   Calls **EapPeerGetResponsePacket** to retrieve the response packet to send to the authenticator.
    -   Optionally, if EAP attributes need to be retrieved or sent during the authentication session, EAPHost calls [**EapPeerGetResponseAttributes**](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeergetresponseattributes) and [**EapPeerSetResponseAttributes**](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeersetresponseattributes) respectively.
-   When the authenticator sends an action code that indicates authentication is complete, EAPHost calls [**EapPeerGetResult**](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeergetresult) and obtains the results of the authentication.
-   Calls [**EapPeerEndSession**](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerendsession) to end the authentication session.
-   Calls [**EapPeerShutdown**](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeershutdown) to unload the peer method DLL.
-   Unloads the EAP Method Library.

## Related topics

<dl> <dt>

[Supplicant API Call Sequence](supplicant-api-call-sequence.md)
</dt> <dt>

[Authenticator Method API Call Sequence](authenticator-method-api-call-sequence.md)
</dt> <dt>

[EAPHost Call Sequences](about-eaphost-call-sequences.md)
</dt> </dl>

 

 




