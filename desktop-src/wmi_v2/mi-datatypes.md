---
title: MI Datatypes
description: The following types are used by various functions in the MI API.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: DC412382-253C-4A86-83DC-2E57699B23F2
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MI_Boolean
- MI_Char
- MI_Char16
- MI_Sint8
- MI_Uint8
- MI_Sint16
- MI_Uint16
- MI_Sint32
- MI_Uint32
- MI_Sint64
- MI_Uint64
- MI_Real32
- MI_Real64
- MI_StringPtr
- MI_ConstStringPtr
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MI Datatypes

The following types are used by various functions in the MI API.


```C++
typedef unsigned char MI_Boolean;
typedef wchar_t MI_Char;
typedef unsigned short MI_Char16;
typedef signed char MI_Sint8;
typedef unsigned char MI_Uint8;
typedef signed short MI_Sint16;
typedef unsigned short MI_Uint16;
typedef signed int MI_Sint32;
typedef unsigned int MI_Uint32;
typedef signed __int64 MI_Sint64;
typedef unsigned __int64 MI_Uint64;
typedef float MI_Real32;
typedef double MI_Real64;
typedef _Null_terminated_ MI_Char* MI_StringPtr;
typedef _Null_terminated_ const MI_Char* MI_ConstStringPtr;
```



## Requirements



|                                     |                                                                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                                                                 |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                                                       |
| Redistributable<br/>          | Windows Management Framework 3.0 on Windows Server 2008 R2 with SP1, Windows 7 with SP1, and Windows Server 2008 with SP2<br/> |
| Header<br/>                   | <dl> <dt>Mi.h</dt> </dl>                                                      |



## See also

<dl> <dt>

[**MI\_Type**](/windows/previous-versions/Mi/ne-mi-_mi_type?branch=master)
</dt> <dt>

[**MI\_Value**](/windows/previous-versions/mi/ns-mi-_mi_value?branch=master)
</dt> </dl>

 

 





