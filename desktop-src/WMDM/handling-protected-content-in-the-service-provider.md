---
title: Handling Protected Content in the Service Provider
description: Handling Protected Content in the Service Provider
ms.assetid: 5c18c8ec-d579-41df-8c25-c143fb9cdbef
keywords:
- Windows Media Device Manager,certificates
- Device Manager,certificates
- programming guide,certificates
- service providers,certificates
- creating service providers,certificates
- certificates
- Windows Media Device Manager,DRM-protected content
- Device Manager,DRM-protected content
- programming guide,DRM-protected content
- service providers,DRM-protected content
- creating service providers,DRM-protected content
- DRM-protected content
ms.topic: article
ms.date: 05/31/2018
---

# Handling Protected Content in the Service Provider

You can build a service provider that can send DRM-protected content to a device built on Portable Device DRM (PDDRM), but you cannot build a service provider that can send DRM-protected content to devices built on Windows Media DRM 10 for Portable Devices. These devices use MTP, and you cannot build your own MTP service provider.

The only extra step that a service provider must take to send DRM material to a PDDRM device is to get a Microsoft-issued certificate/key pair. See [Tools for Development](tools-for-development.md) to learn where to get this certificate/key. The licenses issued to these devices will be simplified licenses that only support simple playback of purchased content; they will not support time-expiring licenses. This license will be created for you by the secure content provider (provided by Microsoft for WMA/WMV files) and stored in the header of the file sent to the service provider. You will not have to take any special steps for protected files.

After sending the protected file, Windows Media Device Manager will call the service provider to request a special license storage file from the device. Windows Media Device Manager will add a copy of the new license to this file, and return it to the service provider to send back to the device. However, even if the service provider fails to find or return this file, the device should still be able to play the protected file by using the license copy in the file header.

## Related topics

<dl> <dt>

[**Creating a Service Provider**](creating-a-service-provider.md)
</dt> <dt>

[**Handling Protected Content**](handling-protected-content.md)
</dt> </dl>

 

 




