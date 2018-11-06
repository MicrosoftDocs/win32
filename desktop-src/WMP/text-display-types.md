---
title: Text Display Types
description: Text Display Types
ms.assetid: 6aa3fc89-e5f5-420f-82e0-c605676078cb
keywords:
- Windows Media Player Mobile skins,text
- text in skins,display types
- skins,text
ms.topic: article
ms.date: 05/31/2018
---

# Text Display Types

You do not need to include text displays in your skin, but there are many instances where you might want to. For example, you might want to include a Seek trackbar to allow the user to move to any position in the media item, but you also might want to include a text display that shows the number of seconds that have elapsed since the current media item started playing.

**Display Boxes**

The following are several attributes a text element can display:

-   Time
-   Playlist
-   Track\#
-   \#Tracks
-   Title
-   Author
-   Copyright
-   Filename
-   FilenameExt
-   Bitrate
-   Frequency
-   Status
-   VolPercent

For more information about text display types, see the [Text](text.md) section of the Skin Reference.

**Scrolling Marquee**

In addition to using the individual text elements, you can combine one or more attributes into a scrolling text marquee. This is useful if you want to display a grouping of related text information in a small area. For example, you could display Title, Author, and Copyright information in a Marquee.

For more information about creating a text marquee, see the [Marquee](marquee.md) section of the Skin Reference.

**Status Display**

Another type of text display is the status display. This lets you automatically display information about the current state of Windows Media Player Mobile. For example, the status display will inform the user when a media item is buffering so that it is evident that the Player is working.

The following messages appear in the status display:

-   Buffering
-   Connecting
-   Paused
-   Playing
-   Ready
-   Stopped

> [!Note]  
> When a media item is playing, the status display will rotate through subtitle, artist, album, genre, and current bitrate.

 

For information about creating a status display through the Status element, see the [Status](status.md) section of the Skin Reference; however, it is preferred that you use the status attribute in the Text element instead of the Status element.

## Related topics

<dl> <dt>

[**Windows Media Player Mobile Functionality**](windows-media-player-mobile-functionality.md)
</dt> </dl>

 

 




