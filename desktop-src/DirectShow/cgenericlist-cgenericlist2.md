---
description: "Learn about the constructor method for CGenericList.CGenericList (Wxlist.h). This method uses the 'pName' parameter."
ms.assetid: 6311d84d-1723-4607-87f8-7cd2ad2582f3
title: CGenericList.CGenericList constructor (Wxlist.h) - pName parameter
ms.topic: reference
ms.date: 4/26/2023
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
ms.custom: UpdateFrequency5
---

# CGenericList.CGenericList constructor (Wxlist.h) - pName parameter

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Constructor method.

## Syntax


```C++
CGenericList(
   TCHAR *pName
);
```



## Parameters

<dl> <dt>

*pName* 
</dt> <dd>

Pointer to the name of the list.

</dd> </dl>

## Remarks

For efficiency, the `CGenericList` class maintains a cache of list nodes. This version of the constructor uses a default cache size.

## Requirements

| Requirement | Value |
|-|-|
| Header | Wxlist.h (include Streams.h) |
| Library| Strmbase.lib (retail builds); Strmbasd.lib (debug builds) |

## See also

<dl> <dt>

[**CGenericList Class**](cgenericlist.md)
</dt> </dl>

 

 




