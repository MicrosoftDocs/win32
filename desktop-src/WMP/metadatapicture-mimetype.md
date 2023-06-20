---
title: MetadataPicture.mimeType
description: The mimeType property retrieves the standard MIME type of the metadata image.
ms.assetid: dde541e3-ddbc-437e-a3a8-64a116e122e0
keywords:
- MetadataPicture.mimeType Windows Media Player
topic_type:
- apiref
api_name:
- MetadataPicture.mimeType
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# MetadataPicture.mimeType

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **mimeType** property retrieves the standard MIME type of the metadata image.

## Syntax

*player*.*currentMedia*.**getItemInfoByType**( *name*, *language*, *index*).**mimeType**

## Possible Values

This property is a read-only **String**.

## Remarks

To retrieve the value of this property, read access to the library is required. For more information, see [Library Access](library-access.md).

**Windows Media Player 10 Mobile:** This property is not supported.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later.<br/>                                 |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**MetadataPicture Object**](metadatapicture-object.md)
</dt> <dt>

[**Settings.mediaAccessRights**](settings-mediaaccessrights.md)
</dt> <dt>

[**Settings.requestMediaAccessRights**](settings-requestmediaaccessrights.md)
</dt> </dl>

 

 





