---
title: About the Library
description: About the Library
ms.assetid: a43c57ac-deb4-4c86-a8a2-bcfd214b9d0a
keywords:
- Windows Media Player,library
- Windows Media Player object model,library
- object model,library
- Windows Media Player ActiveX control,library for object model
- ActiveX control,library for object model
- Windows Media Player Mobile ActiveX control,library for object model
- Windows Media Player Mobile,library for object model
- Windows Media Player library,about
- library,about
- metadata,Windows Media Player library
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# About the Library

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The library is a database of information, or *metadata*, about the digital media content that is available to Windows Media Player. Some of the information is displayed in the **Library** pane in the Player; more of it is available through code.

(In Windows Media Player 9 Series and earlier, this feature is called **Media Library**.)

The library gives users an easy way to organize and access digital media content. For example, users can view music organized by album, by artist, by genre, or simply as a list of all music. You can use the Windows Media Player SDK object model to access the library to play content, retrieve playlists, add content, remove content, and change the associated metadata. Windows Media Player protects users' privacy by restricting your ability to access the library from code under certain conditions. For more information about access rights, see [Library Access](library-access.md).

The library stores metadata about two basic types of digital media content. The first type, digital media items, are individual content files, such as a music track or a photo. The second type, playlists, are files that represent a group of digital media items, typically intended to be played in a specified order. The metadata associated with digital media content is stored as name-value pairs. For example, the metadata that describes the person who performed a song is named "Artist" and the value associated with it typically is a text string containing the performer's name. Each unique metadata name is called an *attribute*. For a listing of supported attributes, see the [Attribute Reference](attribute-reference.md). For information about using attributes in code, see [Media Item Attributes](media-item-attributes.md).

The following sections provide more information about working with the library:

-   [Accessing the Library Programmatically](accessing-the-library-programmatically.md)
-   [About Library Services](about-library-services.md)

## Related topics

<dl> <dt>

[**About the Player Object Model**](about-the-player-object-model.md)
</dt> </dl>

 

 




