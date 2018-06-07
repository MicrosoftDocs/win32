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
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CSecureChannelClient Class

The **CSecureChannelClient** class is a helper class (not an interface) that enables applications to authenticate themselves, encrypt and decrypt data, and create MACs.

The **CSecureChannelClient** class exposes the following methods.



| Method                                                            | Description                                                                                                               |
|-------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| [**Authenticate**](/windows/desktop/api/scclient/nf-scclient-csecurechannelclient-authenticate)         | Triggers the exchange of certificates between components to establish trust.                                              |
| [**DecryptParam**](/windows/desktop/api/scclient/nf-scclient-csecurechannelclient-decryptparam)         | Decrypts data received through a parameter.                                                                               |
| [**EncryptParam**](/windows/desktop/api/scclient/nf-scclient-csecurechannelclient-encryptparam)         | Encrypts data being sent out through a parameter.                                                                         |
| [**fIsAuthenticated**](/windows/desktop/api/scclient/nf-scclient-csecurechannelclient-fisauthenticated) | Verifies that a secure authentication channel has been successfully established. This method is not used by applications. |
| [**GetAppSec**](/windows/desktop/api/scclient/nf-scclient-csecurechannelclient-getappsec)               | Retrieves the application security levels of the local and remote components.                                             |
| [**GetSessionKey**](/windows/desktop/api/scclient/nf-scclient-csecurechannelclient-getsessionkey)       | Retrieves the current session key. This method is not used by applications.                                               |
| [**MACFinal**](/windows/desktop/api/scclient/nf-scclient-csecurechannelclient-macfinal)                 | Releases the message authentication code (MAC) channel and retrieves a final MAC value.                                   |
| [**MACInit**](/windows/desktop/api/scclient/nf-scclient-csecurechannelclient-macinit)                   | Acquires a message authentication code (MAC) channel.                                                                     |
| [**MACUpdate**](/windows/desktop/api/scclient/nf-scclient-csecurechannelclient-macupdate)               | Adds a value to a message authentication code (MAC).                                                                      |
| [**SetCertificate**](/windows/desktop/api/scclient/nf-scclient-csecurechannelclient-setcertificate)     | Specifies the certificate and private key of the secure authenticated channel (SAC) client.                               |
| [**SetInterface**](/windows/desktop/api/scclient/nf-scclient-csecurechannelclient-setinterface)         | Selects the interface used for secure authenticated channel (SAC) communications.                                         |
| [**SetSessionKey**](/windows/desktop/api/scclient/nf-scclient-csecurechannelclient-setsessionkey)       | Sets the session key that is used to communicate with another component. This method is not used by applications.         |



 

## Related topics

<dl> <dt>

[**CSecureChannelServer Class**](csecurechannelserver-class.md)
</dt> <dt>

[**IComponentAuthenticate Interface**](/windows/desktop/api/mswmdm/nn-mswmdm-icomponentauthenticate)
</dt> <dt>

[**Interfaces for Applications**](interfaces-for-applications.md)
</dt> </dl>

 

 




