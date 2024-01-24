---
title: Compatibility Issues
description: Compatibility Issues
ms.assetid: 2a912f95-4edd-48b8-80c9-c226b06077f8
keywords:
- Windows Media metafile playlists,compatibility issues
- playlists,compatibility issues
- metafile playlists,compatibility issues
- Windows Media metafile playlists,Netscape
- playlists,Netscape
- metafile playlists,Netscape
- compatibility,HTMLView
- compatibility,Netscape
- Windows Media Player,Netscape
- Windows Media Player,compatibility issues
- HTMLView,Netscape
- HTMLView,compatibility issues
- Netscape compatibility issues
ms.topic: article
ms.date: 4/26/2023
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
ms.custom: UpdateFrequency5
---

# Compatibility Issues

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

## Netscape support

Web pages opened by the HTMLView feature are displayed using an embedded instance of Microsoft Internet Explorer. No Netscape compatibility is required for HTMLView content.

## No HTMLView support in earlier versions of Windows Media Player

Currently, only Windows Media Player 9 Series or later supports the HTMLView feature. Earlier versions of the Player and versions created for other platforms ignore the HTMLView parameter when parsing an .asx file. When this happens, the digital media content plays as expected, but the Web-based content is not displayed in the **Now Playing** feature.

## Related topics

<dl> <dt>

[**Building the Plug-in for a Type 2 Online Store**](building-the-plug-in-for-a-type-2-online-store.md)
</dt> </dl>

 

 




