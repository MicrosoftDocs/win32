---
title: Handling Protected Content
description: Handling Protected Content
ms.assetid: f218d69e-ac80-43ba-be31-af3abf2b8de9
keywords:
- Windows Media Device Manager,certificates
- Device Manager,certificates
- desktop applications,certificates
- service providers,certificates
- programming guide,certificates
- certificates
- Windows Media Device Manager,secure content provider (SCP)
- Device Manager,secure content provider (SCP)
- desktop applications,secure content provider (SCP)
- service providers,secure content provider (SCP)
- programming guide,secure content provider (SCP)
- secure content provider (SCP)
- SCP (secure content provider)
- Windows Media Device Manager,DRM-protected content
- Device Manager,DRM-protected content
- programming guide,DRM-protected content
- desktop applications,DRM-protected content
- service providers,DRM-protected content
- DRM-protected content
ms.topic: article
ms.date: 05/31/2018
---

# Handling Protected Content

If you are building an application or service provider that will consume content protected by Windows Media digital rights management (DRM), you must have a key/certificate pair issued by Microsoft. To learn where to get this certificate, see [Tools for Development](tools-for-development.md). If you do not intend to handle protected content, you can use the dummy key and certificate provided with this SDK in a file named key.c.

For any file that is protected by DRM technology, Windows Media Device Manager requires the presence of a secure content provider (SCP) for that file format. Microsoft provides an SCP module for WMA and WMV files. If your application or service provider will be handling DRM-protected content of another format, you must provide your own SCP module. An SCP module is a COM object that implements all the [interfaces for Secure Content Providers](interfaces-for-secure-content-providers.md).

An application can send DRM-protected content to devices built on either Windows Media DRM 10 for Portable Devices, or Portable Device DRM (PDDRM). However, you can only create a service provider for devices built on PDDRM; you cannot create a service provider for devices built on Windows Media DRM 10 for Portable Devices. These latter devices can only use the Microsoft-provided MTP service provider.

Devices built on PDDRM can only support licenses for purchased content. Licenses that have time-expiration conditions are only supported by devices built on Windows Media DRM 10 for Portable Devices, which have special requirements such as a secure clock and individualization. Windows Media DRM 10 for Portable Devices SDK gives details on device requirements to support version 10 technology.

Before sending DRM content to the device, an application should verify several things:

-   That the device supports DRM technology.
-   What version of DRM technology it supports (version 10 or earlier).
-   If the device is built on version 10, that all its components are up to date (such as the secure clock and any individualization requirements).

All method calls to answer these questions are made by the client and handled by Windows Media Device Manager and the secure content provider component; the service provider does not handle any of these calls.

If the device does not support Windows Media DRM 10 for Portable Devices, it might still be able to consume protected content (depending on the content license and the device design), but any content sent to it will have a simplified use license with limited rights (for example, no time expiration).

-   For examples demonstrating how an application verifies whether a device can handle protected content, and whether it needs to update its DRM components, see [Handling Protected Content in the Application](handling-protected-content-in-the-application.md).
-   For more information about building a service provider that can handle protected content, see [Handling Protected Content in the Service Provider](handling-protected-content-in-the-service-provider.md).

> [!Note]  
> Many Windows Media Device Manager file transfer or rights requesting methods will fail (often with a mysterious **HRESULT** value) when handling DRM-protected files with a debugger attached. Therefore, you must use alternate ways to debug your code, such as logging outputs to a Windows form or a log file. For more information on logging options, see [Enabling Logging](enabling-logging.md). If you are running a debugger on protected content, a method will return one of the error codes listed in the DRM section [Error Codes](error-codes.md), or possibly an unknown error code. If you get mysterious **HRESULT** values when running a debugger on protected content or methods, DRM protection might be the cause.

 

## Related topics

<dl> <dt>

[**Programming Guide**](programming-guide.md)
</dt> </dl>

 

 




