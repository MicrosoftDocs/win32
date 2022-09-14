---
description: The SetFormatType method specifies the format type.
ms.assetid: e8ed9190-7169-4d51-ace7-597f43ff083e
title: CMediaType.SetFormatType method (Mtype.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaType.SetFormatType
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaType.SetFormatType method

The ``SetFormatType method specifies the format type.

## Syntax


```C++
void SetFormatType(
   const GUID *pformattype
);
```



## Parameters

<dl> <dt>

*pformattype* 
</dt> <dd>

Pointer to a **GUID** that specifies the format type.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This method sets the **formattype** member. The format type defines the layout of the format block. For example, if the format type is FORMAT\_VideoInfo, the format block should contain a **VIDEOINFOHEADER** structure. To set the format block, call the [**CMediaType::SetFormat**](cmediatype-setformat.md) method. The caller is responsible for making sure that the format block matches the format type.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Mtype.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaType Class**](cmediatype.md)
</dt> </dl>

 

 


``
