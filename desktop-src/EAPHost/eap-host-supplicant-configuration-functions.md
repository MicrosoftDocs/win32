---
title: EAPHost Supplicant Configuration Functions
description: EAPHost Supplicant Configuration Functions
ms.assetid: 92a1df11-10f9-4e55-a7ec-db026aaf5c24
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# EAPHost Supplicant Configuration Functions

The EAP Supplicant API configuration functions are as follows.



| Function                                                                                                           | Description                                                                                                                                                                                                                                                                          |
|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**EapHostPeerConfigBlob2Xml**](https://msdn.microsoft.com/library/windows/desktop/aa363551)                                                 | Converts the configuration blob to XML.                                                                                                                                                                                                                                              |
| [**EapHostPeerConfigXml2Blob**](https://msdn.microsoft.com/library/windows/desktop/aa363552)                                                 | Converts XML into the configuration blob.                                                                                                                                                                                                                                            |
| [**EapHostPeerCredentialsXml2Blob**](https://msdn.microsoft.com/library/windows/desktop/aa363553)                                       | Generates the credentials BLOB.                                                                                                                                                                                                                                                      |
| [**EapHostPeerFreeErrorMemory**](https://msdn.microsoft.com/library/windows/desktop/aa363557)                                               | Frees memory allocated to an [**EAP\_ERROR**](/windows/previous-versions/eaptypes/ns-eaptypes-_eap_error?branch=master) structure.                                                                                                                                                                                                              |
| [**EapHostPeerFreeMemory**](https://msdn.microsoft.com/library/windows/desktop/aa363558)                                                         | Frees memory returned by the configuration APIs. This function must not be used to free error memory. To free error memory, use either the [**EapHostPeerFreeEapError**](/windows/previous-versions/eappapis/nf-eappapis-eaphostpeerfreeeaperror?branch=master) or [**EapHostPeerFreeErrrorMemory**](/windows/previous-versions/eaphostpeerconfigapis/nf-eaphostpeerconfigapis-eaphostpeerfreeerrormemory?branch=master) function. |
| [**EapHostPeerGetMethodProperties**](/windows/previous-versions/eaphostpeerconfigapis/nf-eaphostpeerconfigapis-eaphostpeergetmethodproperties?branch=master)                                           | Retrieves properties of an EAP method given the connection and user data.                                                                                                                                                                                                            |
| [**EapHostPeerGetMethods**](https://msdn.microsoft.com/library/windows/desktop/aa363560)                                                         | Enumerates all EAP methods installed and available for use, including legacy EAP methods.                                                                                                                                                                                            |
| [**EapHostPeerInvokeConfigUI**](/windows/previous-versions/eaphostpeerconfigapis/nf-eaphostpeerconfigapis-eaphostpeerinvokeconfigui?branch=master)                                                     | Starts the configuration user interface of the specified EAP method.                                                                                                                                                                                                                 |
| [**EapHostPeerInvokeIdentityUI**](/windows/previous-versions/eaphostpeerconfigapis/nf-eaphostpeerconfigapis-eaphostpeerinvokeidentityui?branch=master)                                                 | Starts the identity user interface.                                                                                                                                                                                                                                                  |
| [**EapHostPeerInvokeInteractiveUI**](https://msdn.microsoft.com/library/windows/desktop/aa363569)                                       | Provides credentials interactivity to the user, such as a smart card and PIN for example.                                                                                                                                                                                            |
| [**EapHostPeerQueryCredentialInputFields**](/windows/previous-versions/eaphostpeerconfigapis/nf-eaphostpeerconfigapis-eaphostpeerquerycredentialinputfields?branch=master)                             | Allows the user to determine what kind of credentials are required by the methods to perform authentication. It also obtains the fields to be displayed in the user interface.                                                                                                       |
| [**EapHostPeerQueryInteractiveUIInputFields**](/windows/previous-versions/eaphostpeerconfigapis/nf-eaphostpeerconfigapis-eaphostpeerqueryinteractiveuiinputfields?branch=master)                       | Obtains the input fields for interactive user interface components to raise on the supplicant.                                                                                                                                                                                       |
| [**EapHostPeerQueryUIBlobFromInteractiveUIInputFields**](/windows/previous-versions/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerqueryuiblobfrominteractiveuiinputfields?branch=master)       | Converts user information into a user BLOB that can consumed by EAPHost run-time functions.                                                                                                                                                                                          |
| [**EapHostPeerQueryUserBlobFromCredentialInputFields**](https://msdn.microsoft.com/library/windows/desktop/aa363574) | Obtains the credential BLOB that could be used start authentication once user inputs have been received from the from single sign-on user interface.                                                                                                                                 |



 

 

 




