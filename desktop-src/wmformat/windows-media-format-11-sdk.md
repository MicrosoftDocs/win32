---
title: Windows Media Format 11 SDK
description: Windows Media Format 11 SDK
ms.assetid: 875e8914-b861-46f1-9391-8724ff77d26b
keywords:
- Windows Media Format SDK,about
- Windows Media SDK
- Windows Media Format SDK,Advanced Systems Format (ASF)
- Advanced Systems Format (ASF),about
- ASF (Advanced Systems Format),about
- Windows Media Format SDK,features
- Windows Media Format SDK,key features
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Windows Media Format 11 SDK

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This documentation describes the Microsoft Windows Media Format Software Development Kit (SDK) and applies to the 32-bit and x64-based versions of the SDK.

The Windows Media Format SDK is a component of the Microsoft Windows Media Software Development Kit (SDK). Other components include the Windows Media Services SDK, Windows Media Encoder SDK, Windows Media Rights Manager SDK, Windows Media Device Manager SDK, and Windows Media Player SDK.

The Windows Media Format SDK provides application developers with access to the components of the Windows Media Format. These components include the Advanced Systems Format (ASF) file container, the Windows Media Audio and Video codecs, basic network streaming capability, and digital rights management. The objects of the Windows Media Format SDK manipulate the components of Windows Media at a low level; the other components of the Windows Media SDK include objects that work on a higher level.

The primary purpose of the Windows Media Format SDK is to enable developers to create applications that play, write, edit, encrypt, and deliver Advanced Systems Format (ASF) files and network streams. These files and streams commonly contain audio and video content encoded using the Windows Media Audio and Video codecs. However, ASF can contain any type of data. For more information about the Advanced Systems Format container structure, see [Overview of the ASF Format](overview-of-the-asf-format.md).

The key features of the Windows Media Format SDK are:

-   Support for industry-leading codecs. The Windows Media Format 11 SDK includes the Microsoft Windows Media Video 9 codec and the Microsoft Windows Media Audio 9.1 codec. Both of these codecs provide exceptional encoding of digital media content. New for this release is the Windows Media Video 9 Advanced Profile codec, which provides optimizations for broadcast video. This SDK also includes the Microsoft Windows Media Video 9 Screen codec for compressing computer-screen activity during sessions of user applications, and the Windows Media Audio 9.1 Voice codec, which encodes low-complexity audio such as speech and intelligently adapts to more complex audio such as music, for superior representation of combined voice-music scenarios.
-   Support for writing ASF files. Files are created based on customizable profiles, enabling easy configuration and standardization of files. This SDK can be used to write files in excess of 2 gigabytes, enabling longer, better-quality, continuous files.
-   Support for reading ASF files. This SDK provides support for reading local ASF files as well as reading ASF data being streamed over a network. Support is also provided for many advanced reading features, such as native support for multiple bit rate (MBR) files, which contain multiple streams with the same content encoded at different bit rates. The reader automatically selects which MBR stream to use, depending upon available bandwidth at the time of playback.
-   Support for delivering ASF streams over a network. This SDK provides support for delivering ASF data through HTTP to remote computers on a network, and also for delivering data directly to a remote Windows Media server.
-   Support for editing metadata in ASF files. Information about a file and its content is easily manipulated with this SDK. Developers can use the robust system of metadata attributes included in the SDK, or create custom attributes to suit their needs.
-   Support for content editing applications. This SDK enables applications to seek to points within a file by presentation time and by video frame. In addition, files created by using the Windows Media Format SDK can maintain timestamps in formats used in film and television production.
-   Support for reading and editing metadata in MP3 files. This SDK provides integrated support for reading MP3 files with the same methods used to read ASF files. Applications built with the Windows Media Format SDK can also edit metadata attributes in MP3 files using built-in support for the most common ID3 tags used by content creators.
-   Support for Digital Rights Management protection. This SDK provides methods for reading and writing ASF files and network streams that are protected by Digital Rights Management to prevent unauthorized playback or copying of the content.

To download the Windows Media Format SDK, see the [Windows Media Downloads](https://msdn.microsoft.com/windows/desktop/aa904949) page at the Microsoft Web site.

This document describes how you can develop digital media applications using the Windows Media Format SDK. It is divided into the following sections.

> [!Note]  
> Although this document contains information about the latest version of the Windows Media Format SDK, most of the features it describes are supported by older versions of the SDK. Reference pages for the methods, functions, structures, and enumerations of the Windows Media Format SDK include version requirements.

 



| Section                                                                                                          | Description                                                                                                                                                                                              |
|------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [About the Windows Media Format SDK](about-the-windows-media-format-sdk.md)                                     | Provides overview and background information that you should be familiar with before attempting to create applications.                                                                                  |
| [Programming Guide](programming-guide.md)                                                                       | Provides detailed instructions for performing various tasks, such as reading, writing and indexing files, protecting files with Digital Rights Management, streaming ASF data over a network, and so on. |
| [Programming Reference](programming-reference.md)                                                               | Provides reference information for the interfaces, methods, functions, structures, enumeration types, and constants related to Windows Media Format.                                                     |
| [Windows Media Audio and Video Codec Interfaces](windows-media-audio-and-video-codec-interfaces--deprecated.md) | Provides instructions for using the Windows Media Audio and Video codec digital media objects (DMOs) directly.                                                                                           |
| [*Glossary*](wmformat-glossary.md)                                                                              | Defines the terms used in the Windows Media Format SDK documentation.                                                                                                                                    |



 

 

 




