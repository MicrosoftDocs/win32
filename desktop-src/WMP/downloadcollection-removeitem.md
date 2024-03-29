---
title: DownloadCollection.removeItem method
description: Note This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported. The removeItem method removes a download item from a download collection.
ms.assetid: 0008752e-c81a-4f91-a582-9d6b46569479
keywords:
- removeItem method Windows Media Player
- removeItem method Windows Media Player , DownloadCollection class
- DownloadCollection class Windows Media Player , removeItem method
topic_type:
- apiref
api_name:
- DownloadCollection.removeItem
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DownloadCollection.removeItem method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **removeItem** method removes a download item from a download collection.

## Syntax


```JScript
DownloadCollection.removeItem(
  itemID
)
```



## Parameters

<dl> <dt>

*itemID* \[in\]
</dt> <dd>

**Number** (**long**) specifying the index of the **DownloadItem** to remove.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

If the download represented by *itemID* is in progress, this method cancels the download.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/>                                  |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**DownloadCollection.item**](downloadcollection-item.md)
</dt> <dt>

[**DownloadCollection Object**](downloadcollection-object.md)
</dt> </dl>

 

 





