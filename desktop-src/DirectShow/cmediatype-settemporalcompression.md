---
description: The SetTemporalCompression method specifies whether samples are compressed using temporal (interframe) compression.
ms.assetid: cdd181ee-d1e9-48b0-96f6-e76db9f3f933
title: CMediaType.SetTemporalCompression method (Mtype.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaType.SetTemporalCompression
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaType.SetTemporalCompression method

The `SetTemporalCompression` method specifies whether samples are compressed using temporal (interframe) compression.

## Syntax


```C++
void SetTemporalCompression(
   BOOL bCompressed
);
```



## Parameters

<dl> <dt>

*bCompressed* 
</dt> <dd>

Boolean value that specifies whether the stream uses temporal compression. If the stream uses temporal compression, set the value to **TRUE**.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This method sets the **bTemporalCompression** member.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Mtype.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaType Class**](cmediatype.md)
</dt> </dl>

 

 




