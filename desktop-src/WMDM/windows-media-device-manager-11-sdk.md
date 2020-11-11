---
title: Windows Media Device Manager 11 SDK
description: Windows Media Device Manager 11 SDK
ms.assetid: 9c0c9a96-1335-4ae2-9393-bfab0dfe24c6
keywords:
- Windows Media Device Manager,about
- Device Manager,about
- Media Transfer Protocol (MTP)
- MTP (Media Transfer Protocol)
- Mass Storage Class (MSC)
- MSC (Mass Storage Class)
- Windows Media Device Manager,desktop applications
- Device Manager,desktop applications
- desktop applications,about
- Windows Media Device Manager,service providers
- Device Manager,service providers
- service providers,about
- Windows Media Device Manager,plug-ins
- Device Manager,plug-insp
- plug-ins,about
ms.topic: article
ms.date: 05/31/2018
---

# Windows Media Device Manager 11 SDK

> [!IMPORTANT]
> The Windows Media Device Manager APIs are now included in the Windows SDK. No additional SDK downloads are required.

 

The Microsoft Windows Media Device Manager Software Development Kit (SDK) enables you to build desktop applications and components that can communicate with connected portable devices. Windows Media Device Manager enables your application or component to enumerate, explore, and exchange files with a device, query for metadata, and request play count information. Applications or components built on Windows Media Device Manager have a consistent API for communicating with a wide range of devices including Media Transfer Protocol (MTP), Mass Storage Class (MSC), RAPI, and other devices built on both the latest and previous versions of Windows Media technology.

You can build the following items using the Windows Media Device Manager SDK:

-   Desktop applications, such as custom media players. All communication between an application and a portable device must go through Windows Media Device Manager, which acts as a broker between the application, the Microsoft digital rights management system, and the service provider.
-   Service providers, which act as the communication link between a custom device and a desktop application. Although Microsoft provides a number of service providers that can communicate with most devices out of the box, you can build a custom service provider to customize the communication between a device and a desktop application.
-   Plug-ins, which can perform tasks such as requesting and logging play counts on devices. These plug-ins can be attached to other desktop applications, such as the Windows Media Player to send information to content providers to handle royalty payments to artists.

To download the Windows Media Device Manager SDK, see [the Windows Media Download page](https://msdn.microsoft.com/windows/desktop/aa904949) on the MSDN Web site.

This SDK is a component of the Microsoft Windows Media Software Development Kit. Other components include the Windows Media Format SDK, the Windows Media Services SDK, the Windows Media Encoder SDK, the Windows Media Rights Manager SDK, and the Windows Media Player SDK.

This documentation includes the following sections.



| Section                                            | Description                                                                                                                                                                                                                                                     |
|----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Getting Started](getting-started.md)             | Describes what is new in this version of Windows Media Device Manager, gives an overview of how Windows Media Device Manager works, describes what will be needed to develop an application or service provider, and explains the samples shipped with the SDK. |
| [Programming Guide](programming-guide.md)         | Discusses how to build applications and service providers.                                                                                                                                                                                                      |
| [Programming Reference](programming-reference.md) | Provides C++ reference information for the interfaces, methods, classes, and structures supported by the Windows Media Device Manager SDK.                                                                                                                      |
| [*Glossary*](wmdm-glossary.md)                    | Defines terms used in this documentation.                                                                                                                                                                                                                       |



 

 

 




