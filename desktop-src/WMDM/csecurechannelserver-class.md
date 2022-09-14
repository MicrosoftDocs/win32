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
ms.topic: article
ms.date: 05/31/2018
---

# CSecureChannelServer Class

The **CSecureChannelServer** class is a helper class (not an interface) that enables a service provider or secure content provider to authenticate an application using the [**IComponentAuthenticate**](/windows/desktop/api/mswmdm/nn-mswmdm-icomponentauthenticate) interface, to encrypt and decrypt data, and to create MAC signatures. The authentication process requires that the application create a **CSecureChannelClient** object and that the service provider create a **CSecureChannelServer** object. The **CSecureChannelClient** and **CSecureChannelServer** classes are declared in the static link library, Mssachlp.lib. All methods of Windows Media Device Manager, service provider, and secure content provider interfaces can return WMDM\_E\_NOTCERTIFIED to indicate that the caller has not authenticated successfully.

The **CSecureChannelServer** class exposes the following methods.



| Method                                                            | Description                                                                                 |
|-------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| [**DecryptParam**](/previous-versions/bb231598(v=vs.85))         | Decrypts the data contained in a parameter.                                                 |
| [**EncryptParam**](/previous-versions/ms868509(v=msdn.10))         | Encrypts the data contained in a parameter.                                                 |
| [**fIsAuthenticated**](/previous-versions/bb231600(v=vs.85)) | Verifies that a secure authentication channel has been successfully established.            |
| [**GetAppSec**](/previous-versions/bb231601(v=vs.85))               | Retrieves the application security levels of the local and remote components.               |
| [**GetSessionKey**](/previous-versions/bb231602(v=vs.85))       | Retrieves the current session key.                                                          |
| [**MACFinal**](/previous-versions/ms868513(v=msdn.10))                 | Releases the message authentication code (MAC) channel and retrieves a final MAC value.     |
| [**MACInit**](/previous-versions/ms868514(v=msdn.10))                   | Acquires a message authentication code (MAC) channel.                                       |
| [**MACUpdate**](/previous-versions/ms868515(v=msdn.10))               | Updates the message authentication code (MAC) value with a parameter value.                 |
| [**SACAuth**](/previous-versions/ms868516(v=msdn.10))                   | Establishes a secure authenticated channel between components.                              |
| [**SACGetProtocols**](/previous-versions/ms868517(v=msdn.10))   | Reports the protocols supported by a component.                                             |
| [**SetCertificate**](/previous-versions/ms868518(v=msdn.10))     | Specifies the certificate and private key of the secure authenticated channel (SAC) server. |
| [**SetSessionKey**](/previous-versions/ms868519(v=msdn.10))       | Sets the session key that is used to communicate with another component.                    |



 

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

 

 