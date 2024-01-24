---
description: The LARGEINT datatype defines a LARGE\_INTEGER value.
ms.assetid: '65801136-bde7-4bca-af1f-243e757f3d8d'
title: LARGEINT (Netmon.h)
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbSyntax
api_name: 
api_type: 
api_location: 
---

# LARGEINT

The **LARGEINT** datatype defines a [**LARGE\_INTEGER**](/windows/win32/api/winnt/ns-winnt-large_integer-r1) value.


```C++
typedef LARGE_INTEGER* LPLARGEINT;
typedef LARGE_INTEGER UNALIGNED* ULPLARGEINT;
```



## Remarks

The **lpLargeIntTable** member of the [**SET**](set.md) structure points to an array of **SET** structures that define one or more LARGEINT values. When this type of **SET** structure is specified, Network Monitor displays one of the following labels with each LARGEINT value that it finds in the protocol packet.

-   Matches set value. The LARGEINT value is included in the set.
-   Unknown set value. The LARGEINT value is not included in the set.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



## See also

<dl> <dt>

[SET](set.md)
</dt> </dl>

 

