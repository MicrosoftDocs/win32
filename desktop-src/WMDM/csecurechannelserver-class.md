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
| [**DecryptParam**](https://msdn.microsoft.com/en-us/library/Ff801048(v=VS.85).aspx)         | Decrypts the data contained in a parameter.                                                 |
| [**EncryptParam**](https://msdn.microsoft.com/en-us/library/Ff801049(v=VS.85).aspx)         | Encrypts the data contained in a parameter.                                                 |
| [**fIsAuthenticated**](https://msdn.microsoft.com/en-us/library/Ff801050(v=VS.85).aspx) | Verifies that a secure authentication channel has been successfully established.            |
| [**GetAppSec**](https://msdn.microsoft.com/en-us/library/Ff801051(v=VS.85).aspx)               | Retrieves the application security levels of the local and remote components.               |
| [**GetSessionKey**](https://msdn.microsoft.com/en-us/library/Ff801052(v=VS.85).aspx)       | Retrieves the current session key.                                                          |
| [**MACFinal**](https://msdn.microsoft.com/en-us/library/Ff801053(v=VS.85).aspx)                 | Releases the message authentication code (MAC) channel and retrieves a final MAC value.     |
| [**MACInit**](https://msdn.microsoft.com/en-us/library/Ff801054(v=VS.85).aspx)                   | Acquires a message authentication code (MAC) channel.                                       |
| [**MACUpdate**](https://msdn.microsoft.com/en-us/library/Ff801056(v=VS.85).aspx)               | Updates the message authentication code (MAC) value with a parameter value.                 |
| [**SACAuth**](https://msdn.microsoft.com/en-us/library/Ff801058(v=VS.85).aspx)                   | Establishes a secure authenticated channel between components.                              |
| [**SACGetProtocols**](https://msdn.microsoft.com/en-us/library/Ff801060(v=VS.85).aspx)   | Reports the protocols supported by a component.                                             |
| [**SetCertificate**](https://msdn.microsoft.com/en-us/library/Ff801063(v=VS.85).aspx)     | Specifies the certificate and private key of the secure authenticated channel (SAC) server. |
| [**SetSessionKey**](https://msdn.microsoft.com/en-us/library/Ff801065(v=VS.85).aspx)       | Sets the session key that is used to communicate with another component.                    |



 

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

 

 




