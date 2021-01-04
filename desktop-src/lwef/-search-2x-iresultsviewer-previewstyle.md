---
title: IResultsViewer PreviewStyle property (WdsView.h)
description: Controls the preview pane's display mode.
ms.assetid: 750664ea-506a-4219-ade5-1c7f1ffbd0d7
keywords:
- PreviewStyle property Legacy Windows Environment Features
- PreviewStyle property Legacy Windows Environment Features , IResultsViewer interface
- IResultsViewer interface Legacy Windows Environment Features , PreviewStyle property
topic_type:
- apiref
api_name:
- IResultsViewer.PreviewStyle
- IResultsViewer.get_PreviewStyle
- IResultsViewer.put_PreviewStyle
api_location:
- WdsView.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IResultsViewer::PreviewStyle property

> [!NOTE]
> Windows Desktop Search 2.x is an obsolete technology that was originally available as an add-in for Windows XP and Windows Server 2003. On later releases, use the [Windows Search API](../search/-search-reference-entry-page.md) instead. 

Controls the preview pane's display mode.

This property is read/write.

## Syntax


```C++
HRESULT put_PreviewStyle(
  [in]          PreviewDisplayStyle style
);

HRESULT get_PreviewStyle(
  [out, retval] PreviewDisplayStyle *style
);
```



## Property value

Sets the current style property for the preview pane.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                                 |
| Minimum supported server<br/> | Windows Server 2003 with SP1 \[desktop apps only\]<br/>                        |
| Redistributable<br/>          | Windows Desktop Search (WDS) 2.6.5<br/>                                        |
| Header<br/>                   | <dl> <dt>WdsView.h</dt> </dl> |



 

 





