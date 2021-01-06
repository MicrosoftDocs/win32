---
description: The CSystemClock class implements a clock that returns the system time.
ms.assetid: 22f8b641-6472-433f-bff4-4e62eae25c9b
title: CSystemClock class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSystemClock
api_type: 
- COM
api_location: 
---

# CSystemClock class

![csystemclock class hierarchy](images/sclock01.png)

The `CSystemClock` class implements a clock that returns the system time.

This class derives from the [**CBaseReferenceClock**](cbasereferenceclock.md) class, and adds support for the **IPersist** and [**IAMClockAdjust**](/windows/desktop/api/Strmif/nn-strmif-iamclockadjust) interfaces.



| Public Methods                                        | Description                                         |
|-------------------------------------------------------|-----------------------------------------------------|
| [**CreateInstance**](csystemclock-createinstance.md) | Creates a new instance of this object.              |
| [**CSystemClock**](csystemclock-csystemclock.md)     | Constructor method.                                 |
| IAMClockAdjust Methods                                | Description                                         |
| [**SetClockDelta**](csystemclock-setclockdelta.md)   | Adjusts the clock time.                             |
| IPersist Methods                                      | Description                                         |
| [**GetClassID**](csystemclock-getclassid.md)         | Returns the class identifier (CLSID) of the object. |



 

 

 



