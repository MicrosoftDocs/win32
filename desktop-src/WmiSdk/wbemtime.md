---
description: The WBEMTime class facilitates conversions between various Windows and ANSI C run-time time formats. For more information, see also WBEMTimeSpan Class Methods.
ms.assetid: b633bc8c-9d02-4bcf-8528-10773fb5ae7a
ms.tgt_platform: multiple
title: WBEMTime class (WbemTime.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WBEMTime
api_type: 
- COM
api_location: 
- FrameDynOS.dll
- FrameDyn.dll
---

# WBEMTime class

\[The **WBEMTime** class is part of the WMI Provider Framework which is now considered in final state, and no further development, enhancements, or updates will be available for non-security related issues affecting these libraries. The [MI APIs](/previous-versions/windows/desktop/wmi_v2/windows-management-infrastructure) should be used for all new development.\]

The **WBEMTime** class facilitates conversions between various Windows and ANSI C run-time time formats. For more information, see also [**WBEMTimeSpan Class Methods**](/windows/desktop/api/WbemTime/nl-wbemtime-wbemtimespan).

## Members

The **WBEMTime** class has these types of members:

-   [Constructors](#constructors)
-   [Methods](#methods)

### Constructors

The **WBEMTime** class has these constructors.



| Constructor                           | Description                                                                                                   |
|:--------------------------------------|:--------------------------------------------------------------------------------------------------------------|
| [**WBEMTime**](/windows/desktop/api/WbemTime/nf-wbemtime-wbemtime-wbemtime(constbstr)) | Constructor that facilitates conversions between various Windows and ANSI C run-time time formats.<br/> |



 

### Methods

The **WBEMTime** class has these methods.



| Method                                                           | Description                                                                                                                            |
|:-----------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------|
| [**Clear**](/windows/desktop/api/WbemTime/nf-wbemtime-wbemtime-clear)                                  | Sets the time in the **WBEMTime** object to an invalid time.<br/>                                                                |
| [**GetBSTR**](/windows/desktop/api/WbemTime/nf-wbemtime-wbemtime-getbstr)                              | Presents the time as a **BSTR** value.<br/>                                                                                      |
| [**GetDMTF**](/windows/desktop/api/WbemTime/nf-wbemtime-wbemtime-getdmtf)                              | Gets the time as a **BSTR** value in CIM datetime format.<br/>                                                                   |
| [**GetDMTFNonNtfs**](/windows/desktop/api/WbemTime/nf-wbemtime-wbemtime-getdmtfnonntfs)                | Gets a DMTF date that is based upon a FAT or a [Date and Time Format](date-and-time-format.md) where the UTC is not known.<br/> |
| [**GetFILETIME**](/windows/desktop/api/WbemTime/nf-wbemtime-wbemtime-getfiletime)                      | Gets the time as an MFC **FILETIME** structure.<br/>                                                                             |
| [**GetLocalOffsetForDate**](/previous-versions/windows/desktop/legacy/aa394049(v=vs.85)) | Overloaded. Returns the offset in minutes(+ or -) between GMT and local time for the time supplied in the argument.<br/>         |
| [**GetStructtm**](/windows/desktop/api/WbemTime/nf-wbemtime-wbemtime-getstructtm)                      | Gets the time as an ANSI C run-time **struct tm** structure.<br/>                                                                |
| [**GetSYSTEMTIME**](/windows/desktop/api/WbemTime/nf-wbemtime-wbemtime-getsystemtime)                  | Gets the time as an MFC **SYSTEMTIME** structure.<br/>                                                                           |
| [**GetTime**](/windows/desktop/api/WbemTime/nf-wbemtime-wbemtime-gettime)                              | Gets the time as a 64-bit integer.<br/>                                                                                          |
| [**Gettime\_t**](/windows/desktop/api/WbemTime/nf-wbemtime-wbemtime-gettime_t)                         | Gets the time as an ANSI C run-time time\_t variable.<br/>                                                                       |
| [**IsOk**](/windows/desktop/api/WbemTime/nf-wbemtime-wbemtime-isok)                                    | Indicates whether the **WBEMTime** object represents a valid time.<br/>                                                          |
| [**SetDMTF**](/windows/desktop/api/WbemTime/nf-wbemtime-wbemtime-setdmtf)                              | Sets the time in the **WBEMTime** object in CIM datetime format.<br/>                                                            |



 

## WBEMTime overloaded operators

The **WBEMTime** object defines the following overloaded operators.



| WBEMTime overloaded operators                                                                                                                                                                                                                                                                                                                                                                                                                                        | Description                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| [**operator =**](/previous-versions/windows/desktop/legacy/aa394050(v=vs.85))                                                                                                                                                                                                                                                                                                                                                                                                                       | *Assignment* operator facilitates conversions between various Windows and ANSI C run-time time formats.                           |
| [**operator +**](/windows/desktop/api/WbemTime/nf-wbemtime-wbemtime-operator-add)                                                                                                                                                                                                                                                                                                                                                                                                                         | *Addition* operator increments an object's time by a time span. The result is returned in a new **WBEMTime** object.              |
| [**operator +=**](/windows/win32/api/directxmath/nf-directxmath-operator-add-assign)                                                                                                                                                                                                                                                                                                                                                                                                                  | *Add-and-assign* operator increments an object's time by a time span.                                                             |
| [**operator -**](/previous-versions/windows/desktop/legacy/aa394051(v=vs.85))                                                                                                                                                                                                                                                                                                                                                                                                                       | *Subtraction* operator decrements an object's time by another object's time. The result is returned in a new **WBEMTime** object. |
| [**operator -=**](/windows/win32/api/directxmath/nf-directxmath-operator-sub-assign)                                                                                                                                                                                                                                                                                                                                                                                                                 | *Subtract-and-assign* operator decrements an object's time by a time span.                                                        |
| [**operator ==**](/windows/desktop/api/WbemTime/nf-wbemtime-wbemtime-operator-equal-equal-to)[**operator !=**](/windows/desktop/api/WbemTime/nf-wbemtime-wbemtime-operator-not-equal-to)<br/> [**operator >**](/windows/desktop/api/WbemTime/nf-wbemtime-wbemtime-operator-greater-than)<br/> [**operator >=**](/windows/desktop/api/WbemTime/nf-wbemtime-wbemtime-operator-greater-than-equal-to)<br/> [**operator <**](/windows/win32/api/wbemtime/nf-wbemtime-wbemtime-operator-less-than)<br/> [**operator <=**](/windows/win32/api/wbemtime/nf-wbemtime-wbemtime-operator-less-than-equal-to)<br/> | Comparison operators compare two **WBEMTime** objects.                                                                            |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                                                                |
| Header<br/>                   | <dl> <dt>WbemTime.h</dt> </dl>                                                                         |
| DLL<br/>                      | <dl> <dt>FrameDynOS.dll; </dt> <dt>FrameDyn.dll</dt> </dl> |



 

