---
title: DownloadCollection.item method
description: Note This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported. The item method retrieves a pending download object.
ms.assetid: a79db9db-e80c-48db-aee6-9bd8f77a7dff
keywords:
- item method Windows Media Player
- item method Windows Media Player , DownloadCollection class
- DownloadCollection class Windows Media Player , item method
topic_type:
- apiref
api_name:
- DownloadCollection.item
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# DownloadCollection.item method

> [!Note]  
> This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **item** method retrieves a pending download object.

## Syntax


```JScript
retVal = DownloadCollection.item(
  itemId
)
```



## Parameters

<dl> <dt>

*itemId* \[in\]
</dt> <dd>

**Number** (**long**) specifying the index of the **DownloadItem** to retrieve.

</dd> </dl>

## Return value

This method returns a **DownloadItem** object.

## Remarks

The *itemID* value is zero-based.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/>                                  |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**DownloadCollection Object**](downloadcollection-object.md)
</dt> <dt>

[**DownloadItem Object**](downloaditem-object.md)
</dt> </dl>

 

 





