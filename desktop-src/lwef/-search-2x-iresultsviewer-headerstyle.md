---
title: IResultsViewer HeaderStyle property
description: The style of header displayed in the view.
ms.assetid: 092a2ff2-eb88-4347-a81c-6a8005971ca9
keywords:
- HeaderStyle property Legacy Windows Environment Features
- HeaderStyle property Legacy Windows Environment Features , IResultsViewer interface
- IResultsViewer interface Legacy Windows Environment Features , HeaderStyle property
topic_type:
- apiref
api_name:
- IResultsViewer.HeaderStyle
- IResultsViewer.get_HeaderStyle
- IResultsViewer.put_HeaderStyle
api_location:
- WdsView.h
api_type:
- COM
ms.topic: article
ms.date: 05/31/2018
---

# IResultsViewer::HeaderStyle property

\[Windows Search 2.x is available for use in the operating system specified in the Requirements section. It might be altered or unavailable in later versions. Use the [Windows Search API](https://docs.microsoft.com/windows/desktop/search/-search-reference-entry-page) instead.\]

The style of header displayed in the view.

This property is read/write.

## Syntax


```C++
HRESULT put_HeaderStyle(
  [in]          HeaderDisplayStyle style
);

HRESULT get_HeaderStyle(
  [out, retval] HeaderDisplayStyle *style
);
```



## Property value

Sets the style of the header displayed.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                                 |
| Minimum supported server<br/> | Windows Server 2003 with SP1 \[desktop apps only\]<br/>                        |
| Redistributable<br/>          | Windows Desktop Search (WDS) 2.6.5<br/>                                        |
| Header<br/>                   | <dl> <dt>WdsView.h</dt> </dl> |



 

 





