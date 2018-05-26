---
title: Interfaces
description: Interfaces
ms.assetid: 748a8db7-159d-4043-beac-e0516327bcef
keywords:
- Windows Media Player,interfaces
- Windows Media Player Mobile,interfaces
- Windows Media Player object model,interfaces
- object model,interfaces
- ActiveX control,interfaces
- Windows Media Player ActiveX control,interfaces
- Windows Media Player Mobile ActiveX control,interfaces
- reference for object model,interfaces
- interface object model reference
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Interfaces

This section documents the COM interfaces exposed by the Windows Media Player ActiveX control and the Windows Media Player Mobile ActiveX control.

The accessor methods of the **IWMPCore** or **IWMPPlayer** interface are used to retrieve specific interfaces. These interfaces, in turn, may have accessor methods for retrieving further interfaces. Calling **QueryInterface** on one of these interfaces is only necessary when you retrieve the base version of an interface and want to call a method on a later version of the same interface.

> [!Note]  
> All methods and events are fully supported in Windows Media Player 10 Mobile and later unless explicitly stated otherwise.

 

The Windows Media Player control exposes the following interfaces.



| Interface                                                    | Description                                                                                                                                                                               |
|--------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [\_WMPOCXEvents](-wmpocxevents-interface.md)                | Provides events originating from the Windows Media Player control to which an embedding program can respond.                                                                              |
| [IWMPCdrom](/windows/win32/wmp/nn-wmp-iwmpcdrom?branch=master)                                   | Accesses a CD or DVD in a drive.                                                                                                                                                          |
| [IWMPCdromBurn](/windows/win32/wmp/nn-wmp-iwmpcdromburn?branch=master)                           | Provides methods to manage creating audio CDs.                                                                                                                                            |
| [IWMPCdromCollection](/windows/win32/wmp/nn-wmp-iwmpcdromcollection?branch=master)               | Accesses a collection of CD or DVD drives.                                                                                                                                                |
| [IWMPCdromRip](/windows/win32/wmp/nn-wmp-iwmpcdromrip?branch=master)                             | Provides methods to manage copying tracks from an audio CD.                                                                                                                               |
| [IWMPClosedCaption](/windows/win32/wmp/nn-wmp-iwmpclosedcaption?branch=master)                   | Includes captions with a media clip.                                                                                                                                                      |
| [IWMPClosedCaption2](/windows/win32/wmp/nn-wmp-iwmpclosedcaption2?branch=master)                 | Provides additional closed-captioning methods.                                                                                                                                            |
| [IWMPControls](/windows/win32/wmp/nn-wmp-iwmpcontrols?branch=master)                             | Represents the transport controls of Windows Media Player, such as Play, Stop, and Pause.                                                                                                 |
| [IWMPControls2](/windows/win32/wmp/nn-wmp-iwmpcontrols2?branch=master)                           | Provides additional control methods.                                                                                                                                                      |
| [IWMPControls3](/windows/win32/wmp/nn-wmp-iwmpcontrols3?branch=master)                           | Provides additional control methods.                                                                                                                                                      |
| [IWMPCore](/windows/win32/wmp/nn-wmp-iwmpcore?branch=master)                                     | Retrieves pointers to other interfaces and accesses basic features of the control. This is the root interface for the Windows Media Player object model.                                  |
| [IWMPCore2](/windows/win32/wmp/nn-wmp-iwmpcore2?branch=master)                                   | Provides additional core methods.                                                                                                                                                         |
| [IWMPCore3](/windows/win32/wmp/nn-wmp-iwmpcore3?branch=master)                                   | Provides additional core methods.                                                                                                                                                         |
| [IWMPDVD](/windows/win32/wmp/nn-wmp-iwmpdvd?branch=master)                                       | Accesses the content menu of a DVD.                                                                                                                                                       |
| [IWMPError](/windows/win32/wmp/nn-wmp-iwmperror?branch=master)                                   | Accesses a collection of [IWMPErrorItem](/windows/win32/wmp/nn-wmp-iwmperroritem?branch=master) pointers.                                                                                                                     |
| [IWMPErrorItem](/windows/win32/wmp/nn-wmp-iwmperroritem?branch=master)                           | Provides information about errors.                                                                                                                                                        |
| [IWMPErrorItem2](/windows/win32/wmp/nn-wmp-iwmperroritem2?branch=master)                         | Provides additional error item methods.                                                                                                                                                   |
| [IWMPEvents](/windows/win32/wmp/nn-wmp-iwmpevents?branch=master)                       | Exposes events that originate from the Windows Media Player control to which an embedding program can respond.                                                                            |
| [IWMPEvents2](/windows/win32/wmp/nn-wmp-iwmpevents2?branch=master)                     | Exposes events that originate from the Windows Media Player 10 control to which an embedding program can respond. These events are specifically used for device synchronization programs. |
| [IWMPEvents3](/windows/win32/wmp/nn-wmp-iwmpevents3?branch=master)                               | Provides events related to CD ripping, CD burning, folder monitoring, and remote library services.                                                                                        |
| [IWMPFolderMonitorServices](/windows/win32/wmp/nn-wmp-iwmpfoldermonitorservices?branch=master)   | Provides methods to enumerate, scan, and modify file folders that Windows Media Player monitors for digital media content.                                                                |
| [IWMPGraphCreation](/windows/win32/wmpservices/nn-wmpservices-iwmpgraphcreation?branch=master)                   | Manages the DirectShow graph.                                                                                                                                                             |
| [IWMPLibrary](/windows/win32/wmp/nn-wmp-iwmplibrary?branch=master)                               | Represents a library.                                                                                                                                                                     |
| [IWMPLibraryServices](/windows/win32/wmp/nn-wmp-iwmplibraryservices?branch=master)               | Provides methods to enumerate libraries.                                                                                                                                                  |
| [IWMPLibrarySharingServices](/windows/win32/wmp/nn-wmp-iwmplibrarysharingservices?branch=master) | Provides methods to manage library sharing.                                                                                                                                               |
| [IWMPMedia](/windows/win32/wmp/nn-wmp-iwmpmedia?branch=master)                                   | Sets and retrieves the properties of a media item.                                                                                                                                        |
| [IWMPMedia2](/windows/win32/wmp/nn-wmp-iwmpmedia2?branch=master)                                 | Provides additional methods to set and retrieve the properties of a media item.                                                                                                           |
| [IWMPMedia3](/windows/win32/wmp/nn-wmp-iwmpmedia3?branch=master)                                 | Provides additional methods to set and retrieve the properties of a media item.                                                                                                           |
| [IWMPMediaCollection](/windows/win32/wmp/nn-wmp-iwmpmediacollection?branch=master)               | Accesses a collection of [IWMPMedia](/windows/win32/wmp/nn-wmp-iwmpmedia?branch=master) pointers.                                                                                                                             |
| [IWMPMediaCollection2](/windows/win32/wmp/nn-wmp-iwmpmediacollection2?branch=master)             | Provides methods that supplement the **IWMPMediaCollection** interface.                                                                                                                   |
| [IWMPMetadataPicture](/windows/win32/wmp/nn-wmp-iwmpmetadatapicture?branch=master)               | Retrieves information about the **WM/Picture** metadata attribute.                                                                                                                        |
| [IWMPMetadataText](/windows/win32/wmp/nn-wmp-iwmpmetadatatext?branch=master)                     | Retrieves information about complex textual metadata attributes.                                                                                                                          |
| [IWMPNetwork](/windows/win32/wmp/nn-wmp-iwmpnetwork?branch=master)                               | Sets and retrieves the properties of the network connection used by Windows Media Player.                                                                                                 |
| [IWMPPlayer](/windows/win32/wmp/nn-wmp-iwmpplayer?branch=master)                                 | Controls the behavior of the Windows Media Player control user interface.                                                                                                                 |
| [IWMPPlayer2](/windows/win32/wmp/nn-wmp-iwmpplayer2?branch=master)                               | Provides additional methods for controlling Windows Media Player.                                                                                                                         |
| [IWMPPlayer3](/windows/win32/wmp/nn-wmp-iwmpplayer3?branch=master)                               | Provides additional methods for controlling Windows Media Player.                                                                                                                         |
| [IWMPPlayer4](/windows/win32/wmp/nn-wmp-iwmpplayer4?branch=master)                               | Provides additional methods for controlling Windows Media Player.                                                                                                                         |
| [IWMPPlayerApplication](/windows/win32/wmp/nn-wmp-iwmpplayerapplication?branch=master)           | Switches between a remoted Windows Media Player control and the full mode of the Player. Designed for use by C++ programs that embed the control in remote mode.                          |
| [IWMPPlayerServices](/windows/win32/wmp/nn-wmp-iwmpplayerservices?branch=master)                 | Used by the host of a remoted control to manipulate the full mode of Windows Media Player. Designed for use with C++.                                                                     |
| [IWMPPlayerServices2](/windows/win32/wmp/nn-wmp-iwmpplayerservices2?branch=master)               | Sets the background processing priority.                                                                                                                                                  |
| [IWMPPlaylist](/windows/win32/wmp/nn-wmp-iwmpplaylist?branch=master)                             | Creates and manages playlists.                                                                                                                                                            |
| [IWMPPlaylistArray](/windows/win32/wmp/nn-wmp-iwmpplaylistarray?branch=master)                   | Accesses a collection of [IWMPPlaylist](/windows/win32/wmp/nn-wmp-iwmpplaylist?branch=master) pointers by index number.                                                                                                       |
| [IWMPPlaylistCollection](/windows/win32/wmp/nn-wmp-iwmpplaylistcollection?branch=master)         | Manipulates [IWMPPlaylist](/windows/win32/wmp/nn-wmp-iwmpplaylist?branch=master) and [IWMPPlaylistArray](/windows/win32/wmp/nn-wmp-iwmpplaylistarray?branch=master) pointers.                                                                                     |
| [IWMPQuery](/windows/win32/wmp/nn-wmp-iwmpquery?branch=master)                                   | Represents a compound query.                                                                                                                                                              |
| [IWMPRemoteMediaServices](/windows/win32/wmp/nn-wmp-iwmpremotemediaservices?branch=master)       | Provides services to Windows Media Player from a program that hosts the Player control. Designed for use with C++.                                                                        |
| [IWMPRenderConfig](/windows/win32/wmprealestate/nn-wmprealestate-iwmprenderconfig?branch=master)                     | Provides methods to specify or retrieve a value indicating whether playback happens only in the current process.                                                                          |
| [IWMPSettings](/windows/win32/wmp/nn-wmp-iwmpsettings?branch=master)                             | Sets or retrieves Windows Media Player settings.                                                                                                                                          |
| [IWMPSettings2](/windows/win32/wmp/nn-wmp-iwmpsettings2?branch=master)                           | Sets or retrieves Windows Media Player settings.                                                                                                                                          |
| [IWMPSkinManager](/windows/win32/wmp/nn-wmp-iwmpskinmanager?branch=master)                       | Specifies the skin used with Windows Media Player.                                                                                                                                        |
| [IWMPStringCollection](/windows/win32/wmp/nn-wmp-iwmpstringcollection?branch=master)             | Accesses a collection of strings.                                                                                                                                                         |
| [IWMPStringCollection2](/windows/win32/wmp/nn-wmp-iwmpstringcollection2?branch=master)           | Provides methods that supplement the **IWMPStringCollection** interface.                                                                                                                  |
| [IWMPSyncDevice](/windows/win32/wmp/nn-wmp-iwmpsyncdevice?branch=master)                         | Represents a device that can synchronize digital media files with Windows Media Player 10.                                                                                                |
| [IWMPSyncDevice2](/windows/win32/wmp/nn-wmp-iwmpsyncdevice2?branch=master)                       | Provides a method that supplements the **IWMPSyncDevice** interface.                                                                                                                      |
| [IWMPSyncServices](/windows/win32/wmp/nn-wmp-iwmpsyncservices?branch=master)                     | Enumerates available devices that can synchronize digital media files with Windows Media Player 10.                                                                                       |
| [IWMPTranscodePolicy](/windows/win32/wmpservices/nn-wmpservices-iwmptranscodepolicy?branch=master)               | Provides a method implemented by DirectShow source filters to manage changing the format of digital media files.                                                                          |
| [IWMPVideoRenderConfig](/windows/win32/wmprealestate/nn-wmprealestate-iwmpvideorenderconfig?branch=master)           | Provides a method that configures the enhanced video renderer used by Windows Media Player.                                                                                               |



 

## Related topics

<dl> <dt>

[**Object Model Reference for C++**](object-model-reference-for-c.md)
</dt> </dl>

 

 




