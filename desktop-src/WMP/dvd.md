---
title: DVD
description: DVD
ms.assetid: b3634a28-b1d6-44a5-97e4-fcc1f655d652
keywords:
- Windows Media Player,migrating DVDs
- Windows Media Player object model,DVDs
- object model,DVDs
- Windows Media Player ActiveX control,DVDs
- ActiveX control,DVDs
- Windows Media Player Mobile ActiveX control,DVDs
- Windows Media Player Mobile,migrating DVDs
- migration guide,DVDs
- DVD migration
ms.topic: article
ms.date: 05/31/2018
---

# DVD

The Windows Media Player 6.4 ActiveX control contains a **DVD** object that exposes a variety of methods and properties, and one event, for dealing specifically with DVD content. For instance, to determine the number of DVD titles available, you use the **Player6**.**titlesAvailable** property:


```C++
var numTitles = WMP64.DVD.TitlesAvailable;

```



The Windows Media Player 7 or later object model implements a more integrated approach to DVD. DVD-specific properties, methods, and events are implemented only where needed. Otherwise, existing object model functionality works with DVD media as you might expect. For example, to determine the number of DVD titles available when using Windows Media Player 7 or later, you retrieve a **Playlist** object from the **Cdrom** object:


```C++
var dvdTitles = WMP9.cdromCollection.item(0).playlist;

```



The preceding example retrieves a **Playlist** object with a first entry representing the DVD media in the first drive. Additional entries represent individual DVD titles. Therefore, the number of titles available can be calculated as follows:


```C++
var numTitles = dvdTitles.count - 1;

```



Here are the main differences to keep in mind when migrating from version 6.4:

-   DVD playback is supported only when using Windows Media Player for Windows XP or later and the Windows XP operating system or later.
-   DVD-ROM drives are enumerated exactly like CD-ROM drives using the **CdromCollection** object.
-   Individual DVD-ROM drives are managed using the **Cdrom** object.
-   The **DVD** object extends the object model with methods and one property specifically for working with DVD.
-   There are two new events, **OpenPlaylistSwitch** and **DomainChange**, specifically for working with DVD.
-   DVD content is organized using **Playlist** objects and **Media** objects.
-   DVD languages are managed using the language functionality available from the **Controls** object (Windows Media Player 9 Series or later).
-   Transport controls and position information for DVD work the same as for other digital media types.

## Related topics

<dl> <dt>

[**Object Model Migration Guide**](object-model-migration-guide.md)
</dt> <dt>

[**Using the Windows Media Player Control with Visual Basic**](using-the-windows-media-player-control-with-visual-basic.md)
</dt> </dl>

 

 




