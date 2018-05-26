---
title: EAPHost Authenticator Method Functions
description: EAPHost Authenticator Method Functions
ms.assetid: 319516ee-b21d-4375-8c90-e3abe0a457e8
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# EAPHost Authenticator Method Functions

The EAPHost Authenticator Method API functions are as follows.



| Function                                                                                               | Description                                                                                                                                                                                 |
|--------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**EapMethodAuthenticatorBeginSession**](/windows/previous-versions/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorbeginsession?branch=master)                       | Creates a new EAP authentication session on the server EAPHost.                                                                                                                             |
| [**EapMethodAuthenticatorEndSession**](/windows/previous-versions/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorendsession?branch=master)                           | Closes an EAP authentication session on the server EAPHost.                                                                                                                                 |
| [**EapMethodAuthenticatorFreeErrorMemory**](/windows/previous-versions/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorfreeerrormemory?branch=master)                 | Releases error-specific memory allocated by the EAP authenticator method.                                                                                                                   |
| [**EapMethodAuthenticatorGetAttributes**](/windows/previous-versions/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorgetattributes?branch=master)                     | Obtains an array of EAP authentication attributes from the EAP authenticator method.                                                                                                        |
| [**EapMethodAuthenticatorGetInfo**](/windows/previous-versions/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorgetinfo?branch=master)                                 | Obtains a set of function pointers for an implementation of the loaded EAP authenticator method.                                                                                            |
| [**EapMethodAuthenticatorGetResult**](/windows/previous-versions/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorgetresult?branch=master)                             | Obtains the authentication result from the EAP authenticator method.                                                                                                                        |
| [**EapMethodAuthenticatorInitialize**](/windows/previous-versions/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorinitialize?branch=master)                           | Initializes an EAP authenticator method for the server EAPHost.                                                                                                                             |
| [**EapMethodAuthenticatorInvokeConfigUI**](/windows/previous-versions/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorinvokeconfigui?branch=master)                   | Defines a function that raises the EAP method's connection configuration user interface dialog box on the client.                                                                           |
| [**EapMethodAuthenticatorReceivePacket**](/windows/previous-versions/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorreceivepacket?branch=master)                     | Processes an EAP authentication packet received by the server EAPHost and returns a response action.                                                                                        |
| [**EapMethodAuthenticatorSendPacket**](/windows/previous-versions/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorsendpacket?branch=master)                           | Obtains an authentication packet from the EAP authenticator method to send to the supplicant.                                                                                               |
| [**EapMethodAuthenticatorSetAttributes**](/windows/previous-versions/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorsetattributes?branch=master)                     | Provides updated EAP authentication attributes to set on the EAP authenticator method.                                                                                                      |
| [**EapMethodAuthenticatorShutdown**](/windows/previous-versions/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorshutdown?branch=master)                               | Shuts down the EAP authenticator method and prepares to unload it from the server EAPHost.                                                                                                  |
| [**EapMethodAuthenticatorUpdateInnerMethodParams**](/windows/previous-versions/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorupdateinnermethodparams?branch=master) | Updates the EAP authentication session settings previous established by a call to [**EapMethodAuthenticatorBeginSession**](/windows/previous-versions/eapmethodauthenticatorapis/nf-eapmethodauthenticatorapis-eapmethodauthenticatorbeginsession?branch=master) from the server EAPHost. |



 

 

 




