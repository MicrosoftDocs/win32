---
title: Supplicant API Call Sequence
description: Learn about the supplicant API call sequence. See an overview of the call sequence and view additional available resources.
ms.assetid: 83276783-aee5-43ac-982d-1144df982a7d
ms.topic: article
ms.date: 05/31/2018
---

# Supplicant API Call Sequence

This topic provides the specific call sequence for the supplicant API.

## Supplicant API Call Sequence Overview

When the supplicant receives an EAP packet from a provider, such as an access point, the following supplicant API call flow typically occurs.

-   The application calls [**EapHostPeerBeginSession**](/previous-versions/windows/desktop/api/eappapis/nf-eappapis-eaphostpeerbeginsession) with EAPHost configuration data and user data. A successful call returns an **EAP\_SESSION\_HANDLE** session handle.
-   Each packet received by the supplicant is processed by a call to [**EapHostPeerProcessReceivedPacket**](/previous-versions/windows/desktop/api/eappapis/nf-eappapis-eaphostpeerprocessreceivedpacket). The supplicant then calls the function corresponding to the action code returned by the function.
-   If the action code is **EapHostPeerResponseSend**, then the supplicant calls [**EapHostPeerGetSendPacket**](/previous-versions/windows/desktop/api/eappapis/nf-eappapis-eaphostpeergetsendpacket) to obtain the response to be sent to the authenticator.
-   If during the session, the action code returned to the supplicant is **EapHostPeerResponseRespond**, it indicates that EAP attributes are available. The supplicant then calls [**EapHostPeerGetResponseAttributes**](/previous-versions/windows/desktop/api/eappapis/nf-eappapis-eaphostpeergetresponseattributes) to obtain them. These attributes contain supplemental data used during the authentication process. After supplicant completes processing the attributes it calls [**EapHostPeerSetResponseAttributes**](/previous-versions/windows/desktop/api/eappapis/nf-eappapis-eaphostpeersetresponseattributes) which updates the data. This function returns an action code which determines the supplicant's next action.
-   If the action code is **EapHostPeerResponseInvokeUI** the supplicant raises a user interface dialog to obtain interactive data from the user, such as credentials or identity information. See User Interaction with the Supplicant API Call Flow below.
-   If the action code is **EapHostPeerResponseResult**, it indicates that the results of the authentication session are available to the supplicant. The supplicant then calls [**EapHostPeerGetResult**](/previous-versions/windows/desktop/api/eappapis/nf-eappapis-eaphostpeergetresult) to obtain the results. Regardless of whether the results indicate success or failure, the supplicant calls [**EapHostPeerEndSession**](/previous-versions/windows/desktop/api/eappapis/nf-eappapis-eaphostpeerendsession). In the case of failure, re-authentication can be attempted by opening another session with EAPHost and providing a new identity, or attempting authentication with the original identity again.

## User Interaction with the Supplicant API Call Flow

In certain cases, the supplicant needs to obtain information from the user to continue the authentication process.

The following list demonstrates the sequence of calls on the supplicant and EAPHost UI process necessary to enable interactive input.

1.  The supplicant obtains the current user interface context by calling [**EapHostPeerGetUIContext**](/previous-versions/windows/desktop/api/eappapis/nf-eappapis-eaphostpeergetuicontext).
2.  The supplicant then sends the UI context data to the supplicant UI process.
    > [!Note]  
    > The UI process, which typically collects UI or handles interactive UI, is separate from the supplicant process. Separating the two processes is not a requirement of EAPHost, but doing so has the advantage of allowing the UI process to interact with the desktop.

     

3.  If the supplicant wants to render the UI by itself then it calls the [**EapHostPeerQueryInteractiveUIInputFields**](/previous-versions/windows/desktop/api/eaphostpeerconfigapis/nf-eaphostpeerconfigapis-eaphostpeerqueryinteractiveuiinputfields) function to obtain the input fields for interactive UI components to be raised. Otherwise, it follows the traditional model of invoking method interactive UI by calling [**EapHostPeerInvokeInteractiveUI**](/previous-versions/windows/desktop/api/eaphostpeerconfigapis/nf-eaphostpeerconfigapis-eaphostpeerinvokeinteractiveui)
    > [!Note]  
    > If [**EAP\_E\_EAPHOST\_METHOD\_OPERATION\_NOT\_SUPPORTED**](eap-related-error-and-information-constants.md) is returned, the supplicant must follow the traditional model of invoking method interactive UI by calling [**EapHostPeerInvokeInteractiveUI**](/previous-versions/windows/desktop/api/eaphostpeerconfigapis/nf-eaphostpeerconfigapis-eaphostpeerinvokeinteractiveui). If there is an error, [**EapHostPeerQueryInteractiveUIInputFields**](/previous-versions/windows/desktop/api/eaphostpeerconfigapis/nf-eaphostpeerconfigapis-eaphostpeerqueryinteractiveuiinputfields) will return a return code other than **NULL**.

     

4.  Whether the supplicant calls [**EapHostPeerQueryInteractiveUIInputFields**](/previous-versions/windows/desktop/api/eaphostpeerconfigapis/nf-eaphostpeerconfigapis-eaphostpeerqueryinteractiveuiinputfields) or [**EaphostPeerInvokeInteractiveUI**](/previous-versions/windows/desktop/api/eaphostpeerconfigapis/nf-eaphostpeerconfigapis-eaphostpeerinvokeinteractiveui) the UI process passes the existing context data and loads Eappcfg.dll. Appropriate UI is raised to collect the new data. The new UI context data, which may now contain user input, is copied, and the old context data is released with a call to [**EapPeerFreeMemory**](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerfreememory).
5.  The UI process returns the new context data to the supplicant, which calls [**EapHostPeerSetUIContext**](/previous-versions/windows/desktop/api/eappapis/nf-eappapis-eaphostpeersetuicontext) to set it.

## Related topics

<dl> <dt>

[Peer Method API Call Sequence](peer-method-api-call-sequence.md)
</dt> <dt>

[Authenticator Method API Call Sequence](authenticator-method-api-call-sequence.md)
</dt> <dt>

[EAPHost Call Sequence](about-eaphost-call-sequences.md)
</dt> <dt>

[EAPHost Supplicants](eaphost-supplicants.md)
</dt> </dl>

 

 




