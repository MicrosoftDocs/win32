---
title: IResultsViewer QueryText property (WdsView.h)
description: Gets or sets the current query text.
ms.assetid: 3d6b31fa-3f17-45de-a91a-f24a6b076099
keywords:
- QueryText property Legacy Windows Environment Features
- QueryText property Legacy Windows Environment Features , IResultsViewer interface
- IResultsViewer interface Legacy Windows Environment Features , QueryText property
topic_type:
- apiref
api_name:
- IResultsViewer.QueryText
- IResultsViewer.get_QueryText
- IResultsViewer.put_QueryText
api_location:
- WdsView.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IResultsViewer::QueryText property

\[Windows Search 2.x is available for use in the operating system specified in the Requirements section. It might be altered or unavailable in later versions. Use the [Windows Search API](https://docs.microsoft.com/windows/desktop/search/-search-reference-entry-page) instead.\]

Gets or sets the current query text.

This property is read/write.

## Syntax


```C++
HRESULT put_QueryText(
  [in]          BSTR query
);

HRESULT get_QueryText(
  [out, retval] BSTR *query
);
```



## Property value

Sets the current query text.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                                 |
| Minimum supported server<br/> | Windows Server 2003 with SP1 \[desktop apps only\]<br/>                        |
| Redistributable<br/>          | Windows Desktop Search (WDS) 2.6.5<br/>                                        |
| Header<br/>                   | <dl> <dt>WdsView.h</dt> </dl> |



 

 





