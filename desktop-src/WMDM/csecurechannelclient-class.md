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
| [**Authenticate**](https://msdn.microsoft.com/en-us/library/Ff801017(v=VS.85).aspx)         | Triggers the exchange of certificates between components to establish trust.                                              |
| [**DecryptParam**](https://msdn.microsoft.com/en-us/library/Ff801022(v=VS.85).aspx)         | Decrypts data received through a parameter.                                                                               |
| [**EncryptParam**](https://msdn.microsoft.com/en-us/library/Ff801024(v=VS.85).aspx)         | Encrypts data being sent out through a parameter.                                                                         |
| [**fIsAuthenticated**](https://msdn.microsoft.com/en-us/library/Ff801027(v=VS.85).aspx) | Verifies that a secure authentication channel has been successfully established. This method is not used by applications. |
| [**GetAppSec**](https://msdn.microsoft.com/en-us/library/Ff801030(v=VS.85).aspx)               | Retrieves the application security levels of the local and remote components.                                             |
| [**GetSessionKey**](https://msdn.microsoft.com/en-us/library/Ff801034(v=VS.85).aspx)       | Retrieves the current session key. This method is not used by applications.                                               |
| [**MACFinal**](https://msdn.microsoft.com/en-us/library/Ff801036(v=VS.85).aspx)                 | Releases the message authentication code (MAC) channel and retrieves a final MAC value.                                   |
| [**MACInit**](https://msdn.microsoft.com/en-us/library/Ff801038(v=VS.85).aspx)                   | Acquires a message authentication code (MAC) channel.                                                                     |
| [**MACUpdate**](https://msdn.microsoft.com/en-us/library/Ff801040(v=VS.85).aspx)               | Adds a value to a message authentication code (MAC).                                                                      |
| [**SetCertificate**](https://msdn.microsoft.com/en-us/library/Ff801042(v=VS.85).aspx)     | Specifies the certificate and private key of the secure authenticated channel (SAC) client.                               |
| [**SetInterface**](https://msdn.microsoft.com/en-us/library/Ff801044(v=VS.85).aspx)         | Selects the interface used for secure authenticated channel (SAC) communications.                                         |
| [**SetSessionKey**](https://msdn.microsoft.com/en-us/library/Ff801046(v=VS.85).aspx)       | Sets the session key that is used to communicate with another component. This method is not used by applications.         |



 

## Related topics

<dl> <dt>

[**CSecureChannelServer Class**](csecurechannelserver-class.md)
</dt> <dt>

[**IComponentAuthenticate Interface**](/windows/desktop/api/mswmdm/nn-mswmdm-icomponentauthenticate)
</dt> <dt>

[**Interfaces for Applications**](interfaces-for-applications.md)
</dt> </dl>

 

 




