---
title: Sample Marquee Section
description: Sample Marquee Section
ms.assetid: 44ed3257-2e1a-4b8d-9d55-a13b0400422d
keywords:
- Windows Media Player Mobile skins,marquees
- skins,marquees
- reference for skins,marquees
- marquees in skins,Marquee section
- skin definition files,Marquee section
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Sample Marquee Section

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following lines show a typical Marquee section of a skin definition file:


```C++
//  <Location>   <Font>       <Color>      <Text item combinations>

//  ----------   ------       -------      ------------------------

    3,2,234,20   Tahoma,12,N  255,0,0    Title+Author, Title, Author


```



This defines a marquee display box that shows the title and author if both are defined, the title if only Title is defined, or the name of the author if only Author is defined. If neither is defined, nothing will be displayed.

## Related topics

<dl> <dt>

[**Marquee**](marquee.md)
</dt> </dl>

 

 




