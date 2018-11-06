---
title: Requirements for Portable Audio Players to Appear in Windows Explorer
description: Requirements for Portable Audio Players to Appear in Windows Explorer
ms.assetid: 94227ed8-56e7-4366-9c38-9b5dbf907e16
keywords:
- Windows Media Device Manager,portable audio players
- Device Manager,portable audio players
- programming guide,portable audio players
- service providers,portable audio players
- creating service providers,portable audio players
- portable audio players
ms.topic: article
ms.date: 05/31/2018
---

# Requirements for Portable Audio Players to Appear in Windows Explorer

The portable audio player shell namespace extension provides Windows users with a consistent way to manage audio devices that are managed by Windows Media Device Manager. If you author your service provider and driver components according to the following guidelines, your device will show up in the shell namespace. Users will be able to interact with the contents of your device in a consistent manner in Windows Explorer to perform basic operations such as copy, delete, and rename.

The following shell requirements for service provider and driver components are intended to supplement the general Windows Media Device Manager guidelines.

Device Capabilities

Windows Media Device Manager service providers should be explicit in their supported capabilities. If a call is not supported, an error code must be returned. The appropriate fields must be set for the presence or absence of capabilities on return from the following functions:

-   [**IMDSPStorageGlobals::GetCapabilities**](/windows/desktop/api/mswmdm/nf-mswmdm-imdspstorageglobals-getcapabilities)
-   [**IMDSPStorage::GetAttributes**](/windows/desktop/api/mswmdm/nf-mswmdm-imdspstorage-getattributes)
-   [**IMDSPDevice::GetFormatSupport**](/windows/desktop/api/mswmdm/nf-mswmdm-imdspdevice-getformatsupport)

Service providers must support the following capabilities to be compatible with the shell:

-   Copy to device (with support for cancel and progress callbacks)
-   Delete file from device (with support for cancel and progress callbacks)
-   Rename file on device
-   Space reporting (total space, free space, unusable space)
-   Plug and Play (see [Enabling PnP for Devices](enabling-pnp-for-devices.md))
-   Format (preferably with support for cancel and progress callbacks)

If metadata is supported, the following fields must be supported for individual files. If no data is available, the field should be initialized as an empty string:



| Field        | Constant (defined in WMDM.idl) | Metadata tag    |
|--------------|--------------------------------|-----------------|
| Song Title   | g\_wszWMDMTitle                | WMDM/Title      |
| Track Number | g\_wszWMDMTrack                | WMDM/Track      |
| Artist       | g\_wszWMDMAuthor               | WMDM/Author     |
| Album        | g\_wszWMDMAlbumTitle           | WMDM/AlbumTitle |
| Year         | g\_wszWMDMYear                 | WMDM/Year       |
| Genre        | g\_wszWMDMGenre                | WMDM/Genre      |



 

Concurrency

Kernel mode drivers for Windows Media Device Manager need to be robust in handling concurrent access. For example, a user can be concurrently accessing the device through both the shell and media player or simply through multiple windows in the shell. As part of handling concurrency, drivers should not assume, just because the service provider is loaded, that the device is in use. Instead, they should implement a locking mechanism to serialize access to the device as needed for individual operations.

UI

Service providers for Windows Media Device Manager should not show any user interface. Any errors should be returned from method calls as specific Windows Media Device Manager error codes whenever possible.

Enabling in the Shell

If your package meets all of the shell requirements, you can enable your device to be shown in the shell by setting the *ShowInShell* value to 1 under the device parameters. For more information, see [Device Parameters](device-parameters.md).

## Related topics

<dl> <dt>

[**Creating a Service Provider**](creating-a-service-provider.md)
</dt> </dl>

 

 




