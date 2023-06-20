---
description: The CRefTime class is a helper class for managing reference times.
ms.assetid: 4be0fc23-77fb-4c45-a899-c1dfc6ee89b9
title: CRefTime class (Reftime.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CRefTime
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CRefTime class

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

![creftime class hierarchy](images/cutil05.png)

The `CRefTime` class is a helper class for managing reference times.

A *reference time* is a unit of time represented in 100-nanosecond units. This class shares the same data layout as the [**REFERENCE\_TIME**](reference-time.md) data type, but adds some methods and operators that provide comparison, conversion, and arithmetic functions. For more information about reference times, see [Time and Clocks in DirectShow](time-and-clocks-in-directshow.md).



| Public Member Variables                                                 | Description                                           |
|-------------------------------------------------------------------------|-------------------------------------------------------|
| [**m\_time**](creftime-m-time.md)                                      | Specifies the **REFERENCE\_TIME** value.              |
| Public Methods                                                          | Description                                           |
| [**CRefTime**](creftime-creftime.md)                                   | Constructor method.                                   |
| [**GetUnits**](creftime-getunits.md)                                   | Retrieves the reference time in 100-nanosecond units. |
| [**Millisecs**](creftime-millisecs.md)                                 | Converts the reference time to milliseconds.          |
| Operators                                                               | Description                                           |
| [**operator REFERENCE\_TIME()**](creftime-operator-reference-time-.md) | Casts the object to a **REFERENCE\_TIME** data type.  |
| [**operator=**](creftime-operator-assign.md)                           | Assigns a new reference time.                         |
| [**operator+=**](creftime-operator-plus-assign.md)                     | Adds two reference times.                             |
| [**operator =**](creftime-operator-minus-assign.md)                    | Subtracts one reference time from another.            |



 

## Remarks

There is a potential pitfall with using this class. If you apply the += operator with a **CRefTime** object as the left operand and a variable of type **LONG** as the right operand, the compiler will implicitly coerce the right operand into a **CRefTime** object. This coercion uses the **CRefTime** constructor that converts milliseconds into REFERENCE\_TIME units; as a result, the right operand is multiplied by 10,000:


```
CRefTime rt;   // rt.m_time is 0.
LONG val = 20;
rt += val;    // Coerce val to CRefTime, rt.m_time is now 200,000.
```



However, the same thing does not happen using the + operator:


```
CRefTime rt;   // rt.m_time is 0.
LONG val = 20;
rt = rt + val; // CRefTime, rt.m_time is 20.
```



## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Reftime.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




