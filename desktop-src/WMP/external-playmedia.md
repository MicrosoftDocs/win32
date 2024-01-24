---
title: External.playMedia method
description: This page documents a feature of the Windows Media Player 9 Series SDK and the Windows Media Player 10 SDK. It may be unavailable in subsequent versions.
ms.assetid: 48071318-e853-4139-8fe4-17d1cdbef8f5
keywords:
- playMedia method Windows Media Player
- playMedia method Windows Media Player , External class
- External class Windows Media Player , playMedia method
topic_type:
- apiref
api_name:
- External.playMedia
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# External.playMedia method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This page documents a feature of the Windows Media Player 9 Series SDK and the Windows Media Player 10 SDK. It may be unavailable in subsequent versions.

> [!Note]  
> This topic describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **playMedia** method specifies the URL of a digital media item to play.

## Syntax


```JScript
External.playMedia(
  URL
)
```



## Parameters

<dl> <dt>

*URL* \[in\]
</dt> <dd>

**String** specifying the URL of the digital media item to play.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This method is only available to webpages hosted in the **Guide** feature.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later.<br/>                                 |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**External Object for Type 2 Online Stores**](external-object-for-type-2-online-stores.md)
</dt> </dl>

 

 





