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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CSecureChannelClient Class

The **CSecureChannelClient** class is a helper class (not an interface) that enables applications to authenticate themselves, encrypt and decrypt data, and create MACs.

The **CSecureChannelClient** class exposes the following methods.



| Method                                                            | Description                                                                                                               |
|-------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| [**Authenticate**](/windows/win32/scclient/nf-scclient-csecurechannelclient-authenticate?branch=master)         | Triggers the exchange of certificates between components to establish trust.                                              |
| [**DecryptParam**](/windows/win32/scclient/nf-scclient-csecurechannelclient-decryptparam?branch=master)         | Decrypts data received through a parameter.                                                                               |
| [**EncryptParam**](/windows/win32/scclient/nf-scclient-csecurechannelclient-encryptparam?branch=master)         | Encrypts data being sent out through a parameter.                                                                         |
| [**fIsAuthenticated**](/windows/win32/scclient/nf-scclient-csecurechannelclient-fisauthenticated?branch=master) | Verifies that a secure authentication channel has been successfully established. This method is not used by applications. |
| [**GetAppSec**](/windows/win32/scclient/nf-scclient-csecurechannelclient-getappsec?branch=master)               | Retrieves the application security levels of the local and remote components.                                             |
| [**GetSessionKey**](/windows/win32/scclient/nf-scclient-csecurechannelclient-getsessionkey?branch=master)       | Retrieves the current session key. This method is not used by applications.                                               |
| [**MACFinal**](/windows/win32/scclient/nf-scclient-csecurechannelclient-macfinal?branch=master)                 | Releases the message authentication code (MAC) channel and retrieves a final MAC value.                                   |
| [**MACInit**](/windows/win32/scclient/nf-scclient-csecurechannelclient-macinit?branch=master)                   | Acquires a message authentication code (MAC) channel.                                                                     |
| [**MACUpdate**](/windows/win32/scclient/nf-scclient-csecurechannelclient-macupdate?branch=master)               | Adds a value to a message authentication code (MAC).                                                                      |
| [**SetCertificate**](/windows/win32/scclient/nf-scclient-csecurechannelclient-setcertificate?branch=master)     | Specifies the certificate and private key of the secure authenticated channel (SAC) client.                               |
| [**SetInterface**](/windows/win32/scclient/nf-scclient-csecurechannelclient-setinterface?branch=master)         | Selects the interface used for secure authenticated channel (SAC) communications.                                         |
| [**SetSessionKey**](/windows/win32/scclient/nf-scclient-csecurechannelclient-setsessionkey?branch=master)       | Sets the session key that is used to communicate with another component. This method is not used by applications.         |



 

## Related topics

<dl> <dt>

[**CSecureChannelServer Class**](csecurechannelserver-class.md)
</dt> <dt>

[**IComponentAuthenticate Interface**](/windows/win32/mswmdm/nn-mswmdm-icomponentauthenticate?branch=master)
</dt> <dt>

[**Interfaces for Applications**](interfaces-for-applications.md)
</dt> </dl>

 

 




