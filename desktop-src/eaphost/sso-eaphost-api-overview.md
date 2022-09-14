---
title: SSO EAPHost API Overview
description: Provides an overview of the EAPHost APIs that support Single-Sign-On (SSO).
ms.assetid: 3c01d10a-9098-4965-8983-c7f65be31884
ms.topic: article
ms.date: 05/31/2018
---

# SSO EAPHost API Overview

This topic provides an overview of the EAPHost APIs that support Single-Sign-On (SSO). For specific SSO scenarios, see [SSO EAPHost Scenarios](why-eaphost-sso.md).

## EAPHost Enumerations

The following enumerations support SSO.



| Name                                                                    | Purpose                                                                                      |
|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| [**EAP\_CONFIG\_INPUT\_FIELD\_TYPE**](/windows/desktop/api/eaptypes/ne-eaptypes-eap_config_input_field_type)  | Defines a set of possible input field types available when querying for user credentials.    |
| [**EAP\_INTERACTIVE\_UI\_DATA\_TYPE**](/windows/desktop/api/eaptypes/ne-eaptypes-eap_config_input_field_type) | Specifies the types of interactive UI context data supplied to certain supplicant API calls. |



 

## EAPHost Structures

The following data structures support SSO.



| Name                                                                     | Purpose                                                                                                                                                                         |
|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**EAP\_CONFIG\_INPUT\_FIELD\_DATA**](/windows/desktop/api/eaptypes/ns-eaptypes-eap_config_input_field_data)   | Contains the data associated with a single input field.                                                                                                                         |
| [**EAP\_CONFIG\_INPUT\_FIELD\_ARRAY**](/windows/desktop/api/eaptypes/ns-eaptypes-eap_config_input_field_array) | Contains a set of [**EAP\_CONFIG\_INPUT\_FIELD\_DATA**](/windows/desktop/api/eaptypes/ns-eaptypes-eap_config_input_field_data) structures that collectively contain the user input field data obtained from the user. |
| [**EAP\_INTERACTIVE\_UI\_DATA**](/windows/desktop/api/eaptypes/ns-eaptypes-eap_interactive_ui_data)            | Contains configuration information for interactive UI components raised on an EAP supplicant.                                                                                   |
| [**EAP\_CRED\_REQ**](eap-cred-req.md)                                   | Contains both the old and new EAP credentials for a credential change operations.                                                                                               |
| [**EAP\_CRED\_RESP**](eap-cred-resp.md)                                 | Contains both the old and new EAP credentials for a credential change operations.                                                                                               |
| [**EAP\_CRED\_EXPIRY\_REQ**](/windows/desktop/api/eaptypes/ns-eaptypes-eap_cred_expiry_req)                    | Contains both the old and new EAP credentials for credential expiry operations.                                                                                                 |
| [**EAP\_CRED\_EXPIRY\_RESP**](/previous-versions/windows/desktop/legacy/bb530539(v=vs.85))              | Contains both the old and new EAP credentials for credential expiry operations.                                                                                                 |



 

## EAPHost Peer (Supplicant) APIs

The following supplicant functions support SSO.

The [**EapHostPeerQueryCredentialInputFields**](/previous-versions/windows/desktop/api/eaphostpeerconfigapis/nf-eaphostpeerconfigapis-eaphostpeerquerycredentialinputfields) and [**EapHostPeerQueryUserBlobFromCredentialInputFields**](/previous-versions/windows/desktop/api/eaphostpeerconfigapis/nf-eaphostpeerconfigapis-eaphostpeerqueryuserblobfromcredentialinputfields) functions are exclusive to SSO.



| Name                                                                                                             | Purpose                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Order Called |
|------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| [**EapHostPeerQueryInteractiveUIInputFields**](/previous-versions/windows/desktop/api/eaphostpeerconfigapis/nf-eaphostpeerconfigapis-eaphostpeerqueryinteractiveuiinputfields)                     | Obtains the input fields for interactive UI components to be raised on the supplicant.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 4            |
| [**EapHostPeerQueryCredentialInputFields**](/previous-versions/windows/desktop/api/eaphostpeerconfigapis/nf-eaphostpeerconfigapis-eaphostpeerquerycredentialinputfields)                           | Allows the user to determine what kind of credentials are required by the methods to perform authentication in a SSO scenario.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 1            |
| [**EapHostPeerQueryUIBlobFromInteractiveUIInputFields**](/previous-versions/windows/desktop/api/eaphostpeerconfigapis/nf-eaphostpeerconfigapis-eaphostpeerqueryuiblobfrominteractiveuiinputfields) | Converts user information into a user BLOB that can be consumed by EAPHost run-time functions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 5            |
| [**EapHostPeerQueryUserBlobFromCredentialInputFields**](/previous-versions/windows/desktop/api/eaphostpeerconfigapis/nf-eaphostpeerconfigapis-eaphostpeerqueryuserblobfromcredentialinputfields)   | Obtains a credential BLOB that can be used to start authentication from user input received by the SSO UI.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 2            |
| [**EapHostPeerBeginSession**](/previous-versions/windows/desktop/api/eappapis/nf-eappapis-eaphostpeerbeginsession)                                                       | The supplicant uses the **EAP\_FLAG\_PRE\_LOGON** flag to indicate that EAPHost should provide SSO. If the [EapHostPeerResponseInvokeUI](/windows/win32/api/eaphostpeertypes/ne-eaphostpeertypes-eaphostpeerresponseaction) action code is returned, EAPHost calls [**EapPeerQueryInteractiveUIInputFields**](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerqueryinteractiveuiinputfields), and then calls [**EapHostPeerQueryUIBlobFromInteractiveUIInputFields**](/previous-versions/windows/desktop/api/eaphostpeerconfigapis/nf-eaphostpeerconfigapis-eaphostpeerqueryuiblobfrominteractiveuiinputfields)<br/> If the [EapHostPeerResponseInvokeUI](/windows/win32/api/eaphostpeertypes/ne-eaphostpeertypes-eaphostpeerresponseaction) action code is not returned, EAPHost proceeds with the regular, non SSO call sequence. For more information, see [Supplicant API Call Sequence](supplicant-api-call-sequence.md).<br/> | 3            |



 

## EAPHost Peer Method APIs

The following peer functions support SSO.

The [**EapPeerQueryCredentialInputFields**](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerquerycredentialinputfields) and [**EapPeerQueryUserBlobFromCredentialInputFields**](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerqueryuserblobfromcredentialinputfields) functions are exclusive to SSO.



| Name                                                                                                      | Purpose                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Order Called |
|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| [**EapPeerQueryInteractiveUIInputFields**](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerqueryinteractiveuiinputfields)                      | Defines the implementation of an EAP method API that provides the input fields for interactive UI components to be raised on the supplicant.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 4            |
| [**EapPeerQueryCredentialInputFields**](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerquerycredentialinputfields)                            | Defines the implementation of an EAP method-specific function that obtains the EAP SSO credential input fields for that EAP method.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 1            |
| [**EapPeerQueryUIBlobFromInteractiveUIInputFields**](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerqueryuiblobfrominteractiveuiinputfields)  | Converts user information into a user BLOB that can be consumed by EAPHost run-time functions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 5            |
| [**EapPeerQueryUserBlobFromCredentialInputFields**](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerqueryuserblobfromcredentialinputfields) | Defines the implementation of an EAP method function that obtains the user BLOB data provided by the interactive SSO UI raised on the supplicant.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | 2            |
| [**EapPeerBeginSession**](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerbeginsession)                                                        | The **EAP\_FLAG\_PRE\_LOGON** flag indicates that EAPHost should provide SSO. In an SSO scenario if the **EapPeerResponseInvokeUI** action code is returned, EAPHost calls [**EapPeerQueryInteractiveUIInputFields**](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerqueryinteractiveuiinputfields), and then calls [**EapPeerQueryUserBlobFromCredentialInputFields**](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerqueryuserblobfromcredentialinputfields)<br/> If the **EapPeerResponseInvokeUI** action code is not returned, EAPHost proceeds with the regular, non SSO call sequence. For more information, see [Peer Method API Call Sequence](peer-method-api-call-sequence.md).<br/> | 3            |



 

## Related topics

<dl> <dt>

[SSO and PLAP](understanding-sso-and-plap.md)
</dt> <dt>

[SSO EAPHost Scenarios](why-eaphost-sso.md)
</dt> </dl>

 

