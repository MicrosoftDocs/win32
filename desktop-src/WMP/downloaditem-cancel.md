---
title: DownloadItem.cancel method
description: Note This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported. The cancel method cancels the download.
ms.assetid: b3715fde-6a83-45fa-92ea-1cbffbee7274
keywords:
- cancel method Windows Media Player
- cancel method Windows Media Player , DownloadItem class
- DownloadItem class Windows Media Player , cancel method
topic_type:
- apiref
api_name:
- DownloadItem.cancel
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DownloadItem.cancel method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **cancel** method cancels the download.

## Syntax


```JScript
DownloadItem.cancel()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

Cancelled items are not removed from the download collection. Cancelled items return a **downloadState** value of 4 (canceled).

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later.<br/>                                 |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**DownloadItem Object**](downloaditem-object.md)
</dt> <dt>

[**DownloadItem.downloadState**](downloaditem-downloadstate.md)
</dt> </dl>

 

 





