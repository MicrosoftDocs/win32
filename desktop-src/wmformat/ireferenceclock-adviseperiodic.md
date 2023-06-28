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
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# IReferenceClock::AdvisePeriodic method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 




