---
title: DVD.domain
description: The domain property retrieves the current domain of the DVD.
ms.assetid: 74f4a6a3-8518-48c7-b023-f0255a3a62fd
keywords:
- DVD.domain Windows Media Player
topic_type:
- apiref
api_name:
- DVD.domain
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DVD.domain

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **domain** property retrieves the current domain of the DVD.

``` syntax
player.dvd.domain
      
```

## Possible Values

This property is a read-only **String** containing one of the following values.



| String            | Description                                                                                                                           |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| firstPlay         | Performing default initialization of a DVD disc.                                                                                      |
| videoManagerMenu  | Displaying menus for the entire disc. Also known as topMenu for Windows Media Player. Commonly called the title menu or the top menu. |
| videoTitleSetMenu | Displaying menus for current title set. Also known as titleMenu for Windows Media Player. Commonly called the root menu.              |
| title             | Usually displaying the current title.                                                                                                 |
| stop              | The DVD Navigator is in the DVD Stop domain.                                                                                          |
| undefined         | Player is not in any DVD domain.                                                                                                      |



 

## Remarks

Every DVD is authored differently. Some DVDs do not contain the firstPlay, videoManagerMenu, or videoTitleSetMenu domains.

**Windows Media Player 10 Mobile:** This property always returns an empty string.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Version<br/>                  | Windows Media Player for Windows XP or later<br/>                            |
| DLL<br/>                      | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**DVD Object**](dvd-object.md)
</dt> </dl>

 

 





