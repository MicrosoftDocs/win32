---
title: IReferenceClock interface
description: The IReferenceClock interface provides access to an external clock. This interface is provided to enable all rendering routines to be synchronized to the same clock.This interface can be obtained from a reader object.
ms.assetid: 1424fd74-d56c-4338-801f-319ef975169f
keywords:
- IReferenceClock interface windows Media Format
- IReferenceClock interface windows Media Format , described
topic_type:
- apiref
api_name:
- IReferenceClock
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IReferenceClock interface

The **IReferenceClock** interface provides access to an external clock. This interface is provided to enable all rendering routines to be synchronized to the same clock.

This interface can be obtained from a reader object.

## Members

The **IReferenceClock** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IReferenceClock** also has these types of members:

-   [Methods](#methods)

### Methods

The **IReferenceClock** interface has these methods.



| Method                                                   | Description                                                               |
|:---------------------------------------------------------|:--------------------------------------------------------------------------|
| [**AdvisePeriodic**](ireferenceclock-adviseperiodic.md) | Not implemented by this SDK.<br/>                                   |
| [**AdviseTime**](ireferenceclock-advisetime.md)         | Requests an asynchronous notification that a time has elapsed.<br/> |
| [**GetTime**](ireferenceclock-gettime.md)               | Retrieves the current reference time.<br/>                          |
| [**Unadvise**](ireferenceclock-unadvise.md)             | Cancels a notification request.<br/>                                |



 

## Remarks

For information on other interfaces that can be obtained by using the QueryInterface method of this interface, see Reader Object.

## See also

<dl> <dt>

[**Interfaces**](interfaces.md)
</dt> </dl>

 

