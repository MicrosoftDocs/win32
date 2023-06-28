---
title: Changing Attribute Values
description: Changing Attribute Values
ms.assetid: c7dd7355-453c-44a5-9932-c41bb3ae2e40
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
- attributes,changing values
- changing attribute values
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Changing Attribute Values

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You can change the value of an attribute if your webpage or application has read/write access to the library and the attribute can be both read and written.

You can change an attribute of the current media item. To change attributes of multiple media items, you can assign each one in turn to the *Player*.**currentMedia** property.

Throughout this topic, the **Player** object was defined in the following manner:


```C++
AxWMPLib.AxWindowsMediaPlayer Player;
using WMPLib;

```



To change an attribute, call the *Player*.*currentMedia*.**setItemInfo** method as shown in the following C# example.


```C++
IWMPMedia3 media;
// Initialize the Media object
media = Player.currentMedia;
// Set the new genre value
media.setItemInfo("WM/Genre", "My New Genre");

```



We recommend that you call the *Media*.**isReadOnlyItem** method to determine whether you can change a particular attribute.

> [!Note]  
> If you embed the control in your application, file attributes that you change will not be written to the digital media file until the user runs Windows Media Player. If you use the control in a remoted application written in C++, file attributes that you change will be written to the digital media file shortly after you make the changes. In either case, the changes are immediately available to you through the library.

 

## Related topics

<dl> <dt>

[**Media Item Attributes**](media-item-attributes.md)
</dt> <dt>

[**Library Access**](library-access.md)
</dt> <dt>

[**Media Object**](media-object.md)
</dt> <dt>

[**Reading Attribute Values**](reading-attribute-values.md)
</dt> </dl>

 

 




