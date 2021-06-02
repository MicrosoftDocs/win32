---
description: The TimeStamp data type holds information about the time validity of security tokens. The format of the value of the TimeStamp data type is the same as that of the FILETIME structure.
ms.assetid: 0a609b32-dbd7-4905-8990-65ebabcd0668
title: TimeStamp (Sspi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# TimeStamp

The **TimeStamp** data type holds information about the time validity of security tokens. The format of the value of the **TimeStamp** data type is the same as that of the [**FILETIME**](/windows/win32/api/minwinbase/ns-minwinbase-filetime) structure.


```C++
typedef SECURITY_INTEGER TimeStamp, *PTimeStamp;
```



## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                   |
| Header<br/>                   | <dl> <dt>Sspi.h (include Security.h)</dt> </dl> |



 

 
