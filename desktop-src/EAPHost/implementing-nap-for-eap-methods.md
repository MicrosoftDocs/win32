---
title: Implementing NAP Support for EAP Methods
description: Explains how to implement NAP for an EAPHost supplicant.
ms.assetid: 'c25e4f03-759a-47a7-8b35-bbe669501c5c'
---

# Implementing NAP Support for EAP Methods

This topic explains how to implement NAP for an EAPHost supplicant. In Windows Vista and Windows Server 2008 a NAP Enforcement Client (NAP EC) is available for [802.1X](Http://go.microsoft.com/fwlink/p/?linkid=83938) authenticated connections.

## Implementing Network Access Protection (NAP)

To support NAP, an EAPHost supplicant implements a callback function matching the [**NotificationHandler**](notificationhandler.md) callback prototype and must provide a pointer to this callback function when calling [**EapHostPeerBeginSession**](eaphostpeerbeginsession.md).

The callback function takes two parameters.

-   A GUID that uniquely identifies the interface associated with the authentication.
-   A VOID pointer to an opaque data structure that is supplied by the supplicant.

EAPHost will call the supplicant-provided callback function with the unique interface GUID and the VOID pointer when the quarantine state of the machine changes. When EAPHost calls the supplicant-provided callback function, the supplicant responds by tearing down the logical network connection identified by the interface GUID/VOID pointer and begins authentication again using **EapHostPeerBeginSession**.

EAPHost may call the supplicant-supplied callback function at any time: before, during an active authentication, or after the authentication has been completed (after [**EapHostPeerEndSession**](eaphostpeerendsession.md) has been called but not before [**EapHostPeerClearConnection**](eaphostpeerclearconnection.md) has been called). The supplicant should always respond by tearing down the logical network connection and re-authenticating.

If the supplicant is shutting down or choosing to no longer receive notification of isolation state changes, the supplicant should call [**EapHostPeerClearConnection**](eaphostpeerclearconnection.md) and specify the appropriate interface GUID. If the supplicant wishes to determine the isolation of the logical network connection, the supplicant can obtain that information from **EapHostPeerMethodResult.isolationState** when the [**EapHostPeerMethodResult**](eaphostpeermethodresult.md) is obtained from [**EapHostPeerGetResult**](eaphostpeergetresult.md).

## EAPHost Related NAP Information

For EAPHost API related NAP information refer to the following topics.

-   [**EAP\_ATTRIBUTE\_TYPE**](eap-attribute-type.md)
-   [**EAP\_ERROR**](eap-error.md)
-   [EAPHost Supplicant Frequently Asked Questions](eaphost-supplicant-frequently-asked-questions.md)
-   [**EAP Method Properties**](eap-method-properties.md)
-   [**EapHostPeerBeginSession**](eaphostpeerbeginsession.md)
-   [**EAP Related Error and Information Constants**](eap-related-error-and-information-constants.md)
-   [**ISOLATION\_STATE**](isolation-state.md)
-   [**NotificationHandler**](notificationhandler.md)

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

 

 




