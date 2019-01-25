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
ms.date: 05/31/2018
---

# About SAMI URLs

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

 

 




