---
title: Ratings
description: Ratings
ms.assetid: babc9db5-2782-4261-a571-acb7be4ea770
keywords:
- Windows Media Player Mobile skins,ratings
- skins,ratings
- reference for skins,ratings
- ratings in skins
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Ratings

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

When you create a skin for Windows Media Player 10.1 Mobile, you can display the rating associated with Windows Media Audio-based content that is currently playing. The rating is displayed as a star with a number on it. The star will be numbered one through five, denoting the current rating for that content. If the content is not rated, the star will be numbered zero.

The Ratings section of the skin definition file begins with this line:


```C++
[ Ratings ]

```



You then must add a line that contains information about the size and location of your ratings icon in your skin.


```C++
147, 3, 22, 21       ratings96S.gif

```



You can use the following template for the Ratings section of your skin definition file:


```C++
// <Location>           <Image>
// ---------------      --------------------
```



You can also assign a ratings value to a media item through the user interface in Windows Media Player 10.1 Mobile, and the next time the device synchronizes with the a computer, the new ratings value will be propagated to that media item if it resides in the Windows Media Player 10 library.

## Related topics

<dl> <dt>

[**Skin Reference**](skin-reference.md)
</dt> </dl>

 

 




