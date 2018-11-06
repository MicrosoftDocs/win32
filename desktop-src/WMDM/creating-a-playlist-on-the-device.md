---
title: Creating a Playlist on the Device
description: Creating a Playlist on the Device
ms.assetid: 9f803e1a-ff33-443a-9448-e8c875d77e51
keywords:
- Windows Media Device Manager,playlists
- Device Manager,playlists
- programming guide,playlists
- desktop applications,playlists
- creating Windows Media Device Manager applications,playlists
- abstract playlists
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Playlist on the Device

The Windows Media Device Manager SDK provides the means for an MTP application to create a playlist on a device. This type of playlist is called an *abstract* playlist, because the file created on the device contains no media data, but only metadata, which holds the links to media files in the playlist.

Other abstract items that can be created on the device include albums (essentially playlists with extra properties such as cover art), contacts, and messages.

**To create a playlist**

1.  Acquire an [**IWMDMDevice3**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdmdevice3) interface to the target device.
2.  Call [**IWMDMDevice3::GetProperty**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmdevice3-getproperty) to obtain the g\_wszWMDMFormatsSupported property.
3.  If no playlist formats are supported, disallow sending playlists to the device, and skip the following steps. Otherwise, choose the device-supported format code that matches most closely the intended object type. The generic WMDM\_FORMATCODE\_ABSTRACTAUDIOVIDEOPLAYLIST and WMDM\_FORMATCODE\_ABSTRACTAUDIOLAYLIST format codes are the most commonly supported.
4.  Obtain an [**IWMDMStorage3**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdmstorage3) interface for the storage (the root or a folder) where you want to create the object. Some devices work best if the playlist object is placed in a top level folder named "Playlists".
5.  Create an empty metadata object by using [**IWMDMStorage3::CreateEmptyMetadataObject**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmstorage3-createemptymetadataobject).
6.  Using the **IWMDMMetaData** interface obtained in the previous step, call [**IWMDMMetaData::AddItem**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmmetadata-additem) to add your chosen format code (from step 3) to the storage metadata properties.
7.  Obtain the [**IWMDMStorageControl3**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdmstoragecontrol3) interface from the **IWMDMStorage3** interface.
8.  Call [**IWMDMStorageControl3::Insert3**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmstoragecontrol3-insert3) to insert a new playlist file in the selected storage. This file contains the metadata represented by the **IWMDMMetaData** interface you created in step 5 and passed to **Insert3**. The method returns an **IWMDMStorage** interface for the playlist file; you can query for the [**IWMDMStorage4**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdmstorage4) interface.
9.  Call [**IWMDMStorage4::SetReferences**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmstorage4-setreferences) to create references to the **IWMDMStorage** interfaces of the media files in the playlist.

For example code, see the \_OnCreatePlaylist function in the [Sample Desktop Application](sample-desktop-application.md).

> [!Note]  
> The Microsoft-provided MTP service provider enables an application to set references in metadata. To implement playlists, your application must be communicating with an MTP device or using a custom service provider that can handle abstract objects. The CE service provider handles playlist and album objects.

 

## Related topics

<dl> <dt>

[**Writing Files to the Device**](writing-files-to-the-device.md)
</dt> </dl>

 

 




