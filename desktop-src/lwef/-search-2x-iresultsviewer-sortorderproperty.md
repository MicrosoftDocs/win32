---
title: IResultsViewer SortOrderProperty property (WdsView.h)
description: This property will set or return the order of columns to sort results by.
ms.assetid: ea05f4df-4caf-404f-8890-a109ca88555c
keywords:
- SortOrderProperty property Legacy Windows Environment Features
- SortOrderProperty property Legacy Windows Environment Features , IResultsViewer interface
- IResultsViewer interface Legacy Windows Environment Features , SortOrderProperty property
topic_type:
- apiref
api_name:
- IResultsViewer.SortOrderProperty
- IResultsViewer.get_SortOrderProperty
- IResultsViewer.put_SortOrderProperty
api_location:
- WdsView.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IResultsViewer::SortOrderProperty property

> [!NOTE]
> Windows Desktop Search 2.x is an obsolete technology that was originally available as an add-in for Windows XP and Windows Server 2003. On later releases, use the [Windows Search API](../search/-search-reference-entry-page.md) instead. 

This property will set or return the order of columns to sort results by.

This property is read/write.

## Syntax


```C++
HRESULT put_SortOrderProperty(
  [in]          ColumnSortOrder order
);

HRESULT get_SortOrderProperty(
  [out, retval] ColumnSortOrder *order
);
```



## Property value

Sets the [**ColumnSortOrder**](/windows/win32/api/mmcobj/ne-mmcobj-_columnsortorder) property.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                                 |
| Minimum supported server<br/> | Windows Server 2003 with SP1 \[desktop apps only\]<br/>                        |
| Redistributable<br/>          | Windows Desktop Search (WDS) 2.6.5<br/>                                        |
| Header<br/>                   | <dl> <dt>WdsView.h</dt> </dl> |



 

 





