---
title: WMP SDK Interfaces
description: WMP SDK Interfaces
ms.assetid: '68a0bdaf-ae1b-4ba1-817b-a31c68b9fddd'
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
ms.topic: article
ms.date: 05/31/2018
---

# WMP SDK Interfaces

This section documents the COM interfaces exposed by the Windows Media Player ActiveX control and the Windows Media Player Mobile ActiveX control.

The accessor methods of the **IWMPCore** or **IWMPPlayer** interface are used to retrieve specific interfaces. These interfaces, in turn, may have accessor methods for retrieving further interfaces. Calling **QueryInterface** on one of these interfaces is only necessary when you retrieve the base version of an interface and want to call a method on a later version of the same interface.

> [!Note]  
> All methods and events are fully supported in Windows Media Player 10 Mobile and later unless explicitly stated otherwise.

The Windows Media Player control exposes the following interfaces.

| Interface                                                    | Description                                                                                                                                                                               |
|--------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [\_WMPOCXEvents](-wmpocxevents-interface.md)                | Provides events originating from the Windows Media Player control to which an embedding program can respond.                                                                              |
| [IWMPCdrom](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpcdrom)                                   | Accesses a CD or DVD in a drive.                                                                                                                                                          |
| [IWMPCdromBurn](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpcdromburn)                           | Provides methods to manage creating audio CDs.                                                                                                                                            |
| [IWMPCdromCollection](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpcdromcollection)               | Accesses a collection of CD or DVD drives.                                                                                                                                                |
| [IWMPCdromRip](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpcdromrip)                             | Provides methods to manage copying tracks from an audio CD.                                                                                                                               |
| [IWMPClosedCaption](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpclosedcaption)                   | Includes captions with a media clip.                                                                                                                                                      |
| [IWMPClosedCaption2](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpclosedcaption2)                 | Provides additional closed-captioning methods.                                                                                                                                            |
| [IWMPControls](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpcontrols)                             | Represents the transport controls of Windows Media Player, such as Play, Stop, and Pause.                                                                                                 |
| [IWMPControls2](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpcontrols2)                           | Provides additional control methods.                                                                                                                                                      |
| [IWMPControls3](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpcontrols3)                           | Provides additional control methods.                                                                                                                                                      |
| [IWMPCore](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpcore)                                     | Retrieves pointers to other interfaces and accesses basic features of the control. This is the root interface for the Windows Media Player object model.                                  |
| [IWMPCore2](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpcore2)                                   | Provides additional core methods.                                                                                                                                                         |
| [IWMPCore3](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpcore3)                                   | Provides additional core methods.                                                                                                                                                         |
| [IWMPDVD](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpdvd)                                       | Accesses the content menu of a DVD.                                                                                                                                                       |
| [IWMPError](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmperror)                                   | Accesses a collection of [IWMPErrorItem](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmperroritem) pointers.                                                                                                                     |
| [IWMPErrorItem](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmperroritem)                           | Provides information about errors.                                                                                                                                                        |
| [IWMPErrorItem2](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmperroritem2)                         | Provides additional error item methods.                                                                                                                                                   |
| [IWMPEvents](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpevents)                       | Exposes events that originate from the Windows Media Player control to which an embedding program can respond.                                                                            |
| [IWMPEvents2](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpevents2)                     | Exposes events that originate from the Windows Media Player 10 control to which an embedding program can respond. These events are specifically used for device synchronization programs. |
| [IWMPEvents3](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpevents3)                               | Provides events related to CD ripping, CD burning, folder monitoring, and remote library services.                                                                                        |
| [IWMPFolderMonitorServices](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpfoldermonitorservices)   | Provides methods to enumerate, scan, and modify file folders that Windows Media Player monitors for digital media content.                                                                |
| [IWMPGraphCreation](/previous-versions/windows/desktop/api/wmpservices/nn-wmpservices-iwmpgraphcreation)                   | Manages the DirectShow graph.                                                                                                                                                             |
| [IWMPLibrary](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmplibrary)                               | Represents a library.                                                                                                                                                                     |
| [IWMPLibraryServices](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmplibraryservices)               | Provides methods to enumerate libraries.                                                                                                                                                  |
| [IWMPLibrarySharingServices](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmplibrarysharingservices) | Provides methods to manage library sharing.                                                                                                                                               |
| [IWMPMedia](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpmedia)                                   | Sets and retrieves the properties of a media item.                                                                                                                                        |
| [IWMPMedia2](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpmedia2)                                 | Provides additional methods to set and retrieve the properties of a media item.                                                                                                           |
| [IWMPMedia3](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpmedia3)                                 | Provides additional methods to set and retrieve the properties of a media item.                                                                                                           |
| [IWMPMediaCollection](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpmediacollection)               | Accesses a collection of [IWMPMedia](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpmedia) pointers.                                                                                                                             |
| [IWMPMediaCollection2](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpmediacollection2)             | Provides methods that supplement the **IWMPMediaCollection** interface.                                                                                                                   |
| [IWMPMetadataPicture](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpmetadatapicture)               | Retrieves information about the **WM/Picture** metadata attribute.                                                                                                                        |
| [IWMPMetadataText](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpmetadatatext)                     | Retrieves information about complex textual metadata attributes.                                                                                                                          |
| [IWMPNetwork](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpnetwork)                               | Sets and retrieves the properties of the network connection used by Windows Media Player.                                                                                                 |
| [IWMPPlayer](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpplayer)                                 | Controls the behavior of the Windows Media Player control user interface.                                                                                                                 |
| [IWMPPlayer2](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpplayer2)                               | Provides additional methods for controlling Windows Media Player.                                                                                                                         |
| [IWMPPlayer3](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpplayer3)                               | Provides additional methods for controlling Windows Media Player.                                                                                                                         |
| [IWMPPlayer4](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpplayer4)                               | Provides additional methods for controlling Windows Media Player.                                                                                                                         |
| [IWMPPlayerApplication](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpplayerapplication)           | Switches between a remoted Windows Media Player control and the full mode of the Player. Designed for use by C++ programs that embed the control in remote mode.                          |
| [IWMPPlayerServices](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpplayerservices)                 | Used by the host of a remoted control to manipulate the full mode of Windows Media Player. Designed for use with C++.                                                                     |
| [IWMPPlayerServices2](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpplayerservices2)               | Sets the background processing priority.                                                                                                                                                  |
| [IWMPPlaylist](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpplaylist)                             | Creates and manages playlists.                                                                                                                                                            |
| [IWMPPlaylistArray](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpplaylistarray)                   | Accesses a collection of [IWMPPlaylist](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpplaylist) pointers by index number.                                                                                                       |
| [IWMPPlaylistCollection](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpplaylistcollection)         | Manipulates [IWMPPlaylist](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpplaylist) and [IWMPPlaylistArray](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpplaylistarray) pointers.                                                                                     |
| [IWMPQuery](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpquery)                                   | Represents a compound query.                                                                                                                                                              |
| [IWMPRemoteMediaServices](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpremotemediaservices)       | Provides services to Windows Media Player from a program that hosts the Player control. Designed for use with C++.                                                                        |
| [IWMPRenderConfig](/previous-versions/windows/desktop/api/wmprealestate/nn-wmprealestate-iwmprenderconfig)                     | Provides methods to specify or retrieve a value indicating whether playback happens only in the current process.                                                                          |
| [IWMPSettings](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpsettings)                             | Sets or retrieves Windows Media Player settings.                                                                                                                                          |
| [IWMPSettings2](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpsettings2)                           | Sets or retrieves Windows Media Player settings.                                                                                                                                          |
| [IWMPSkinManager](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpskinmanager)                       | Specifies the skin used with Windows Media Player.                                                                                                                                        |
| [IWMPStringCollection](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpstringcollection)             | Accesses a collection of strings.                                                                                                                                                         |
| [IWMPStringCollection2](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpstringcollection2)           | Provides methods that supplement the **IWMPStringCollection** interface.                                                                                                                  |
| [IWMPSyncDevice](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpsyncdevice)                         | Represents a device that can synchronize digital media files with Windows Media Player 10.                                                                                                |
| [IWMPSyncDevice2](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpsyncdevice2)                       | Provides a method that supplements the **IWMPSyncDevice** interface.                                                                                                                      |
| [IWMPSyncServices](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpsyncservices)                     | Enumerates available devices that can synchronize digital media files with Windows Media Player 10.                                                                                       |
| [IWMPTranscodePolicy](/previous-versions/windows/desktop/api/wmpservices/nn-wmpservices-iwmptranscodepolicy)               | Provides a method implemented by DirectShow source filters to manage changing the format of digital media files.                                                                          |
| [IWMPVideoRenderConfig](/previous-versions/windows/desktop/api/wmprealestate/nn-wmprealestate-iwmpvideorenderconfig)           | Provides a method that configures the enhanced video renderer used by Windows Media Player.                                                                                               |



 

## Related topics

<dl> <dt>

[**Object Model Reference for C++**](object-model-reference-for-c.md)
</dt> </dl>

 

 




