---
description: The CAutoLock class holds a critical section for the scope of a code block.
ms.assetid: 8013b3a7-297b-4cf8-8107-4cee1fc12b56
title: CAutoLock class (Wxutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAutoLock
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CAutoLock class

The `CAutoLock` class holds a critical section for the scope of a code block.

This class works in conjunction with the [**CCritSec**](ccritsec.md) class, which is a wrapper for critical section objects. The `CAutoLock` constructor locks the critical section, and the destructor unlocks it. By using a `CAutoLock` object as a local variable, you can lock a critical section with the guarantee that all code paths will unlock the critical section.

The following code example shows how to use this class:


```
CCritSec csMyLock;  // Critical section is not locked yet.
{
    CAutoLock cObjectLock(&csMyLock);  // Lock the critical section.

    // Protected section of code.     

} // Lock goes out of scope here.

```



The methods in this class are not designed to be overridden.



| Protected Member Variables                 | Description                                                      |
|--------------------------------------------|------------------------------------------------------------------|
| [**m\_pLock**](cautolock-m-plock.md)      | Critical section for this lock.                                  |
| Public Methods                             | Description                                                      |
| [**CAutoLock**](cautolock-cautolock.md)   | Constructor method. Locks the specified critical section object. |
| [**~CAutoLock**](cautolock--cautolock.md) | Destructor method. Unlocks the critical section object.          |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




