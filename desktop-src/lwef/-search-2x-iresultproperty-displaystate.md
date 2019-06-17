---
title: IResultProperty DisplayState property
description: Visability of the property.
ms.assetid: 4fdf6cdb-30bd-4582-a573-a1cc9f4052e6
keywords:
- DisplayState property Legacy Windows Environment Features
- DisplayState property Legacy Windows Environment Features , IResultProperty interface
- IResultProperty interface Legacy Windows Environment Features , DisplayState property
topic_type:
- apiref
api_name:
- IResultProperty.DisplayState
- IResultProperty.get_DisplayState
api_location:
- WdsSharedIDL.h
api_type:
- COM
ms.topic: article
ms.date: 05/31/2018
---

# IResultProperty::DisplayState property

\[Windows Search 2.x is available for use in the operating system specified in the Requirements section. It might be altered or unavailable in later versions. Use the [Windows Search API](https://docs.microsoft.com/windows/desktop/search/-search-reference-entry-page) instead.\]

Visability of the property.

This property is read-only.

## Syntax


```C++
HRESULT get_DisplayState(
  [out, retval] PropertyDisplayState *state
);
```



## Property value

returns a pointer to the display state value.

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2003 with SP1 \[desktop apps only\]<br/>                             |
| Redistributable<br/>          | Windows Desktop Search (WDS) 2.6.5<br/>                                             |
| Header<br/>                   | <dl> <dt>WdsSharedIDL.h</dt> </dl> |



 

 





