---
title: EAP Attributes
description: Is an EAP\_ATTRIBUTE structure that contains a predetermined type of data relating to an authentication session.
ms.assetid: 3c54cca2-cd3b-4149-bb0e-036d490cdd3b
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# EAP Attributes

An EAP attribute is an [**EAP\_ATTRIBUTE**](/windows/previous-versions/eaptypes/ns-eaptypes-_eap_attribute?branch=master) structure that contains a predetermined type of data relating to an authentication session. Attributes are used to communicate information between EAP methods and supplicants or between EAP methods and authenticators. Peer and authenticator implementations of an EAP method may exchange these attributes over a network.

A complete list of supported attribute types appears in the topic [**EAP\_ATTRIBUTE\_TYPE**](/windows/previous-versions/eaptypes/ne-eaptypes-_eap_attribute_type?branch=master).

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

The following attribute type is exported by EAP [Transport Level Security (TLS)](Http://go.microsoft.com/fwlink/p/?linkid=83935) (EAP-TLS) methods.

-   **eatCertificateOID**

The following attribute types are exported by [Microsoft Challenge Handshake Authentication Protocol version 2.0](Http://go.microsoft.com/fwlink/p/?linkid=83939) (MS-CHAPv2) methods.

-   **eatUserName**
-   **eatCredentialsChanged**

The following attribute type is consumed by Network Policy Server (NPS).

-   **eatCertificateOID**

The following attribute types are exported by [Protected Extensible Authentication Protocol (PEAP)](Http://go.microsoft.com/fwlink/p/?linkid=83939) methods.

-   **eatUserName**
-   **eatPEAPEmbeddedEAPTypeId**
-   **eatPEAPFastRoamedSession**
-   **eatQuarantineSoH**

## Related topics

<dl> <dt>

[**EAP\_ATTRIBUTE**](/windows/previous-versions/eaptypes/ns-eaptypes-_eap_attribute?branch=master)
</dt> <dt>

[**EAP\_ATTRIBUTE\_TYPE**](/windows/previous-versions/eaptypes/ne-eaptypes-_eap_attribute_type?branch=master)
</dt> </dl>

 

 




