---
title: IResultProperty Hint property
description: Special value used to aid data retrieval.
ms.assetid: fa888c5e-898e-4f48-b87e-2d0d078fd1fe
keywords:
- Hint property Legacy Windows Environment Features
- Hint property Legacy Windows Environment Features , IResultProperty interface
- IResultProperty interface Legacy Windows Environment Features , Hint property
topic_type:
- apiref
api_name:
- IResultProperty.Hint
- IResultProperty.get_Hint
api_location:
- WdsSharedIDL.h
api_type:
- COM
ms.topic: article
ms.date: 05/31/2018
---

# IResultProperty::Hint property

\[Windows Search 2.x is available for use in the operating system specified in the Requirements section. It might be altered or unavailable in later versions. Use the [Windows Search API](https://msdn.microsoft.com/library/windows/desktop/ee872061) instead.\]

Special value used to aid data retrieval.

This property is read-only.

## Syntax


```C++
HRESULT get_Hint(
  [out, retval] ling *hint
);
```



## Property value

returns a pointer to the hint.

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2003 with SP1 \[desktop apps only\]<br/>                             |
| Redistributable<br/>          | Windows Desktop Search (WDS) 2.6.5<br/>                                             |
| Header<br/>                   | <dl> <dt>WdsSharedIDL.h</dt> </dl> |



 

 





