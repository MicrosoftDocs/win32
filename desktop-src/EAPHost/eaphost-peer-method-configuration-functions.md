---
title: EAPHost Peer Method Configuration Functions
description: EAPHost Peer Method Configuration Functions
ms.assetid: 'ba5c90b2-5185-4810-84a2-d08e62e8105c'
---

# EAPHost Peer Method Configuration Functions

The EAP Peer Method API configuration functions are as follows.



| Function                                                                                                  | Description                                                                                                                                                                                                                                                      |
|-----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**EapPeerConfigBlob2Xml**](eappeerconfigblob2xml.md)                                                    | Converts the configuration blob to XML.                                                                                                                                                                                                                          |
| [**EapPeerConfigXml2Blob**](eappeerconfigxml2blob.md)                                                    | Converts XML into the configuration blob.                                                                                                                                                                                                                        |
| [**EapPeerCredentialsXml2Blob**](eappeercredentialsxml2blob.md)                                          | Converts XML credentials into a BLOB.                                                                                                                                                                                                                            |
| [**EapPeerFreeErrorMemory**](eappeerfreeerrormemory.md)                                                  | Frees all EAP error-specific memory returned by EapHost peer APIs.                                                                                                                                                                                               |
| [**EapPeerFreeMemory**](eappeerfreememory.md)                                                            | Releases all memory allocated by EAP method OUT parameters.                                                                                                                                                                                                      |
| [**EapPeerInvokeConfigUI**](eappeerinvokeconfigui.md)                                                    | Raises the EAP method's specific connection configuration user interface dialog on the client.                                                                                                                                                                   |
| [**EapPeerInvokeIdentityUI**](eappeerinvokeidentityui.md)                                                | Raises a custom interactive user interface dialog to obtain user identity information for the EAP method on the client.                                                                                                                                          |
| [**EapPeerInvokeInteractiveUI**](eappeerinvokeinteractiveui.md)                                          | Raises a custom interactive user interface dialog for the EAP method on the client.                                                                                                                                                                              |
| [**EapPeerQueryCredentialInputFields**](eappeerquerycredentialinputfields.md)                            | Defines the implementation of an EAP method-specific function that obtains the EAP Single-Sign-On (SSO) credential input fields for that EAP method                                                                                                              |
| [**EapPeerQueryInteractiveUIInputFields**](eappeerqueryinteractiveuiinputfields.md)                      | Defines the implementation of an EAP supplicant function that obtains the input fields for interactive user interface components to raise on the supplicant.                                                                                                     |
| [**EapPeerQueryUIBlobFromInteractiveUIInputFields**](eappeerqueryuiblobfrominteractiveuiinputfields.md)  | Converts user information into a user BLOB that can be consumed by EAPHost run-time functions.                                                                                                                                                                   |
| [**EapPeerQueryUserBlobFromCredentialInputFields**](eappeerqueryuserblobfrominteractiveuiinputfields.md) | Defines the implementation of an EAP method-specific function that generates an EAP user credential blob from an [**EAP\_CONFIG\_INPUT\_FIELD\_ARRAY**](eap-config-input-field-array.md) structure that contains credential data supplied by a supplicant user. |



 

## Related topics

<dl> <dt>

[EAPHost Peer Method Run-Time Functions](eaphost-peer-method-run-time-functions.md)
</dt> </dl>

 

 




