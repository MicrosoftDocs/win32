---
description: The NewSegment method delivers a new segment to the input pin.
ms.assetid: 53189729-9f47-425e-9df6-faea01dd4482
title: COutputQueue.NewSegment method (Outputq.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- COutputQueue.NewSegment
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# COutputQueue.NewSegment method

The `NewSegment` method delivers a new segment to the input pin.

## Syntax


```C++
HRESULT NewSegment(
   REFERENCE_TIME tStart,
   REFERENCE_TIME tStop,
   double         dRate
);
```



## Parameters

<dl> <dt>

*tStart* 
</dt> <dd>

Starting media position of the segment, in 100-nanosecond units.

</dd> <dt>

*tStop* 
</dt> <dd>

End media position of the segment, in 100-nanosecond units.

</dd> <dt>

*dRate* 
</dt> <dd>

Rate at which this segment should be processed, as a percentage of the original rate.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

If the object is using a thread, it queues the following items, in order:

-   A NEW\_SEGMENT control message.
-   The segment data.

The NEW\_SEGMENT message notifies the thread that the next item on the queue will contain segment data. The segment data is bundled in a structure, declared as follows:


```C++
struct NewSegmentPacket {
    REFERENCE_TIME tStart;
    REFERENCE_TIME tStop;
    double dRate;
}; 
```



The thread calls the [**IPin::NewSegment**](/windows/desktop/api/Strmif/nf-strmif-ipin-newsegment) method on the input pin, using the data given in the structure.

If the object is not using a thread, it calls the [**COutputQueue::SendAnyway**](coutputqueue-sendanyway.md) method to deliver any pending samples. Then it calls **IPin::NewSegment** on the input pin.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Outputq.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**COutputQueue Class**](coutputqueue.md)
</dt> </dl>

 

 




