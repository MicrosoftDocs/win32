---
description: The CGenericList class template that implements a type-specific list. For more information, see CBaseList.
ms.assetid: 69067530-3a7d-4731-8ac6-9d02dbba8440
title: CGenericList class (Wxlist.h)
ms.topic: reference
ms.date: 4/26/2023
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
ms.custom: UpdateFrequency5
---

# CGenericList class

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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



 

 




