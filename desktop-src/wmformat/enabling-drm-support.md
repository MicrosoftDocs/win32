---
title: Enabling DRM Support
description: Enabling DRM Support
ms.assetid: 90e92373-7fc2-4478-a179-22f22dbc3a3d
keywords:
- Windows Media Format SDK,enabling DRM support
- Advanced Systems Format (ASF),enabling DRM support
- ASF (Advanced Systems Format),enabling DRM support
- digital rights management (DRM),enabling support
- DRM (digital rights management),enabling support
ms.topic: article
ms.date: 05/31/2018
---

# Enabling DRM Support

You can use the Microsoft Windows Media Format Software Development Kit (SDK) to build applications that can apply digital rights management (DRM) protection and play live-DRM streams or DRM-protected files. Support is also provided for backing up and restoring a player's DRM licenses, and for [*individualizing*](wmformat-glossary.md) players.

This documentation assumes that you have a basic familiarity with Microsoft's digital rights management technology. A basic overview of Windows Media DRM is provided in the [Digital Rights Management Features](digital-rights-management-features.md) section of this documentation. 

> [!Note]  
> DRM is not supported by the x64-based version of this SDK.

 

The following sections describe how to enable DRM support.



| Section                                                                                                                        | Description                                                                                                                                                                                     |
|--------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Obtaining the Required DRM Library](obtaining-the-required-drm-library.md)                                                   | Describes the steps involved in obtaining the static library that is required to create DRM-enabled applications.                                                                               |
| [DRM Protection and Content License Distribution](drm-protection-and-content-license-distribution.md)                         | Compares the DRM capabilities of the Windows Media Format SDK with the Windows Media Rights Manager SDK.                                                                                        |
| [DRM Network Operations](drm-network-operations.md)                                                                           | Describes how your application should handle the DRM operations that communicate over the Internet, or other networks.                                                                          |
| [Creating Protected Files](creating-protected-files.md)                                                                       | Describes how to create DRM-protected files.                                                                                                                                                    |
| [Reading Protected Files](reading-protected-files.md)                                                                         | Describes ways to acquire licenses for content and the benefits of implementing silent license acquisition.                                                                                     |
| [Viewing Attributes of Protected Files](viewing-attributes-of-protected-files.md)                                             | Describes how to use the [**IWMDRMEditor**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmdrmeditor) interface on the metadata editor object to view attributes of protected files without having the required static library for DRM. |
| [Working with Revocation Lists](working-with-revocation-lists.md)                                                             | Describes revocation lists and how they are implemented.                                                                                                                                        |
| [Backing Up and Restoring Licenses](backing-up-and-restoring-licenses.md)                                                     | Describes how users can manage their content licenses by backing up and restoring them to their current computer or to other computers.                                                         |
| [Individualizing DRM Applications](individualizing-drm-applications.md)                                                       | Describes how the [*individualization*](wmformat-glossary.md) feature increases security in a DRM system.                                                           |
| [Working with Output Protection Levels](working-with-output-protection-levels.md)                                             | Describes how to support Output Protection Levels, which are used to record allowed actions in DRM version 10 licenses.                                                                         |
| [Using the Windows Media DRM 10 for Network Devices Protocol](using-the-windows-media-drm-10-for-network-devices-protocol.md) | Describes how to support secure device streaming by using the Windows Media DRM 10 for Network Devices protocol.                                                                                |
| [Implementing License Revocation](implementing-license-revocation.md)                                                         | Describes the process of license revocation, and the actions your application must take to implement it.                                                                                        |
| [Burning Playlists That Contain Secure Files](burning-playlists-that-contain-secure-files.md)                                 | Describes how to implement playlist burning in your application.                                                                                                                                |



 

The SDK includes several sample applications that demonstrate how to read protected files; the fullest example is DRMShow. For more information, see [Sample Applications](sample-applications.md).

## Related topics

<dl> <dt>

[**Features**](features.md)
</dt> </dl>

 

 




