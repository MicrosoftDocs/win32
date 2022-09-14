---
title: Implementing In-Band NAP Support for EAP Methods
description: Can be enabled for EAPHost EAP methods that support the transmission of type-length-value objects (TLVs).
ms.assetid: 298c89d9-7a6a-4280-9af9-77c7c00cab92
ms.topic: reference
ms.date: 05/31/2018
---

# Implementing In-Band NAP Support for EAP Methods

In-band [Network Access Protection](/windows/desktop/NAP/network-access-protection-start-page) (NAP) support for an EAP method can be enabled for EAPHost EAP methods that support the transmission of type-length-value objects (TLVs). When in-band NAP support is enabled, NAP packets are transported inside EAP method packets.

In contrast, when out-of-band NAP support is enabled, the NAP [Statement of Health](https://go.microsoft.com/fwlink/p/?linkid=83917) (SoH) exchange occurs through means other than internal to EAP method packets.

All TLVs are vendor specific.

## Implementing NAP Support on EAP Peer Methods

The EAP peer method implementation receives a TLV containing the [Statement of Health](https://go.microsoft.com/fwlink/p/?linkid=83917) (SoH) request TLV from an EAP server.

The EAP peer method implementation then passes the TLV containing the SoH request TLV to EAPHost as follows.

-   The EAP peer method implementation returns the action code [**EapPeerMethodResponseActionRespond**](/windows/win32/api/eapauthenticatoractiondefine/ne-eapauthenticatoractiondefine-eappeermethodresponseaction) to EAPHost on return from [**EapPeerProcessRequestPacket**](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerprocessrequestpacket).
-   EAPHost calls [**EapPeerGetResponseAttributes**](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeergetresponseattributes) from the EAP peer method implementation. The attributes are passed in the process.
-   The EAP peer method implementation returns the TLV containing the SoH request TLV in [**EapPeerGetResponseAttributes**](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeergetresponseattributes). The attributes are received in the process.

The EAP peer method implementation receives a TLV containing an SoH TLV from EAPHost as follows.

-   EAPHost calls [**EapPeerSetResponseAttributes**](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeersetresponseattributes) from the EAP peer method implementation. **EapPeerSetResponseAttributes** contains a TLV that houses an SoH TLV.
-   The EAP peer method implementation sends the SoH TLV to the EAP server.
-   The EAP peer method implementation receives a TLV containing an SoH response TLV from the EAP server.

The EAP peer method implementation passes the TLV containing the SoH response TLV to EAPHost as follows.

-   The EAP peer method implementation returns the action code **EapPeerMethodResponseActionRespond** to EAPHost on return from [**EapPeerProcessRequestPacket**](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerprocessrequestpacket).
-   EAPHost calls [**EapPeerGetResponseAttributes**](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeergetresponseattributes) from the EAP peer method implementations. The [**EAP\_ATTRIBUTES**](/windows/desktop/api/eaptypes/ns-eaptypes-eap_attributes) structure is passed in the process.
-   The EAP peer method implementation returns the TLV containing the SoH response TLV in [**EapPeerSetResponseAttributes**](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeersetresponseattributes).

> [!Note]  
> The **eapType** member of the [**EAP\_ATTRIBUTE**](/windows/desktop/api/eaptypes/ns-eaptypes-eap_attribute) structure will always be set to **eatEAPTLV** and the **pValue** member will point to the first byte of the TLV that contains the SoH response TLV.

 

### Implementing NAP Support on EAP Server Methods

The EAP server method implementation constructs a TLV containing an SoH request TLV. The EAP server method implementation sends this TLV containing the SoH Request TLV to the EAP peer. The EAP server method implementation receives the TLV from the EAP peer.

The EAP server method implementation passes the TLV containing an SoH TLV to EAPHost as follows.

-   The EAP server method implementation returns the action code **EAP\_METHOD\_AUTHENTICATOR\_RESPONSE\_RESPOND** to EAPHost on return from [**EapMethodAuthenticatorReceivePacket**](/previous-versions/windows/desktop/api/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorreceivepacket).
-   EAPHost calls [**EapMethodAuthenticatorGetAttributes**](/previous-versions/windows/desktop/api/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorgetattributes) from the EAP server method implementation.
-   The EAP server method implementation returns the TLV containing the SoH TLV in [**EapMethodAuthenticatorGetAttributes**](/previous-versions/windows/desktop/api/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorgetattributes).

The EAP server method implementation receives a TLV containing an SoH response TLV from EAPHost as follows.

-   EAPHost calls [**EapMethodAuthenticatorSetAttributes**](/previous-versions/windows/desktop/api/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorsetattributes) from the EAP server method implementation.
-   The TLV containing the SoH response TLV is returned in [**EapMethodAuthenticatorSetAttributes**](/previous-versions/windows/desktop/api/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorsetattributes)
-   The EAP server method implementation sends the TLV containing the SoH response TLV.

> [!Note]  
> The **eapType** member of the [**EAP\_ATTRIBUTE**](/windows/desktop/api/eaptypes/ns-eaptypes-eap_attribute) structure will always be set to **eatEAPTLV** and the **pValue** member will point to the first byte of the TLV that contains the SoH response TLV.

 

### Messages

The EAP SoH TLV is used to encapsulate the SoH protocol for transmission via an EAP method. All EAP SoH TLVs have the same structure, differing only on the message ID and data portion of the message.

For more information, see [Network Access Protection (NAP) Statement of Health (SoH) Messages](https://go.microsoft.com/fwlink/p/?linkid=83918).

## Related topics

<dl> <dt>

[Configuring the EAP Method User Interface](configuring-the-eap-method-user-interface.md)
</dt> <dt>

[Enabling Group Policy](enabling-group-policy.md)
</dt> <dt>

[Implementing NAP Support for EAP Methods](implementing-nap-for-eap-methods.md)
</dt> <dt>

[Transferring Data Between the Supplicant and EAP Methods](transferring-data-between-the-supplicant-and-eap-methods.md)
</dt> <dt>

[EAPHost Supplicants](eaphost-supplicants.md)
</dt> </dl>

 

 