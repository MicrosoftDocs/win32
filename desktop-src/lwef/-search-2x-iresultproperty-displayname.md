---
title: IResultProperty DisplayName property
description: Localized display name of the property.
ms.assetid: 8f9e118a-9e92-4919-afe1-735c61af38f7
keywords:
- DisplayName property Legacy Windows Environment Features
- DisplayName property Legacy Windows Environment Features , IResultProperty interface
- IResultProperty interface Legacy Windows Environment Features , DisplayName property
topic_type:
- apiref
api_name:
- IResultProperty.DisplayName
- IResultProperty.get_DisplayName
api_location:
- WdsSharedIDL.h
api_type:
- COM
ms.topic: article
ms.date: 05/31/2018
---

# IResultProperty::DisplayName property

\[Windows Search 2.x is available for use in the operating system specified in the Requirements section. It might be altered or unavailable in later versions. Use the [Windows Search API](https://msdn.microsoft.com/library/windows/desktop/ee872061) instead.\]

Localized display name of the property.

This property is read-only.

## Syntax


```C++
HRESULT get_DisplayName(
  [out, retval] BSTR *name
);
```



## Property value

returns a pointer to the localized display name.

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2003 with SP1 \[desktop apps only\]<br/>                             |
| Redistributable<br/>          | Windows Desktop Search (WDS) 2.6.5<br/>                                             |
| Header<br/>                   | <dl> <dt>WdsSharedIDL.h</dt> </dl> |



 

 





