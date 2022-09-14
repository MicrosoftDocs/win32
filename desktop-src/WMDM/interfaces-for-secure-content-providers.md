---
title: Interfaces for Secure Content Providers
description: Interfaces for Secure Content Providers
ms.assetid: a3eecdb8-55a9-46e3-95d1-0fb9bd59f393
keywords:
- Windows Media Device Manager,DRM-protected content
- Device Manager,DRM-protected content
- programming reference,DRM-protected content
- reference for Windows Media Device Manager,DRM-protected content
- DRM-protected content
- Windows Media Device Manager,secure content provider (SCP)
- Device Manager,secure content provider (SCP)
- programming reference,secure content provider (SCP)
- reference for Windows Media Device Manager,secure content provider (SCP)
- secure content provider (SCP)
- SCP (secure content provider)
- Windows Media Device Manager,SCP interfaces
- Device Manager,SCP interfaces
- programming reference,SCP interfaces
- reference for Windows Media Device Manager,SCP interfaces
- SCP interfaces,about
ms.topic: article
ms.date: 05/31/2018
---

# Interfaces for Secure Content Providers

A secure content provider (SCP) is a plug-in component that enables Windows Media Device Manager to transfer and request rights information from DRM-protected content. Microsoft provides an SCP component that can handle DRM-protected WMA and WMV files. If your device or application will use DRM-protected content of other formats, it should create an SCP component by implementing all of these interfaces. Otherwise, you will not need to use these interfaces.



| Interface                                                  | Description                                                                                                                                                                                                                                          |
|------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ISCPSecureAuthenticate**](/windows/desktop/api/mswmdm/nn-mswmdm-iscpsecureauthenticate)   | The primary interface of the secure content provider.                                                                                                                                                                                                |
| [**ISCPSecureAuthenticate2**](/windows/desktop/api/mswmdm/nn-mswmdm-iscpsecureauthenticate2) | Extends **ISCPSecureAuthenticate** by providing a way to get a session object.                                                                                                                                                                       |
| [**ISCPSecureExchange**](/windows/desktop/api/mswmdm/nn-mswmdm-iscpsecureexchange)           | Used to exchange secured content and rights associated with content.                                                                                                                                                                                 |
| [**ISCPSecureExchange2**](/windows/desktop/api/mswmdm/nn-mswmdm-iscpsecureexchange2)         | Extends **ISCPSecureExchange** by providing a new version of the **TransferContainerData** method.                                                                                                                                                   |
| [**ISCPSecureExchange3**](/windows/desktop/api/mswmdm/nn-mswmdm-iscpsecureexchange3)         | Extends **ISCPSecureExchange2** by providing improved data exchange performance, and a transfer complete callback method.                                                                                                                            |
| [**ISCPSecureQuery**](/windows/desktop/api/mswmdm/nn-mswmdm-iscpsecurequery)                 | Queried by Windows Media Device Manager to determine ownership of secured content.                                                                                                                                                                   |
| [**ISCPSecureQuery2**](/windows/desktop/api/mswmdm/nn-mswmdm-iscpsecurequery2)               | Extends **ISCPSecureQuery** through functionality that determines whether the secure content provider is responsible for the content, and if so, providing a URL for updating revoked components and determining which components have been revoked. |
| [**ISCPSecureQuery3**](/windows/desktop/api/mswmdm/nn-mswmdm-iscpsecurequery3)               | Extends **ISCPSecureQuery2** by providing a set of new methods for retrieving the rights and making decision on a clear channel.                                                                                                                     |
| [**ISCPSession**](/windows/desktop/api/mswmdm/nn-mswmdm-iscpsession)                         | Provides efficient common state management for multiple operations.                                                                                                                                                                                  |



 

 

 




