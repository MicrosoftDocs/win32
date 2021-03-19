---
description: The DisplayType function sends information about a media type to the debug output location. Ignored in retail builds.
ms.assetid: '63a88508-dff8-4869-97e5-0f75f4a9dca0'
title: DisplayType function (Wxdebug.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DisplayType
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# DisplayType function

The `DisplayType` function sends information about a media type to the debug output location. Ignored in retail builds.

## Syntax


```C++
void DisplayType(
         LPTSTR        label,
   const AM_MEDIA_TYPE *pmtIn
);
```



## Parameters

<dl> <dt>

*label* 
</dt> <dd>

String that contains a message to display with the media type information.

</dd> <dt>

*pmtIn* 
</dt> <dd>

ointer to the [**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type) structure that contains the media type.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

This function generates several LOG\_TRACE messages. At logging level 2 or higher, the function displays the major type, subtype, and format type, and data from the format block. At logging level 5 or higher, the function displays additional information, such as the source and target rectangles for video types.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxdebug.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Debug Output Functions](debug-output-functions.md)
</dt> </dl>

 

 




