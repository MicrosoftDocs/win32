---
title: Attribute Values for TV Content
description: Attribute Values for TV Content
ms.assetid: 70afb0fc-9eb0-4b94-a32a-f9202db94270
keywords:
- Windows Media Player,attributes for media items
- Windows Media Player object model,attributes for media items
- object model,attributes for media items
- Windows Media Player Mobile,attributes for media items
- Windows Media Player ActiveX control,attributes for media items
- Windows Media Player Mobile ActiveX control,attributes for media items
- ActiveX control,attributes for media items
- Windows Media Player library,attributes for media items
- library,attributes for media items
- attributes,TV content
- TV content attribute values
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Attribute Values for TV Content

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Throughout this topic, the **Player** object was defined in the following manner:


```C++
AxWMPLib.AxWindowsMediaPlayer Player;
using WMPLib;

```



Windows Media Player 10 or later can organize TV content in the library. Windows Media Player treats TV content as a subcategory of video content. To make video content appear in the TV nodes in the library, set the **WM/MediaClassPrimaryID** and the **WM/MediaClassSecondaryID** attributes to the values in the following table by using the *media*.**setItemInfo** method:



| Attribute                    | Value                                |
|------------------------------|--------------------------------------|
| **WM/MediaClassPrimaryID**   | DB9830BD-3AB3-4FAB-8A37-1A995F7FF74B |
| **WM/MediaClassSecondaryID** | BA7F258A-62F7-47A9-B21F-4651C42A000E |



 

You can also use these values to determine whether a particular digital media item contains TV content by using the *media*.**getItemInfo** or *media*.**getItemInfoByType** methods.

Remember to use the **GUID** values as **string** values when specifying or retrieving these values.

The following C# example code sets the media class attributes so that a media item will be identified as TV content.


```C++
// Initialize the media object.
// This code assumes only 1 item named MyFile.
IWMPMedia3 media = (IWMPMedia3)Player.mediaCollection.getByName("MyFile").item(0);

// Set the primary media-class identifier.
media.setItemInfo("WM/MediaClassPrimaryID", "DB9830BD-3AB3-4FAB-8A37-1A995F7FF74B");

// Set the secondary media-class identifier.
media.setItemInfo("WM/MediaClassSecondaryID", "BA7F258A-62F7-47A9-B21F-4651C42A000E");

```



For more info about the possible values for the media class attributes, see the [Windows Media Metadata Usage Guidelines](/previous-versions/ms867702(v=msdn.10)).

## Related topics

<dl> <dt>

[**Media Item Attributes**](media-item-attributes.md)
</dt> <dt>

[**Library Access**](library-access.md)
</dt> <dt>

[**Media Object**](media-object.md)
</dt> </dl>

 

 




