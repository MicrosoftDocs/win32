---
title: Interfaces
description: Interfaces
ms.assetid: '748a8db7-159d-4043-beac-e0516327bcef'
keywords: ["Windows Media Player,interfaces", "Windows Media Player Mobile,interfaces", "Windows Media Player object model,interfaces", "object model,interfaces", "ActiveX control,interfaces", "Windows Media Player ActiveX control,interfaces", "Windows Media Player Mobile ActiveX control,interfaces", "reference for object model,interfaces", "interface object model reference"]
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
| [IWMPCdrom](iwmpcdrom.md)                                   | Accesses a CD or DVD in a drive.                                                                                                                                                          |
| [IWMPCdromBurn](iwmpcdromburn.md)                           | Provides methods to manage creating audio CDs.                                                                                                                                            |
| [IWMPCdromCollection](iwmpcdromcollection.md)               | Accesses a collection of CD or DVD drives.                                                                                                                                                |
| [IWMPCdromRip](iwmpcdromrip.md)                             | Provides methods to manage copying tracks from an audio CD.                                                                                                                               |
| [IWMPClosedCaption](iwmpclosedcaption.md)                   | Includes captions with a media clip.                                                                                                                                                      |
| [IWMPClosedCaption2](iwmpclosedcaption2.md)                 | Provides additional closed-captioning methods.                                                                                                                                            |
| [IWMPControls](iwmpcontrols.md)                             | Represents the transport controls of Windows Media Player, such as Play, Stop, and Pause.                                                                                                 |
| [IWMPControls2](iwmpcontrols2.md)                           | Provides additional control methods.                                                                                                                                                      |
| [IWMPControls3](iwmpcontrols3.md)                           | Provides additional control methods.                                                                                                                                                      |
| [IWMPCore](iwmpcore.md)                                     | Retrieves pointers to other interfaces and accesses basic features of the control. This is the root interface for the Windows Media Player object model.                                  |
| [IWMPCore2](iwmpcore2.md)                                   | Provides additional core methods.                                                                                                                                                         |
| [IWMPCore3](iwmpcore3.md)                                   | Provides additional core methods.                                                                                                                                                         |
| [IWMPDVD](iwmpdvd.md)                                       | Accesses the content menu of a DVD.                                                                                                                                                       |
| [IWMPError](iwmperror.md)                                   | Accesses a collection of [IWMPErrorItem](iwmperroritem.md) pointers.                                                                                                                     |
| [IWMPErrorItem](iwmperroritem.md)                           | Provides information about errors.                                                                                                                                                        |
| [IWMPErrorItem2](iwmperroritem2.md)                         | Provides additional error item methods.                                                                                                                                                   |
| [IWMPEvents](iwmpevents-interface.md)                       | Exposes events that originate from the Windows Media Player control to which an embedding program can respond.                                                                            |
| [IWMPEvents2](iwmpevents2-interface.md)                     | Exposes events that originate from the Windows Media Player 10 control to which an embedding program can respond. These events are specifically used for device synchronization programs. |
| [IWMPEvents3](iwmpevents3.md)                               | Provides events related to CD ripping, CD burning, folder monitoring, and remote library services.                                                                                        |
| [IWMPFolderMonitorServices](iwmpfoldermonitorservices.md)   | Provides methods to enumerate, scan, and modify file folders that Windows Media Player monitors for digital media content.                                                                |
| [IWMPGraphCreation](iwmpgraphcreation.md)                   | Manages the DirectShow graph.                                                                                                                                                             |
| [IWMPLibrary](iwmplibrary.md)                               | Represents a library.                                                                                                                                                                     |
| [IWMPLibraryServices](iwmplibraryservices.md)               | Provides methods to enumerate libraries.                                                                                                                                                  |
| [IWMPLibrarySharingServices](iwmplibrarysharingservices.md) | Provides methods to manage library sharing.                                                                                                                                               |
| [IWMPMedia](iwmpmedia.md)                                   | Sets and retrieves the properties of a media item.                                                                                                                                        |
| [IWMPMedia2](iwmpmedia2.md)                                 | Provides additional methods to set and retrieve the properties of a media item.                                                                                                           |
| [IWMPMedia3](iwmpmedia3.md)                                 | Provides additional methods to set and retrieve the properties of a media item.                                                                                                           |
| [IWMPMediaCollection](iwmpmediacollection.md)               | Accesses a collection of [IWMPMedia](iwmpmedia.md) pointers.                                                                                                                             |
| [IWMPMediaCollection2](iwmpmediacollection2.md)             | Provides methods that supplement the **IWMPMediaCollection** interface.                                                                                                                   |
| [IWMPMetadataPicture](iwmpmetadatapicture.md)               | Retrieves information about the **WM/Picture** metadata attribute.                                                                                                                        |
| [IWMPMetadataText](iwmpmetadatatext.md)                     | Retrieves information about complex textual metadata attributes.                                                                                                                          |
| [IWMPNetwork](iwmpnetwork.md)                               | Sets and retrieves the properties of the network connection used by Windows Media Player.                                                                                                 |
| [IWMPPlayer](iwmpplayer.md)                                 | Controls the behavior of the Windows Media Player control user interface.                                                                                                                 |
| [IWMPPlayer2](iwmpplayer2.md)                               | Provides additional methods for controlling Windows Media Player.                                                                                                                         |
| [IWMPPlayer3](iwmpplayer3.md)                               | Provides additional methods for controlling Windows Media Player.                                                                                                                         |
| [IWMPPlayer4](iwmpplayer4.md)                               | Provides additional methods for controlling Windows Media Player.                                                                                                                         |
| [IWMPPlayerApplication](iwmpplayerapplication.md)           | Switches between a remoted Windows Media Player control and the full mode of the Player. Designed for use by C++ programs that embed the control in remote mode.                          |
| [IWMPPlayerServices](iwmpplayerservices.md)                 | Used by the host of a remoted control to manipulate the full mode of Windows Media Player. Designed for use with C++.                                                                     |
| [IWMPPlayerServices2](iwmpplayerservices2.md)               | Sets the background processing priority.                                                                                                                                                  |
| [IWMPPlaylist](iwmpplaylist.md)                             | Creates and manages playlists.                                                                                                                                                            |
| [IWMPPlaylistArray](iwmpplaylistarray.md)                   | Accesses a collection of [IWMPPlaylist](iwmpplaylist.md) pointers by index number.                                                                                                       |
| [IWMPPlaylistCollection](iwmpplaylistcollection.md)         | Manipulates [IWMPPlaylist](iwmpplaylist.md) and [IWMPPlaylistArray](iwmpplaylistarray.md) pointers.                                                                                     |
| [IWMPQuery](iwmpquery.md)                                   | Represents a compound query.                                                                                                                                                              |
| [IWMPRemoteMediaServices](iwmpremotemediaservices.md)       | Provides services to Windows Media Player from a program that hosts the Player control. Designed for use with C++.                                                                        |
| [IWMPRenderConfig](iwmprenderconfig.md)                     | Provides methods to specify or retrieve a value indicating whether playback happens only in the current process.                                                                          |
| [IWMPSettings](iwmpsettings.md)                             | Sets or retrieves Windows Media Player settings.                                                                                                                                          |
| [IWMPSettings2](iwmpsettings2.md)                           | Sets or retrieves Windows Media Player settings.                                                                                                                                          |
| [IWMPSkinManager](iwmpskinmanager.md)                       | Specifies the skin used with Windows Media Player.                                                                                                                                        |
| [IWMPStringCollection](iwmpstringcollection.md)             | Accesses a collection of strings.                                                                                                                                                         |
| [IWMPStringCollection2](iwmpstringcollection2.md)           | Provides methods that supplement the **IWMPStringCollection** interface.                                                                                                                  |
| [IWMPSyncDevice](iwmpsyncdevice.md)                         | Represents a device that can synchronize digital media files with Windows Media Player 10.                                                                                                |
| [IWMPSyncDevice2](iwmpsyncdevice2.md)                       | Provides a method that supplements the **IWMPSyncDevice** interface.                                                                                                                      |
| [IWMPSyncServices](iwmpsyncservices.md)                     | Enumerates available devices that can synchronize digital media files with Windows Media Player 10.                                                                                       |
| [IWMPTranscodePolicy](iwmptranscodepolicy.md)               | Provides a method implemented by DirectShow source filters to manage changing the format of digital media files.                                                                          |
| [IWMPVideoRenderConfig](iwmpvideorenderconfig.md)           | Provides a method that configures the enhanced video renderer used by Windows Media Player.                                                                                               |



 

## Related topics

<dl> <dt>

[**Object Model Reference for C++**](object-model-reference-for-c.md)
</dt> </dl>

 

 




