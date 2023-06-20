---
title: About SAMI Files
description: About SAMI Files
ms.assetid: 39b1e8a8-bbeb-4376-89d9-03a147f4c4fd
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
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# About SAMI Files

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

SAMI files are text files that have an .smi or .sami file name extension. They contain the text strings used for synchronized closed captions, subtitles, and audio descriptions. They also specify the timing parameters used by the Windows Media Player control to synchronize closed caption text with audio or video content. When a digital media file reaches a time designated in the SAMI file, the text changes accordingly in the closed caption display area of the webpage.

Other than a simple text editor (such as Microsoft Notepad), special software is not required to create a SAMI file. SAMI and HTML share common elements, such as the <HEAD> and &lt;BODY&gt; tags. As in HTML, tags used in SAMI files must always be used in pairs. For example, a BODY element begins with a &lt;BODY&gt; tag and must always end with a &lt;/BODY&gt; tag.

A basic SAMI file requires three fundamental tags: &lt;SAMI&gt;, <HEAD>, and &lt;BODY&gt;.

The &lt;SAMI&gt; tag identifies the document as a SAMI document so other applications can recognize its file format.

Between the <HEAD> and </HEAD> tags, you define basic guidelines and other format information for the SAMI document, such as the document title, general information, and style properties for closed captions. Like HTML, content declared within the HEAD element does not display as output.

Elements and attributes defined between the &lt;BODY&gt; and &lt;/BODY&gt; tags display content seen by the user. In SAMI, the BODY element contains the parameters for synchronization and the text strings used for closed captions.

Defined within the HEAD element, the STYLE element provides for added functionality in SAMI. Between the &lt;STYLE&gt; and </STYLE> tags, you can define several Cascading Style Sheet (CSS) selectors for style and layout. Style properties such as fonts, sizes, and alignments can be customized to provide a rich user experience while also promoting accessibility. For example, defining a large text font style class can improve the readability for users who have difficulty reading small text. In addition, by defining several different language classes, you can help international users better understand the digital media content.

## Related topics

<dl> <dt>

[**Adding Closed Captions to Digital Media**](adding-closed-captions-to-digital-media.md)
</dt> </dl>

 

 




