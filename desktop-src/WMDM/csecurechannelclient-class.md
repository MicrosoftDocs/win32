---
title: CSecureChannelClient Class
description: CSecureChannelClient Class
ms.assetid: 'f02220b8-0d1c-416c-97ea-e5e7455fcbba'
keywords: ["Windows Media Device Manager,CSecureChannelClient class", "Device Manager,CSecureChannelClient class", "desktop applications,CSecureChannelClient class", "programming reference,CSecureChannelClient class", "reference for Windows Media Device Manager,CSecureChannelClient class", "CSecureChannelClient class"]
---

# CSecureChannelClient Class

The **CSecureChannelClient** class is a helper class (not an interface) that enables applications to authenticate themselves, encrypt and decrypt data, and create MACs.

The **CSecureChannelClient** class exposes the following methods.



| Method                                                            | Description                                                                                                               |
|-------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| [**Authenticate**](csecurechannelclient-authenticate.md)         | Triggers the exchange of certificates between components to establish trust.                                              |
| [**DecryptParam**](csecurechannelclient-decryptparam.md)         | Decrypts data received through a parameter.                                                                               |
| [**EncryptParam**](csecurechannelclient-encryptparam.md)         | Encrypts data being sent out through a parameter.                                                                         |
| [**fIsAuthenticated**](csecurechannelclient-fisauthenticated.md) | Verifies that a secure authentication channel has been successfully established. This method is not used by applications. |
| [**GetAppSec**](csecurechannelclient-getappsec.md)               | Retrieves the application security levels of the local and remote components.                                             |
| [**GetSessionKey**](csecurechannelclient-getsessionkey.md)       | Retrieves the current session key. This method is not used by applications.                                               |
| [**MACFinal**](csecurechannelclient-macfinal.md)                 | Releases the message authentication code (MAC) channel and retrieves a final MAC value.                                   |
| [**MACInit**](csecurechannelclient-macinit.md)                   | Acquires a message authentication code (MAC) channel.                                                                     |
| [**MACUpdate**](csecurechannelclient-macupdate.md)               | Adds a value to a message authentication code (MAC).                                                                      |
| [**SetCertificate**](csecurechannelclient-setcertificate.md)     | Specifies the certificate and private key of the secure authenticated channel (SAC) client.                               |
| [**SetInterface**](csecurechannelclient-setinterface.md)         | Selects the interface used for secure authenticated channel (SAC) communications.                                         |
| [**SetSessionKey**](csecurechannelclient-setsessionkey.md)       | Sets the session key that is used to communicate with another component. This method is not used by applications.         |



 

## Related topics

<dl> <dt>

[**CSecureChannelServer Class**](csecurechannelserver-class.md)
</dt> <dt>

[**IComponentAuthenticate Interface**](icomponentauthenticate.md)
</dt> <dt>

[**Interfaces for Applications**](interfaces-for-applications.md)
</dt> </dl>

 

 




