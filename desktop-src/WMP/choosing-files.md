---
title: Choosing Files
description: Choosing Files
ms.assetid: dfa44a32-7d72-47f7-a872-33b823a34798
keywords:
- creating skins,choosing files
- Windows Media Player skins,choosing files
- skins,choosing files
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Choosing Files

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

If you want to choose a file, you can use code similar to the Playlist example, but substitute the following for the PLAYELEMENT section:


```C++
<PLAYELEMENT
  mappingColor = "#00FF00"
  onClick = "JScript:player.URL=theme.openDialog('FILE_OPEN','FILES_ALL');"
  />

```



This line will use the **openDialog** method of **THEME** to define a **URL** for the player. You can use this to choose files that are not in playlists.

You can see a similar working **openDialog** example in the sample section of the SDK.

## Related topics

<dl> <dt>

[**Skin Creation Guide**](skin-creation-guide.md)
</dt> </dl>

 

 




