---
title: IResultsViewer ItemStore property (WdsView.h)
description: This property will set or return the name of the store to filter results by.
ms.assetid: c2a60485-c8f7-4951-a75e-2e6f6dcc2e4f
keywords:
- ItemStore property Legacy Windows Environment Features
- ItemStore property Legacy Windows Environment Features , IResultsViewer interface
- IResultsViewer interface Legacy Windows Environment Features , ItemStore property
topic_type:
- apiref
api_name:
- IResultsViewer.ItemStore
- IResultsViewer.get_ItemStore
- IResultsViewer.put_ItemStore
api_location:
- WdsView.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IResultsViewer::ItemStore property

> [!NOTE]
> Windows Desktop Search 2.x is an obsolete technology that was originally available as an add-in for Windows XP and Windows Server 2003. On later releases, use the [Windows Search API](../search/-search-reference-entry-page.md) instead. 

This property will set or return the name of the store to filter results by.

This property is read/write.

## Syntax


```C++
HRESULT put_ItemStore(
  [in]          BSTR name
);

HRESULT get_ItemStore(
  [out, retval] BSTR *name
);
```



## Property value

Sets the names of the store.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                                 |
| Minimum supported server<br/> | Windows Server 2003 with SP1 \[desktop apps only\]<br/>                        |
| Redistributable<br/>          | Windows Desktop Search (WDS) 2.6.5<br/>                                        |
| Header<br/>                   | <dl> <dt>WdsView.h</dt> </dl> |



 

 





