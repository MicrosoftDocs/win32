---
title: IResultProperty DataType property
description: A properties data type.
ms.assetid: 2bf83256-0d69-48f2-aa7d-d34dcba17050
keywords:
- DataType property Legacy Windows Environment Features
- DataType property Legacy Windows Environment Features , IResultProperty interface
- IResultProperty interface Legacy Windows Environment Features , DataType property
topic_type:
- apiref
api_name:
- IResultProperty.DataType
- IResultProperty.get_DataType
api_location:
- WdsSharedIDL.h
api_type:
- COM
ms.topic: article
ms.date: 05/31/2018
---

# IResultProperty::DataType property

\[Windows Search 2.x is available for use in the operating system specified in the Requirements section. It might be altered or unavailable in later versions. Use the [Windows Search API](https://msdn.microsoft.com/library/windows/desktop/ee872061) instead.\]

A properties data type.

This property is read-only.

## Syntax


```C++
HRESULT get_DataType(
  [out, retval] VARTYPE *vt
);
```



## Property value

returns a pointer to the properties data type.

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2003 with SP1 \[desktop apps only\]<br/>                             |
| Redistributable<br/>          | Windows Desktop Search (WDS) 2.6.5<br/>                                             |
| Header<br/>                   | <dl> <dt>WdsSharedIDL.h</dt> </dl> |



 

 





