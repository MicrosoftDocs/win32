---
title: IReferenceClock AdvisePeriodic method
description: This method is not implemented.
ms.assetid: b34ef914-992e-4ce2-943b-8bc36687a88a
keywords:
- AdvisePeriodic method windows Media Format
- AdvisePeriodic method windows Media Format , IReferenceClock interface
- IReferenceClock interface windows Media Format , AdvisePeriodic method
topic_type:
- apiref
api_name:
- IReferenceClock.AdvisePeriodic
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IReferenceClock::AdvisePeriodic method

This method is not implemented.

In other implementations of the **IReferenceClock** interface, such as in the DirectShow® component of Microsoft® DirectX®, the **AdvisePeriodic** method is used to create a periodic advise request that would signal the specified event object each time the specified time interval elapses. This SDK does not implement the functionality of this method, and any calls made to it will result in a return value of E\_NOTIMPL.

## Syntax


```C++
 AdvisePeriodic();
```



## Parameters

This method has no parameters.

## See also

<dl> <dt>

[**IReferenceClock Interface**](ireferenceclock.md)
</dt> </dl>

 

 




