---
Description: Constructor method.
ms.assetid: 2258ecd6-7594-4ff8-961b-9e5e1ae9ff82
title: CGenericList.CGenericList constructor
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CGenericList.CGenericList
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CGenericList.CGenericList constructor

Constructor method.

## Syntax


```C++
CGenericList(
   TCHAR *pName,
   INT   iItems,
   BOOL  bLock,
   BOOL  bAlert
);
```



## Parameters

<dl> <dt>

*pName* 
</dt> <dd>

Pointer to the name of the list.

</dd> <dt>

*iItems* 
</dt> <dd>

Size of the node cache.

</dd> <dt>

*bLock* 
</dt> <dd>

Not used.

</dd> <dt>

*bAlert* 
</dt> <dd>

Not used.

</dd> </dl>

## Remarks

For efficiency, the `CGenericList` class maintains a cache of list nodes. If you know approximately how many items the list will hold, use this version of the constructor.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxlist.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CGenericList Class**](cgenericlist.md)
</dt> </dl>

 

 




