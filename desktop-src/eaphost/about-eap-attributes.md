---
title: EAP Attributes
description: Is an EAP\_ATTRIBUTE structure that contains a predetermined type of data relating to an authentication session.
ms.assetid: 3c54cca2-cd3b-4149-bb0e-036d490cdd3b
ms.topic: article
ms.date: 05/31/2018
---

# EAP Attributes

An EAP attribute is an [**EAP\_ATTRIBUTE**](/windows/desktop/api/eaptypes/ns-eaptypes-eap_attribute) structure that contains a predetermined type of data relating to an authentication session. Attributes are used to communicate information between EAP methods and supplicants or between EAP methods and authenticators. Peer and authenticator implementations of an EAP method may exchange these attributes over a network.

A complete list of supported attribute types appears in the topic [**EAP\_ATTRIBUTE\_TYPE**](/windows/desktop/api/eaptypes/ne-eaptypes-eap_attribute_type).

## Attributes Consumed by Supplicants

The following attribute types are consumed by 802.1X supplicants.

-   **eatVendorSpecific**

The following attribute types are consumed by PPP client supplicants.

-   **eatMinimum**
-   **eatEAPTLV**

The following attribute types are consumed by PPP server supplicants.

-   **eatUserName**
-   **eatReplyMessage**
-   **eatState**
-   **eatSessionTimeout**
-   **eatEAPMessage**

## Attributes Exported by Methods

The following attribute types could be exported by EAP methods.

-   **eatClearTextPassword**
-   **eatQuarantineSoH**
-   **eatMethodId**

The following attribute type is exported by EAP [Transport Level Security (TLS)](/previous-versions/windows/embedded/ms885336(v=msdn.10)) (EAP-TLS) methods.

-   **eatCertificateOID**

The following attribute types are exported by [Microsoft Challenge Handshake Authentication Protocol version 2.0](/previous-versions/windows/embedded/ms899190(v=msdn.10)) (MS-CHAPv2) methods.

-   **eatUserName**
-   **eatCredentialsChanged**

The following attribute type is consumed by Network Policy Server (NPS).

-   **eatCertificateOID**

The following attribute types are exported by [Protected Extensible Authentication Protocol (PEAP)](/previous-versions/windows/embedded/ms899190(v=msdn.10)) methods.

-   **eatUserName**
-   **eatPEAPEmbeddedEAPTypeId**
-   **eatPEAPFastRoamedSession**
-   **eatQuarantineSoH**

## Related topics

<dl> <dt>

[**EAP\_ATTRIBUTE**](/windows/desktop/api/eaptypes/ns-eaptypes-eap_attribute)
</dt> <dt>

[**EAP\_ATTRIBUTE\_TYPE**](/windows/desktop/api/eaptypes/ne-eaptypes-eap_attribute_type)
</dt> </dl>

 

 