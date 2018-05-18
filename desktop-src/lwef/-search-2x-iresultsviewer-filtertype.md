---
title: IResultsViewer FilterType property
description: This property will set or return the name of the preceived type to filter results by.
ms.assetid: '025955eb-3e44-4e26-8b5f-ae92eb4c8300'
keywords: ["FilterType property Legacy Windows Environment Features", "FilterType property Legacy Windows Environment Features , IResultsViewer interface", "IResultsViewer interface Legacy Windows Environment Features , FilterType property"]
topic_type:
- apiref
api_name:
- IResultsViewer.FilterType
- IResultsViewer.get_FilterType
- IResultsViewer.put_FilterType
api_location:
- WdsView.h
api_type:
- COM
---

# IResultsViewer::FilterType property

\[Windows Search 2.x is available for use in the operating system specified in the Requirements section. It might be altered or unavailable in later versions. Use the [Windows Search API](https://msdn.microsoft.com/library/windows/desktop/ee872061) instead.\]

This property will set or return the name of the preceived type to filter results by.

This property is read/write.

## Syntax


```C++
HRESULT put_FilterType(
  [in]          BSTR name
);

HRESULT get_FilterType(
  [out, retval] BSTR *name
);
```



## Property value

Sets the perceived type used to filter results.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                                 |
| Minimum supported server<br/> | Windows Server 2003 with SP1 \[desktop apps only\]<br/>                        |
| Redistributable<br/>          | Windows Desktop Search (WDS) 2.6.5<br/>                                        |
| Header<br/>                   | <dl> <dt>WdsView.h</dt> </dl> |



 

 





