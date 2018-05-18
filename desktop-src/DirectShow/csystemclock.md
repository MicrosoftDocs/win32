---
Description: 'The CSystemClock class implements a clock that returns the system time.'
ms.assetid: '22f8b641-6472-433f-bff4-4e62eae25c9b'
title: CSystemClock class
---

# CSystemClock class

![csystemclock class hierarchy](images/sclock01.png)

The `CSystemClock` class implements a clock that returns the system time.

This class derives from the [**CBaseReferenceClock**](cbasereferenceclock.md) class, and adds support for the **IPersist** and [**IAMClockAdjust**](iamclockadjust.md) interfaces.



| Public Methods                                        | Description                                         |
|-------------------------------------------------------|-----------------------------------------------------|
| [**CreateInstance**](csystemclock-createinstance.md) | Creates a new instance of this object.              |
| [**CSystemClock**](csystemclock-csystemclock.md)     | Constructor method.                                 |
| IAMClockAdjust Methods                                | Description                                         |
| [**SetClockDelta**](csystemclock-setclockdelta.md)   | Adjusts the clock time.                             |
| IPersist Methods                                      | Description                                         |
| [**GetClassID**](csystemclock-getclassid.md)         | Returns the class identifier (CLSID) of the object. |



 

 

 



