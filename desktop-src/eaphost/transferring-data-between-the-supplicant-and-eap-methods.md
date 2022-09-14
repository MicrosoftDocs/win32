---
title: Transferring Data Between the Supplicant and EAP Methods
description: Learn about transferring data between the Supplicant and EAP methods. Transferring data between methods is accomplished by using EAP attributes.
ms.assetid: f1bcff61-286a-4f18-8a5d-93d5d1fd2b5b
ms.topic: reference
ms.date: 05/31/2018
---

# Transferring Data Between the Supplicant and EAP Methods

Using EAP attributes allows data to be exchanged between supplicants and EAP methods.

## Attribute Consumption

[**EapHostPeerBeginSession**](/previous-versions/windows/desktop/api/eappapis/nf-eappapis-eaphostpeerbeginsession) consumes EAP attributes that are passed directly to the configured EAP method. Similarly, EAP methods are free to return an action code that indicates to the supplicant that attributes are available and that it should collect the attributes using [**EapHostPeerGetResponseAttributes**](/previous-versions/windows/desktop/api/eappapis/nf-eappapis-eaphostpeergetresponseattributes).

For more information, see the following topics.

-   [EAP Peer Supplicant Action Codes](/windows/win32/api/eaphostpeertypes/ne-eaphostpeertypes-eaphostpeerresponseaction).
-   [EAP Peer Supplicant Reason Codes](/windows/win32/api/eaphostpeertypes/ne-eaphostpeertypes-eaphostpeermethodresultreason).
-   [EAP Authenticator Method Action Codes](/windows/desktop/api/EapAuthenticatorActionDefine/ne-eapauthenticatoractiondefine-eap_method_authenticator_response_action).

Supplicants are expected to ignore attributes that they do not recognize or cannot act upon. Using [**EapHostPeerSetResponseAttributes**](/previous-versions/windows/desktop/api/eappapis/nf-eappapis-eaphostpeersetresponseattributes) these ignored attributes are sent back to EAPHost and the EAP method.

## Vendor Specific Attributes

By using the vendor-specific EAP attribute, EAP methods and supplicants can engage in data exchange for a specific purpose. Vendor-specific attributes are ignored by supplicants and methods that do not support the vendor-specific attribute.

For more information, see the following topics.

-   [EAP Attributes](about-eap-attributes.md).
-   [**EAP\_ATTRIBUTE\_TYPE**](/windows/desktop/api/eaptypes/ne-eaptypes-eap_attribute_type).

## Related topics

<dl> <dt>

[Configuring the EAP Method User Interface](configuring-the-eap-method-user-interface.md)
</dt> <dt>

[Enabling Group Policy](enabling-group-policy.md)
</dt> <dt>

[Implementing In-Band NAP Support for EAP Methods](enabling-in-band-nap-support.md)
</dt> <dt>

[Implementing NAP Support for EAP Methods](implementing-nap-for-eap-methods.md)
</dt> <dt>

[EAPHost Supplicants](eaphost-supplicants.md)
</dt> </dl>

 

 




