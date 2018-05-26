---
title: EAPHost Peer Method Configuration Functions
description: EAPHost Peer Method Configuration Functions
ms.assetid: ba5c90b2-5185-4810-84a2-d08e62e8105c
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# EAPHost Peer Method Configuration Functions

The EAP Peer Method API configuration functions are as follows.



| Function                                                                                                  | Description                                                                                                                                                                                                                                                      |
|-----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**EapPeerConfigBlob2Xml**](/windows/previous-versions/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerconfigblob2xml?branch=master)                                                    | Converts the configuration blob to XML.                                                                                                                                                                                                                          |
| [**EapPeerConfigXml2Blob**](/windows/previous-versions/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerconfigxml2blob?branch=master)                                                    | Converts XML into the configuration blob.                                                                                                                                                                                                                        |
| [**EapPeerCredentialsXml2Blob**](/windows/previous-versions/eapmethodpeerapis/nf-eapmethodpeerapis-eappeercredentialsxml2blob?branch=master)                                          | Converts XML credentials into a BLOB.                                                                                                                                                                                                                            |
| [**EapPeerFreeErrorMemory**](/windows/previous-versions/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerfreeerrormemory?branch=master)                                                  | Frees all EAP error-specific memory returned by EapHost peer APIs.                                                                                                                                                                                               |
| [**EapPeerFreeMemory**](/windows/previous-versions/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerfreememory?branch=master)                                                            | Releases all memory allocated by EAP method OUT parameters.                                                                                                                                                                                                      |
| [**EapPeerInvokeConfigUI**](/windows/previous-versions/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerinvokeconfigui?branch=master)                                                    | Raises the EAP method's specific connection configuration user interface dialog on the client.                                                                                                                                                                   |
| [**EapPeerInvokeIdentityUI**](/windows/previous-versions/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerinvokeidentityui?branch=master)                                                | Raises a custom interactive user interface dialog to obtain user identity information for the EAP method on the client.                                                                                                                                          |
| [**EapPeerInvokeInteractiveUI**](/windows/previous-versions/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerinvokeinteractiveui?branch=master)                                          | Raises a custom interactive user interface dialog for the EAP method on the client.                                                                                                                                                                              |
| [**EapPeerQueryCredentialInputFields**](/windows/previous-versions/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerquerycredentialinputfields?branch=master)                            | Defines the implementation of an EAP method-specific function that obtains the EAP Single-Sign-On (SSO) credential input fields for that EAP method                                                                                                              |
| [**EapPeerQueryInteractiveUIInputFields**](/windows/previous-versions/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerqueryinteractiveuiinputfields?branch=master)                      | Defines the implementation of an EAP supplicant function that obtains the input fields for interactive user interface components to raise on the supplicant.                                                                                                     |
| [**EapPeerQueryUIBlobFromInteractiveUIInputFields**](/windows/previous-versions/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerqueryuiblobfrominteractiveuiinputfields?branch=master)  | Converts user information into a user BLOB that can be consumed by EAPHost run-time functions.                                                                                                                                                                   |
| [**EapPeerQueryUserBlobFromCredentialInputFields**](/windows/previous-versions/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerqueryuserblobfromcredentialinputfields?branch=master) | Defines the implementation of an EAP method-specific function that generates an EAP user credential blob from an [**EAP\_CONFIG\_INPUT\_FIELD\_ARRAY**](/windows/previous-versions/eaptypes/ns-eaptypes-_eap_config_input_field_array?branch=master) structure that contains credential data supplied by a supplicant user. |



 

## Related topics

<dl> <dt>

[EAPHost Peer Method Run-Time Functions](eaphost-peer-method-run-time-functions.md)
</dt> </dl>

 

 




