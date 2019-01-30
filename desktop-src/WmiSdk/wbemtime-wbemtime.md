---
Description: 'The WBEMTime class constructor facilitates conversions between various Windows and ANSI C run-time time formats.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '8b0ce221-2186-4aed-a474-00f88cef6350'
ms.tgt_platform: multiple
title: 'WBEMTime::WBEMTime constructors'
---

# WBEMTime::WBEMTime constructors

\[The [**WBEMTime**](wbemtime.md) class is part of the WMI Provider Framework which is now considered in final state, and no further development, enhancements, or updates will be available for non-security related issues affecting these libraries. The [MI APIs](https://msdn.microsoft.com/library/jj152383) should be used for all new development.\]

The **WBEMTime** class constructor facilitates conversions between various Windows and ANSI C run-time time formats.

### Overload list



| Constructor                                                                 | Description                                                               |
|:----------------------------------------------------------------------------|:--------------------------------------------------------------------------|
| [**WBEMTime()**](https://msdn.microsoft.com/en-us/library/Aa394048(v=VS.85).aspx)                                   | Creates an uninitialized time object.<br/>                          |
| [**WBEMTime(BSTR)**](https://msdn.microsoft.com/en-us/library/Aa394043(v=VS.85).aspx)                           | Initializes the new time object to the value in the parameter.<br/> |
| [**WBEMTime(const time\_t&)**](https://msdn.microsoft.com/en-us/library/Aa394047(v=VS.85).aspx)        | Initializes the new time object to the value in the parameter.<br/> |
| [**WBEMTime(const struct tm)**](https://msdn.microsoft.com/en-us/library/Aa394045(v=VS.85).aspx)    | Initializes the new time object to the value in the parameter.<br/> |
| [**WBEMTime(const FILETIME&)**](https://msdn.microsoft.com/en-us/library/Aa394044(v=VS.85).aspx)     | Initializes the new time object to the value in the parameter.<br/> |
| [**WBEMTime(const SYSTEMTIME&)**](https://msdn.microsoft.com/en-us/library/Aa394046(v=VS.85).aspx) | Initializes the new time object to the value in the parameter.<br/> |



## Requirements



|                                     |                                                                                                                                                               |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows�Vista<br/>                                                                                                                                      |
| Minimum supported server<br/> | Windows Server�2008<br/>                                                                                                                                |
| Header<br/>                   | <dl> <dt>WbemTime.h</dt> </dl>                                                                         |
| DLL<br/>                      | <dl> <dt>FrameDynOS.dll; </dt> <dt>FrameDyn.dll</dt> </dl> |



�

�




