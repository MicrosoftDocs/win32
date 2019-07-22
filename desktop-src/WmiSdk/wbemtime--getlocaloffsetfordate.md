---
Description: The GetLocalOffsetForDate method returns the offset in minutes (+ or &\#8211;) between GMT and local time for the time supplied in the argument.
audience: developer
ms.assetid: 15cc5f45-604c-4335-bcd3-92d62dc15420
ms.tgt_platform: multiple
title: WBEMTime::GetLocalOffsetForDate methods
ms.date: 07/02/2019
ms.topic: reference
---

# WBEMTime::GetLocalOffsetForDate methods

\[The [**WBEMTime**](wbemtime.md) class is part of the WMI Provider Framework which is now considered in final state, and no further development, enhancements, or updates will be available for non-security related issues affecting these libraries. The [MI APIs](https://docs.microsoft.com/previous-versions/windows/desktop/wmi_v2/windows-management-infrastructure) should be used for all new development.\]

The **GetLocalOffsetForDate** method returns the offset in minutes (+ or �) between GMT and local time for the time supplied in the argument.

### Overload list



| Method                                                                                           | Description                                           |
|:-------------------------------------------------------------------------------------------------|:------------------------------------------------------|
| [**GetLocalOffsetForDate(time\_t&)**](https://msdn.microsoft.com/en-us/library/Aa394025(v=VS.85).aspx)         | Argument is a reference to a **time\_t**.<br/>  |
| [**GetLocalOffsetForDate(FILETIME\*)**](https://msdn.microsoft.com/en-us/library/Aa394022(v=VS.85).aspx)     | Argument is a pointer to a **FILETIME**.<br/>   |
| [**GetLocalOffsetForDate(struct tm\*)**](https://msdn.microsoft.com/en-us/library/Aa394023(v=VS.85).aspx)   | Argument is a pointer to **tm** structure.<br/> |
| [**GetLocalOffsetForDate(SYSTEMTIME\*)**](https://msdn.microsoft.com/en-us/library/Aa394024(v=VS.85).aspx) | Argument is a pointer to a **SYSTEMTIME**.<br/> |



## Requirements



|                                     |                                                                                                                                                               |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows�Vista<br/>                                                                                                                                      |
| Minimum supported server<br/> | Windows Server�2008<br/>                                                                                                                                |
| Header<br/>                   | <dl> <dt>WbemTime.h</dt> </dl>                                                                         |
| DLL<br/>                      | <dl> <dt>FrameDynOS.dll; </dt> <dt>FrameDyn.dll</dt> </dl> |



�

�




