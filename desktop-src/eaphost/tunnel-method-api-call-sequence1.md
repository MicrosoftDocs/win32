---
title: Tunnel Method API Call Sequence
description: Learn about the API call sequence for Tunnel Methods. See an overview and view additional available resources.
ms.assetid: 48aad213-1d29-4809-9599-b56325b2b8e8
ms.topic: article
ms.date: 05/31/2018
---

# Tunnel Method API Call Sequence

This topic covers the API call sequence for Tunnel Methods

## Tunnel Method Call Sequence Overview

When Supplicant gets request for user identity and user data the following API call flow typically occurs.

-   The Supplicant calls EapHostPeerProcessReceivedPacket on EapHost, to process the packet received from the authenticator.
-   Upon processing this packet, EAPHost determines it as IdentityRequest packet and calls [**EapPeerGetIdentity**](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeergetidentity) on tunnel method to obtain the user identity to use for authentication.
-   If tunnel method needs to obtain user identity from the inner method, it calls [**EAPHostPeerGetIdentity**](/previous-versions/windows/desktop/api/eappapis/nf-eappapis-eaphostpeergetidentity) on inner EAPHost, which in turn calls [**EapPeerGetIdentity**](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeergetidentity) on the inner method.

## User Interaction with the Tunnel Methods API Call Flow

In certain cases, when the identity is not available, or when the user must provide additional information, Eap Method raises an user interface dialog box on the supplicant.

In such cases following call sequence typically takes place to get information directly from the user.

-   Tunnel Eap Method returns action code to invoke UI to EapHost. Supplicant calls [**EapHostPeerGetUIContext**](/previous-versions/windows/desktop/api/eappapis/nf-eappapis-eaphostpeergetuicontext)to obtain the current user interface context information for the user interface dialog box.
-   Supplicant then calls [**EapHostPeerInvokeInteractiveUI.**](/previous-versions/windows/desktop/api/eaphostpeerconfigapis/nf-eaphostpeerconfigapis-eaphostpeerinvokeinteractiveui) This function uses the UI context information to raise an interactive user interface which is used to get credential information from the user. The UI process loads Eappcfg.dll and obtains the pointers to EapPeerInvokeInteractiveUI and EapPeerFreeMemory.
    > [!Note]  
    > UI process typically collects UI or handles interactive UI and is separate from the supplicant process. Separating the two processes is not a requirement of EAPHost, but doing so has the advantage of allowing the UI process to interact with the desktop.

     

-   EapHost calls [**EapPeerInvokeIdentityUI**](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerinvokeidentityui) on tunnel method to obtain user identity information.
-   In order to obtain user identity from inner method, tunnel method calls [**EapHostPeerInvokeIdentityUI**](/previous-versions/windows/desktop/api/eaphostpeerconfigapis/nf-eaphostpeerconfigapis-eaphostpeerinvokeidentityui) on inner EAPHost.
-   Inner EAPHost calls [**EapPeerInvokeIdentityUI**](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerinvokeidentityui) on inner method to invoke user identity UI.
-   [**EapHostPeerSetUIContext**](/previous-versions/windows/desktop/api/eappapis/nf-eappapis-eaphostpeersetuicontext) provides a new or updated UI context information to the EAP peer method loaded on EAPHost after the UI has been raised.

Following diagram explains the API Call Sequence for Tunnel Methods

![tunnel methods api call sequence](images/tunnel-identity-processing-new.png)

## Related topics

<dl> <dt>

[EAPHost Call Sequence](about-eaphost-call-sequences.md)
</dt> <dt>

[Supplicant API Call Sequence](supplicant-api-call-sequence.md)
</dt> <dt>

[EAPHost Supplicant API Reference](eap-host-supplicant-api-reference.md)
</dt> </dl>

 

 




