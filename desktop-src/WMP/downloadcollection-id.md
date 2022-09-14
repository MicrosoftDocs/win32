---
title: DownloadCollection.id
description: Note This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported. The id property retrieves the ID of the download collection.
ms.assetid: b5b17f22-913c-4055-8958-e3efac819b2b
keywords:
- DownloadCollection.id Windows Media Player
topic_type:
- apiref
api_name:
- DownloadCollection.id
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# DownloadCollection.id

> [!Note]  
> This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **id** property retrieves the ID of the download collection.

## Syntax

``` syntax
DownloadManager.getDownloadCollection(
        collectionId
        ).id
      
```

## Possible Values

This property is a read-only **Number** (**long**).

## Remarks

When the Download Manager creates a new download collection, it assigns the collection an ID number. ID numbers persist between Windows Media Player sessions and operating system sessions.

ID numbers are not unique. However, there are enough ID numbers available in the 32-bit value that it is extremely unlikely that an existing ID number will ever be overwritten by a new one.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/>                                  |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**DownloadCollection Object**](downloadcollection-object.md)
</dt> </dl>

 

 





