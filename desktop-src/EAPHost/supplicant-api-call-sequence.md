---
title: Supplicant API Call Sequence
description: Provides the specific call sequence for the supplicant API.
ms.assetid: '83276783-aee5-43ac-982d-1144df982a7d'
---

# Supplicant API Call Sequence

This topic provides the specific call sequence for the supplicant API.

## Supplicant API Call Sequence Overview

When the supplicant receives an EAP packet from a provider, such as an access point, the following supplicant API call flow typically occurs.

-   The application calls [**EapHostPeerBeginSession**](eaphostpeerbeginsession.md) with EAPHost configuration data and user data. A successful call returns an **EAP\_SESSION\_HANDLE** session handle.
-   Each packet received by the supplicant is processed by a call to [**EapHostPeerProcessReceivedPacket**](eaphostpeerprocessreceivedpacket.md). The supplicant then calls the function corresponding to the action code returned by the function.
-   If the action code is **EapHostPeerResponseSend**, then the supplicant calls [**EapHostPeerGetSendPacket**](eaphostpeergetsendpacket.md) to obtain the response to be sent to the authenticator.
-   If during the session, the action code returned to the supplicant is **EapHostPeerResponseRespond**, it indicates that EAP attributes are available. The supplicant then calls [**EapHostPeerGetResponseAttributes**](eaphostpeergetresponseattributes.md) to obtain them. These attributes contain supplemental data used during the authentication process. After supplicant completes processing the attributes it calls [**EapHostPeerSetResponseAttributes**](eaphostpeersetresponseattributes.md) which updates the data. This function returns an action code which determines the supplicant's next action.
-   If the action code is **EapHostPeerResponseInvokeUI** the supplicant raises a user interface dialog to obtain interactive data from the user, such as credentials or identity information. See User Interaction with the Supplicant API Call Flow below.
-   If the action code is **EapHostPeerResponseResult**, it indicates that the results of the authentication session are available to the supplicant. The supplicant then calls [**EapHostPeerGetResult**](eaphostpeergetresult.md) to obtain the results. Regardless of whether the results indicate success or failure, the supplicant calls [**EapHostPeerEndSession**](eaphostpeerendsession.md). In the case of failure, re-authentication can be attempted by opening another session with EAPHost and providing a new identity, or attempting authentication with the original identity again.

## User Interaction with the Supplicant API Call Flow

In certain cases, the supplicant needs to obtain information from the user to continue the authentication process.

The following list demonstrates the sequence of calls on the supplicant and EAPHost UI process necessary to enable interactive input.

1.  The supplicant obtains the current user interface context by calling [**EapHostPeerGetUIContext**](eaphostpeergetuicontext.md).
2.  The supplicant then sends the UI context data to the supplicant UI process.
    > [!Note]  
    > The UI process, which typically collects UI or handles interactive UI, is separate from the supplicant process. Separating the two processes is not a requirement of EAPHost, but doing so has the advantage of allowing the UI process to interact with the desktop.

     

3.  If the supplicant wants to render the UI by itself then it calls the [**EapHostPeerQueryInteractiveUIInputFields**](eaphostpeerqueryinteractiveuiinputfields.md) function to obtain the input fields for interactive UI components to be raised. Otherwise, it follows the traditional model of invoking method interactive UI by calling [**EapHostPeerInvokeInteractiveUI**](eaphostpeerinvokeinteractiveui.md)
    > [!Note]  
    > If [**EAP\_E\_EAPHOST\_METHOD\_OPERATION\_NOT\_SUPPORTED**](eap-related-error-and-information-constants.md) is returned, the supplicant must follow the traditional model of invoking method interactive UI by calling [**EapHostPeerInvokeInteractiveUI**](eaphostpeerinvokeinteractiveui.md). If there is an error, [**EapHostPeerQueryInteractiveUIInputFields**](eaphostpeerqueryinteractiveuiinputfields.md) will return a return code other than **NULL**.

     

4.  Whether the supplicant calls [**EapHostPeerQueryInteractiveUIInputFields**](eaphostpeerqueryinteractiveuiinputfields.md) or [**EaphostPeerInvokeInteractiveUI**](eaphostpeerinvokeinteractiveui.md) the UI process passes the existing context data and loads Eappcfg.dll. Appropriate UI is raised to collect the new data. The new UI context data, which may now contain user input, is copied, and the old context data is released with a call to [**EapPeerFreeMemory**](eappeerfreememory.md).
5.  The UI process returns the new context data to the supplicant, which calls [**EapHostPeerSetUIContext**](eaphostpeersetuicontext.md) to set it.

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

 

 




