---
description: Defines units of 100 nanoseconds.
ms.assetid: 9273ff1f-382e-4c58-b571-4852545915b3
title: MFTIME (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFTIME

Defines units of 100 nanoseconds.


```C++
typedef LONGLONG MFTIME;
```



## Examples


```C++
const MFTIME ONE_SECOND = 10000000; // One second.
const LONG   ONE_MSEC = 1000;       // One millisecond

// Convert 100-nanosecond units to milliseconds.

inline LONG MFTimeToMsec(const LONGLONG& time)
{
    return (LONG)(time / (ONE_SECOND / ONE_MSEC));
}
```



## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Datatypes](media-foundation-datatypes.md)
</dt> </dl>

 

 




