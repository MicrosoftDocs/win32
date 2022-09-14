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
ms.date: 05/31/2018
---

# DownloadCollection.removeItem method

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

 

 





