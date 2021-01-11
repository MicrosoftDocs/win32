---
description: The Mid method extracts a substring of length nCount characters from a CHString string, starting at position nFirst (zero-based). The method returns a copy of the extracted substring.
audience: developer
ms.assetid: 2036813b-f991-4ca3-95d3-8bbe858aae09
ms.tgt_platform: multiple
title: CHString::Mid methods (ChString.h)
ms.date: 07/02/2019
ms.topic: reference
---

# CHString::Mid methods

\[The [**CHString**](chstring.md) class is part of the WMI Provider Framework which is now considered in final state, and no further development, enhancements, or updates will be available for non-security related issues affecting these libraries. The [MI APIs](/previous-versions/windows/desktop/wmi_v2/windows-management-infrastructure) should be used for all new development.\]

The **Mid** method extracts a substring of length *nCount* characters from a [**CHString**](chstring.md) string, starting at position *nFirst* (zero-based). The method returns a copy of the extracted substring.

### Overload list



| Method                                        | Description                                                              |
|:----------------------------------------------|:-------------------------------------------------------------------------|
| [**Mid(int,int)**](/windows/win32/api/chstring/nf-chstring-chstring-mid(int_int)) | Extracts a substring of specified length and beginning point.<br/> |
| [**Mid(int)**](/windows/win32/api/chstring/nf-chstring-chstring-mid(int))         | Extracts a substring beginning at int.<br/>                        |



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows�Vista<br/>                                                                                                                                      |
| Minimum supported server<br/> | Windows Server�2008<br/>                                                                                                                                |
| Header<br/>                   | <dl> <dt>ChString.h (include FwCommon.h)</dt> </dl>                                                    |
| Library<br/>                  | <dl> <dt>FrameDyn.lib</dt> </dl>                                                                       |
| DLL<br/>                      | <dl> <dt>FrameDynOS.dll; </dt> <dt>FrameDyn.dll</dt> </dl> |



�

�
