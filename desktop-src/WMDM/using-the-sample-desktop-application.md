---
title: Using the Sample Desktop Application
description: Using the Sample Desktop Application
ms.assetid: 5e3e5283-9e27-4f6a-93a9-84d84f2e875a
keywords:
- Windows Media Device Manager,samples
- Device Manager,samples
- desktop applications,samples
- Windows Media Device Manager,desktop application sample
- Device Manager,desktop application sample
- samples,desktop applications
ms.topic: article
ms.date: 05/31/2018
---

# Using the Sample Desktop Application

The sample desktop application is a basic two-paned window somewhat like Windows Explorer. It allows you to browse the contents of a device, using a tree view display of folders in the left pane, and files in the right pane. The root of each folder tree is logically considered a different device, although some devices might represent themselves as several objects (one for each root storage). To read the basic properties of either a folder or a file, right-click the object and select **Properties**.

You can delete files on the device by selecting a file in the right pane and selecting **Delete** on the **File** menu. To add media files to the device, you can drag files from the desktop onto the right pane of the program. Note that files must be of a media format supported by the device; files of unacceptable formats (non-media files such as .txt files, or media formats not supported by the device) will not be sent to the device. (Note that this restriction is the program's; Windows Media Device Manager enables you to send any file to a device if the device will accept it.)

To capture callback events sent to the [**IWMDMOperation**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdmoperation) interface, you must check the "Use Operation Interface" option in the **Options** menu.

The **Options** menu also enables you to choose whether to use several more advanced interfaces with features supported by advanced devices.

The **Containers** menu has options to allow you to create a playlist or an album. To create a playlist, select one or more songs on the device and click **Create Playlist** on the **Containers** menu. This feature only works on MTP devices, because the code only supports the creation of an "virtual" playlist file. (A virtual playlist is a playlist that is specified only by metadata values, rather than by a physical file, for example a WPL file.) The device must support empty playlists to use this feature.

To create an album (a playlist with an associated image), select one or more songs on the device and click **Create Album** on the **Containers** menu. A dialog box allows you to browse to a picture file on your computer to associate with the album. Similarly to the way it creates playlists, the application creates an "empty" album file; if the device does not support empty albums, this feature will not work.

## Related topics

<dl> <dt>

[**Sample Desktop Application**](sample-desktop-application.md)
</dt> </dl>

 

 




