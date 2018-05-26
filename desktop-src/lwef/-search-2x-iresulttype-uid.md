---
title: IResultType UID property
description: This property contains the unique identifier for the type.
ms.assetid: 31c2ef7d-f5a7-441e-80ea-fd7e46fded07
keywords:
- UID property Legacy Windows Environment Features
- UID property Legacy Windows Environment Features , IResultType interface
- IResultType interface Legacy Windows Environment Features , UID property
topic_type:
- apiref
api_name:
- IResultType.UID
- IResultType.get_UID
api_location:
- WdsSharedIDL.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IResultType::UID property

\[Windows Search 2.x is available for use in the operating system specified in the Requirements section. It might be altered or unavailable in later versions. Use the [Windows Search API](https://msdn.microsoft.com/library/windows/desktop/ee872061) instead.\]

This property contains the unique identifier for the type.

This property is read-only.

## Syntax


```C++
HRESULT get_UID(
  [out, retval] long *uid
);
```



## Property value

the address of the location containing the uid.

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2003 with SP1 \[desktop apps only\]<br/>                             |
| Redistributable<br/>          | Windows Desktop Search (WDS) 2.6.5<br/>                                             |
| Header<br/>                   | <dl> <dt>WdsSharedIDL.h</dt> </dl> |



 

 





