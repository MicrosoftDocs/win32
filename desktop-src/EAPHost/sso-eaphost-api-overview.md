---
title: SSO EAPHost API Overview
description: Provides an overview of the EAPHost APIs that support Single-Sign-On (SSO).
ms.assetid: '3c01d10a-9098-4965-8983-c7f65be31884'
---

# SSO EAPHost API Overview

This topic provides an overview of the EAPHost APIs that support Single-Sign-On (SSO). For specific SSO scenarios, see [SSO EAPHost Scenarios](why-eaphost-sso.md).

## EAPHost Enumerations

The following enumerations support SSO.



| Name                                                                    | Purpose                                                                                      |
|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| [**EAP\_CONFIG\_INPUT\_FIELD\_TYPE**](eap-config-input-field-type.md)  | Defines a set of possible input field types available when querying for user credentials.    |
| [**EAP\_INTERACTIVE\_UI\_DATA\_TYPE**](eap-config-input-field-type.md) | Specifies the types of interactive UI context data supplied to certain supplicant API calls. |



 

## EAPHost Structures

The following data structures support SSO.



| Name                                                                     | Purpose                                                                                                                                                                         |
|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**EAP\_CONFIG\_INPUT\_FIELD\_DATA**](eap-config-input-field-data.md)   | Contains the data associated with a single input field.                                                                                                                         |
| [**EAP\_CONFIG\_INPUT\_FIELD\_ARRAY**](eap-config-input-field-array.md) | Contains a set of [**EAP\_CONFIG\_INPUT\_FIELD\_DATA**](eap-config-input-field-data.md) structures that collectively contain the user input field data obtained from the user. |
| [**EAP\_INTERACTIVE\_UI\_DATA**](eap-interactive-ui-data.md)            | Contains configuration information for interactive UI components raised on an EAP supplicant.                                                                                   |
| [**EAP\_CRED\_REQ**](eap-cred-req.md)                                   | Contains both the old and new EAP credentials for a credential change operations.                                                                                               |
| [**EAP\_CRED\_RESP**](eap-cred-resp.md)                                 | Contains both the old and new EAP credentials for a credential change operations.                                                                                               |
| [**EAP\_CRED\_EXPIRY\_REQ**](eap-cred-expiry-req.md)                    | Contains both the old and new EAP credentials for credential expiry operations.                                                                                                 |
| [**EAP\_CRED\_EXPIRY\_RESP**](https://msdn.microsoft.com/library/windows/desktop/bb530539)              | Contains both the old and new EAP credentials for credential expiry operations.                                                                                                 |



 

## EAPHost Peer (Supplicant) APIs

The following supplicant functions support SSO.

The [**EapHostPeerQueryCredentialInputFields**](eaphostpeerquerycredentialinputfields.md) and [**EapHostPeerQueryUserBlobFromCredentialInputFields**](eaphostpeerqueryuserblobfromcredentialinputfields.md) functions are exclusive to SSO.



| Name                                                                                                             | Purpose                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Order Called |
|------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| [**EapHostPeerQueryInteractiveUIInputFields**](eaphostpeerqueryinteractiveuiinputfields.md)                     | Obtains the input fields for interactive UI components to be raised on the supplicant.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 4            |
| [**EapHostPeerQueryCredentialInputFields**](eaphostpeerquerycredentialinputfields.md)                           | Allows the user to determine what kind of credentials are required by the methods to perform authentication in a SSO scenario.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 1            |
| [**EapHostPeerQueryUIBlobFromInteractiveUIInputFields**](eaphostpeerqueryuiblobfrominteractiveuiinputfields.md) | Converts user information into a user BLOB that can be consumed by EAPHost run-time functions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 5            |
| [**EapHostPeerQueryUserBlobFromCredentialInputFields**](eaphostpeerqueryuserblobfromcredentialinputfields.md)   | Obtains a credential BLOB that can be used to start authentication from user input received by the SSO UI.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 2            |
| [**EapHostPeerBeginSession**](eaphostpeerbeginsession.md)                                                       | The supplicant uses the **EAP\_FLAG\_PRE\_LOGON** flag to indicate that EAPHost should provide SSO. If the [EapHostPeerResponseInvokeUI](eaphostpeerresponseaction.md) action code is returned, EAPHost calls [**EapPeerQueryInteractiveUIInputFields**](eappeerqueryinteractiveuiinputfields.md), and then calls [**EapHostPeerQueryUIBlobFromInteractiveUIInputFields**](eaphostpeerqueryuiblobfrominteractiveuiinputfields.md)<br/> If the [EapHostPeerResponseInvokeUI](eaphostpeerresponseaction.md) action code is not returned, EAPHost proceeds with the regular, non SSO call sequence. For more information, see [Supplicant API Call Sequence](supplicant-api-call-sequence.md).<br/> | 3            |



 

## EAPHost Peer Method APIs

The following peer functions support SSO.

The [**EapPeerQueryCredentialInputFields**](eappeerquerycredentialinputfields.md) and [**EapPeerQueryUserBlobFromCredentialInputFields**](eappeerqueryuserblobfrominteractiveuiinputfields.md) functions are exclusive to SSO.



| Name                                                                                                      | Purpose                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Order Called |
|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| [**EapPeerQueryInteractiveUIInputFields**](eappeerqueryinteractiveuiinputfields.md)                      | Defines the implementation of an EAP method API that provides the input fields for interactive UI components to be raised on the supplicant.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 4            |
| [**EapPeerQueryCredentialInputFields**](eappeerquerycredentialinputfields.md)                            | Defines the implementation of an EAP method-specific function that obtains the EAP SSO credential input fields for that EAP method.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 1            |
| [**EapPeerQueryUIBlobFromInteractiveUIInputFields**](eappeerqueryuiblobfrominteractiveuiinputfields.md)  | Converts user information into a user BLOB that can be consumed by EAPHost run-time functions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 5            |
| [**EapPeerQueryUserBlobFromCredentialInputFields**](eappeerqueryuserblobfrominteractiveuiinputfields.md) | Defines the implementation of an EAP method function that obtains the user BLOB data provided by the interactive SSO UI raised on the supplicant.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | 2            |
| [**EapPeerBeginSession**](eappeerbeginsession.md)                                                        | The **EAP\_FLAG\_PRE\_LOGON** flag indicates that EAPHost should provide SSO. In an SSO scenario if the **EapPeerResponseInvokeUI** action code is returned, EAPHost calls [**EapPeerQueryInteractiveUIInputFields**](eappeerqueryinteractiveuiinputfields.md), and then calls [**EapPeerQueryUserBlobFromCredentialInputFields**](eappeerqueryuserblobfrominteractiveuiinputfields.md)<br/> If the **EapPeerResponseInvokeUI** action code is not returned, EAPHost proceeds with the regular, non SSO call sequence. For more information, see [Peer Method API Call Sequence](peer-method-api-call-sequence.md).<br/> | 3            |



 

## Related topics

<dl> <dt>

[SSO and PLAP](understanding-sso-and-plap.md)
</dt> <dt>

[SSO EAPHost Scenarios](why-eaphost-sso.md)
</dt> </dl>

 

 





