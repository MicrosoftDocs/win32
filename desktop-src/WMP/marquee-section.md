---
title: Marquee Section
description: Marquee Section
ms.assetid: ff48c922-e6fc-4ba2-89ad-dcb34be0fea5
keywords:
- Windows Media Player Mobile skins,marquees
- skins,marquees
- creating skins,Marquee section
- writing code for skins,Marquee section
- marquees in skins,Marquee section
- skin definition files,Marquee section
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Marquee Section

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Marquee section contains information about the marquee text box, which will display scrolling text:


```C++
[ Marquee ]

//  <Location>   <Font>       <Color>      <Text item combinations>
//  ----------   ------       -------      ------------------------
    100,150,100,20   Tahoma,12,N  255,0,0    Title+Author, Author, Title

```



This will display the title and author of the current media item although you can display any text type in the marquee. For example, you could also include Filename, Status, and Playlist in your marquee.

> [!Note]  
> To maintain compatibility with versions of Windows Media Player Mobile older than Windows Media Player 10 Mobile, using "Marquis" in a skin definition file is still considered valid.

 

For more about the Marquee section, see [Marquee](marquee.md) in the Skin Reference.

## Related topics

<dl> <dt>

[**Writing the Code**](writing-the-code.md)
</dt> </dl>

 

 




