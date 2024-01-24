---
title: Media.error
description: The error property retrieves an ErrorItem object if the media item has an error condition.
ms.assetid: cd572688-12f9-4615-8f22-9442d615a2b6
keywords:
- Media.error Windows Media Player
topic_type:
- apiref
api_name:
- Media.error
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Media.error

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **error** property retrieves an **ErrorItem** object if the media item has an error condition.

## Syntax

*player*.*currentMedia*.**error**

## Possible Values

This property is a read-only **ErrorItem** object.

## Remarks

If the media item cannot be played, this property retrieves an **ErrorItem** object that contains information about the problem encountered.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player for Windows XP or later.<br/>                           |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**ErrorItem Object**](erroritem-object.md)
</dt> <dt>

[**Media Object**](media-object.md)
</dt> </dl>

 

 





