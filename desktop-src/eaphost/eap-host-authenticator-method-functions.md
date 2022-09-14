---
title: EAPHost Authenticator Method Functions
description: Learn about EAPHost Authenticator Method API functions, such as EapMethodAuthenticatorFreeErrorMemory.
ms.assetid: 319516ee-b21d-4375-8c90-e3abe0a457e8
ms.topic: article
ms.date: 05/31/2018
---

# EAPHost Authenticator Method Functions

The EAPHost Authenticator Method API functions are as follows.



| Function                                                                                               | Description                                                                                                                                                                                 |
|--------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**EapMethodAuthenticatorBeginSession**](/previous-versions/windows/desktop/api/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorbeginsession)                       | Creates a new EAP authentication session on the server EAPHost.                                                                                                                             |
| [**EapMethodAuthenticatorEndSession**](/previous-versions/windows/desktop/api/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorendsession)                           | Closes an EAP authentication session on the server EAPHost.                                                                                                                                 |
| [**EapMethodAuthenticatorFreeErrorMemory**](/previous-versions/windows/desktop/api/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorfreeerrormemory)                 | Releases error-specific memory allocated by the EAP authenticator method.                                                                                                                   |
| [**EapMethodAuthenticatorGetAttributes**](/previous-versions/windows/desktop/api/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorgetattributes)                     | Obtains an array of EAP authentication attributes from the EAP authenticator method.                                                                                                        |
| [**EapMethodAuthenticatorGetInfo**](/previous-versions/windows/desktop/api/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorgetinfo)                                 | Obtains a set of function pointers for an implementation of the loaded EAP authenticator method.                                                                                            |
| [**EapMethodAuthenticatorGetResult**](/previous-versions/windows/desktop/api/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorgetresult)                             | Obtains the authentication result from the EAP authenticator method.                                                                                                                        |
| [**EapMethodAuthenticatorInitialize**](/previous-versions/windows/desktop/api/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorinitialize)                           | Initializes an EAP authenticator method for the server EAPHost.                                                                                                                             |
| [**EapMethodAuthenticatorInvokeConfigUI**](/previous-versions/windows/desktop/api/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorinvokeconfigui)                   | Defines a function that raises the EAP method's connection configuration user interface dialog box on the client.                                                                           |
| [**EapMethodAuthenticatorReceivePacket**](/previous-versions/windows/desktop/api/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorreceivepacket)                     | Processes an EAP authentication packet received by the server EAPHost and returns a response action.                                                                                        |
| [**EapMethodAuthenticatorSendPacket**](/previous-versions/windows/desktop/api/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorsendpacket)                           | Obtains an authentication packet from the EAP authenticator method to send to the supplicant.                                                                                               |
| [**EapMethodAuthenticatorSetAttributes**](/previous-versions/windows/desktop/api/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorsetattributes)                     | Provides updated EAP authentication attributes to set on the EAP authenticator method.                                                                                                      |
| [**EapMethodAuthenticatorShutdown**](/previous-versions/windows/desktop/api/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorshutdown)                               | Shuts down the EAP authenticator method and prepares to unload it from the server EAPHost.                                                                                                  |
| [**EapMethodAuthenticatorUpdateInnerMethodParams**](/previous-versions/windows/desktop/api/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorupdateinnermethodparams) | Updates the EAP authentication session settings previous established by a call to [**EapMethodAuthenticatorBeginSession**](/previous-versions/windows/desktop/api/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorbeginsession) from the server EAPHost. |



 

 

 




