---
Description: The WBEMTime class facilitates conversions between various Windows and ANSI C run-time time formats. For more information, see also WBEMTimeSpan Class Methods.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b633bc8c-9d02-4bcf-8528-10773fb5ae7a
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: WBEMTime class
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# WBEMTime class

\[The **WBEMTime** class is part of the WMI Provider Framework which is now considered in final state, and no further development, enhancements, or updates will be available for non-security related issues affecting these libraries. The [MI APIs](https://msdn.microsoft.com/library/jj152383) should be used for all new development.\]

The **WBEMTime** class facilitates conversions between various Windows and ANSI C run-time time formats. For more information, see also [**WBEMTimeSpan Class Methods**](/windows/win32/WbemTime/nl-wbemtime-wbemtimespan?branch=master).

## Members

The **WBEMTime** class has these types of members:

-   [Constructors](#constructors)
-   [Methods](#methods)

### Constructors

The **WBEMTime** class has these constructors.



| Constructor                           | Description                                                                                                   |
|:--------------------------------------|:--------------------------------------------------------------------------------------------------------------|
| [**WBEMTime**](/windows/win32/WbemTime/nf-wbemtime-wbemtime-wbemtime(const bstr)?branch=master) | Constructor that facilitates conversions between various Windows and ANSI C run-time time formats.<br/> |



 

### Methods

The **WBEMTime** class has these methods.



| Method                                                           | Description                                                                                                                            |
|:-----------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------|
| [**Clear**](/windows/win32/WbemTime/nf-wbemtime-wbemtime-clear?branch=master)                                  | Sets the time in the **WBEMTime** object to an invalid time.<br/>                                                                |
| [**GetBSTR**](/windows/win32/WbemTime/nf-wbemtime-wbemtime-getbstr?branch=master)                              | Presents the time as a **BSTR** value.<br/>                                                                                      |
| [**GetDMTF**](/windows/win32/WbemTime/nf-wbemtime-wbemtime-getdmtf?branch=master)                              | Gets the time as a **BSTR** value in CIM datetime format.<br/>                                                                   |
| [**GetDMTFNonNtfs**](/windows/win32/WbemTime/nf-wbemtime-wbemtime-getdmtfnonntfs?branch=master)                | Gets a DMTF date that is based upon a FAT or a [Date and Time Format](date-and-time-format.md) where the UTC is not known.<br/> |
| [**GetFILETIME**](/windows/win32/WbemTime/nf-wbemtime-wbemtime-getfiletime?branch=master)                      | Gets the time as an MFC **FILETIME** structure.<br/>                                                                             |
| [**GetLocalOffsetForDate**](/windows/win32/WbemTime/?branch=master) | Overloaded. Returns the offset in minutes(+ or -) between GMT and local time for the time supplied in the argument.<br/>         |
| [**GetStructtm**](/windows/win32/WbemTime/nf-wbemtime-wbemtime-getstructtm?branch=master)                      | Gets the time as an ANSI C run-time **struct tm** structure.<br/>                                                                |
| [**GetSYSTEMTIME**](/windows/win32/WbemTime/nf-wbemtime-wbemtime-getsystemtime?branch=master)                  | Gets the time as an MFC **SYSTEMTIME** structure.<br/>                                                                           |
| [**GetTime**](/windows/win32/WbemTime/nf-wbemtime-wbemtime-gettime?branch=master)                              | Gets the time as a 64-bit integer.<br/>                                                                                          |
| [**Gettime\_t**](/windows/win32/WbemTime/nf-wbemtime-wbemtime-gettime_t?branch=master)                         | Gets the time as an ANSI C run-time time\_t variable.<br/>                                                                       |
| [**IsOk**](/windows/win32/WbemTime/nf-wbemtime-wbemtime-isok?branch=master)                                    | Indicates whether the **WBEMTime** object represents a valid time.<br/>                                                          |
| [**SetDMTF**](/windows/win32/WbemTime/nf-wbemtime-wbemtime-setdmtf?branch=master)                              | Sets the time in the **WBEMTime** object in CIM datetime format.<br/>                                                            |



 

## WBEMTime overloaded operators

The **WBEMTime** object defines the following overloaded operators.



| WBEMTime overloaded operators                                                                                                                                                                                                                                                                                                                                                                                                                                        | Description                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| [**operator =**](/windows/win32/WbemTime/?branch=master)                                                                                                                                                                                                                                                                                                                                                                                                                       | *Assignment* operator facilitates conversions between various Windows and ANSI C run-time time formats.                           |
| [**operator +**](/windows/win32/WbemTime/nf-wbemtime-wbemtime-operator+?branch=master)                                                                                                                                                                                                                                                                                                                                                                                                                         | *Addition* operator increments an object's time by a time span. The result is returned in a new **WBEMTime** object.              |
| [**operator +=**](/windows/win32/WbemTime/nf-wbemtime-wbemtime-operator+=?branch=master)                                                                                                                                                                                                                                                                                                                                                                                                                  | *Add-and-assign* operator increments an object's time by a time span.                                                             |
| [**operator -**](/windows/win32/WbemTime/?branch=master)                                                                                                                                                                                                                                                                                                                                                                                                                       | *Subtraction* operator decrements an object's time by another object's time. The result is returned in a new **WBEMTime** object. |
| [**operator -=**](/windows/win32/WbemTime/nf-wbemtime-wbemtime-operator-=?branch=master)                                                                                                                                                                                                                                                                                                                                                                                                                 | *Subtract-and-assign* operator decrements an object's time by a time span.                                                        |
| [**operator ==**](/windows/win32/WbemTime/?branch=master)[**operator !=**](/windows/win32/WbemTime/?branch=master)<br/> [**operator &gt;**](/windows/win32/WbemTime/?branch=master)<br/> [**operator &gt;=**](/windows/win32/WbemTime/?branch=master)<br/> [**operator &lt;**](/windows/win32/WbemTime/?branch=master)<br/> [**operator &lt;=**](/windows/win32/WbemTime/?branch=master)<br/> | Comparison operators compare two **WBEMTime** objects.                                                                            |



 

## Requirements



|                                     |                                                                                                                                                               |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                                                                |
| Header<br/>                   | <dl> <dt>WbemTime.h</dt> </dl>                                                                         |
| DLL<br/>                      | <dl> <dt>FrameDynOS.dll; </dt> <dt>FrameDyn.dll</dt> </dl> |



 

 




