---
title: Authenticator Method API Call Sequence
description: Learn about the authenticator method API call sequence. See a list that demonstrates the sequence of calls made by an EAPHost on an EAP authenticator method.
ms.assetid: 4756300c-5e49-44e8-ab49-1993d780d2a3
ms.topic: article
ms.date: 05/31/2018
---

# Authenticator Method API Call Sequence

This topic provides the specific call sequence for the authenticator method API. During a typical EAP authentication session EAPHost makes a number of calls on an EAP method that implement the EAPHost authenticator method APIs.

The following list demonstrates the sequence of calls made by EAPHost on an EAP authenticator method.

-   The EAP authenticator first loads the EAP method DLL used for the specific authentication on a network policy server (NPS) or other authentication server.
-   Calls [**EapAuthenticatorGetInfo**](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeergetinfo) on the method with a populated [**EAP\_TYPE**](/windows/desktop/api/eaptypes/ns-eaptypes-eap_type) structure to obtain a list of pointers to functions implemented on the DLL. Subsequent function calls by the authenticator methods (server) are assumed to be implemented on the DLL.
-   Calls [**EapAuthenticatorInitialize**](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerinitialize) to instruct the EAP method library to prepare for at least one authentication session using this authenticator method.
-   Calls [**EapMethodAuthenticatorBeginSession**](/previous-versions/windows/desktop/api/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorbeginsession) to establish a unique authentication session.
-   Repeats the following steps until [**EapMethodAuthenticatorReceivePacket**](/previous-versions/windows/desktop/api/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorreceivepacket) indicates that an authentication result is available.
    -   Calls [**EapMethodAuthenticatorSendPacket**](/previous-versions/windows/desktop/api/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorsendpacket) with a pointer to a request packet to pass to the supplicant.
    -   Calls [**EapMethodAuthenticatorReceivePacket**](/previous-versions/windows/desktop/api/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorreceivepacket) to retrieve the response packet sent by the supplicant. This function returns a **EAP\_METHOD\_AUTHENTICATOR\_RESPONSE\_ACTION** code that indicates the next action the authenticator must take in the EAP authentication session.
    -   If the action code is [EAP\_METHOD\_AUTHENTICATOR\_RESPONSE\_RESPOND](/windows/desktop/api/EapAuthenticatorActionDefine/ne-eapauthenticatoractiondefine-eap_method_authenticator_response_action), it indicates that the EAP method has attributes available for the authenticator to retrieve and pass to the peer method. Authenticator calls [**EapMethodAuthenticatorGetAttributes**](/previous-versions/windows/desktop/api/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorgetattributes) to obtain the various EAP authentication attributes from the EAP authenticator method. After the authenticator processes the attributes it calls [**EapMethodAuthenticatorSetAttributes**](/previous-versions/windows/desktop/api/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorsetattributes) which provides updated EAP authentication attributes to set on the EAP authenticator method. This function returns a **EAP\_METHOD\_AUTHENTICATOR\_RESPONSE\_ACTION** code which determines the subsequent action.
-   If the action code is [EAP\_METHOD\_AUTHENTICATOR\_RESPONSE\_RESULT](/windows/desktop/api/EapAuthenticatorActionDefine/ne-eapauthenticatoractiondefine-eap_method_authenticator_response_action), it indicates that the authenticator has determined the results of the authentication session, and those results are available to EAPHost. Authenticator calls [**EapMethodAuthenticatorGetResult**](/previous-versions/windows/desktop/api/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorgetresult) and obtains the results of the authentication session.
-   This is followed by a call to[**EapMethodAuthenticatorEndSession**](/previous-versions/windows/desktop/api/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorendsession) to end the authentication session.
-   Finally, a call is made to [**EapMethodAuthenticatorShutdown**](/previous-versions/windows/desktop/api/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorshutdown) to unload the authenticator method DLL.
-   Unloads the EAP method library.

## Related topics

<dl> <dt>

[**EAP\_METHOD\_AUTHENTICATOR\_RESPONSE\_ACTION**](/windows/desktop/api/EapAuthenticatorActionDefine/ne-eapauthenticatoractiondefine-eap_method_authenticator_response_action)
</dt> <dt>

[Supplicant API Call Sequence](supplicant-api-call-sequence.md)
</dt> <dt>

[Peer Method API Call Sequence](peer-method-api-call-sequence.md)
</dt> <dt>

[EAPHost Call Sequences](about-eaphost-call-sequences.md)
</dt> </dl>

 

 




