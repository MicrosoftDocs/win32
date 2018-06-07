---
Description: The LARGEINT datatype defines a LARGE\_INTEGER value.
ms.assetid: ca565be0-96bb-4265-9422-793db0723563
title: LARGEINT
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LARGEINT

The **LARGEINT** datatype defines a [**LARGE\_INTEGER**](https://msdn.microsoft.com/library/windows/desktop/aa383713) value.


```C++
typedef LARGE_INTEGER* LPLARGEINT;
typedef LARGE_INTEGER UNALIGNED* ULPLARGEINT;
```



## Remarks

The **lpLargeIntTable** member of the [**SET**](set.md) structure points to an array of **SET** structures that define one or more LARGEINT values. When this type of **SET** structure is specified, Network Monitor displays one of the following labels with each LARGEINT value that it finds in the protocol packet.

-   Matches set value. The LARGEINT value is included in the set.
-   Unknown set value. The LARGEINT value is not included in the set.

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



## See also

<dl> <dt>

[SET](set.md)
</dt> </dl>

 

 




