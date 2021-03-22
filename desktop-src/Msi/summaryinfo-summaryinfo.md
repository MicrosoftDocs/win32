---
description: The Property property of the SummaryInfo object sets or gets the value for the specified property in the summary information stream.
ms.assetid: 8e8f0987-c92b-43f3-a61a-35099188c629
title: SummaryInfo.Property property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SummaryInfo.Property
api_type: 
- COM
api_location: 
- Msi.dll
---

# SummaryInfo.Property property

The **Property** property of the [**SummaryInfo**](summaryinfo-object.md) object sets or gets the value for the specified property in the summary information stream. The properties are read when the [**SummaryInfo**](summaryinfo-object.md) object is created, but they are not written until the [**Persist**](summaryinfo-persist.md) method is called. Setting a property to Empty causes its removal; likewise, requesting a nonexistent property returns an Empty value. Otherwise values may be transferred as strings, integers, or date (date time) types.

This property is read-only.

## Syntax


```JScript
propVal = SummaryInfo.Property
```



## Property value

Required property ID of one of the summary properties.

## Remarks

**Standard Summary Property IDs**

(not an enumeration)



| Parameter name     | Value | Description                                       |
|--------------------|-------|---------------------------------------------------|
| PID\_DICTIONARY    | 0     | Special format, not support by SummaryInfo object |
| PID\_CODEPAGE      | 1     | VT\_I2                                            |
| PID\_TITLE         | 2     | VT\_LPSTR                                         |
| PID\_SUBJECT       | 3     | VT\_LPSTR                                         |
| PID\_AUTHOR        | 4     | VT\_LPSTR                                         |
| PID\_KEYWORDS      | 5     | VT\_LPSTR                                         |
| PID\_COMMENTS      | 6     | VT\_LPSTR                                         |
| PID\_TEMPLATE      | 7     | VT\_LPSTR                                         |
| PID\_LASTAUTHOR    | 8     | VT\_LPSTR                                         |
| PID\_REVNUMBER     | 9     | VT\_LPSTR                                         |
| PID\_EDITTIME      | 10    | VT\_FILETIME                                      |
| PID\_LASTPRINTED   | 11    | VT\_FILETIME                                      |
| PID\_CREATE\_DTM   | 12    | VT\_FILETIME                                      |
| PID\_LASTSAVE\_DTM | 13    | VT\_FILETIME                                      |
| PID\_PAGECOUNT     | 14    | VT\_I4                                            |
| PID\_WORDCOUNT     | 15    | VT\_I4                                            |
| PID\_CHARCOUNT     | 16    | VT\_I4                                            |
| PID\_THUMBNAIL     | 17    | VT\_CF (not supported)                            |
| PID\_APPNAME       | 18    | VT\_LPSTR                                         |
| PID\_SECURITY      | 19    | VT\_I4                                            |



 

**Property Data Types**

(not an enumeration)



| Parameter name | Value | Description                                                                              |
|----------------|-------|------------------------------------------------------------------------------------------|
| VT\_I2         | 2     | 16-bit integer                                                                           |
| VT\_I4         | 3     | 32-bit integer                                                                           |
| VT\_LPSTR      | 30    | String                                                                                   |
| VT\_FILETIME   | 64    | Date time (FILETIME, converted to Variant time)                                          |
| VT\_CF         | 71    | Clipboard format + data, not handled by [**SummaryInfo**](summaryinfo-object.md) object |



 

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_ISummaryInfo is defined as 000C109B-0000-0000-C000-000000000046<br/>                                                                                                                                                                         |



## See also

<dl> <dt>

[**MsiSummaryInfoSetProperty**](/windows/desktop/api/Msiquery/nf-msiquery-msisummaryinfosetpropertya)
</dt> <dt>

[**MsiSummaryInfoGetProperty**](/windows/desktop/api/Msiquery/nf-msiquery-msisummaryinfogetpropertya)
</dt> </dl>

 

 




