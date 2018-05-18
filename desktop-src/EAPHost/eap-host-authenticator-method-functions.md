---
title: EAPHost Authenticator Method Functions
description: EAPHost Authenticator Method Functions
ms.assetid: '319516ee-b21d-4375-8c90-e3abe0a457e8'
---

# EAPHost Authenticator Method Functions

The EAPHost Authenticator Method API functions are as follows.



| Function                                                                                               | Description                                                                                                                                                                                 |
|--------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**EapMethodAuthenticatorBeginSession**](eapmethodauthenticatorbeginsession.md)                       | Creates a new EAP authentication session on the server EAPHost.                                                                                                                             |
| [**EapMethodAuthenticatorEndSession**](eapmethodauthenticatorendsession.md)                           | Closes an EAP authentication session on the server EAPHost.                                                                                                                                 |
| [**EapMethodAuthenticatorFreeErrorMemory**](eapmethodauthenticatorfreeerrormemory.md)                 | Releases error-specific memory allocated by the EAP authenticator method.                                                                                                                   |
| [**EapMethodAuthenticatorGetAttributes**](eapmethodauthenticatorgetattributes.md)                     | Obtains an array of EAP authentication attributes from the EAP authenticator method.                                                                                                        |
| [**EapMethodAuthenticatorGetInfo**](eapmethodauthenticatorgetinfo.md)                                 | Obtains a set of function pointers for an implementation of the loaded EAP authenticator method.                                                                                            |
| [**EapMethodAuthenticatorGetResult**](eapmethodauthenticatorgetresult.md)                             | Obtains the authentication result from the EAP authenticator method.                                                                                                                        |
| [**EapMethodAuthenticatorInitialize**](eapmethodauthenticatorinitialize.md)                           | Initializes an EAP authenticator method for the server EAPHost.                                                                                                                             |
| [**EapMethodAuthenticatorInvokeConfigUI**](eapmethodauthenticatorinvokeconfigui.md)                   | Defines a function that raises the EAP method's connection configuration user interface dialog box on the client.                                                                           |
| [**EapMethodAuthenticatorReceivePacket**](eapmethodauthenticatorreceivepacket.md)                     | Processes an EAP authentication packet received by the server EAPHost and returns a response action.                                                                                        |
| [**EapMethodAuthenticatorSendPacket**](eapmethodauthenticatorsendpacket.md)                           | Obtains an authentication packet from the EAP authenticator method to send to the supplicant.                                                                                               |
| [**EapMethodAuthenticatorSetAttributes**](eapmethodauthenticatorsetattributes.md)                     | Provides updated EAP authentication attributes to set on the EAP authenticator method.                                                                                                      |
| [**EapMethodAuthenticatorShutdown**](eapmethodauthenticatorshutdown.md)                               | Shuts down the EAP authenticator method and prepares to unload it from the server EAPHost.                                                                                                  |
| [**EapMethodAuthenticatorUpdateInnerMethodParams**](eapmethodauthenticatorupdateinnermethodparams.md) | Updates the EAP authentication session settings previous established by a call to [**EapMethodAuthenticatorBeginSession**](eapmethodauthenticatorbeginsession.md) from the server EAPHost. |



 

 

 




