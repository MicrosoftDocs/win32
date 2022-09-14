---
title: Writing Files to the Device
description: Writing Files to the Device
ms.assetid: 66eaed16-032b-4ac0-a768-aded80f10255
keywords:
- Windows Media Device Manager,writing files to devices
- Device Manager,writing files to devices
- programming guide,writing files to devices
- desktop applications,writing files to devices
- creating Windows Media Device Manager applications,writing files to devices
- writing files to devices,about
ms.topic: article
ms.date: 05/31/2018
---

# Writing Files to the Device

Before sending a file to a device, your application must find out what types of files and formats the device can handle, so that the application can determine whether the file should be transcoded before sending, or sent unmodified, or not sent at all.

The following steps show how to send an existing file down to the device. To create a new file on the device, such as a playlist, see [Creating a Playlist on the Device](creating-a-playlist-on-the-device.md).

1.  Get the format of the file you intend to send to the device. For more information, see [Discovering a File's Format](discovering-a-files-format.md).
2.  If the device is intended to play the file,
    -   Query the file for its format capabilities. For more information, see [Discovering Device Format Capabilities](discovering-device-format-capabilities.md).
    -   Find an acceptable format that the application can create from the original file.
    -   If the file needs to be transcoded, transcode it.
3.  Find a parent storage for the new object. Windows Media Device Manager does not provide a way to discover the standard storage location for any particular file types (video or audio files, WMV or BMP, a "Favorites" folder, and so on), so you will have to examine each device to try to figure out where best to store the new object. (Other applications enforce a certain folder structure, for example, Windows Media Player creates Albums, Playlists and Music folders where the Music folder contains an Artist and AlbumName heirarchy. For this reason, and because some devices may not have been tested with software other than Windows Media Player, be aware that the placement of playlist or album objects in any folder other than the Playlists or Albums folders may sometimes lead to nonfunctioning objects on some devices.)
4.  If the target storage supports [**IWMDMStorageControl3**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdmstoragecontrol3), create a new metadata interface by calling [**IWMDMStorage3::CreateEmptyMetadataObject**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmstorage3-createemptymetadataobject). Set metadata on an [**IWMDMMetaData**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdmmetadata) interface. For more information, see [Setting Metadata on a File](setting-metadata-on-a-file.md). The only required metadata is g\_wszWMDMFormatCode (a [**WMDM\_FORMATCODE**](wmdm-formatcode.md) value describing the content), but the more metadata you can provide, the more efficient the transfer will be for the service provider.
5.  Send the file to the device by using the [**Insert**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmstoragecontrol-insert), [**Insert2**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmstoragecontrol2-insert2), or [**Insert3**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmstoragecontrol3-insert3) method. **Insert3** allows you to include the metadata on the device as part of the method. For more information, see [Sending the File to the Device](sending-the-file-to-the-device.md).

Code demonstrating each of these steps is provided on the linked topic pages.

## Related topics

<dl> <dt>

[**Creating a Windows Media Device Manager Application**](creating-a-windows-media-device-manager-application.md)
</dt> </dl>

 

 




