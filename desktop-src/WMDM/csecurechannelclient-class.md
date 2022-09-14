---
title: CSecureChannelClient Class
description: CSecureChannelClient Class
ms.assetid: f02220b8-0d1c-416c-97ea-e5e7455fcbba
keywords:
- Windows Media Device Manager,CSecureChannelClient class
- Device Manager,CSecureChannelClient class
- desktop applications,CSecureChannelClient class
- programming reference,CSecureChannelClient class
- reference for Windows Media Device Manager,CSecureChannelClient class
- CSecureChannelClient class
ms.topic: article
ms.date: 05/31/2018
---

# CSecureChannelClient Class

The **CSecureChannelClient** class is a helper class (not an interface) that enables applications to authenticate themselves, encrypt and decrypt data, and create MACs.

The **CSecureChannelClient** class exposes the following methods.



| Method                                                            | Description                                                                                                               |
|-------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| [**Authenticate**](/previous-versions/ms983906(v=msdn.10))         | Triggers the exchange of certificates between components to establish trust.                                              |
| [**DecryptParam**](/previous-versions/bb231586(v=vs.85))         | Decrypts data received through a parameter.                                                                               |
| [**EncryptParam**](/previous-versions/bb231587(v=vs.85))         | Encrypts data being sent out through a parameter.                                                                         |
| [**fIsAuthenticated**](/previous-versions/ms868497(v=msdn.10)) | Verifies that a secure authentication channel has been successfully established. This method is not used by applications. |
| [**GetAppSec**](/previous-versions/ms868498(v=msdn.10))               | Retrieves the application security levels of the local and remote components.                                             |
| [**GetSessionKey**](/previous-versions/bb231590(v=vs.85))       | Retrieves the current session key. This method is not used by applications.                                               |
| [**MACFinal**](/previous-versions/bb231591(v=vs.85))                 | Releases the message authentication code (MAC) channel and retrieves a final MAC value.                                   |
| [**MACInit**](/previous-versions/bb231592(v=vs.85))                   | Acquires a message authentication code (MAC) channel.                                                                     |
| [**MACUpdate**](/previous-versions/bb231593(v=vs.85))               | Adds a value to a message authentication code (MAC).                                                                      |
| [**SetCertificate**](/previous-versions/ms868504(v=msdn.10))     | Specifies the certificate and private key of the secure authenticated channel (SAC) client.                               |
| [**SetInterface**](/previous-versions/bb231595(v=vs.85))         | Selects the interface used for secure authenticated channel (SAC) communications.                                         |
| [**SetSessionKey**](/previous-versions/ms868506(v=msdn.10))       | Sets the session key that is used to communicate with another component. This method is not used by applications.         |



 

## Related topics

<dl> <dt>

[**CSecureChannelServer Class**](csecurechannelserver-class.md)
</dt> <dt>

[**IComponentAuthenticate Interface**](/windows/desktop/api/mswmdm/nn-mswmdm-icomponentauthenticate)
</dt> <dt>

[**Interfaces for Applications**](interfaces-for-applications.md)
</dt> </dl>

 

 