---
description: The WBEMTime class constructor facilitates conversions between various Windows and ANSI C run-time time formats.
audience: developer
ms.assetid: 8b0ce221-2186-4aed-a474-00f88cef6350
ms.tgt_platform: multiple
title: WBEMTime::WBEMTime constructors (WbemTime.h)
ms.date: 07/02/2019
ms.topic: reference
---

# WBEMTime::WBEMTime constructors

\[The [**WBEMTime**](wbemtime.md) class is part of the WMI Provider Framework which is now considered in final state, and no further development, enhancements, or updates will be available for non-security related issues affecting these libraries. The [MI APIs](/previous-versions/windows/desktop/wmi_v2/windows-management-infrastructure) should be used for all new development.\]

The **WBEMTime** class constructor facilitates conversions between various Windows and ANSI C run-time time formats.

### Overload list



| Constructor                                                                 | Description                                                               |
|:----------------------------------------------------------------------------|:--------------------------------------------------------------------------|
| [**WBEMTime()**](/windows/win32/api/wbemtime/nf-wbemtime-wbemtime-wbemtime(constbstr))                                   | Creates an uninitialized time object.<br/>                          |
| [**WBEMTime(BSTR)**](/windows/win32/api/wbemtime/nf-wbemtime-wbemtime-wbemtime(constbstr))                           | Initializes the new time object to the value in the parameter.<br/> |
| [**WBEMTime(const time\_t&)**](/windows/win32/api/wbemtime/nf-wbemtime-wbemtime-wbemtime(consttime_t_))        | Initializes the new time object to the value in the parameter.<br/> |
| [**WBEMTime(const struct tm)**](/windows/win32/api/wbemtime/nf-wbemtime-wbemtime-wbemtime(consttm_))    | Initializes the new time object to the value in the parameter.<br/> |
| [**WBEMTime(const FILETIME&)**](/windows/win32/api/wbemtime/nf-wbemtime-wbemtime-wbemtime(constfiletime_))     | Initializes the new time object to the value in the parameter.<br/> |
| [**WBEMTime(const SYSTEMTIME&)**](/windows/win32/api/wbemtime/nf-wbemtime-wbemtime-wbemtime(constsystemtime_)) | Initializes the new time object to the value in the parameter.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows�Vista<br/>                                                                                                                                      |
| Minimum supported server<br/> | Windows Server�2008<br/>                                                                                                                                |
| Header<br/>                   | <dl> <dt>WbemTime.h</dt> </dl>                                                                         |
| DLL<br/>                      | <dl> <dt>FrameDynOS.dll; </dt> <dt>FrameDyn.dll</dt> </dl> |



�

�
