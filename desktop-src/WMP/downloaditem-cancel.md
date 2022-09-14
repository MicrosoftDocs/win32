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
ms.date: 05/31/2018
---

# DownloadItem.cancel method

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

 

 





