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
ms.date: 05/31/2018
---

# External.DownloadManager

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

 

 





