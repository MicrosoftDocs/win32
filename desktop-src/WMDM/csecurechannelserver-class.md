---
title: CSecureChannelServer Class
description: CSecureChannelServer Class
ms.assetid: e6e1463a-5a26-4b83-85e0-a639d384a199
keywords:
- Windows Media Device Manager,CSecureChannelServer class
- Device Manager,CSecureChannelServer class
- service providers,CSecureChannelServer class
- programming reference,CSecureChannelServer class
- reference for Windows Media Device Manager,CSecureChannelServer class
- CSecureChannelServer class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CSecureChannelServer Class

The **CSecureChannelServer** class is a helper class (not an interface) that enables a service provider or secure content provider to authenticate an application using the [**IComponentAuthenticate**](/windows/win32/mswmdm/nn-mswmdm-icomponentauthenticate?branch=master) interface, to encrypt and decrypt data, and to create MAC signatures. The authentication process requires that the application create a **CSecureChannelClient** object and that the service provider create a **CSecureChannelServer** object. The **CSecureChannelClient** and **CSecureChannelServer** classes are declared in the static link library, Mssachlp.lib. All methods of Windows Media Device Manager, service provider, and secure content provider interfaces can return WMDM\_E\_NOTCERTIFIED to indicate that the caller has not authenticated successfully.

The **CSecureChannelServer** class exposes the following methods.



| Method                                                            | Description                                                                                 |
|-------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| [**DecryptParam**](/windows/win32/scserver/nf-scserver-csecurechannelserver-decryptparam?branch=master)         | Decrypts the data contained in a parameter.                                                 |
| [**EncryptParam**](/windows/win32/scserver/nf-scserver-csecurechannelserver-encryptparam?branch=master)         | Encrypts the data contained in a parameter.                                                 |
| [**fIsAuthenticated**](/windows/win32/scserver/nf-scserver-csecurechannelserver-fisauthenticated?branch=master) | Verifies that a secure authentication channel has been successfully established.            |
| [**GetAppSec**](/windows/win32/scserver/nf-scserver-csecurechannelserver-getappsec?branch=master)               | Retrieves the application security levels of the local and remote components.               |
| [**GetSessionKey**](/windows/win32/scserver/nf-scserver-csecurechannelserver-getsessionkey?branch=master)       | Retrieves the current session key.                                                          |
| [**MACFinal**](/windows/win32/scserver/nf-scserver-csecurechannelserver-macfinal?branch=master)                 | Releases the message authentication code (MAC) channel and retrieves a final MAC value.     |
| [**MACInit**](/windows/win32/scserver/nf-scserver-csecurechannelserver-macinit?branch=master)                   | Acquires a message authentication code (MAC) channel.                                       |
| [**MACUpdate**](/windows/win32/scserver/nf-scserver-csecurechannelserver-macupdate?branch=master)               | Updates the message authentication code (MAC) value with a parameter value.                 |
| [**SACAuth**](/windows/win32/scserver/nf-scserver-csecurechannelserver-sacauth?branch=master)                   | Establishes a secure authenticated channel between components.                              |
| [**SACGetProtocols**](/windows/win32/scserver/nf-scserver-csecurechannelserver-sacgetprotocols?branch=master)   | Reports the protocols supported by a component.                                             |
| [**SetCertificate**](/windows/win32/scserver/nf-scserver-csecurechannelserver-setcertificate?branch=master)     | Specifies the certificate and private key of the secure authenticated channel (SAC) server. |
| [**SetSessionKey**](/windows/win32/scserver/nf-scserver-csecurechannelserver-setsessionkey?branch=master)       | Sets the session key that is used to communicate with another component.                    |



 

## Related topics

<dl> <dt>

[**CSecureChannelClient Class**](csecurechannelclient-class.md)
</dt> <dt>

[**IComponentAuthenticate Interface**](/windows/win32/mswmdm/nn-mswmdm-icomponentauthenticate?branch=master)
</dt> <dt>

[**Interfaces for Service Providers**](interfaces-for-service-providers.md)
</dt> <dt>

[**Using Secure Authenticated Channels**](using-secure-authenticated-channels.md)
</dt> </dl>

 

 




