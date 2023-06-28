---
title: About SAMI URLs
description: About SAMI URLs
ms.assetid: 6898a0d5-cfd0-4ba5-8cd1-907cf110667c
keywords:
- Windows Media Player,Synchronized Accessible Media Interchange (SAMI)
- Windows Media Player object model,Synchronized Accessible Media Interchange (SAMI)
- object model,Synchronized Accessible Media Interchange (SAMI)
- Windows Media Player Mobile,Synchronized Accessible Media Interchange (SAMI)
- Windows Media Player ActiveX control,Synchronized Accessible Media Interchange (SAMI)
- Windows Media Player Mobile ActiveX control,Synchronized Accessible Media Interchange (SAMI)
- ActiveX control,Synchronized Accessible Media Interchange (SAMI)
- Synchronized Accessible Media Interchange (SAMI),files
- SAMI (Synchronized Accessible Media Interchange),files
- Synchronized Accessible Media Interchange (SAMI),URLs
- SAMI (Synchronized Accessible Media Interchange),URLs
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# About SAMI URLs

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

SAMI files can be associated with digital media files by using a single URL. This is accomplished by using *the sami* URL parameter. The URL parameter is preceded by the base URL and a ? character. A URL with a *sami* parameter follows this syntax:

*URL*?*sami*=*captionsURL*.

The value of the URL parameter follows the parameter name and an equals sign, as in the following example:


```C++
https://proseware.com/samitest.wma?sami=https://acc.proseware.com/test.smi

```



This URL syntax is commonly used in a hyperlink or a Windows Media metafile to link directly to the locations of both the digital media file and the SAMI file. When the user clicks on the hyperlink, Windows Media Player launches in full mode and plays the digital media content.

If the *sami* URL parameter is not specified, Windows Media Player will look for a SAMI file that is in the same location as the digital media file and that has the same file name except for the file name extension, which must be .smi. If such a file is present, it will be opened automatically if caption display has been enabled in the Player.

Closed captions are enabled in Windows Media Player by clicking the **Play** menu, then clicking **Captions and Subtitles**, and then clicking **On**. If closed captions are enabled, the captions contained in the SAMI file will display while the media item plays.

## Related topics

<dl> <dt>

[**Adding Closed Captions to Digital Media**](adding-closed-captions-to-digital-media.md)
</dt> </dl>

 

 




