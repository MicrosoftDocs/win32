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
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# IReferenceClock interface

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

