---
title: Media Item Attributes
description: Media Item Attributes
ms.assetid: d43addec-e06c-4ef3-9012-3ecf589b105c
keywords:
- Windows Media Player,library
- Windows Media Player object model,library
- object model,library
- Windows Media Player Mobile,library for object model
- Windows Media Player ActiveX control,library for object model
- Windows Media Player Mobile ActiveX control,library for object model
- ActiveX control,library for object model
- Windows Media Player,attributes for media items
- Windows Media Player object model,attributes for media items
- object model,attributes for media items
- Windows Media Player Mobile,attributes for media items
- Windows Media Player ActiveX control,attributes for media items
- Windows Media Player Mobile ActiveX control,attributes for media items
- ActiveX control,attributes for media items
- Windows Media Player library,attributes for media items
- library,attributes for media items
- attributes,about
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Media Item Attributes

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

When you look at the library in Windows Media Player, you typically see a great deal of information about a media item. In addition to the name of an audio track, for example, you will likely see the name of the album the track is on, the names of the artist and composer, the genre of the music, and so on.

In the Windows Media Player object model, these metadata items are called attributes. The object model includes properties and methods you can use to query media items and playlists for attributes. You can then display attribute values in your user interface, or your code can take actions based on the value of an attribute.

The following topics describe working with media item attributes.



| Topic                                                                                      | Description                                                                                     |
|--------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| [Understanding Attribute Sources](understanding-attribute-sources.md)                     | Describes how the source of a media item affects the attributes that may be associated with it. |
| [Reading Attribute Values](reading-attribute-values.md)                                   | Shows the methods for retrieving the value of an attribute.                                     |
| [Attributes with Multiple Values](attributes-with-multiple-values.md)                     | Shows the methods for retrieving the value of a multi-valued attribute.                         |
| [Reading Attribute Values from a CD or DVD](reading-attribute-values-from-a-cd-or-dvd.md) | Provides a sample application that reads all of the attributes of a media item.                 |
| [Changing Attribute Values](changing-attribute-values.md)                                 | Shows the method for changing the value of an attribute.                                        |
| [Attribute Values for TV Content](attribute-values-for-tv-content.md)                     | Shows how to specify attributes for digital video content that contains TV shows.               |



 

## Related topics

<dl> <dt>

[**Playlist Attributes**](playlist-attributes.md)
</dt> <dt>

[**Working with the Library**](working-with-the-library.md)
</dt> </dl>

 

 




