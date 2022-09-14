---
title: Using Secure Authenticated Channels
description: Using Secure Authenticated Channels
ms.assetid: ca4ab93c-0a3e-4fb5-be7f-a8f4eea3c9b7
keywords:
- Windows Media Device Manager,authentication
- Device Manager,authentication
- desktop applications,authentication
- service providers,authentication
- programming guide,authentication
- authentication
- Windows Media Device Manager,secure communication
- Device Manager,secure communication
- desktop applications,secure communication
- service providers,secure communication
- programming guide,secure communication
- secure communication
ms.topic: article
ms.date: 05/31/2018
---

# Using Secure Authenticated Channels

Windows Media Device Manager enables authentication and secure communication between components by providing two helper classes, [CSecureChannelClient](csecurechannelclient-class.md) (for applications) and [CSecureChannelServer](csecurechannelserver-class.md) (for service providers), and one interface, [**IComponentAuthenticate**](/windows/desktop/api/mswmdm/nn-mswmdm-icomponentauthenticate) (for both). Together these make up an API for the use of secure authenticated channels (SAC). SAC handles the following three tasks for service providers or applications using Windows Media Device Manager:

-   [Component Authentication](component-authentication.md)
-   [Encryption and Decryption](encryption-and-decryption.md)
-   [Message Authentication](message-authentication.md)

An application or service provider must handle component authentication, encryption, and decryption; message authentication is optional.

## Related topics

<dl> <dt>

[**Tasks Common to Applications and Service Providers**](tasks-common-to-applications-and-service-providers.md)
</dt> </dl>

 

 




