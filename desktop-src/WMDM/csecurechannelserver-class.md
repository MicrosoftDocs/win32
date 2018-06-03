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
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CSecureChannelServer Class

The **CSecureChannelServer** class is a helper class (not an interface) that enables a service provider or secure content provider to authenticate an application using the [**IComponentAuthenticate**](/windows/desktop/api/mswmdm/nn-mswmdm-icomponentauthenticate) interface, to encrypt and decrypt data, and to create MAC signatures. The authentication process requires that the application create a **CSecureChannelClient** object and that the service provider create a **CSecureChannelServer** object. The **CSecureChannelClient** and **CSecureChannelServer** classes are declared in the static link library, Mssachlp.lib. All methods of Windows Media Device Manager, service provider, and secure content provider interfaces can return WMDM\_E\_NOTCERTIFIED to indicate that the caller has not authenticated successfully.

The **CSecureChannelServer** class exposes the following methods.



| Method                                                            | Description                                                                                 |
|-------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| [**DecryptParam**](/windows/desktop/api/scserver/nf-scserver-csecurechannelserver-decryptparam)         | Decrypts the data contained in a parameter.                                                 |
| [**EncryptParam**](/windows/desktop/api/scserver/nf-scserver-csecurechannelserver-encryptparam)         | Encrypts the data contained in a parameter.                                                 |
| [**fIsAuthenticated**](/windows/desktop/api/scserver/nf-scserver-csecurechannelserver-fisauthenticated) | Verifies that a secure authentication channel has been successfully established.            |
| [**GetAppSec**](/windows/desktop/api/scserver/nf-scserver-csecurechannelserver-getappsec)               | Retrieves the application security levels of the local and remote components.               |
| [**GetSessionKey**](/windows/desktop/api/scserver/nf-scserver-csecurechannelserver-getsessionkey)       | Retrieves the current session key.                                                          |
| [**MACFinal**](/windows/desktop/api/scserver/nf-scserver-csecurechannelserver-macfinal)                 | Releases the message authentication code (MAC) channel and retrieves a final MAC value.     |
| [**MACInit**](/windows/desktop/api/scserver/nf-scserver-csecurechannelserver-macinit)                   | Acquires a message authentication code (MAC) channel.                                       |
| [**MACUpdate**](/windows/desktop/api/scserver/nf-scserver-csecurechannelserver-macupdate)               | Updates the message authentication code (MAC) value with a parameter value.                 |
| [**SACAuth**](/windows/desktop/api/scserver/nf-scserver-csecurechannelserver-sacauth)                   | Establishes a secure authenticated channel between components.                              |
| [**SACGetProtocols**](/windows/desktop/api/scserver/nf-scserver-csecurechannelserver-sacgetprotocols)   | Reports the protocols supported by a component.                                             |
| [**SetCertificate**](/windows/desktop/api/scserver/nf-scserver-csecurechannelserver-setcertificate)     | Specifies the certificate and private key of the secure authenticated channel (SAC) server. |
| [**SetSessionKey**](/windows/desktop/api/scserver/nf-scserver-csecurechannelserver-setsessionkey)       | Sets the session key that is used to communicate with another component.                    |



 

## Related topics

<dl> <dt>

[**CSecureChannelClient Class**](csecurechannelclient-class.md)
</dt> <dt>

[**IComponentAuthenticate Interface**](/windows/desktop/api/mswmdm/nn-mswmdm-icomponentauthenticate)
</dt> <dt>

[**Interfaces for Service Providers**](interfaces-for-service-providers.md)
</dt> <dt>

[**Using Secure Authenticated Channels**](using-secure-authenticated-channels.md)
</dt> </dl>

 

 




