---
title: Authenticator Method API Call Sequence
description: Provides the specific call sequence for the authenticator method API.
ms.assetid: '4756300c-5e49-44e8-ab49-1993d780d2a3'
---

# Authenticator Method API Call Sequence

This topic provides the specific call sequence for the authenticator method API. During a typical EAP authentication session EAPHost makes a number of calls on an EAP method that implement the EAPHost authenticator method APIs.

The following list demonstrates the sequence of calls made by EAPHost on an EAP authenticator method.

-   The EAP authenticator first loads the EAP method DLL used for the specific authentication on a network policy server (NPS) or other authentication server.
-   Calls [**EapAuthenticatorGetInfo**](eappeergetinfo.md) on the method with a populated [**EAP\_TYPE**](eap-type.md) structure to obtain a list of pointers to functions implemented on the DLL. Subsequent function calls by the authenticator methods (server) are assumed to be implemented on the DLL.
-   Calls [**EapAuthenticatorInitialize**](eappeerinitialize.md) to instruct the EAP method library to prepare for at least one authentication session using this authenticator method.
-   Calls [**EapMethodAuthenticatorBeginSession**](eapmethodauthenticatorbeginsession.md) to establish a unique authentication session.
-   Repeats the following steps until [**EapMethodAuthenticatorReceivePacket**](eapmethodauthenticatorreceivepacket.md) indicates that an authentication result is available.
    -   Calls [**EapMethodAuthenticatorSendPacket**](eapmethodauthenticatorsendpacket.md) with a pointer to a request packet to pass to the supplicant.
    -   Calls [**EapMethodAuthenticatorReceivePacket**](eapmethodauthenticatorreceivepacket.md) to retrieve the response packet sent by the supplicant. This function returns a **EAP\_METHOD\_AUTHENTICATOR\_RESPONSE\_ACTION** code that indicates the next action the authenticator must take in the EAP authentication session.
    -   If the action code is [EAP\_METHOD\_AUTHENTICATOR\_RESPONSE\_RESPOND](eap-method-authenticator-response-action.md), it indicates that the EAP method has attributes available for the authenticator to retrieve and pass to the peer method. Authenticator calls [**EapMethodAuthenticatorGetAttributes**](eapmethodauthenticatorgetattributes.md) to obtain the various EAP authentication attributes from the EAP authenticator method. After the authenticator processes the attributes it calls [**EapMethodAuthenticatorSetAttributes**](eapmethodauthenticatorsetattributes.md) which provides updated EAP authentication attributes to set on the EAP authenticator method. This function returns a **EAP\_METHOD\_AUTHENTICATOR\_RESPONSE\_ACTION** code which determines the subsequent action.
-   If the action code is [EAP\_METHOD\_AUTHENTICATOR\_RESPONSE\_RESULT](eap-method-authenticator-response-action.md), it indicates that the authenticator has determined the results of the authentication session, and those results are available to EAPHost. Authenticator calls [**EapMethodAuthenticatorGetResult**](eapmethodauthenticatorgetresult.md) and obtains the results of the authentication session.
-   This is followed by a call to[**EapMethodAuthenticatorEndSession**](eapmethodauthenticatorendsession.md) to end the authentication session.
-   Finally, a call is made to [**EapMethodAuthenticatorShutdown**](eapmethodauthenticatorshutdown.md) to unload the authenticator method DLL.
-   Unloads the EAP method library.

## Related topics

<dl> <dt>

[**EAP\_METHOD\_AUTHENTICATOR\_RESPONSE\_ACTION**](eap-method-authenticator-response-action.md)
</dt> <dt>

[Supplicant API Call Sequence](supplicant-api-call-sequence.md)
</dt> <dt>

[Peer Method API Call Sequence](peer-method-api-call-sequence.md)
</dt> <dt>

[EAPHost Call Sequences](about-eaphost-call-sequences.md)
</dt> </dl>

 

 




