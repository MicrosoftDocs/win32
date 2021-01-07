---
description: The WBEMTime class assignment operators are overloaded to facilitate conversions between various Windows and ANSI C run-time time formats. The various overloaded signatures are listed below.
audience: developer
ms.assetid: 47978056-d46f-4f8f-99cb-8463b44da7cf
ms.tgt_platform: multiple
title: WBEMTime::operator= operators (WbemTime.h)
ms.date: 07/02/2019
ms.topic: reference
---

# WBEMTime::operator= operators

\[The [**WBEMTime**](wbemtime.md) class is part of the WMI Provider Framework which is now considered in final state, and no further development, enhancements, or updates will be available for non-security related issues affecting these libraries. The [MI APIs](/previous-versions/windows/desktop/wmi_v2/windows-management-infrastructure) should be used for all new development.\]

The [**WBEMTime**](wbemtime.md) class assignment operators are overloaded to facilitate conversions between various Windows and ANSI C run-time time formats. The various overloaded signatures are listed below.

### Overload list



| Operator                                                                     | Description                                                    |
|:-----------------------------------------------------------------------------|:---------------------------------------------------------------|
| [**operator=(BSTR)**](/windows/win32/api/wbemtime/nf-wbemtime-wbemtime-operator-assign(constbstr))               | Converts a **BSTR** to **WBEMTime** format.<br/>         |
| [**operator=(time\_t&)**](/windows/win32/api/wbemtime/nf-wbemtime-wbemtime-operator-assign(consttime_t_))        | Converts **time\_t** to **WBEMTime** format.<br/>        |
| [**operator=(FILETIME&)**](/windows/win32/api/wbemtime/nf-wbemtime-wbemtime-operator-assign(constfiletime_))     | Converts **FILETIME** to **WBEMTime** format.<br/>       |
| [**operator=(struct tm&)**](/windows/win32/api/wbemtime/nf-wbemtime-wbemtime-operator-assign(consttm_))   | Converts a **tm** structure to **WBEMTime** format.<br/> |
| [**operator=(SYSTEMTIME&)**](/windows/win32/api/wbemtime/nf-wbemtime-wbemtime-operator-assign(constsystemtime_)) | Converts **SYSTEMTIME** to **WBEMTime** format.<br/>     |



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows�Vista<br/>                                                                                                                                      |
| Minimum supported server<br/> | Windows Server�2008<br/>                                                                                                                                |
| Header<br/>                   | <dl> <dt>WbemTime.h</dt> </dl>                                                                         |
| DLL<br/>                      | <dl> <dt>FrameDynOS.dll; </dt> <dt>FrameDyn.dll</dt> </dl> |



�

�
