---
title: IResultsViewer SortOrderProperty property
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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IResultsViewer::SortOrderProperty property

\[Windows Search 2.x is available for use in the operating system specified in the Requirements section. It might be altered or unavailable in later versions. Use the [Windows Search API](https://msdn.microsoft.com/library/windows/desktop/ee872061) instead.\]

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

Sets the [**ColumnSortOrder**](/windows/win32/mmcobj/ne-mmcobj-columnsortorder?branch=master) property.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                                 |
| Minimum supported server<br/> | Windows Server 2003 with SP1 \[desktop apps only\]<br/>                        |
| Redistributable<br/>          | Windows Desktop Search (WDS) 2.6.5<br/>                                        |
| Header<br/>                   | <dl> <dt>WdsView.h</dt> </dl> |



 

 





