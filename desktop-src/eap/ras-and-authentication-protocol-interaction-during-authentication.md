---
title: Access Point and Authentication Protocol Interaction During Authentication
description: The RasEapMakeMessage function controls the majority of the interaction between the authentication protocol and the Access Point (AP).
ms.assetid: edc128e0-3104-4df9-80f4-b2aebcfe1087
ms.topic: article
ms.date: 05/31/2018
---

# Access Point and Authentication Protocol Interaction During Authentication

The [**RasEapMakeMessage**](/previous-versions/windows/desktop/legacy/aa363532(v=vs.85)) function controls the majority of the interaction between the authentication protocol and the Access Point (AP). **RasEapMakeMessage** processes incoming EAP packets and creates EAP packets for transmission to the remote peer. It also processes events such as time outs and authentication completion.

If a message is received from the remote peer, the AP authentication service calls [**RasEapMakeMessage**](/previous-versions/windows/desktop/legacy/aa363532(v=vs.85)), passing a pointer to the received message in the *pReceivePacket* parameter.

If the service calls [**RasEapMakeMessage**](/previous-versions/windows/desktop/legacy/aa363532(v=vs.85)) with *pReceivePacket* set to **NULL**, the AP is either initiating the dialog with the authentication protocol, or requesting that the protocol resend the last packet. The authentication protocol should determine which action the service is taking based on its state and from the message context.

On return from [**RasEapMakeMessage**](/previous-versions/windows/desktop/legacy/aa363532(v=vs.85)), the value of the **Action** member of the [**PPP\_EAP\_OUTPUT**](/windows/desktop/api/Raseapif/ns-raseapif-ppp_eap_output) structure indicates what action, if any, the authentication service takes. The **Action** member takes values from the [**PPP\_EAP\_ACTION**](/windows/desktop/api/Raseapif/ne-raseapif-ppp_eap_action) enumerated type.

If **Action** is **EAPACTION\_Send**, **EAPACTION\_SendAndDone**, **EAPACTION\_SendWithTimeout**, or **EAPACTION\_SendWithTimeoutInteractive**, the service transmits the packet that is pointed to by the *pSendPacket* parameter to the remote peer.

The **EAPACTION\_SendWithTimeout** value allows for a time out, after which time the authentication service assumes the link was lost, and disconnects the session.

The **EAPACTION\_SendWithTimeoutInteractive** value allows an infinite amount of time out to occur. The authenticator should use this value when expecting user input on the client. This time out allows the user an unspecified amount of time to complete the required input.

If **Action** is **EAPACTION\_SendWithTimeout** or **EAPACTION\_SendWithTimeoutInteractive**, the authentication protocol should set the **dwIdExpected** member of the [**PPP\_EAP\_OUTPUT**](/windows/desktop/api/Raseapif/ns-raseapif-ppp_eap_output) structure to the identifier of the next packet that is expected from the remote peer. Regardless of whether the next packet received from the peer matches this value, the authentication service passes the packet to the authentication protocol in a subsequent call to [**RasEapMakeMessage**](/previous-versions/windows/desktop/legacy/aa363532(v=vs.85)). The authentication protocol may silently discard the packet by simply returning **ERROR\_PPP\_INVALID\_PACKET**. If a packet with the expected identifier is not received within the configured time-out period, the authentication service still calls **RasEapMakeMessage**. In this case, the call is made with the *pReceivePacket* parameter set to **NULL**, to indicate that the previous packet needs to be sent again.

If the **Action** member is **EAPACTION\_Done** or **EAPACTION\_SendAndDone**, the authentication service examines the **dwAuthResultCode** member of [**PPP\_EAP\_OUTPUT**](/windows/desktop/api/Raseapif/ns-raseapif-ppp_eap_output). If **dwAuthResultCode** is NO\_ERROR, the authentication succeeded. If **dwAuthResultCode** is a value other than NO\_ERROR, the authentication failed. The error code returned for the failure case should come from Raserror.h, Mprerror.h, or Winerror.h. Possible return codes include, but are not limited to, the following:

-   ERROR\_NO\_DIALIN\_PERMISSION
-   ERROR\_PASSWD\_EXPIRED
-   ERROR\_ACCT\_DISABLED
-   ERROR\_RESTRICTED\_LOGON\_HOURS
-   ERROR\_AUTH\_INTERNAL

In the case where **Action** is **EAPACTION\_Done** or **EAPACTION\_SendAndDone**, the **pUserAttributes** member should point to attributes that override attributes of the same type that were passed to the server in the call to [**RasEapBegin**](/previous-versions/windows/desktop/legacy/aa363520(v=vs.85)).

The authentication protocol on the server can request that the authentication service invoke the current authentication provider by returning **EAPACTION\_Authenticate** in the **Action** member in [**PPP\_EAP\_OUTPUT**](/windows/desktop/api/Raseapif/ns-raseapif-ppp_eap_output). In this case, the **pUserAttributes** pointer in **PPP\_EAP\_OUTPUT** points only to attributes that were generated by the authentication protocol on the server. It does not include any of the attributes that were passed to the server in the call to [**RasEapBegin**](/previous-versions/windows/desktop/legacy/aa363520(v=vs.85)). The authentication provider does not require these initial attributes because the authentication credentials are inside the EAP message itself, not in a separate RADIUS attribute. When the authentication service responds to the **EAPACTION\_Authenticate** action, **pUserAttributes** in [**PPP\_EAP\_INPUT**](/windows/desktop/api/Raseapif/ns-raseapif-ppp_eap_input), points to all attributes generated during authentication. These attributes are returned to the authentication protocol on the client.

If the authentication protocol uses **EAPACTION\_Authenticate**, the authentication provider performs either PAP or MD5-CHAP. This authentication method can be used only with Windows clients.

If the authentication protocol authenticates the user without relying on an authentication provider, there is no need for the protocol to ever set **Action** to **EAPACTION\_Authenticate**. An example of this case is EAP-Transport Layer Security (TLS).

The EAP success packet is a non-acknowledged packet. Therefore, it can be lost and not resent by the server. If the authentication service on the client receives a Network Control Protocol (NCP) packet, the server-side authentication service proceeds as though the authentication was successful. This is because the server has moved on to the NCP phase of PPP. Accordingly, the authentication service calls [**RasEapMakeMessage**](/previous-versions/windows/desktop/legacy/aa363532(v=vs.85)) with the **fSuccessPacketReceived** member of the [**PPP\_EAP\_INPUT**](/windows/desktop/api/Raseapif/ns-raseapif-ppp_eap_input) structure set to **TRUE**.

During the course of the authentication session, the authentication protocol may require interaction directly with the user on the client. The authentication protocol vendor can provide an interactive user interface for this purpose. The authentication protocol can request that the service display the interactive UI by setting the **fInvokeInteractiveUI**, **pUIContextData**, and **dwSizeOfUIContextData** members in the [**PPP\_EAP\_OUTPUT**](/windows/desktop/api/Raseapif/ns-raseapif-ppp_eap_output) structure. For more information on using an interactive UI, see [Interactive User Interface](interactive-user-interface.md).

The authentication protocol should display a user interface only through the mechanism described under [Interactive User Interface](interactive-user-interface.md). If the authentication protocol itself displays the user interface, the PPP thread blocks until the user interface is dismissed.

If during the authentication process, [**RasEapMakeMessage**](/previous-versions/windows/desktop/legacy/aa363532(v=vs.85)) returns any value other than **NO\_ERROR** or **ERROR\_PPP\_INVALID\_PACKET**, the session is disconnected and the error is logged (on the server) or displayed to the user (on the client).

 

 