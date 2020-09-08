---
title: Tools for Development
description: Tools for Development
ms.assetid: 7932f599-a073-4fc8-82da-c0e7001c1809
keywords:
- Windows Media Device Manager,development tools
- Device Manager,development tools
- Windows Media Device Manager,certificates
- Device Manager,certificates
- Windows Media Device Manager,keys
- Device Manager,keys
- Windows Media Device Manager,libraries
- Device Manager,libraries
- Windows Media Device Manager,software development kit (SDK)
- Device Manager,software development kit (SDK)
- Windows Media Device Manager SDK
- Device Manager SDK
- Windows Media Player SDK
- Windows Media Format SDK
- Windows Media Rights Manager SDK
ms.topic: article
ms.date: 05/31/2018
---

# Tools for Development

This section describes the various certificates and keys, libraries, and SDKs you will need to program using the Windows Media Device Manager SDK.

Certificates and Keys

The Windows Media Device Manager SDK ships with a test key/certificate pair (in the key.c file) that can be used by an application or a service provider to use Windows Media Device Manager methods on unprotected content. This key/certificate pair allows the application or service provider to use most of the Windows Media Device Manager functionality.

However, to develop an application or service provider that can handle DRM-protected content, you must request one or more certificates (each with a key) from the [Windows Media Licensing Page](https://www.microsoft.com/licensing/default). Certificates are required for the following applications or objects:

-   Service Providers that handle DRM-protected content require a Windows Media Device Manager Service Provider Certificate (and key)
-   Applications that transfer DRM-protected content require a Windows Media Device Manager Transfer Certificate (and key)
-   Applications that play DRM-protected content require a DRM Certificate (and key).
-   License metering components require a metering certificate. This is provided by a license metering service built on the Windows Media Rights Manager SDK, which can be requested on the Windows Media Licensing Page.

Libraries and Headers

In addition to the libraries and headers mentioned in [Required Library and Header Files for an Application](required-library-and-header-files-for-an-application.md) or [Required Libraries and Headers for a Service Provider](required-libraries-and-headers-for-a-service-provider.md), any application or plug-in that formerly linked to WMDRMSDK.lib to call Windows Media Format SDK functions should now instead link to WMDRMSDKStub.Lib. This library file is used to access DRM-protected files. You can request this library from the Windows Media Licensing Page as well.

Related SDKs

The following Microsoft SDKs provide elements you may need in designing solutions for portable media devices.



| SDK Required                     | Required for...                                                                                                                                                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Windows Media Device Manager SDK | Desktop media player applications that communicate with portable devices<br/> Desktop applications that can exchange files or information with portable devices<br/> Windows Media Player metering COM objects<br/> |
| Windows Media Player SDK         | Windows Media Player plug-ins<br/> Windows Media Player metering COM objects<br/> Windows Media Player skins<br/>                                                                                                   |
| Windows Media Format SDK         | Audio or video players that can create or play files (particularly ASF files)<br/> Audio or video editing applications<br/>                                                                                               |
| Windows Media Rights Manager SDK | Applications or plug-ins that meter play counts on the desktop or device.                                                                                                                                                             |



 

## Related topics

<dl> <dt>

[**Getting Started**](getting-started.md)
</dt> </dl>

 

 





