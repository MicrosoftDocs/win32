---
title: CSecureChannelServer Class
description: CSecureChannelServer Class
ms.assetid: 'e6e1463a-5a26-4b83-85e0-a639d384a199'
keywords: ["Windows Media Device Manager,CSecureChannelServer class", "Device Manager,CSecureChannelServer class", "service providers,CSecureChannelServer class", "programming reference,CSecureChannelServer class", "reference for Windows Media Device Manager,CSecureChannelServer class", "CSecureChannelServer class"]
---

# CSecureChannelServer Class

The **CSecureChannelServer** class is a helper class (not an interface) that enables a service provider or secure content provider to authenticate an application using the [**IComponentAuthenticate**](icomponentauthenticate.md) interface, to encrypt and decrypt data, and to create MAC signatures. The authentication process requires that the application create a **CSecureChannelClient** object and that the service provider create a **CSecureChannelServer** object. The **CSecureChannelClient** and **CSecureChannelServer** classes are declared in the static link library, Mssachlp.lib. All methods of Windows Media Device Manager, service provider, and secure content provider interfaces can return WMDM\_E\_NOTCERTIFIED to indicate that the caller has not authenticated successfully.

The **CSecureChannelServer** class exposes the following methods.



| Method                                                            | Description                                                                                 |
|-------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| [**DecryptParam**](csecurechannelserver-decryptparam.md)         | Decrypts the data contained in a parameter.                                                 |
| [**EncryptParam**](csecurechannelserver-encryptparam.md)         | Encrypts the data contained in a parameter.                                                 |
| [**fIsAuthenticated**](csecurechannelserver-fisauthenticated.md) | Verifies that a secure authentication channel has been successfully established.            |
| [**GetAppSec**](csecurechannelserver-getappsec.md)               | Retrieves the application security levels of the local and remote components.               |
| [**GetSessionKey**](csecurechannelserver-getsessionkey.md)       | Retrieves the current session key.                                                          |
| [**MACFinal**](csecurechannelserver-macfinal.md)                 | Releases the message authentication code (MAC) channel and retrieves a final MAC value.     |
| [**MACInit**](csecurechannelserver-macinit.md)                   | Acquires a message authentication code (MAC) channel.                                       |
| [**MACUpdate**](csecurechannelserver-macupdate.md)               | Updates the message authentication code (MAC) value with a parameter value.                 |
| [**SACAuth**](csecurechannelserver-sacauth.md)                   | Establishes a secure authenticated channel between components.                              |
| [**SACGetProtocols**](csecurechannelserver-sacgetprotocols.md)   | Reports the protocols supported by a component.                                             |
| [**SetCertificate**](csecurechannelserver-setcertificate.md)     | Specifies the certificate and private key of the secure authenticated channel (SAC) server. |
| [**SetSessionKey**](csecurechannelserver-setsessionkey.md)       | Sets the session key that is used to communicate with another component.                    |



 

## Related topics

<dl> <dt>

[**CSecureChannelClient Class**](csecurechannelclient-class.md)
</dt> <dt>

[**IComponentAuthenticate Interface**](icomponentauthenticate.md)
</dt> <dt>

[**Interfaces for Service Providers**](interfaces-for-service-providers.md)
</dt> <dt>

[**Using Secure Authenticated Channels**](using-secure-authenticated-channels.md)
</dt> </dl>

 

 




