---
title: Interfaces for Visual Basic .NET and C
description: Interfaces for Visual Basic .NET and C\
ms.assetid: c66f1e03-20eb-45b1-8710-be9eae63e7ad
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
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Interfaces for Visual Basic .NET and C#

This section documents the interfaces exposed by the Windows Media Player ActiveX control.

Several properties and methods of the [AxWindowsMediaPlayer Object](axwindowsmediaplayer-object--vb-and-c.md) are used to retrieve specific interfaces. These interfaces, in turn, may have properties and accessor methods for retrieving further interfaces.

The Windows Media Player control exposes the following interfaces.



| Interface                                                      | Description                                                                                                                                                       |
|----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [IWMPCdrom](iwmpcdrom--vb-and-c.md)                           | Accesses a CD or DVD in a drive.                                                                                                                                  |
| [IWMPCdromBurn](iwmpcdromburn--vb-and-c.md)                   | Provides properties and methods to manage creating audio CDs.                                                                                                     |
| [IWMPCdromCollection](iwmpcdromcollection--vb-and-c.md)       | Accesses a collection of CD or DVD drives.                                                                                                                        |
| [IWMPCdromRip](iwmpcdromrip--vb-and-c.md)                     | Provides properties and methods to manage copying, or *ripping*, tracks from an audio CD.                                                                         |
| [IWMPClosedCaption](iwmpclosedcaption--vb-and-c.md)           | Provides a way to include captions with a digital media file.                                                                                                     |
| [IWMPClosedCaption2](iwmpclosedcaption2--vb-and-c.md)         | Provides additional closed-captioning properties and methods.                                                                                                     |
| [IWMPControls](iwmpcontrols--vb-and-c.md)                     | Represents the transport controls of Windows Media Player, such as Play, Stop, and Pause.                                                                         |
| [IWMPControls2](iwmpcontrols2--vb-and-c.md)                   | Provides an additional control method to freeze playback on the next or previous frame.                                                                           |
| [IWMPControls3](iwmpcontrols3--vb-and-c.md)                   | Provides additional control properties and methods for audio language selection and support.                                                                      |
| [IWMPDVD](iwmpdvd--vb-and-c.md)                               | Provides properties and methods for working with DVDs.                                                                                                            |
| [IWMPError](iwmperror--vb-and-c.md)                           | Accesses a collection of [IWMPErrorItem](iwmperroritem--vb-and-c.md) interfaces for retrieving error information.                                                |
| [IWMPErrorItem](iwmperroritem--vb-and-c.md)                   | Provides access to error information.                                                                                                                             |
| [IWMPErrorItem2](iwmperroritem2--vb-and-c.md)                 | Provides an additional error item property for getting an error condition code.                                                                                   |
| **IWMPFolderMonitorServices**                                  | Not supported for .NET programming.                                                                                                                               |
| [IWMPLibrary](iwmplibrary--vb-and-c.md)                       | Represents a library.                                                                                                                                             |
| [IWMPLibraryServices](iwmplibraryservices--vb-and-c.md)       | Provides methods to enumerate libraries.                                                                                                                          |
| **IWMPLibrarySharingServices**                                 | Not supported for .NET programming.                                                                                                                               |
| [IWMPMedia](iwmpmedia--vb-and-c.md)                           | Provides a way to set and retrieve the properties of a media item.                                                                                                |
| [IWMPMedia2](iwmpmedia2--vb-and-c.md)                         | Provides access to an additional media item property.                                                                                                             |
| [IWMPMedia3](iwmpmedia3--vb-and-c.md)                         | Provides additional methods to access the properties of a media item.                                                                                             |
| [IWMPMediaCollection](iwmpmediacollection--vb-and-c.md)       | Provides methods that can be used to organize a large collection of media items.                                                                                  |
| [IWMPMediaCollection2](iwmpmediacollection2--vb-and-c.md)     | Provides methods that supplement the **IWMPMediaCollection** interface.                                                                                           |
| [IWMPMetadataPicture](iwmpmetadatapicture--vb-and-c.md)       | Provides properties for getting information about the image contained in a digital media file that is represented by a **WM/Picture** metadata attribute.         |
| [IWMPMetadataText](iwmpmetadatatext--vb-and-c.md)             | Provides properties for getting information about complex textual metadata attributes.                                                                            |
| [IWMPNetwork](iwmpnetwork--vb-and-c.md)                       | Provides properties and methods to access statistics relating to the quality of a network connection, and to specify and retrieve the network proxy settings.     |
| **IWMPPlayerApplication**                                      | Not supported for .NET programming.                                                                                                                               |
| **IWMPPlayerServices**                                         | Not supported for .NET programming.                                                                                                                               |
| **IWMPPlayerServices2**                                        | Not supported for .NET programming.                                                                                                                               |
| [IWMPPlaylist](iwmpplaylist--vb-and-c.md)                     | Provides properties and methods to organize, manage, and manipulate media items in a playlist.                                                                    |
| [IWMPPlaylistArray](iwmpplaylistarray--vb-and-c.md)           | Accesses a collection of [IWMPPlaylist](iwmpplaylist--vb-and-c.md) interfaces by index number.                                                                   |
| [IWMPPlaylistCollection](iwmpplaylistcollection--vb-and-c.md) | Provides methods for manipulating [IWMPPlaylist](iwmpplaylist--vb-and-c.md) and [IWMPPlaylistArray](iwmpplaylistarray--vb-and-c.md) interfaces in a collection. |
| [IWMPQuery](iwmpquery--vb-and-c.md)                           | Represents a compound query.                                                                                                                                      |
| [IWMPSettings](iwmpsettings--vb-and-c.md)                     | Provides properties and methods that get or set the values of Windows Media Player settings.                                                                      |
| [IWMPSettings2](iwmpsettings2--vb-and-c.md)                   | Provides properties and a method that supplement the **IWMPSettings** interface.                                                                                  |
| [IWMPStringCollection](iwmpstringcollection--vb-and-c.md)     | Provides a property and a method for accessing a collection of strings by index number.                                                                           |
| [IWMPStringCollection2](iwmpstringcollection2--vb-and-c.md)   | Provides methods that supplement the **IWMPStringCollection** interface.                                                                                          |
| **IWMPSyncDevice**                                             | Not supported for .NET programming.                                                                                                                               |
| **IWMPSyncDevice2**                                            | Not supported for .NET programming.                                                                                                                               |
| **IWMPSyncServices**                                           | Not supported for .NET programming.                                                                                                                               |



 

## Related topics

<dl> <dt>

[**Object Model Reference for Visual Basic .NET and C#**](object-model-reference-for-visual-basic--net-and-c.md)
</dt> </dl>

 

 




