---
title: Enabling Group Policy
description: Learn how to configure the supplicant by enabling group policy. See considerations for supplicants and view additional available resources.
ms.assetid: ac04b83b-1322-41d4-85e0-93687f10a7f6
ms.topic: article
ms.date: 05/31/2018
---

# Enabling Group Policy

This topic explains how to configure the supplicant by enabling group policy. EAPHost supplicants can participate in group policy to allow a network administrator to centrally configure their network machines.

The precise method and mechanism by which the supplicant chooses to participate in group policy is at the discretion of the supplicant. Examples of mechanisms for group policy participation include client/server-side extensions, administrative template, and so forth.

## Considerations When Enabling Group Policy

These are the considerations for supplicants with respect to group policy and EAP.

1.  EAP configuration should always be stored as XML whenever possible and not in the binary format. Group policy may be applied to any machine in the domain, and EAP method configuration and user data are not guaranteed to be portable between 32-bit and 64-bit processor architectures. XML resolves the processor architecture boundary issues as the supplicant locally converts the processor-architecture independent XML to the binary representation of the configuration at authentication time.

    For more information, see the following topics.

    -   [General Frequently Asked Questions](general-frequently-asked-questions.yml)
    -   [EAP Method Frequently Asked Questions](eap-method-frequently-asked-questions.yml).
    -   [**EapHostPeerConfigXml2Blob**](/previous-versions/windows/desktop/api/eaphostpeerconfigapis/nf-eaphostpeerconfigapis-eaphostpeerconfigxml2blob)
    -   [**EapHostPeerCredentialsXml2Blob**](/previous-versions/windows/desktop/api/eaphostpeerconfigapis/nf-eaphostpeerconfigapis-eaphostpeercredentialsxml2blob)

2.  If a group policy server-side extension is used, the extension will call [**EapHostPeerGetMethods**](/previous-versions/windows/desktop/api/eaphostpeerconfigapis/nf-eaphostpeerconfigapis-eaphostpeergetmethods) typically to determine available methods and to generate appropriate EAP configuration for that policy. The policy is then pushed out to appropriate network clients where the policy is applied.

## Related topics

<dl> <dt>

[Configuring the EAP Method User Interface](configuring-the-eap-method-user-interface.md)
</dt> <dt>

[Implementing In-Band NAP Support for EAP Methods](enabling-in-band-nap-support.md)
</dt> <dt>

[Implementing NAP Support for EAP Methods](implementing-nap-for-eap-methods.md)
</dt> <dt>

[Transferring Data Between the Supplicant and EAP Methods](transferring-data-between-the-supplicant-and-eap-methods.md)
</dt> <dt>

[EAPHost Supplicants](eaphost-supplicants.md)
</dt> </dl>

 

 




