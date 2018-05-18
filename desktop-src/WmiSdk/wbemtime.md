---
Description: 'The WBEMTime class facilitates conversions between various Windows and ANSI C run-time time formats. For more information, see also WBEMTimeSpan Class Methods.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'b633bc8c-9d02-4bcf-8528-10773fb5ae7a'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: WBEMTime class
---

# WBEMTime class

\[The **WBEMTime** class is part of the WMI Provider Framework which is now considered in final state, and no further development, enhancements, or updates will be available for non-security related issues affecting these libraries. The [MI APIs](https://msdn.microsoft.com/library/jj152383) should be used for all new development.\]

The **WBEMTime** class facilitates conversions between various Windows and ANSI C run-time time formats. For more information, see also [**WBEMTimeSpan Class Methods**](wbemtimespan.md).

## Members

The **WBEMTime** class has these types of members:

-   [Constructors](#constructors)
-   [Methods](#methods)

### Constructors

The **WBEMTime** class has these constructors.



| Constructor                           | Description                                                                                                   |
|:--------------------------------------|:--------------------------------------------------------------------------------------------------------------|
| [**WBEMTime**](wbemtime-wbemtime.md) | Constructor that facilitates conversions between various Windows and ANSI C run-time time formats.<br/> |



 

### Methods

The **WBEMTime** class has these methods.



| Method                                                           | Description                                                                                                                            |
|:-----------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------|
| [**Clear**](wbemtime-clear.md)                                  | Sets the time in the **WBEMTime** object to an invalid time.<br/>                                                                |
| [**GetBSTR**](wbemtime-getbstr.md)                              | Presents the time as a **BSTR** value.<br/>                                                                                      |
| [**GetDMTF**](wbemtime-getdmtf.md)                              | Gets the time as a **BSTR** value in CIM datetime format.<br/>                                                                   |
| [**GetDMTFNonNtfs**](wbemtime-getdmtfnonntfs.md)                | Gets a DMTF date that is based upon a FAT or a [Date and Time Format](date-and-time-format.md) where the UTC is not known.<br/> |
| [**GetFILETIME**](wbemtime-getfiletime.md)                      | Gets the time as an MFC **FILETIME** structure.<br/>                                                                             |
| [**GetLocalOffsetForDate**](wbemtime--getlocaloffsetfordate.md) | Overloaded. Returns the offset in minutes(+ or -) between GMT and local time for the time supplied in the argument.<br/>         |
| [**GetStructtm**](wbemtime-getstructtm.md)                      | Gets the time as an ANSI C run-time **struct tm** structure.<br/>                                                                |
| [**GetSYSTEMTIME**](wbemtime-getsystemtime.md)                  | Gets the time as an MFC **SYSTEMTIME** structure.<br/>                                                                           |
| [**GetTime**](wbemtime-gettime.md)                              | Gets the time as a 64-bit integer.<br/>                                                                                          |
| [**Gettime\_t**](wbemtime-gettime-t.md)                         | Gets the time as an ANSI C run-time time\_t variable.<br/>                                                                       |
| [**IsOk**](wbemtime-isok.md)                                    | Indicates whether the **WBEMTime** object represents a valid time.<br/>                                                          |
| [**SetDMTF**](wbemtime-setdmtf.md)                              | Sets the time in the **WBEMTime** object in CIM datetime format.<br/>                                                            |



 

## WBEMTime overloaded operators

The **WBEMTime** object defines the following overloaded operators.



| WBEMTime overloaded operators                                                                                                                                                                                                                                                                                                                                                                                                                                        | Description                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| [**operator =**](wbemtime--operator-equal.md)                                                                                                                                                                                                                                                                                                                                                                                                                       | *Assignment* operator facilitates conversions between various Windows and ANSI C run-time time formats.                           |
| [**operator +**](wbemtime-operator-plus.md)                                                                                                                                                                                                                                                                                                                                                                                                                         | *Addition* operator increments an object's time by a time span. The result is returned in a new **WBEMTime** object.              |
| [**operator +=**](wbemtime-operator-plus-equal.md)                                                                                                                                                                                                                                                                                                                                                                                                                  | *Add-and-assign* operator increments an object's time by a time span.                                                             |
| [**operator -**](wbemtime--operator-minus.md)                                                                                                                                                                                                                                                                                                                                                                                                                       | *Subtraction* operator decrements an object's time by another object's time. The result is returned in a new **WBEMTime** object. |
| [**operator -=**](wbemtime-operator-minus-equal.md)                                                                                                                                                                                                                                                                                                                                                                                                                 | *Subtract-and-assign* operator decrements an object's time by a time span.                                                        |
| [**operator ==**](wbemtime-comparison-operators-equal.md)[**operator !=**](wbemtime-comparison-operators-notequal.md)<br/> [**operator &gt;**](wbemtime-comparison-operators-greaterthan.md)<br/> [**operator &gt;=**](wbemtime-comparison-operators-greaterthanorequal.md)<br/> [**operator &lt;**](wbemtime-comparison-operators-lessthan.md)<br/> [**operator &lt;=**](wbemtime-comparison-operators-lessthanorequal.md)<br/> | Comparison operators compare two **WBEMTime** objects.                                                                            |



 

## Requirements



|                                     |                                                                                                                                                               |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                                                                |
| Header<br/>                   | <dl> <dt>WbemTime.h</dt> </dl>                                                                         |
| DLL<br/>                      | <dl> <dt>FrameDynOS.dll; </dt> <dt>FrameDyn.dll</dt> </dl> |



 

 




