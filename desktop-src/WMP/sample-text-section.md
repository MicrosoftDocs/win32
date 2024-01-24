---
title: Sample Text Section
description: Sample Text Section
ms.assetid: 7e59ec56-dedc-46c5-8302-11a7d7c38911
keywords:
- Windows Media Player Mobile skins,text
- skins,text
- reference for skins,text
- text in skins,Text section
- skin definition files,Text section
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Sample Text Section

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following lines show a typical Text section of a skin definition file:


```C++
//  <Type>       <Location>     <Align>  <Font>          <Color>

//  ------       ----------     -------  ------          -------

    Time         180,46,50,30   Right    Tahoma,16,N     255,255,255

    Playlist     3,46,175,20    Left     Tahoma,10,N     255,255,255

    Track#       10,68,40,20    Left     Tahoma,14,N     255,255,255

```



The preceding example defines three text display boxes that show the current time within the media item, the current playlist, and the current track number.

## Related topics

<dl> <dt>

[**Text**](text.md)
</dt> </dl>

 

 




