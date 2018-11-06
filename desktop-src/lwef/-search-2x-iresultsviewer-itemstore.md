---
title: IResultsViewer ItemStore property
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
ms.topic: article
ms.date: 05/31/2018
---

# IResultsViewer::ItemStore property

\[Windows Search 2.x is available for use in the operating system specified in the Requirements section. It might be altered or unavailable in later versions. Use the [Windows Search API](https://msdn.microsoft.com/library/windows/desktop/ee872061) instead.\]

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



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                                 |
| Minimum supported server<br/> | Windows Server 2003 with SP1 \[desktop apps only\]<br/>                        |
| Redistributable<br/>          | Windows Desktop Search (WDS) 2.6.5<br/>                                        |
| Header<br/>                   | <dl> <dt>WdsView.h</dt> </dl> |



 

 





