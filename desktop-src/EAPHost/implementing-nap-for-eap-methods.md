---
title: Implementing NAP Support for EAP Methods
description: Explains how to implement NAP for an EAPHost supplicant.
ms.assetid: c25e4f03-759a-47a7-8b35-bbe669501c5c
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Implementing NAP Support for EAP Methods

This topic explains how to implement NAP for an EAPHost supplicant. In Windows Vista and Windows Server 2008 a NAP Enforcement Client (NAP EC) is available for [802.1X](Http://go.microsoft.com/fwlink/p/?linkid=83938) authenticated connections.

## Implementing Network Access Protection (NAP)

To support NAP, an EAPHost supplicant implements a callback function matching the [**NotificationHandler**](/windows/previous-versions/eappapis/nc-eappapis-notificationhandler?branch=master) callback prototype and must provide a pointer to this callback function when calling [**EapHostPeerBeginSession**](/windows/previous-versions/eappapis/nf-eappapis-eaphostpeerbeginsession?branch=master).

The callback function takes two parameters.

-   A GUID that uniquely identifies the interface associated with the authentication.
-   A VOID pointer to an opaque data structure that is supplied by the supplicant.

EAPHost will call the supplicant-provided callback function with the unique interface GUID and the VOID pointer when the quarantine state of the machine changes. When EAPHost calls the supplicant-provided callback function, the supplicant responds by tearing down the logical network connection identified by the interface GUID/VOID pointer and begins authentication again using **EapHostPeerBeginSession**.

EAPHost may call the supplicant-supplied callback function at any time: before, during an active authentication, or after the authentication has been completed (after [**EapHostPeerEndSession**](/windows/previous-versions/eappapis/nf-eappapis-eaphostpeerendsession?branch=master) has been called but not before [**EapHostPeerClearConnection**](/windows/previous-versions/eappapis/nf-eappapis-eaphostpeerclearconnection?branch=master) has been called). The supplicant should always respond by tearing down the logical network connection and re-authenticating.

If the supplicant is shutting down or choosing to no longer receive notification of isolation state changes, the supplicant should call [**EapHostPeerClearConnection**](/windows/previous-versions/eappapis/nf-eappapis-eaphostpeerclearconnection?branch=master) and specify the appropriate interface GUID. If the supplicant wishes to determine the isolation of the logical network connection, the supplicant can obtain that information from **EapHostPeerMethodResult.isolationState** when the [**EapHostPeerMethodResult**](/windows/previous-versions/eaphostpeertypes/ns-eaphostpeertypes-tageaphostpeermethodresult?branch=master) is obtained from [**EapHostPeerGetResult**](/windows/previous-versions/eappapis/nf-eappapis-eaphostpeergetresult?branch=master).

## EAPHost Related NAP Information

For EAPHost API related NAP information refer to the following topics.

-   [**EAP\_ATTRIBUTE\_TYPE**](/windows/previous-versions/eaptypes/ne-eaptypes-_eap_attribute_type?branch=master)
-   [**EAP\_ERROR**](/windows/previous-versions/eaptypes/ns-eaptypes-_eap_error?branch=master)
-   [EAPHost Supplicant Frequently Asked Questions](eaphost-supplicant-frequently-asked-questions.md)
-   [**EAP Method Properties**](eap-method-properties.md)
-   [**EapHostPeerBeginSession**](/windows/previous-versions/eappapis/nf-eappapis-eaphostpeerbeginsession?branch=master)
-   [**EAP Related Error and Information Constants**](eap-related-error-and-information-constants.md)
-   [**ISOLATION\_STATE**](/windows/previous-versions/eaphostpeertypes/ne-eaphostpeertypes-_isolation_state?branch=master)
-   [**NotificationHandler**](/windows/previous-versions/eappapis/nc-eappapis-notificationhandler?branch=master)

## Additional Resources

-   For a list of NAP resources, see [Network Access Protection](Http://go.microsoft.com/fwlink/p/?linkid=84107).
-   For Statement of Health information, see [Network Access Protection (NAP) Statement of Health (SoH) Messages](Http://go.microsoft.com/fwlink/p/?linkid=83918).
-   For the Enterprise Networking Group webpage and blog, see [Network Access Protection (NAP)](Http://go.microsoft.com/fwlink/p/?linkid=83845).
-   For NAP API information, see [Network Access Protection](https://msdn.microsoft.com/library/windows/desktop/aa369712).

## Related topics

<dl> <dt>

[Configuring the EAP Method User Interface](configuring-the-eap-method-user-interface.md)
</dt> <dt>

[Enabling Group Policy](enabling-group-policy.md)
</dt> <dt>

[Implementing In-Band NAP Support for EAP Methods](enabling-in-band-nap-support.md)
</dt> <dt>

[Transferring Data Between the Supplicant and EAP Methods](transferring-data-between-the-supplicant-and-eap-methods.md)
</dt> <dt>

[EAPHost Supplicants](eaphost-supplicants.md)
</dt> </dl>

 

 




