---
title: External.DownloadManager
description: Note This topic describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported. The DownloadManager property retrieves the DownloadManager object.
ms.assetid: 9fec7175-611e-4e7e-8978-132e6f86329a
keywords:
- External.DownloadManager Windows Media Player
topic_type:
- apiref
api_name:
- External.DownloadManager
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# External.DownloadManager

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This topic describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **DownloadManager** property retrieves the **DownloadManager** object.

``` syntax
window.external.DownloadManager
      
```

## Possible Values

This property is a read-only **DownloadManager** object.

## Remarks

In Windows Media Player 10 or later, the **DownloadManager** property and object are accessible only from online store service task panes. You cannot use the **DownloadManager** from other features where the **External** object is available, such as HTMLView, Info Center View, and album information.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later.<br/>                                 |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**External Object for Type 2 Online Stores**](external-object-for-type-2-online-stores.md)
</dt> </dl>

 

 





