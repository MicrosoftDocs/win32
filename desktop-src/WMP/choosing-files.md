---
title: Choosing Files
description: Choosing Files
ms.assetid: dfa44a32-7d72-47f7-a872-33b823a34798
keywords:
- creating skins,choosing files
- Windows Media Player skins,choosing files
- skins,choosing files
ms.topic: article
ms.date: 05/31/2018
---

# Choosing Files

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

 

 




