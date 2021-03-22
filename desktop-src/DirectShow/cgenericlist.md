---
description: The CGenericList class template that implements a type-specific list. For more information, see CBaseList.
ms.assetid: 69067530-3a7d-4731-8ac6-9d02dbba8440
title: CGenericList class (Wxlist.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CGenericList
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CGenericList class

![cgenericlist class hierarchy](images/list01.png)

The `CGenericList` class template that implements a type-specific list. For more information, see [**CBaseList**](cbaselist.md).

To use this template, declare a variable of type `CGenericList` with a template argument that defines the type of object in the list. For example, the following statement declares a list of [**CBaseFilter**](cbasefilter.md) objects:


```
CGenericList<CBaseFilter> myFilterList("Filters"); 
```



For convenience, Wxlist.h defines the following list types:

``` syntax
typedef CGenericList<CBaseObject> CBaseObjectList;
typedef CGenericList<IUnknown> CBaseInterfaceList;
```



| Public Methods                                          | Description                                                              |
|---------------------------------------------------------|--------------------------------------------------------------------------|
| [**CGenericList**](cgenericlist-cgenericlist.md)       | Constructor method.                                                      |
| [**~CGenericList**](cgenericlist--cgenericlist.md)     | Destructor method.                                                       |
| [**GetHeadPosition**](cgenericlist-getheadposition.md) | Retrieves the position of the first item in the list.                    |
| [**GetTailPosition**](cgenericlist-gettailposition.md) | Retrieves the position of the last item of the list.                     |
| [**GetCount**](cgenericlist-getcount.md)               | Retrieves the number of items in the list.                               |
| [**GetNext**](cgenericlist-getnext.md)                 | Retrieves the item at the specified position, and advances the position. |
| [**Get**](cgenericlist-get.md)                         | Retrieves the item at the specified position.                            |
| [**GetHead**](cgenericlist-gethead.md)                 | Retrieves the item at the head of the list.                              |
| [**RemoveHead**](cgenericlist-removehead.md)           | Removes the first item in the list.                                      |
| [**RemoveTail**](cgenericlist-removetail.md)           | Removes the last item in the list.                                       |
| [**Remove**](cgenericlist-remove.md)                   | Removes the item at the specified position.                              |
| [**AddBefore**](cgenericlist-addbefore.md)             | Inserts an item or list before the specified position.                   |
| [**AddAfter**](cgenericlist-addafter.md)               | Inserts an item or list after the specified position.                    |
| [**AddHead**](cgenericlist-addhead.md)                 | Adds an item or list to the front of the list.                           |
| [**AddTail**](cgenericlist-addtail.md)                 | Appends an item or list to the end of the list.                          |
| [**Find**](cgenericlist-find.md)                       | Retrieves the first position that holds the specified item.              |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxlist.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




