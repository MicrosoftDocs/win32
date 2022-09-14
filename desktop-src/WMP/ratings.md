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
ms.date: 05/31/2018
---

# Ratings

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

 

 




