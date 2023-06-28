---
title: Trackbars Section
description: Trackbars Section
ms.assetid: 'cc6d1286-413b-4c4b-bcbd-6dd12811d24e'
keywords:
- Windows Media Player Mobile skins,trackbars
- skins,trackbars
- creating skins,Trackbars section
- writing code for skins,Trackbars section
- trackbars in skins,Trackbars section
- skin definition files,Trackbars section
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Trackbars Section

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Trackbars section contains information about any trackbars you want to include:


```C++
[ Trackbars ]

//  <Function>  <Location>     <Dis Image Src>  <Thumb Image Src>  <Thumb Size>
//  ----------  ----------     ---------------  -----------------  ------------
    Volume      40,200,170,40  Disabled @ 15,10    VolumeThumb.bmp    23,22

```



Only the Volume trackbar is defined here. For more about the Trackbar section of the skin definition file, see [Trackbars](trackbars.md) in the Skin Reference.

## Related topics

<dl> <dt>

[**Writing the Code**](writing-the-code.md)
</dt> </dl>

 

 




