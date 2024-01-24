---
title: DownloadItem.pause method
description: Note This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported. The pause method pauses the download.
ms.assetid: 763d85da-1044-4a8c-98e7-8889bee6c2c7
keywords:
- pause method Windows Media Player
- pause method Windows Media Player , DownloadItem class
- DownloadItem class Windows Media Player , pause method
topic_type:
- apiref
api_name:
- DownloadItem.pause
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DownloadItem.pause method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **pause** method pauses the download.

## Syntax


```JScript
DownloadItem.pause()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

The **pause** method has no effect on real-time downloads.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later.<br/>                                 |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**DownloadItem Object**](downloaditem-object.md)
</dt> <dt>

[**DownloadItem.resume**](downloaditem-resume.md)
</dt> </dl>

 

 





