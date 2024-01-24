---
title: Text Combinations
description: Text Combinations
ms.assetid: 0220b77e-5f1e-4569-a8fe-5085e0c16338
keywords:
- Windows Media Player Mobile skins,marquees
- skins,marquees
- reference for skins,marquees
- marquees in skins,text combinations
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Text Combinations

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This value is a list of text display box combinations, separated by commas. Text display boxes can be joined together by a plus character to create a new marquee display value and any text type defined in the Text Type section can be used in your marquee.

When determining what to display, Windows Media Player Mobile evaluates each item in the list to see if all parts are available. If not, the next item is evaluated, and so on, until all the available parts have been found. For example, if you want to display Author and Title, but you're not sure whether both are available, use the following value:


```C++
Title+Author, Title, Author

```



In the preceding example, the Title+Author will be displayed if the title and author have been defined for the media item. If both are not defined, the Title is evaluated and displayed if defined. If the Title is not defined, the Author is displayed if defined. If neither is defined, then nothing is displayed.

When using the plus sign for concatenation, be sure you have no spaces on either side of the plus sign.

## Related topics

<dl> <dt>

[**Marquee**](marquee.md)
</dt> <dt>

[**Text Type**](text-type.md)
</dt> </dl>

 

 




