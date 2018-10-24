---
title: IPropertyFilterCollection GetITem property
description: Returns a specific filter within the collection.
ms.assetid: 72a35d98-b2d8-4dfb-84a7-365a3778fc85
keywords:
- GetITem property Legacy Windows Environment Features
- GetITem property Legacy Windows Environment Features , IPropertyFilterCollection interface
- IPropertyFilterCollection interface Legacy Windows Environment Features , GetITem property
topic_type:
- apiref
api_name:
- IPropertyFilterCollection.GetITem
- IPropertyFilterCollection.get_GetITem
- IPropertyFilterCollection.put_GetITem
api_location:
- WdsSharedIDL.h
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPropertyFilterCollection::GetITem property

\[Windows Search 2.x is available for use in the operating system specified in the Requirements section. It might be altered or unavailable in later versions. Use the [Windows Search API](https://msdn.microsoft.com/library/windows/desktop/ee872061) instead.\]

Returns a specific filter within the collection.

This property is read/write.

## Syntax


```C++
HRESULT put_GetITem(
  [in]          long            index
);

HRESULT get_GetITem(
  [out, retval] IPropertyFilter **filter
);
```



## Property value

Sets the address of the filter.

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2003 with SP1 \[desktop apps only\]<br/>                             |
| Redistributable<br/>          | Windows Desktop Search (WDS) 2.6.5<br/>                                             |
| Header<br/>                   | <dl> <dt>WdsSharedIDL.h</dt> </dl> |



 

 





